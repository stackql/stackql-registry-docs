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
| Netlify Deploy Google Ads | [![Netlify Status](https://api.netlify.com/api/v1/badges/c1e3ba8b-af1c-42b0-a703-e1309ca9f1de/deploy-status)](https://app.netlify.com/sites/stackql-googleads-docs/deploys) | [googleads-docs.stackql.io](https://googleads-docs.stackql.io)<br/>[googleads.stackql.io](https://googleads.stackql.io) |
| Netlify Deploy Google Analytics | [![Netlify Status](https://api.netlify.com/api/v1/badges/ca05bc55-e377-4ac5-9eaa-403ee64158b5/deploy-status)](https://app.netlify.com/sites/stackql-googleanalytics-docs/deploys) | [googleanalytics-docs.stackql.io](https://googleanalytics-docs.stackql.io)<br/>[googleanalytics.stackql.io](https://googleanalytics.stackql.io) |
| Netlify Deploy Google Developers | [![Netlify Status](https://api.netlify.com/api/v1/badges/c5c95268-3619-4169-ba84-cfd007d63a3b/deploy-status)](https://app.netlify.com/sites/stackql-googledevelopers-docs/deploys) | [googledevelopers-docs.stackql.io](https://googledevelopers-docs.stackql.io)<br/>[googledevelopers.stackql.io](https://googledevelopers.stackql.io) |
| Netlify Deploy Google MyBusiness | [![Netlify Status](https://api.netlify.com/api/v1/badges/49659b34-f334-43fb-9267-1884ebfbbf67/deploy-status)](https://app.netlify.com/sites/stackql-googlemybusiness-docs/deploys) | [googlemybusiness-docs.stackql.io](https://googlemybusiness-docs.stackql.io)<br/>[googlemybusiness.stackql.io](https://googlemybusiness.stackql.io) |
| Netlify Deploy Google Workspace | [![Netlify Status](https://api.netlify.com/api/v1/badges/ad4ddc57-c98d-4e48-8426-086709089f04/deploy-status)](https://app.netlify.com/sites/stackql-googleworkspace-docs/deploys) | [googleworkspace-docs.stackql.io](https://googleworkspace-docs.stackql.io)<br/>[googleworkspace.stackql.io](https://googleworkspace.stackql.io) |
| Netlify Deploy Youtube | [![Netlify Status](https://api.netlify.com/api/v1/badges/a480d2db-cb95-4d79-be90-6ad5568c1feb/deploy-status)](https://app.netlify.com/sites/stackql-youtube-docs/deploys) | [youtube-docs.stackql.io](https://youtube-docs.stackql.io)<br/>[youtube.stackql.io](https://youtube.stackql.io) |


## Adding Docs for a New Provider

Adding docs for a new provider requires creating a new web property (subdomain) and will force an update to the root/base site and all other providers.  The steps are:  

- create a new netlify site (`stackql-{provider}-docs`)
- add `NETLIFY` record in Netlify DNS (mapping `{provider}.stackql.io to `stackql-{provider}-docs.netlify.app`)
- add GitHub Actions secret for netlify site id - `NETLIFY_SITE_ID_{PROVIDER}`
- add the Netlify deploy status badge to the table in this `README` (see above)
- update the `providers` array in `sidebars.js` with the new provider
- update the `providers` array `src/configs/providers.ts` with the new provider
- update `package.json` with new `start` and `build` scripts
- update frontmatter in the `index.md` at the root of the new providers docs, set `slug` to `/providers/{provider}` and `id` to `{provider}-doc`
- update `allProviders` in `ci-scripts/get-providers-to-deploy.js` with the new provider
- add the new provider docs to `docs/{provider}-docs` (following directory structure of existing providers)
- update `stackql-provider-registry.mdx` in the root of the new provider to add the `currentProvider` prop, e.g. `<RegistryPage currentProvider="okta" />`
- add the root site redirects for provider vanity urls to `.github/workflows/build-docs.yaml` to the `add redirects to root site` step of the `deploy-to-netlify` job

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