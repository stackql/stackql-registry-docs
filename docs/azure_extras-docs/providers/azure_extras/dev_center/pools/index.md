---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - dev_center
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_center.pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of a Pool |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Pools_Get` | `SELECT` |  | Gets a machine pool |
| `Pools_ListByProject` | `SELECT` |  | Lists pools for a project |
| `Pools_CreateOrUpdate` | `INSERT` |  | Creates or updates a machine pool |
| `Pools_Delete` | `DELETE` |  | Deletes a machine pool |
| `Pools_Update` | `EXEC` |  | Partially updates a machine pool |
