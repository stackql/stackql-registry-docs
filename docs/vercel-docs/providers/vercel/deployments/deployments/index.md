---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - deployments
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.deployments.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A string holding the unique ID of the deployment |
| `name` | `string` | The name of the project associated with the deployment at the time that the deployment was created |
| `_alias` | `array` | A list of all the aliases (default aliases, staging aliases and production aliases) that were assigned upon deployment creation |
| `_aliasAssigned` | `boolean` | A boolean that will be true when the aliases from the alias property were assigned successfully |
| `_aliasError` | `object` | An object that will contain a `code` and a `message` when the aliasing fails, otherwise the value will be `null` |
| `_aliasFinal` | `string` |  |
| `_aliasWarning` | `object` |  |
| `_autoAssignCustomDomains` | `boolean` |  |
| `_automaticAliases` | `array` |  |
| `_bootedAt` | `number` |  |
| `_buildErrorAt` | `number` |  |
| `_buildingAt` | `number` |  |
| `_canceledAt` | `number` |  |
| `_checksConclusion` | `string` |  |
| `_checksState` | `string` |  |
| `_createdAt` | `number` | A number containing the date when the deployment was created in milliseconds |
| `_creator` | `object` | Information about the deployment creator |
| `_errorCode` | `string` |  |
| `_errorLink` | `string` |  |
| `_errorMessage` | `string` |  |
| `_errorStep` | `string` |  |
| `_gitSource` | `` |  |
| `_id` | `string` | A string holding the unique ID of the deployment |
| `_lambdas` | `array` |  |
| `_meta` | `object` | An object containing the deployment's metadata |
| `_name` | `string` | The name of the project associated with the deployment at the time that the deployment was created |
| `_previewCommentsEnabled` | `boolean` | Whether or not preview comments are enabled for the deployment |
| `_public` | `boolean` | A boolean representing if the deployment is public or not. By default this is `false` |
| `_readyState` | `string` | The state of the deployment depending on the process of deploying, or if it is ready or in an error state |
| `_readySubstate` | `string` | The substate of the deployment when the state is "READY" |
| `_regions` | `array` | The regions the deployment exists in |
| `_source` | `string` | Where was the deployment created from |
| `_target` | `string` | If defined, either `staging` if a staging alias in the format `&lt;project&gt;.&lt;team&gt;.now.sh` was assigned upon creation, or `production` if the aliases from `alias` were assigned |
| `_team` | `object` | The team that owns the deployment if any |
| `_type` | `string` |  |
| `_url` | `string` | A string with the unique URL of the deployment |
| `_userAliases` | `array` | An array of domains that were provided by the user when creating the Deployment. |
| `_version` | `number` | The platform version that was used to create the deployment. |
| `alias` | `array` | A list of all the aliases (default aliases, staging aliases and production aliases) that were assigned upon deployment creation |
| `aliasAssigned` | `boolean` | A boolean that will be true when the aliases from the alias property were assigned successfully |
| `aliasAssignedAt` | `` |  |
| `aliasError` | `object` | An object that will contain a `code` and a `message` when the aliasing fails, otherwise the value will be `null` |
| `aliasFinal` | `string` |  |
| `aliasWarning` | `object` |  |
| `autoAssignCustomDomains` | `boolean` |  |
| `automaticAliases` | `array` |  |
| `bootedAt` | `number` |  |
| `build` | `object` |  |
| `buildErrorAt` | `number` |  |
| `buildingAt` | `number` |  |
| `builds` | `array` |  |
| `canceledAt` | `number` |  |
| `checksConclusion` | `string` |  |
| `checksState` | `string` |  |
| `connectBuildsEnabled` | `boolean` | The flag saying if Vercel Connect configuration is used for builds |
| `connectConfigurationId` | `string` | The ID of Vercel Connect configuration used for this deployment |
| `createdAt` | `number` | A number containing the date when the deployment was created in milliseconds |
| `createdIn` | `string` | The region where the deployment was first created |
| `creator` | `object` | Information about the deployment creator |
| `env` | `array` | The keys of the environment variables that were assigned during runtime |
| `errorCode` | `string` |  |
| `errorLink` | `string` |  |
| `errorMessage` | `string` |  |
| `errorStep` | `string` |  |
| `functions` | `object` | An object used to configure your Serverless Functions |
| `gitRepo` | `` |  |
| `gitSource` | `` |  |
| `inspectorUrl` | `string` | Vercel URL to inspect the deployment. |
| `isInConcurrentBuildsQueue` | `boolean` | Is the deployment currently queued waiting for a Concurrent Build Slot to be available |
| `lambdas` | `array` |  |
| `meta` | `object` | An object containing the deployment's metadata |
| `monorepoManager` | `string` | An monorepo manager that was used for the deployment |
| `ownerId` | `string` | The unique ID of the user or team the deployment belongs to |
| `plan` | `string` | The pricing plan the deployment was made under |
| `previewCommentsEnabled` | `boolean` | Whether or not preview comments are enabled for the deployment |
| `projectId` | `string` | The ID of the project the deployment is associated with |
| `public` | `boolean` | A boolean representing if the deployment is public or not. By default this is `false` |
| `readyState` | `string` | The state of the deployment depending on the process of deploying, or if it is ready or in an error state |
| `readySubstate` | `string` | The substate of the deployment when the state is "READY" |
| `regions` | `array` | The regions the deployment exists in |
| `routes` | `array` | A list of routes objects used to rewrite paths to point towards other internal or external paths |
| `source` | `string` | Where was the deployment created from |
| `target` | `string` | If defined, either `staging` if a staging alias in the format `&lt;project&gt;.&lt;team&gt;.now.sh` was assigned upon creation, or `production` if the aliases from `alias` were assigned |
| `team` | `object` | The team that owns the deployment if any |
| `type` | `string` |  |
| `url` | `string` | A string with the unique URL of the deployment |
| `userAliases` | `array` | An array of domains that were provided by the user when creating the Deployment. |
| `version` | `number` | The platform version that was used to create the deployment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_deployment` | `SELECT` | `idOrUrl, teamId` | Retrieves information for a deployment either by supplying its ID (`id` property) or Hostname (`url` property). Additional details will be included when the authenticated user or team is an owner of the deployment. |
| `get_deployments` | `SELECT` | `teamId` | List deployments under the authenticated user or team. If a deployment hasn't finished uploading (is incomplete), the `url` property will have a value of `null`. |
| `create_deployment` | `INSERT` | `teamId, data__branch, data__connection_uris, data__database, data__databases, data__endpoint, data__endpoints, data__name, data__pagination, data__password, data__project, data__projects, data__role, data__roles` | Create a new deployment with all the required and intended data. If the deployment is not a git deployment, all files must be provided with the request, either referenced or inlined. Additionally, a deployment id can be specified to redeploy a previous deployment. |
| `delete_deployment` | `DELETE` | `id, teamId` | This API allows you to delete a deployment, either by supplying its `id` in the URL or the `url` of the deployment as a query parameter. You can obtain the ID, for example, by listing all deployments. |
| `_get_deployments` | `EXEC` | `teamId` | List deployments under the authenticated user or team. If a deployment hasn't finished uploading (is incomplete), the `url` property will have a value of `null`. |
| `cancel_deployment` | `EXEC` | `id, teamId` | This endpoint allows you to cancel a deployment which is currently building, by supplying its `id` in the URL. |
