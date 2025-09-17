# stackql-registry-docs

This repository contains documentation for StackQL providers, which is published to [registry.stackql.io](https://registry.stackql.io).  This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.  

## Build and Deploy Status

| Type | Status | Link |
| --- | --- | -- |
| GitHub Actions Build | [![GitHub Actions](https://github.com/stackql/stackql-registry-docs/actions/workflows/build-docs.yaml/badge.svg?branch=main)](https://github.com/stackql/stackql-registry-docs/actions/workflows/build-docs.yaml) | [stackql-registry-docs/actions](https://github.com/stackql/stackql-registry-docs/actions) |
| Netlify Deploy Base | [![Netlify Status](https://api.netlify.com/api/v1/badges/75f838a9-79ea-41dc-96f9-a40dff50cfca/deploy-status)](https://app.netlify.com/sites/stackql-registry-docs/deploys) | [registry.stackql.io](https://registry.stackql.io) |
| Netlify Deploy GitHub | [![Netlify Status](https://api.netlify.com/api/v1/badges/625d7d38-37a9-4224-a9c8-6ee58141b109/deploy-status)](https://app.netlify.com/sites/stackql-github-docs/deploys) | [github-docs.stackql.io](https://github-docs.stackql.io)<br/>[github.stackql.io](https://github.stackql.io) |
| Netlify Deploy K8S | [![Netlify Status](https://api.netlify.com/api/v1/badges/d11ea6c5-7a43-42d5-ac76-555112295b9b/deploy-status)](https://app.netlify.com/sites/stackql-k8s-docs/deploys) | [k8s-docs.stackql.io](https://k8s-docs.stackql.io)<br/>[k8s.stackql.io](https://k8s.stackql.io) |
| Netlify Deploy Sumologic | [![Netlify Status](https://api.netlify.com/api/v1/badges/6c864774-8494-41be-8e2c-441b6d1e368c/deploy-status)](https://app.netlify.com/sites/stackql-sumologic-docs/deploys) | [sumologic-docs.stackql.io](https://sumologic-docs.stackql.io)<br/>[sumologic.stackql.io](https://sumologic.stackql.io) |
| Netlify Deploy Vercel | [![Netlify Status](https://api.netlify.com/api/v1/badges/91cc31b7-0c25-443f-bb2f-71921ef7084e/deploy-status)](https://app.netlify.com/sites/stackql-vercel-docs/deploys) | [vercel-docs.stackql.io](https://vercel-docs.stackql.io)<br/>[vercel.stackql.io](https://vercel.stackql.io) |
| Netlify Deploy Homebrew | [![Netlify Status](https://api.netlify.com/api/v1/badges/2343d34d-5061-4d83-98e6-475fb2150c94/deploy-status)](https://app.netlify.com/sites/stackql-homebrew-docs/deploys) | [homebrew-docs.stackql.io](https://homebrew-docs.stackql.io)<br/>[homebrew.stackql.io](https://homebrew.stackql.io) |
| Netlify Deploy OpenAI | [![Netlify Status](https://api.netlify.com/api/v1/badges/6df5743b-8c5d-4949-866e-eda4ca3f74d0/deploy-status)](https://app.netlify.com/sites/stackql-openai-docs/deploys) | [openai-docs.stackql.io](https://openai-docs.stackql.io)<br/>[openai.stackql.io](https://openai.stackql.io) |
| Netlify Deploy Anthropic | [![Netlify Status](https://api.netlify.com/api/v1/badges/114c5a2a-9b76-4941-a0e8-3669ee7d2016/deploy-status)](https://app.netlify.com/sites/stackql-anthropic-docs/deploys) | [anthropic-docs.stackql.io](https://anthropic-docs.stackql.io)<br/>[anthropic.stackql.io](https://anthropic.stackql.io) |
| Netlify Deploy Confluent | [![Netlify Status](https://api.netlify.com/api/v1/badges/63149c2f-6c3d-43f1-be38-80c55c223ac0/deploy-status)](https://app.netlify.com/sites/stackql-confluent-docs/deploys) | [confluent-docs.stackql.io](https://confluent-docs.stackql.io)<br/>[confluent.stackql.io](https://confluent.stackql.io) |

## Adding Docs for a New Provider

Adding docs for a new provider requires creating a new web property (subdomain) and will force an update to the root/base site and all other providers.  The steps are:  

- [ ] update `scripts/docgen/provider_data.py` with metadata for new provider (not applicable if docs are built elsewhere)
- [ ] generate docs for provider using `cd scripts; sh docgen.sh {provider}` (not applicable if docs are built elsewhere)
- [ ] publish docs for provider using `cd scripts; sh publish.sh {provider}` (not applicable if docs are built elsewhere)
- [x] add the new provider docs to `docs/{provider}-docs` (following directory structure of existing providers) (done automatically by `scripts/publish.sh`)
- [x] update frontmatter in the `index.md` at the root of the new providers docs, set `slug` to `/providers/{provider}` and `id` to `{provider}-doc` (done automatically by `scripts/docgen.sh`)
- [x] update `stackql-provider-registry.mdx` in the root of the new provider to add the `currentProvider` prop, e.g. `<RegistryPage currentProvider="okta" />` (done automatically by `scripts/docgen.sh`)
- [ ] create a new netlify site (`stackql-{provider}-docs`) - use `yarn build:{provider}` as the `build command`
- [ ] stop automatic builds for site in Netlify
- [ ] add `NETLIFY` record in Netlify DNS (mapping `{provider}-docs.stackql.io` (Primary Domain) and `{provider}.stackql.io` (Domain Alias) to `stackql-{provider}-docs.netlify.app`), select `Force HTTPS`
- [ ] add GitHub Actions secret for netlify site id - `NETLIFY_SITE_ID_{PROVIDER}`
- [ ] add the Netlify deploy status badge to the table in this `README` (see above)
- [ ] update the `providers` array in `sidebars.js` with the new provider
- [ ] update the `providers` array `src/configs/providers.ts` with the new provider
- [ ] update `package.json` with new `start` and `build` scripts
- [ ] update `allProviders` in `ci-scripts/get-providers-to-deploy.js` with the new provider
- [ ] add the root site redirects for provider vanity urls to `.github/workflows/build-docs.yaml` to the `add redirects to root site` step of the `deploy-to-netlify` job

## Updating Existing Provider Docs

To update the docs for an existing provider, edit the corresponding markdown file or files in the `{provider}-docs` directory.  Raise a pull request into the `main` branch.  Once merged, the updated docs will be automatically published.  

### Running Locally

Install packages:  

```bash
yarn
```

To build a microsite locally, use `yarn build:{provider}`.  For example, to build the AWS microsite locally, run:

```
export NODE_OPTIONS=--max_old_space_size=4096
yarn run build:aws
```

To run a microsite locally, use `yarn start:{provider}`.  For example, to run the AWS microsite locally, run:  

```bash
yarn start:aws
```