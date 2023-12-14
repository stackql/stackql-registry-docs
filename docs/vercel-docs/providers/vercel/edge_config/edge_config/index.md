---
title: edge_config
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_config
  - edge_config
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
<tr><td><b>Name</b></td><td><code>edge_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.edge_config.edge_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `createdAt` | `number` |  |
| `digest` | `string` |  |
| `itemCount` | `number` |  |
| `ownerId` | `string` |  |
| `sizeInBytes` | `number` |  |
| `slug` | `string` | Name for the Edge Config Names are not unique. Must start with an alphabetic character and can contain only alphanumeric characters and underscores). |
| `transfer` | `object` | Keeps track of the current state of the Edge Config while it gets transferred. |
| `updatedAt` | `number` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_edge_config` | `SELECT` | `edgeConfigId, teamId` | Returns an Edge Config. |
| `get_edge_configs` | `SELECT` | `teamId` | Returns all Edge Configs. |
| `create_edge_config` | `INSERT` | `teamId, data__slug` | Creates an Edge Config. |
| `delete_edge_config` | `DELETE` | `edgeConfigId, teamId` | Delete an Edge Config by id. |
| `update_edge_config` | `EXEC` | `edgeConfigId, teamId, data__slug` | Updates an Edge Config. |
