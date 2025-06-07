---
title: dspy
date: 2025-06-07T15:26:54+08:00
draft: False
image: https://images.unsplash.com/photo-1610225199874-d989d5650b9a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDkyODExODN8&ixlib=rb-4.1.0
tags: ['github',documentation, dspy, git, subtree, contribution, website, repository, github, pull request, docusaurus]
categories: ['github']
---

# [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)

# DSPy Documentation

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

## Contributing to the `docs` Folder

This guide is for contributors looking to make changes to the documentation in the `dspy/docs` folder. 

1. **Pull the up-to-date version of the website**: Please pull the latest version of the live documentation site via its subtree repository with the following command:

```bash
#Ensure you are in the top-level dspy/ folder
git subtree pull --prefix=docs https://github.com/krypticmouse/dspy-docs master
```

2. **Push your new changes on a new branch**: Feel free to add or edit existing documentation and open a PR for your changes. Once your PR is reviewed and approved, the changes will be ready to merge into main. 

3. **Updating the website**: Once your changes are merged to main, they need to be pushed to the subtree repository that hosts the live documentation site. This step will eventually be done automatically, but for now, please run the following command to push the updated `docs` content to the website subtree repository:

```bash
#Ensure you are in the top-level dspy/ folder
git subtree push --prefix=docs https://github.com/krypticmouse/dspy-docs master
```
