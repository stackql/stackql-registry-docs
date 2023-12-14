---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - aliases
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
<tr><td><b>Id</b></td><td><code>vercel.aliases.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `alias` | `string` | The alias name, it could be a `.vercel.app` subdomain or a custom domain |
| `created` | `string` | The date when the alias was created |
| `protectionBypass` | `object` | The protection bypass for the alias |
| `redirect` | `string` | Target destination domain for redirect when the alias is a redirect |
| `uid` | `string` | The unique identifier of the alias |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_deployment_aliases` | `SELECT` | `id, teamId` | Retrieves all Aliases for the Deployment with the given ID. The authenticated user or team must own the deployment. |
| `_list_deployment_aliases` | `EXEC` | `id, teamId` | Retrieves all Aliases for the Deployment with the given ID. The authenticated user or team must own the deployment. |
| `assign_alias` | `EXEC` | `id, teamId` | Creates a new alias for the deployment with the given deployment ID. The authenticated user or team must own this deployment. If the desired alias is already assigned to another deployment, then it will be removed from the old deployment and assigned to the new one. |
