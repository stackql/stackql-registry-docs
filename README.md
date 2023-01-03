# stackql-registry-docs

This repository contains documentation for StackQL providers, which is published to [registry.stackql.io](https://registry.stackql.io).  This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.  

## Build and Deploy Status

| Type | Status | Link |
| --- | --- | -- |
| GitHub Actions Build | [![GitHub Actions](https://github.com/stackql/stackql-registry-docs/actions/workflows/build-docs.yaml/badge.svg?branch=main)](https://github.com/stackql/stackql-registry-docs/actions/workflows/build-docs.yaml) | [stackql-registry-docs/actions](https://github.com/stackql/stackql-registry-docs/actions) |
| Netlify Deploy Base | [![Netlify Status](https://api.netlify.com/api/v1/badges/75f838a9-79ea-41dc-96f9-a40dff50cfca/deploy-status)](https://app.netlify.com/sites/stackql-registry-docs/deploys) | [registry.stackql.io](https://registry.stackql.io) |
| Netlify Deploy AWS | [![Netlify Status](https://api.netlify.com/api/v1/badges/ef161c4a-63ea-4bcc-a5cb-5eaed30ed55f/deploy-status)](https://app.netlify.com/sites/stackql-aws-docs/deploys) | [aws.stackql.io](https://aws.stackql.io) |
| Netlify Deploy Azure | [![Netlify Status](https://api.netlify.com/api/v1/badges/5e2cce2d-3c51-44df-bb14-4ee9c626ca02/deploy-status)](https://app.netlify.com/sites/stackql-azure-docs/deploys) | [azure.stackql.io](https://azure.stackql.io) |
| Netlify Deploy Firebase | [![Netlify Status](https://api.netlify.com/api/v1/badges/6d8fec42-fba2-4d62-afef-30a821863314/deploy-status)](https://app.netlify.com/sites/stackql-firebase-docs/deploys) | [firebase.stackql.io](https://firebase.stackql.io) |  

## Adding Docs for a New Provider

Adding docs for a new provider requires creating a new web property (subdomain) and will force an update to the root/base site and all other providers.  The steps are:  

- create a new netlify site (`stackql-{provider}-docs`)
- add `NETLIFY` record in Netlify DNS (mapping `{provider}.stackql.io to `stackql-{provider}-docs.netlify.app`)
- update the `providers` array in `sidebars.js` with the new provider
- update the `providers` array `src/configs/providers.ts` with the new provider
- add GitHub Actions secret for netlify site id - `NETLIFY_SITE_ID_{PROVIDER}`
- update `package.json` with new `start` and `build` scripts
- update frontmatter in the `index.md` at the root of the new providers docs, set `slug` to `/providers/{provider}` and `id` to `{provider}-doc`

## Updating Existing Provider Docs

To update the docs for an existing provider, edit the corresponding markdown file or files in the `{provider}-docs` directory.  Raise a pull request into the `main` branch.  Once merged, the updated docs will be automatically published.  

### Running Locally

Install packages:  

```bash
yarn
```

To run a microsite locally, use `yarn start:{provider}`.  For example, to run the AWS microsite locally, run:  

```bash
yarn start:aws
```