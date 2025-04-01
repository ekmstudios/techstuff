# Confluence to Markdown Python Script

I'll create a Python script to convert Confluence pages to Markdown. This will be useful for migrating content or maintaining documentation in both formats.

```python
#!/usr/bin/env python3
"""
Confluence to Markdown Converter
This script connects to a Confluence instance, fetches pages, and converts them to Markdown format.
"""

import os
import re
import json
import requests
import argparse
import html2text
from urllib.parse import urljoin
from base64 import b64encode

class ConfluenceToMarkdown:
    def __init__(self, base_url, username, api_token, space_key=None):
        """
        Initialize the converter with Confluence connection details.
        
        Args:
            base_url (str): The base URL of your Confluence instance
            username (str): Your Confluence username
            api_token (str): Your Confluence API token
            space_key (str, optional): Specific Confluence space to target
        """
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.api_token = api_token
        self.space_key = space_key
        self.auth_header = self._get_auth_header()
        self.converter = html2text.HTML2Text()
        self._configure_converter()

    def _get_auth_header(self):
        """Generate the authorization header for API requests."""
        auth_str = f"{self.username}:{self.api_token}"
        return {
            "Authorization": f"Basic {b64encode(auth_str.encode()).decode()}",
            "Content-Type": "application/json"
        }
    
    def _configure_converter(self):
        """Configure HTML to Markdown converter settings."""
        self.converter.ignore_links = False
        self.converter.bypass_tables = False
        self.converter.ignore_images = False
        self.converter.ignore_emphasis = False
        self.converter.body_width = 0  # No line wrapping

    def fetch_page(self, page_id):
        """
        Fetch a specific Confluence page by ID.
        
        Args:
            page_id (str): The Confluence page ID
            
        Returns:
            dict: Page data including title and content
        """
        endpoint = f"/rest/api/content/{page_id}?expand=body.storage"
        response = requests.get(
            urljoin(self.base_url, endpoint),
            headers=self.auth_header
        )
        
        if response.status_code != 200:
            raise Exception(f"Failed to fetch page: {response.status_code} - {response.text}")
        
        return response.json()
    
    def fetch_space_pages(self):
        """
        Fetch all pages from a specific Confluence space.
        
        Returns:
            list: List of page objects with basic metadata
        """
        if not self.space_key:
            raise ValueError("Space key is required to fetch space pages")
        
        all_pages = []
        start = 0
        limit = 50
        
        while True:
            endpoint = f"/rest/api/content?spaceKey={self.space_key}&limit={limit}&start={start}"
            response = requests.get(
                urljoin(self.base_url, endpoint),
                headers=self.auth_header
            )
            
            if response.status_code != 200:
                raise Exception(f"Failed to fetch pages: {response.status_code} - {response.text}")
            
            data = response.json()
            results = data.get('results', [])
            all_pages.extend(results)
            
            if len(results) < limit:
                break
                
            start += limit
        
        return all_pages
    
    def convert_page_content(self, html_content):
        """
        Convert HTML content to Markdown.
        
        Args:
            html_content (str): HTML content from Confluence
            
        Returns:
            str: Converted Markdown content
        """
        # Pre-process HTML to handle Confluence specifics
        html_content = self._preprocess_html(html_content)
        
        # Convert to Markdown
        markdown_content = self.converter.handle(html_content)
        
        # Post-process the Markdown
        markdown_content = self._postprocess_markdown(markdown_content)
        
        return markdown_content
    
    def _preprocess_html(self, html_content):
        """Pre-process HTML content before conversion to handle Confluence specifics."""
        # Handle Confluence macro divs 
        html_content = re.sub(r'<div class="confluence-information-macro[^>]*>.*?</div>', '', html_content, flags=re.DOTALL)
        
        # Handle code blocks
        html_content = re.sub(r'<ac:structured-macro ac:name="code">(.*?)<ac:parameter ac:name="language">(.*?)</ac:parameter>(.*?)<ac:plain-text-body><!\[CDATA\[(.*?)\]\]></ac:plain-text-body>(.*?)</ac:structured-macro>', 
                              r'<pre><code class="\2">\4</code></pre>', 
                              html_content, 
                              flags=re.DOTALL)
        
        # Handle Confluence images
        html_content = re.sub(r'<ac:image[^>]*><ri:attachment ri:filename="([^"]*)"[^>]*></ac:image>', 
                              r'<img src="\1" alt="\1">', 
                              html_content)
        
        return html_content
    
    def _postprocess_markdown(self, markdown_content):
        """Post-process the Markdown content to clean up conversion artifacts."""
        # Clean up extra line breaks
        markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
        
        # Fix code block formatting
        markdown_content = re.sub(r'```\s+', '```\n', markdown_content)
        
        return markdown_content
    
    def save_markdown(self, title, content, output_dir="./markdown"):
        """
        Save the converted Markdown content to a file.
        
        Args:
            title (str): Page title to use for the filename
            content (str): Markdown content to save
            output_dir (str): Directory to save files to
        
        Returns:
            str: Path to the saved file
        """
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Sanitize filename
        filename = re.sub(r'[^\w\-]', '_', title) + '.md'
        filepath = os.path.join(output_dir, filename)
        
        # Add title as H1 at the beginning of the file
        full_content = f"# {title}\n\n{content}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        return filepath
    
    def process_page(self, page_id, output_dir="./markdown"):
        """
        Process a single page by ID: fetch, convert, and save.
        
        Args:
            page_id (str): Confluence page ID
            output_dir (str): Directory to save the output
            
        Returns:
            str: Path to the saved Markdown file
        """
        page_data = self.fetch_page(page_id)
        title = page_data.get('title', 'Untitled')
        html_content = page_data.get('body', {}).get('storage', {}).get('value', '')
        
        markdown_content = self.convert_page_content(html_content)
        return self.save_markdown(title, markdown_content, output_dir)
    
    def process_space(self, output_dir="./markdown"):
        """
        Process all pages in the configured space.
        
        Args:
            output_dir (str): Directory to save the output
            
        Returns:
            list: List of saved file paths
        """
        pages = self.fetch_space_pages()
        saved_files = []
        
        for page in pages:
            page_id = page.get('id')
            try:
                filepath = self.process_page(page_id, output_dir)
                saved_files.append(filepath)
                print(f"Converted: {page.get('title')} -> {filepath}")
            except Exception as e:
                print(f"Error converting page {page.get('title')}: {str(e)}")
        
        return saved_files


def main():
    """Main function to run the script from command line."""
    parser = argparse.ArgumentParser(description='Convert Confluence pages to Markdown')
    parser.add_argument('--url', required=True, help='Confluence base URL')
    parser.add_argument('--username', required=True, help='Confluence username')
    parser.add_argument('--token', required=True, help='Confluence API token')
    parser.add_argument('--space', help='Space key to process all pages from')
    parser.add_argument('--page', help='Specific page ID to process')
    parser.add_argument('--output', default='./markdown', help='Output directory for Markdown files')
    
    args = parser.parse_args()
    
    converter = ConfluenceToMarkdown(
        base_url=args.url,
        username=args.username,
        api_token=args.token,
        space_key=args.space
    )
    
    if args.page:
        file_path = converter.process_page(args.page, args.output)
        print(f"Converted page saved to: {file_path}")
    elif args.space:
        saved_files = converter.process_space(args.output)
        print(f"Converted {len(saved_files)} pages from space {args.space}")
    else:
        parser.error("Either --page or --space must be specified")


if __name__ == "__main__":
    main()

```

This script provides a comprehensive solution for converting Confluence pages to Markdown. Here's how to use it:

### Basic Usage

```bash
python confluence_to_markdown.py --url "https://yourcompany.atlassian.net/wiki" --username "your.email@company.com" --token "your-api-token" --space "DOCS" --output "./markdown_files"
```

### Features

- Convert individual pages by page ID
- Convert all pages in a specific space
- Handles Confluence-specific elements like macros and code blocks
- Preserves images (as references)
- Organizes output in a specified directory

### Getting Your API Token

1. Log in to Atlassian
2. Go to Account Settings > Security > Create and manage API tokens
3. Create a new token for this script

### Requirements

You'll need to install these dependencies:

```bash
pip install requests html2text
```
