Gatsby Themes
Gatsby themes are plugins that include a gatsby-config.js file

Create multiple sites that consume the same theme. To make updates across those sites, update the central theme and bump the version in the sites through the package.json file rather than updating functionality in each individual site.

Getting Started

To get started with an existing theme:
Similar to the way you would install a starter, install a theme starter
gatsby new my-blog https://github.com/gatsbyjs/gatsby-starter-blog-theme

A starter for an official Gatsby theme does the following:
1. Installs the theme and configures it
2. The starter scaffolds out example blog posts

Make some edits and then run
gatsby develop 
to start a development server and view changes in a browser

Updating a theme
Run the install of theme package again:
npm install gatsby-theme-blog


Using a Gatsby Theme

Installing a Theme
To install a theme (in this case, the official Gatsby theme for creating a blog)
npm install gatsby-theme-blog

You can use multiple Gatsby Themes
You can include multiple theme packages in your gatsby-config.js file. 


Shadowing
Allows users to replace a file in the src directory that is included in the webpack bundle with their own implementation. 

Theme file structure


Conventions
