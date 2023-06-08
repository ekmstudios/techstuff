#  Gatsby Tutorial

## Objective: 
Use Gatsby to build a website that pulls content written in markdown located in several different GitHub repositories.

## Problem:
I see a lot of tutorials on using Gatsby to create websites with markdown files located within the same codebase. But I’m not seeing a lot of tutorials on building a website that pulls in markdown files from different GitHub repositories. 

## Goals of the website:
- Build a website using Gatsby that does the following:
— pulls markdown files from different GitHub repos and display they on the website as HTML
— Create a dynamic side navigation that displays titles of each of the pages as organized by each repo and ideally have expandable/collapsable sub groups.
- Bonus features
— Use Firebase for authentication
— Use Google Analytics for page visits
— Use Firebase (or some other database) as the backend database for a demo ecommerce website.

## Resources

- [gatsby-source-git](https://www.gatsbyjs.com/plugins/gatsby-source-git/?=gatsby-source-git)
- [gatsby-plugin-mdx install info](https://www.gatsbyjs.com/plugins/gatsby-plugin-mdx/)


## md vs mdx

Using the .mdx file extension enables you to include JSX in your markdown.

## Installing gatsby-plugin-mdx

- [gatsby-plugin-mdx install info](https://www.gatsbyjs.com/plugins/gatsby-plugin-mdx/)

- Enter the following command in your command line
`npm install gatsby-plugin-mdx gatsby-source-filesystem @mdx-js/react`


## Two types of Components
- page components
- "building-block" components - smaller components that are just part of the user interface on a page. For example, a header, footer, and navbar are all examples of a building block component.



## Setting up Gatsby



