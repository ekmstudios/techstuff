# Git and GitHub: From Fundamentals to Advanced Workflows

This comprehensive Git and GitHub course guides you from beginner to an advanced user. This course is structured to build your skills progressively while providing practical examples along the way. This course follows a logical progression through six modules:

1. **Git Fundamentals** - Learn the core concepts of version control and basic Git commands
2. **GitHub Essentials** - Connect your local repositories to GitHub and understand collaboration basics
3. **Git Branching and Merging** - Master different branching strategies and handle complex merges
4. **Advanced Git Techniques** - Explore history rewriting, advanced commands, hooks, and Git internals
5. **GitHub Advanced Features** - Implement GitHub Actions, project management, security features, and integrations
6. **Professional Git and GitHub** - Scale up to enterprise workflows, open source best practices, and large repository management

Each module includes a hands-on project to reinforce learning with practical experience. The course concludes with a final project to create a complete GitHub portfolio showcasing all your skills.

The course also includes appendices covering troubleshooting, useful tools, and additional resources to support your learning journey.

## Course Overview

This comprehensive course will take you from Git beginner to proficient GitHub user. You'll learn essential version control concepts, master day-to-day Git commands, collaborate effectively with teams, and implement advanced workflows for professional software development.

## Module 1: Git Fundamentals

### 1.1 Introduction to Version Control
- What is version control and why is it important?
- Brief history of version control systems
- Centralized vs. distributed version control
- Git's place in modern software development

### 1.2 Setting Up Git
- Installing Git on different operating systems
- Initial configuration (user.name, user.email)
- Git Bash vs. GUI clients
- Setting up SSH keys for secure connections

### 1.3 Git Basics
- Understanding the Git workflow
- The three states: working directory, staging area, repository
- Basic Git commands:
  - `git init`: Creating a new repository
  - `git clone`: Copying an existing repository
  - `git status`: Checking repository status
  - `git add`: Tracking and staging files
  - `git commit`: Recording changes
  - `git log`: Viewing commit history

### 1.4 Working with Git Locally
- Creating and switching branches with `git branch` and `git checkout`
- Understanding the `HEAD` pointer
- Viewing changes with `git diff`
- Discarding changes with `git restore` and `git reset`
- Using `.gitignore` to exclude files

### Hands-on Project 1:
Create a local Git repository for a personal project, add files, make several commits with meaningful messages, create branches for different features, and navigate between them.

## Module 2: GitHub Essentials

### 2.1 Introduction to GitHub
- GitHub vs. Git: understanding the difference
- Creating a GitHub account
- GitHub interface overview
- Public vs. private repositories
- GitHub free tier vs. paid plans

### 2.2 Connecting Local Git to GitHub
- Adding remote repositories with `git remote`
- Authentication methods (HTTPS vs SSH)
- Pushing to GitHub with `git push`
- Pulling from GitHub with `git pull`
- Understanding origin and upstream

### 2.3 GitHub Collaboration Basics
- Forking repositories
- Creating and managing pull requests
- Code review basics
- Managing issues
- GitHub notifications

### 2.4 GitHub Documentation
- Creating and formatting README.md files
- GitHub-flavored Markdown
- Project wikis
- GitHub Pages basics

### Hands-on Project 2:
Fork an open-source repository, clone it locally, create a new branch with improvements, push it to your fork, and create a pull request to the original repository.

## Module 3: Git Branching and Merging

### 3.1 Advanced Branching
- Branching strategies (feature branches, release branches)
- Long-running vs. topic branches
- Naming conventions
- Remote branches and tracking

### 3.2 Merging in Git
- Fast-forward vs. three-way merges
- Merge conflicts and how to resolve them
- `git merge` vs. `git rebase`
- When to use merging vs. rebasing

### 3.3 GitHub Flow
- Understanding the GitHub Flow workflow
- Branch → Commit → Pull Request → Review → Merge
- Protected branches
- Automating the review process

### 3.4 Other Common Workflows
- Git Flow model
- Trunk-based development
- Release management
- Choosing the right workflow for your team

### Hands-on Project 3:
Work with a team (or simulate one) to implement a GitHub Flow workflow, create multiple branches, handle merge conflicts, and successfully merge several features into the main branch.

## Module 4: Advanced Git Techniques

