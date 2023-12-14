---
title: env
hide_title: false
hide_table_of_contents: false
keywords:
  - env
  - projects
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
<tr><td><b>Name</b></td><td><code>env</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.projects.env</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `configurationId` | `string` |  |
| `contentHint` | `` |  |
| `createdAt` | `number` |  |
| `createdBy` | `string` |  |
| `decrypted` | `boolean` | Whether `value` is decrypted. |
| `edgeConfigId` | `string` |  |
| `edgeConfigTokenId` | `string` |  |
| `gitBranch` | `string` |  |
| `key` | `string` |  |
| `target` | `` |  |
| `type` | `string` |  |
| `updatedAt` | `number` |  |
| `updatedBy` | `string` |  |
| `value` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_project_env` | `SELECT` | `id, idOrName, teamId` | Retrieve the environment variable for a given project. |
| `create_project_env` | `INSERT` | `idOrName, teamId` | Create one ore more environment variables for a project by passing its `key`, `value`, `type` and `target` and by specifying the project by either passing the project `id` or `name` in the URL. |
| `remove_project_env` | `DELETE` | `id, idOrName, teamId` | Delete a specific environment variable for a given project by passing the environment variable identifier and either passing the project `id` or `name` in the URL. |
| `edit_project_env` | `EXEC` | `id, idOrName, teamId` | Edit a specific environment variable for a given project by passing the environment variable identifier and either passing the project `id` or `name` in the URL. |
| `filter_project_envs` | `EXEC` | `idOrName, teamId` | Retrieve the environment variables for a given project by passing either the project `id` or `name` in the URL. |
