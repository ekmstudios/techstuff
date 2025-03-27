import re
import os
import sys
from datetime import datetime

class SwiftDocGenerator:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = self._get_output_file_path()
        self.class_name = None
        self.class_description = None
        self.variables = []
        self.functions = []
        self.swift_code = None

    def _get_output_file_path(self):
        """Generate the output file path based on the input file name."""
        base_name = os.path.basename(self.input_file_path)
        file_name_without_ext = os.path.splitext(base_name)[0]
        return f"{file_name_without_ext}_documentation.md"

    def read_swift_file(self):
        """Read the Swift file content."""
        try:
            with open(self.input_file_path, 'r') as file:
                self.swift_code = file.read()
            return True
        except FileNotFoundError:
            print(f"Error: File '{self.input_file_path}' not found.")
            return False
        except Exception as e:
            print(f"Error reading file: {e}")
            return False

    def parse_class_info(self):
        """Extract class name and description."""
        # Pattern to match class declaration with optional documentation comment
        class_pattern = r'/\*\*\s*([\s\S]*?)\*/\s*(?:public\s+|private\s+|internal\s+|fileprivate\s+|open\s+)*class\s+(\w+)'
        simple_class_pattern = r'(?:public\s+|private\s+|internal\s+|fileprivate\s+|open\s+)*class\s+(\w+)'
        
        class_match = re.search(class_pattern, self.swift_code)
        if class_match:
            self.class_description = self._clean_doc_comment(class_match.group(1))
            self.class_name = class_match.group(2)
        else:
            # Try with simple pattern without documentation
            simple_match = re.search(simple_class_pattern, self.swift_code)
            if simple_match:
                self.class_name = simple_match.group(1)
                self.class_description = "No description provided."

    def parse_variables(self):
        """Extract variable declarations and their documentation."""
        # Pattern to match variable declarations with optional documentation
        var_pattern = r'/\*\*\s*([\s\S]*?)\*/\s*(?:public\s+|private\s+|internal\s+|fileprivate\s+|open\s+)*(?:let|var)\s+(\w+)\s*:\s*([^{=]+)'
        simple_var_pattern = r'(?:public\s+|private\s+|internal\s+|fileprivate\s+|open\s+)*(?:let|var)\s+(\w+)\s*:\s*([^{=]+)'
        
        # Find variables with documentation
        var_matches = re.finditer(var_pattern, self.swift_code)
        for match in var_matches:
            var_name = match.group(2)
            self.variables.append({
                'name': var_name,
                'type': match.group(3).strip(),
                'description': self._clean_doc_comment(match.group(1)),
                'link_id': f"property-{var_name.lower()}"
            })
        
        # Find variables without documentation
        simple_matches = re.finditer(simple_var_pattern, self.swift_code)
        for match in simple_matches:
            var_name = match.group(1)
            # Check if this variable is already documented
            if not any(var['name'] == var_name for var in self.variables):
                self.variables.append({
                    'name': var_name,
                    'type': match.group(2).strip(),
                    'description': "No description provided.",
                    'link_id': f"property-{var_name.lower()}"
                })

    def parse_functions(self):
        """Extract function declarations and their documentation."""
        # Pattern to match function declarations with optional documentation
        func_pattern = r'/\*\*\s*([\s\S]*?)\*/\s*(?:public\s+|private\s+|internal\s+|fileprivate\s+|open\s+)*func\s+(\w+)\s*\(([\s\S]*?)\)(?:\s*->\s*([^{]+))?'
        simple_func_pattern = r'(?:public\s+|private\s+|internal\s+|fileprivate\s+|open\s+)*func\s+(\w+)\s*\(([\s\S]*?)\)(?:\s*->\s*([^{]+))?'
        
        # Find functions with documentation
        func_matches = re.finditer(func_pattern, self.swift_code)
        for match in func_matches:
            func_name = match.group(2)
            return_type = match.group(4).strip() if match.group(4) else "Void"
            self.functions.append({
                'name': func_name,
                'params': self._parse_parameters(match.group(3)),
                'return_type': return_type,
                'description': self._clean_doc_comment(match.group(1)),
                'link_id': f"method-{func_name.lower()}"
            })
        
        # Find functions without documentation
        simple_matches = re.finditer(simple_func_pattern, self.swift_code)
        for match in simple_matches:
            # Check if this function is already documented
            func_name = match.group(1)
            if not any(func['name'] == func_name for func in self.functions):
                return_type = match.group(3).strip() if match.group(3) else "Void"
                self.functions.append({
                    'name': func_name,
                    'params': self._parse_parameters(match.group(2)),
                    'return_type': return_type,
                    'description': "No description provided.",
                    'link_id': f"method-{func_name.lower()}"
                })

    def _parse_parameters(self, params_str):
        """Parse function parameters from a string."""
        if not params_str.strip():
            return []
        
        params = []
        # Split by commas but not within angle brackets (for generic types)
        param_parts = []
        bracket_count = 0
        current_part = ""
        
        for char in params_str:
            if char == '<':
                bracket_count += 1
            elif char == '>':
                bracket_count -= 1
            elif char == ',' and bracket_count == 0:
                param_parts.append(current_part.strip())
                current_part = ""
                continue
            current_part += char
        
        if current_part.strip():
            param_parts.append(current_part.strip())
        
        for part in param_parts:
            # Handle different parameter patterns
            # Format: [external_name] internal_name: type
            param_match = re.search(r'(?:(\w+)\s+)?(\w+)\s*:\s*([^,]+)', part)
            if param_match:
                external_name = param_match.group(1)
                internal_name = param_match.group(2)
                param_type = param_match.group(3).strip()
                
                param_name = f"{external_name} {internal_name}" if external_name else internal_name
                params.append({
                    'name': param_name,
                    'type': param_type
                })
        
        return params

    def _clean_doc_comment(self, comment):
        """Clean up documentation comments."""
        if not comment:
            return "No description provided."
        
        # Remove leading * and whitespace from each line
        lines = comment.split('\n')
        cleaned_lines = [re.sub(r'^\s*\*?\s*', '', line) for line in lines]
        
        # Link variables and methods within the comment
        cleaned_comment = self._create_internal_links(' '.join(cleaned_lines))
        
        return cleaned_comment.strip()

    def _create_internal_links(self, comment):
        """Create internal links for variables and methods in the comment."""
        # Link to properties
        for var in self.variables:
            # Use word boundaries to match whole words
            comment = re.sub(r'\b' + var['name'] + r'\b', 
                             f'[{var["name"]}](#{var["link_id"]})', 
                             comment, 
                             flags=re.IGNORECASE)
        
        # Link to methods
        for func in self.functions:
            # Use word boundaries to match whole words
            comment = re.sub(r'\b' + func['name'] + r'\b', 
                             f'[{func["name"]}](#{func["link_id"]})', 
                             comment, 
                             flags=re.IGNORECASE)
        
        return comment

    def generate_markdown(self):
        """Generate Markdown documentation with internal linking."""
        if not self.class_name:
            return "Error: No Swift class found in the file."
        
        markdown = f"# {self.class_name}\n\n"
        
        # Add class description with internal links
        if self.class_description:
            markdown += f"{self.class_description}\n\n"
        
        # Add file information
        markdown += f"## File Information\n\n"
        markdown += f"- **File:** {os.path.basename(self.input_file_path)}\n"
        markdown += f"- **Documentation Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # Add properties section
        if self.variables:
            markdown += "## Properties\n\n"
            for var in self.variables:
                markdown += f"### <a id='{var['link_id']}'>{var['name']}</a>\n\n"
                markdown += f"- **Type:** `{var['type']}`\n"
                markdown += f"- **Description:** {var['description']}\n\n"
        
        # Add functions section
        if self.functions:
            markdown += "## Methods\n\n"
            for func in self.functions:
                # Format the function signature
                params_str = ", ".join([f"{p['name']}: {p['type']}" for p in func['params']])
                signature = f"{func['name']}({params_str})"
                if func['return_type'] != "Void":
                    signature += f" -> {func['return_type']}"
                
                markdown += f"### <a id='{func['link_id']}'>{func['name']}</a>\n\n"
                markdown += f"```swift\n{signature}\n```\n\n"
                markdown += f"**Description:** {func['description']}\n\n"
                
                # Add parameters section if there are parameters
                if func['params']:
                    markdown += "**Parameters:**\n\n"
                    for param in func['params']:
                        markdown += f"- `{param['name']}` ({param['type']})\n"
                    markdown += "\n"
                
                # Add return value section if not void
                if func['return_type'] != "Void":
                    markdown += f"**Returns:** `{func['return_type']}`\n\n"
        
        return markdown

    def write_markdown_file(self, markdown_content):
        """Write the generated markdown to a file."""
        try:
            with open(self.output_file_path, 'w') as file:
                file.write(markdown_content)
            print(f"Documentation generated successfully: {self.output_file_path}")
            return True
        except Exception as e:
            print(f"Error writing documentation file: {e}")
            return False

    def process(self):
        """Process the Swift file and generate documentation."""
        if not self.read_swift_file():
            return False
        
        self.parse_class_info()
        self.parse_variables()
        self.parse_functions()
        
        markdown_content = self.generate_markdown()
        return self.write_markdown_file(markdown_content)


def main():
    if len(sys.argv) != 2:
        print("Usage: python swift_doc_generator.py <path_to_swift_file>")
        return
    
    input_file = sys.argv[1]
    generator = SwiftDocGenerator(input_file)
    generator.process()


if __name__ == "__main__":
    main()
