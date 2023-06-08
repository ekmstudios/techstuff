#  Adding Gatsby local search

gatsby new my-gatsby-project https://github.com/gatsbyjs/gatsby-starter-blog

1. Install the local search gatsby plugin
```
yarn add gatsby-plugin-local-search

#or 
npm install --save gatsby-plugin-local-search

npm install gastsby-plugin-local-search

```

2. Then add the FlexSearch search library:

```
yarn add flexsearch react-use-flexsearch

# or 

npm install --save react-use-flexsearch

npm install flexsearch react-use-flexsearch

```


1. Create a search.js file in the components directory.
2. Add the following code.

```
import React from 'react';

const SearchBar = ({ searchQuery, setSearchQuery }) => (
    <form 
        action="/"
        method="get"
        autoComplete="off"
    >
        <label htmlFor="header-search"> 
            <span className="visually-hiden">
                Search
            </span>
        </label>
        <input
            value={searchQuery}
            onInput={(e)} => setSearchQuery(e.target.value)}
            type="text"
            id="header-search"
            placeholder="Search blog posts"
            name="s"
        />
        <button tpe="submit">Search</button>
    </form>
    
)

```

3. Create search.css file
4. Add the following to the search.css file (or whatever the css file is named).

```
.vusually-hiden {
    clip: rect(0 0 0 0);
    clip-path: inset(50%);
    height: 1px;
    overflow: hidden;
    position: absolute;
    white-space: nowrap;
    width: 1px;
}

```

5. Add the search component to wherever you want it to load
6. First add the following imports:

```
import Search from '.../components/search';
import './search.css';

```

7. Then add the following:

```
const { search } = window.location
const query = new URLSearchParams(search).get('s)
const [searchQuery, setSearchQuery] = useState(query || '');

```

8. Then inside the return statement, add:

```
<SearchBar
    searchQuery={searchQuery}
    setSearchQuery={setSearchQuery}
/>
```



11. Update the Gatsby config file (gatsby-config.js)

```
plugins: [
    {
        resolve: 'gatsby-plugin-local-search',
        options: {
            name: 'pages',
            engine: 'flexsearch',
            query: 
                {
                    allMarkdownRemark {
                        nodes {
                            id
                            frontmatter {
                                path
                                title
                            }
                            rawMarkdownBody
                        
                        }
                    
                    }
                
                }
            
            ,
            ref: 'id',
            index: ['title', 'body'],
            store: ['id', 'path', 'title'],
            normalizer: ({ data }) => 
                data.allMardownRemark.nodes.map((node) => ({
                    id: node.id,
                    path: node.frontmatter.path,
                    title: node.frontmatter.title,
                    body: node.rawMarkdownBody,
                
                }),

            
            }
    
    
    }


]


```

- Then add the following to the file where you want the component to display:

```
import { graphql } from 'gatsby';
import { useFlexSearch } from 'react-use'flexsearch';

export default ({
    data: {
        localSearchPages: { index, store },
        allMarkdownRemark: { nodes },
    },
}) => {
    const { search } = window.location;
    const query = new URLSearchParams(search).get('s');
    const [searchQuery, setSearchQuery] = useState(query || '');
    
    const posts = nodes;
    const  resuts = useFlexSearch(searchQuery, index, store);
    
    return (
        <div>
            <h1>Blog</h1>
            <Search 
                searchQuery={searchQuery}
                setSearchQuery={setSearchQuery}
            />
            {posts.map(post => (
                <LinkComponent post={post} />
            
            ))}
        </div>
    );
};

export const pageQuery = graphql`
    query {
    


```
