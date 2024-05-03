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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.deployments.deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A string holding the unique ID of the deployment |
| <CopyableCode code="name" /> | `string` | The name of the project associated with the deployment at the time that the deployment was created |
| <CopyableCode code="_alias" /> | `array` | A list of all the aliases (default aliases, staging aliases and production aliases) that were assigned upon deployment creation |
| <CopyableCode code="_aliasAssigned" /> | `boolean` | A boolean that will be true when the aliases from the alias property were assigned successfully |
| <CopyableCode code="_aliasError" /> | `object` | An object that will contain a `code` and a `message` when the aliasing fails, otherwise the value will be `null` |
| <CopyableCode code="_aliasFinal" /> | `string` |  |
| <CopyableCode code="_aliasWarning" /> | `object` |  |
| <CopyableCode code="_autoAssignCustomDomains" /> | `boolean` |  |
| <CopyableCode code="_automaticAliases" /> | `array` |  |
| <CopyableCode code="_bootedAt" /> | `number` |  |
| <CopyableCode code="_buildErrorAt" /> | `number` |  |
| <CopyableCode code="_buildingAt" /> | `number` |  |
| <CopyableCode code="_canceledAt" /> | `number` |  |
| <CopyableCode code="_checksConclusion" /> | `string` |  |
| <CopyableCode code="_checksState" /> | `string` |  |
| <CopyableCode code="_createdAt" /> | `number` | A number containing the date when the deployment was created in milliseconds |
| <CopyableCode code="_creator" /> | `object` | Information about the deployment creator |
| <CopyableCode code="_errorCode" /> | `string` |  |
| <CopyableCode code="_errorLink" /> | `string` |  |
| <CopyableCode code="_errorMessage" /> | `string` |  |
| <CopyableCode code="_errorStep" /> | `string` |  |
| <CopyableCode code="_gitSource" /> | `` |  |
| <CopyableCode code="_id" /> | `string` | A string holding the unique ID of the deployment |
| <CopyableCode code="_lambdas" /> | `array` |  |
| <CopyableCode code="_meta" /> | `object` | An object containing the deployment's metadata |
| <CopyableCode code="_name" /> | `string` | The name of the project associated with the deployment at the time that the deployment was created |
| <CopyableCode code="_previewCommentsEnabled" /> | `boolean` | Whether or not preview comments are enabled for the deployment |
| <CopyableCode code="_public" /> | `boolean` | A boolean representing if the deployment is public or not. By default this is `false` |
| <CopyableCode code="_readyState" /> | `string` | The state of the deployment depending on the process of deploying, or if it is ready or in an error state |
| <CopyableCode code="_readySubstate" /> | `string` | The substate of the deployment when the state is "READY" |
| <CopyableCode code="_regions" /> | `array` | The regions the deployment exists in |
| <CopyableCode code="_source" /> | `string` | Where was the deployment created from |
| <CopyableCode code="_target" /> | `string` | If defined, either `staging` if a staging alias in the format `&lt;project&gt;.&lt;team&gt;.now.sh` was assigned upon creation, or `production` if the aliases from `alias` were assigned |
| <CopyableCode code="_team" /> | `object` | The team that owns the deployment if any |
| <CopyableCode code="_type" /> | `string` |  |
| <CopyableCode code="_url" /> | `string` | A string with the unique URL of the deployment |
| <CopyableCode code="_userAliases" /> | `array` | An array of domains that were provided by the user when creating the Deployment. |
| <CopyableCode code="_version" /> | `number` | The platform version that was used to create the deployment. |
| <CopyableCode code="alias" /> | `array` | A list of all the aliases (default aliases, staging aliases and production aliases) that were assigned upon deployment creation |
| <CopyableCode code="aliasAssigned" /> | `boolean` | A boolean that will be true when the aliases from the alias property were assigned successfully |
| <CopyableCode code="aliasAssignedAt" /> | `` |  |
| <CopyableCode code="aliasError" /> | `object` | An object that will contain a `code` and a `message` when the aliasing fails, otherwise the value will be `null` |
| <CopyableCode code="aliasFinal" /> | `string` |  |
| <CopyableCode code="aliasWarning" /> | `object` |  |
| <CopyableCode code="autoAssignCustomDomains" /> | `boolean` |  |
| <CopyableCode code="automaticAliases" /> | `array` |  |
| <CopyableCode code="bootedAt" /> | `number` |  |
| <CopyableCode code="build" /> | `object` |  |
| <CopyableCode code="buildErrorAt" /> | `number` |  |
| <CopyableCode code="buildingAt" /> | `number` |  |
| <CopyableCode code="builds" /> | `array` |  |
| <CopyableCode code="canceledAt" /> | `number` |  |
| <CopyableCode code="checksConclusion" /> | `string` |  |
| <CopyableCode code="checksState" /> | `string` |  |
| <CopyableCode code="connectBuildsEnabled" /> | `boolean` | The flag saying if Vercel Connect configuration is used for builds |
| <CopyableCode code="connectConfigurationId" /> | `string` | The ID of Vercel Connect configuration used for this deployment |
| <CopyableCode code="createdAt" /> | `number` | A number containing the date when the deployment was created in milliseconds |
| <CopyableCode code="createdIn" /> | `string` | The region where the deployment was first created |
| <CopyableCode code="creator" /> | `object` | Information about the deployment creator |
| <CopyableCode code="env" /> | `array` | The keys of the environment variables that were assigned during runtime |
| <CopyableCode code="errorCode" /> | `string` |  |
| <CopyableCode code="errorLink" /> | `string` |  |
| <CopyableCode code="errorMessage" /> | `string` |  |
| <CopyableCode code="errorStep" /> | `string` |  |
| <CopyableCode code="functions" /> | `object` | An object used to configure your Serverless Functions |
| <CopyableCode code="gitRepo" /> | `` |  |
| <CopyableCode code="gitSource" /> | `` |  |
| <CopyableCode code="inspectorUrl" /> | `string` | Vercel URL to inspect the deployment. |
| <CopyableCode code="isInConcurrentBuildsQueue" /> | `boolean` | Is the deployment currently queued waiting for a Concurrent Build Slot to be available |
| <CopyableCode code="lambdas" /> | `array` |  |
| <CopyableCode code="meta" /> | `object` | An object containing the deployment's metadata |
| <CopyableCode code="monorepoManager" /> | `string` | An monorepo manager that was used for the deployment |
| <CopyableCode code="ownerId" /> | `string` | The unique ID of the user or team the deployment belongs to |
| <CopyableCode code="plan" /> | `string` | The pricing plan the deployment was made under |
| <CopyableCode code="previewCommentsEnabled" /> | `boolean` | Whether or not preview comments are enabled for the deployment |
| <CopyableCode code="projectId" /> | `string` | The ID of the project the deployment is associated with |
| <CopyableCode code="public" /> | `boolean` | A boolean representing if the deployment is public or not. By default this is `false` |
| <CopyableCode code="readyState" /> | `string` | The state of the deployment depending on the process of deploying, or if it is ready or in an error state |
| <CopyableCode code="readySubstate" /> | `string` | The substate of the deployment when the state is "READY" |
| <CopyableCode code="regions" /> | `array` | The regions the deployment exists in |
| <CopyableCode code="routes" /> | `array` | A list of routes objects used to rewrite paths to point towards other internal or external paths |
| <CopyableCode code="source" /> | `string` | Where was the deployment created from |
| <CopyableCode code="target" /> | `string` | If defined, either `staging` if a staging alias in the format `&lt;project&gt;.&lt;team&gt;.now.sh` was assigned upon creation, or `production` if the aliases from `alias` were assigned |
| <CopyableCode code="team" /> | `object` | The team that owns the deployment if any |
| <CopyableCode code="type" /> | `string` |  |
| <CopyableCode code="url" /> | `string` | A string with the unique URL of the deployment |
| <CopyableCode code="userAliases" /> | `array` | An array of domains that were provided by the user when creating the Deployment. |
| <CopyableCode code="version" /> | `number` | The platform version that was used to create the deployment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_deployment" /> | `SELECT` | <CopyableCode code="idOrUrl, teamId" /> | Retrieves information for a deployment either by supplying its ID (`id` property) or Hostname (`url` property). Additional details will be included when the authenticated user or team is an owner of the deployment. |
| <CopyableCode code="get_deployments" /> | `SELECT` | <CopyableCode code="teamId" /> | List deployments under the authenticated user or team. If a deployment hasn't finished uploading (is incomplete), the `url` property will have a value of `null`. |
| <CopyableCode code="create_deployment" /> | `INSERT` | <CopyableCode code="teamId, data__branch, data__connection_uris, data__database, data__databases, data__endpoint, data__endpoints, data__name, data__pagination, data__password, data__project, data__projects, data__role, data__roles" /> | Create a new deployment with all the required and intended data. If the deployment is not a git deployment, all files must be provided with the request, either referenced or inlined. Additionally, a deployment id can be specified to redeploy a previous deployment. |
| <CopyableCode code="delete_deployment" /> | `DELETE` | <CopyableCode code="id, teamId" /> | This API allows you to delete a deployment, either by supplying its `id` in the URL or the `url` of the deployment as a query parameter. You can obtain the ID, for example, by listing all deployments. |
| <CopyableCode code="_get_deployments" /> | `EXEC` | <CopyableCode code="teamId" /> | List deployments under the authenticated user or team. If a deployment hasn't finished uploading (is incomplete), the `url` property will have a value of `null`. |
| <CopyableCode code="cancel_deployment" /> | `EXEC` | <CopyableCode code="id, teamId" /> | This endpoint allows you to cancel a deployment which is currently building, by supplying its `id` in the URL. |
