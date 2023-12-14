---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
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
<tr><td><b>Name</b></td><td><code>tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.edge_config.tokens</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | This is not the token itself, but rather an id to identify the token by |
| `createdAt` | `number` |  |
| `edgeConfigId` | `string` |  |
| `label` | `string` |  |
| `token` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_edge_config_tokens` | `SELECT` | `edgeConfigId, teamId` | Returns all tokens of an Edge Config. |
| `delete_edge_config_tokens` | `DELETE` | `edgeConfigId, teamId, data__tokens` | Deletes one or more tokens of an existing Edge Config. |
