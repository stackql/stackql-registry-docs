# stackql-registry-docs

This repository contains documentation for StackQL providers, which is published to [registry.stackql.io](https://registry.stackql.io).  This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.  

## Build and Deploy Status

| Type | Status | Link |
| --- | --- | -- |
| GitHub Actions Build | [![GitHub Actions](https://github.com/stackql/stackql-registry-docs/actions/workflows/build-docs.yaml/badge.svg?branch=main)](https://github.com/stackql/stackql-registry-docs/actions/workflows/build-docs.yaml) | [stackql-registry-docs/actions](https://github.com/stackql/stackql-registry-docs/actions) |
| Netlify Deploy Base | [![Netlify Status](https://api.netlify.com/api/v1/badges/75f838a9-79ea-41dc-96f9-a40dff50cfca/deploy-status)](https://app.netlify.com/sites/stackql-registry-docs/deploys) | [registry.stackql.io](https://registry.stackql.io) |
| Netlify Deploy AWS | [![Netlify Status](https://api.netlify.com/api/v1/badges/ef161c4a-63ea-4bcc-a5cb-5eaed30ed55f/deploy-status)](https://app.netlify.com/sites/stackql-aws-docs/deploys) | [aws-docs.stackql.io](https://aws-docs.stackql.io)<br/>[aws.stackql.io](https://aws.stackql.io) |
| Netlify Deploy Azure | [![Netlify Status](https://api.netlify.com/api/v1/badges/5e2cce2d-3c51-44df-bb14-4ee9c626ca02/deploy-status)](https://app.netlify.com/sites/stackql-azure-docs/deploys) | [azure-docs.stackql.io](https://azure-docs.stackql.io)<br/>[azure.stackql.io](https://azure.stackql.io) |
| Netlify Deploy Azure Extras | [![Netlify Status](https://api.netlify.com/api/v1/badges/218dfc50-e1ef-4742-bd95-199c67f4ea95/deploy-status)](https://app.netlify.com/sites/stackql-azure-extras-docs/deploys) | [azure-extras-docs.stackql.io](https://azure-extras-docs.stackql.io)<br/>[azure-extras.stackql.io](https://azure-extras.stackql.io) |
| Netlify Deploy Firebase | [![Netlify Status](https://api.netlify.com/api/v1/badges/6d8fec42-fba2-4d62-afef-30a821863314/deploy-status)](https://app.netlify.com/sites/stackql-firebase-docs/deploys) | [firebase-docs.stackql.io](https://firebase-docs.stackql.io)<br/>[firebase.stackql.io](https://firebase.stackql.io) |  
| Netlify Deploy GitHub | [![Netlify Status](https://api.netlify.com/api/v1/badges/625d7d38-37a9-4224-a9c8-6ee58141b109/deploy-status)](https://app.netlify.com/sites/stackql-github-docs/deploys) | [github-docs.stackql.io](https://github-docs.stackql.io)<br/>[github.stackql.io](https://github.stackql.io) |
| Netlify Deploy Google | [![Netlify Status](https://api.netlify.com/api/v1/badges/028e0d31-604b-4852-8b9b-77a71ead6b93/deploy-status)](https://app.netlify.com/sites/stackql-google-docs/deploys) | [google-docs.stackql.io](https://google-docs.stackql.io)<br/>[google.stackql.io](https://google.stackql.io) |
| Netlify Deploy K8S | [![Netlify Status](https://api.netlify.com/api/v1/badges/d11ea6c5-7a43-42d5-ac76-555112295b9b/deploy-status)](https://app.netlify.com/sites/stackql-k8s-docs/deploys) | [k8s-docs.stackql.io](https://k8s-docs.stackql.io)<br/>[k8s.stackql.io](https://k8s.stackql.io) |
| Netlify Deploy Netlify | [![Netlify Status](https://api.netlify.com/api/v1/badges/7d81e59f-e1de-480f-a6d5-5a52f83deb40/deploy-status)](https://app.netlify.com/sites/stackql-netlify-docs/deploys) | [netlify-docs.stackql.io](https://netlify-docs.stackql.io)<br/>[netlify.stackql.io](https://netlify.stackql.io) |
| Netlify Deploy Okta | [![Netlify Status](https://api.netlify.com/api/v1/badges/83d3788d-bbcf-4063-a2e7-65577e3f13f5/deploy-status)](https://app.netlify.com/sites/stackql-okta-docs/deploys) | [okta-docs.stackql.io](https://okta-docs.stackql.io)<br/>[okta.stackql.io](https://okta.stackql.io) |
| Netlify Deploy Sumologic | [![Netlify Status](https://api.netlify.com/api/v1/badges/6c864774-8494-41be-8e2c-441b6d1e368c/deploy-status)](https://app.netlify.com/sites/stackql-sumologic-docs/deploys) | [sumologic-docs.stackql.io](https://sumologic-docs.stackql.io)<br/>[sumologic.stackql.io](https://sumologic.stackql.io) |
| Netlify Deploy Digital Ocean | [![Netlify Status](https://api.netlify.com/api/v1/badges/ebcab4ef-d610-4888-a42f-314942d68c32/deploy-status)](https://app.netlify.com/sites/stackql-digitalocean-docs/deploys) | [digitalocean-docs.stackql.io](https://digitalocean-docs.stackql.io)<br/>[digitalocean.stackql.io](https://digitalocean.stackql.io) |
| Netlify Deploy Linode | [![Netlify Status](https://api.netlify.com/api/v1/badges/d0b573be-3dfb-495c-a0ce-478ec7acecd8/deploy-status)](https://app.netlify.com/sites/stackql-linode-docs/deploys) | [linode-docs.stackql.io](https://linode-docs.stackql.io)<br/>[linode.stackql.io](https://linode.stackql.io) |
| Netlify Deploy Vercel | [![Netlify Status](https://api.netlify.com/api/v1/badges/91cc31b7-0c25-443f-bb2f-71921ef7084e/deploy-status)](https://app.netlify.com/sites/stackql-vercel-docs/deploys) | [vercel-docs.stackql.io](https://vercel-docs.stackql.io)<br/>[vercel.stackql.io](https://vercel.stackql.io) |
| Netlify Deploy Godaddy | [![Netlify Status](https://api.netlify.com/api/v1/badges/8232458e-8e4f-47f2-81bf-bd4aad8b25d6/deploy-status)](https://app.netlify.com/sites/stackql-godaddy-docs/deploys) | [godaddy-docs.stackql.io](https://godaddy-docs.stackql.io)<br/>[godaddy.stackql.io](https://godaddy.stackql.io) |
| Netlify Deploy PagerDuty | [![Netlify Status](https://api.netlify.com/api/v1/badges/76c8752a-32d8-48e2-81ad-29b9e8f53edd/deploy-status)](https://app.netlify.com/sites/stackql-pagerduty-docs/deploys) | [pagerduty-docs.stackql.io](https://pagerduty-docs.stackql.io)<br/>[pagerduty.stackql.io](https://pagerduty.stackql.io) |
| Netlify Deploy Homebrew | [![Netlify Status](https://api.netlify.com/api/v1/badges/2343d34d-5061-4d83-98e6-475fb2150c94/deploy-status)](https://app.netlify.com/sites/stackql-homebrew-docs/deploys) | [homebrew-docs.stackql.io](https://homebrew-docs.stackql.io)<br/>[homebrew.stackql.io](https://homebrew.stackql.io) |
| Netlify Deploy Datadog | [![Netlify Status](https://api.netlify.com/api/v1/badges/9e76122d-09bd-4938-a50f-3b4196e94f0c/deploy-status)](https://app.netlify.com/sites/stackql-datadog-docs/deploys) | [datadog-docs.stackql.io](https://datadog-docs.stackql.io)<br/>[datadog.stackql.io](https://datadog.stackql.io) |


## Adding Docs for a New Provider

Adding docs for a new provider requires creating a new web property (subdomain) and will force an update to the root/base site and all other providers.  The steps are:  

- [ ] update `scripts/docgen/provider_data.py` with metadata for new provider
- [ ] generate docs for provider using `cd scripts; sh docgen.sh {provider}`
- [ ] publish docs for provider using `cd scripts; sh publish.sh {provider}`
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