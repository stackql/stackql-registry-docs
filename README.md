# registry.stackql.io

This repository contains documentation for StackQL providers, which is published to [registry.stackql.io](https://registry.stackql.io).  

[![Netlify Status](https://api.netlify.com/api/v1/badges/6d4dae53-745b-470e-a964-2c0676bfe165/deploy-status)](https://app.netlify.com/sites/registry-stackql-io/deploys)

## Website

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

### Installation

```bash
yarn
```

### Local Development

```bash
yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```bash
yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

```bash
GIT_USER=<Your GitHub username> USE_SSH=true yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.
