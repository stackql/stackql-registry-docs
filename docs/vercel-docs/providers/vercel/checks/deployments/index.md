---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - checks
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
<tr><td><b>Id</b></td><td><code>vercel.checks.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `blocking` | `boolean` |
| `completedAt` | `number` |
| `conclusion` | `string` |
| `createdAt` | `number` |
| `deploymentId` | `string` |
| `detailsUrl` | `string` |
| `externalId` | `string` |
| `integrationId` | `string` |
| `output` | `object` |
| `path` | `string` |
| `rerequestable` | `boolean` |
| `startedAt` | `number` |
| `status` | `string` |
| `updatedAt` | `number` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_all_checks` | `SELECT` | `deploymentId, teamId` | List all of the checks created for a deployment. |
| `get_check` | `SELECT` | `checkId, deploymentId, teamId` | Return a detailed response for a single check. |
| `create_check` | `INSERT` | `deploymentId, teamId, data__blocking, data__name` | Creates a new check. This endpoint must be called with an OAuth2 or it will produce a 400 error. |
| `_get_all_checks` | `EXEC` | `deploymentId, teamId` | List all of the checks created for a deployment. |
| `rerequest_check` | `EXEC` | `checkId, deploymentId, teamId` | Rerequest a selected check that has failed. |
| `update_check` | `EXEC` | `checkId, deploymentId, teamId` | Update an existing check. This endpoint must be called with an OAuth2 or it will produce a 400 error. |