### 4.1 Rewriting History
- Amending commits with `git commit --amend`
- Interactive rebasing with `git rebase -i`
- Squashing commits
- When (and when not) to rewrite history
- Force pushing with `git push --force` and its dangers

### 4.2 Advanced Git Commands
- Cherry-picking with `git cherry-pick`
- Stashing changes with `git stash`
- Finding bugs with `git bisect`
- Tagging releases with `git tag`
- Cleaning up with `git clean`

### 4.3 Git Hooks
- Understanding Git hooks
- Pre-commit hooks for code quality
- Post-commit hooks for notifications
- Pre-push hooks for testing
- Setting up hooks in a team environment

### 4.4 Git Internals
- The `.git` directory structure
- Git objects: blobs, trees, commits
- Understanding Git's content-addressable storage
- Git references and the reflog
- Garbage collection in Git

### Hands-on Project 4:
Implement advanced Git techniques to clean up a messy repository history, set up Git hooks for code quality checks, and create a release with proper tags.

## Module 5: GitHub Advanced Features

### 5.1 GitHub Actions
- Introduction to CI/CD concepts
- Creating workflows with GitHub Actions
- Building, testing, and deploying code
- Creating custom actions
- Workflow optimization

### 5.2 GitHub Projects and Project Management
- Using GitHub Projects for task management
- Creating and managing project boards
- Automating project workflows
- Integrating with issues and pull requests
- GitHub Project templates

### 5.3 Security Features
- Dependency scanning with Dependabot
- Security advisories and vulnerability alerts
- Code scanning with GitHub Advanced Security
- Secret scanning
- Setting up security policies

### 5.4 GitHub Integrations
- GitHub Marketplace overview
- Popular integrations for testing, deployment, and monitoring
- Setting up notifications with Slack, Discord, etc.
- OAuth Apps vs. GitHub Apps
- Creating custom integrations

### Hands-on Project 5:
Set up a complete CI/CD pipeline with GitHub Actions that automatically tests and deploys your application, and configure security scanning for your repository.

## Module 6: Professional Git and GitHub

### 6.1 Large-Scale Git
- Managing large repositories
- Git LFS (Large File Storage)
- Submodules and subtrees
- Performance optimization
- Mono-repos vs. multi-repos

### 6.2 Team Collaboration Strategies
- Code review best practices
- Pull request templates
- Branch protection rules
- Merge queues
- Managing permissions and teams

### 6.3 GitHub for Open Source
- Creating an open source project
- License selection
- Contributing guidelines
- Code of conduct
- Building a community

### 6.4 Git and GitHub in the Enterprise
- GitHub Enterprise overview
- SAML and SSO integration
- Role-based access control
- Compliance and auditing
- GitHub Enterprise API

### Hands-on Project 6:
Set up a complete open source project with appropriate documentation, contribution guidelines, automated CI/CD, and security checks. Alternatively, implement an enterprise-grade workflow for a team project.

## Appendix

### A. Troubleshooting Common Git Issues
- Debugging merge conflicts
- Recovering lost commits
- Fixing detached HEAD states
- Resolving authentication issues
- Dealing with large repositories

### B. Git and GitHub Tools
- GUI clients (GitHub Desktop, GitKraken, SourceTree)
- IDE integrations (VS Code, IntelliJ, etc.)
- Command-line enhancements
- Productivity tools and extensions
- Backup and migration tools

### C. Git and GitHub Resources
- Official documentation
- Recommended books
- Online tutorials and courses
- Community forums
- Cheat sheets and quick references

## Final Project

Create a complete GitHub portfolio that showcases your Git and GitHub skills. This should include:

1. A well-structured repository with appropriate branching
2. Comprehensive documentation with GitHub-flavored Markdown
3. Automated workflows with GitHub Actions
4. Issue templates and pull request templates
5. Project boards for feature planning
6. Security scanning configuration
7. A contributor's guide for collaboration

Your portfolio should demonstrate best practices for code organization, collaboration, and project management using Git and GitHub.

---

## Course Resources

### Templates and Examples
- Sample `.gitignore` files for various project types
- Pull request and issue templates
- GitHub Actions workflow examples
- Example Git hooks for common scenarios

### Cheat Sheets
- Essential Git commands
- GitHub Markdown syntax
- Git branching strategies
- Troubleshooting flowcharts

### Additional Materials
- Video demonstrations of complex Git operations
- Interactive quizzes for each module
- Real-world case studies
- Community forum for questions and discussion
