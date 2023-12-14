---
title: items
hide_title: false
hide_table_of_contents: false
keywords:
  - items
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
<tr><td><b>Name</b></td><td><code>items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.edge_config.items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `createdAt` | `number` |
| `edgeConfigId` | `string` |
| `key` | `string` |
| `updatedAt` | `number` |
| `value` | `` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_edge_config_items` | `SELECT` | `edgeConfigId, teamId` | Returns all items of an Edge Config. |
| `patcht_edge_config_items` | `EXEC` | `edgeConfigId, teamId, data__items` | Update multiple Edge Config Items in batch. |
