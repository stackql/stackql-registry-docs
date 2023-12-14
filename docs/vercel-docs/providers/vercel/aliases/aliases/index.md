---
title: aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases
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
<tr><td><b>Name</b></td><td><code>aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.aliases.aliases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `alias` | `string` | The alias name, it could be a `.vercel.app` subdomain or a custom domain |
| `created` | `string` | The date when the alias was created |
| `createdAt` | `number` | The date when the alias was created in milliseconds since the UNIX epoch |
| `creator` | `object` | Information of the user who created the alias |
| `deletedAt` | `number` | The date when the alias was deleted in milliseconds since the UNIX epoch |
| `deployment` | `object` | A map with the deployment ID, URL and metadata |
| `deploymentId` | `string` | The deployment ID |
| `projectId` | `string` | The unique identifier of the project |
| `protectionBypass` | `object` | The protection bypass for the alias |
| `redirect` | `string` | Target destination domain for redirect when the alias is a redirect |
| `redirectStatusCode` | `number` | Status code to be used on redirect |
| `uid` | `string` | The unique identifier of the alias |
| `updatedAt` | `number` | The date when the alias was updated in milliseconds since the UNIX epoch |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_alias` | `SELECT` | `idOrAlias, teamId` | Retrieves an Alias for the given host name or alias ID. |
| `list_aliases` | `SELECT` | `teamId` | Retrieves a list of aliases for the authenticated User or Team. When `domain` is provided, only aliases for that domain will be returned. When `projectId` is provided, it will only return the given project aliases. |
| `delete_alias` | `DELETE` | `aliasId, teamId` | Delete an Alias with the specified ID. |
| `_list_aliases` | `EXEC` | `teamId` | Retrieves a list of aliases for the authenticated User or Team. When `domain` is provided, only aliases for that domain will be returned. When `projectId` is provided, it will only return the given project aliases. |
