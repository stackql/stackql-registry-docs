---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - dev_center
  - azure    
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
<tr><td><b>Id</b></td><td><code>azure.dev_center.pools</code></td></tr>
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
| `get` | `SELECT` |  | Gets a machine pool |
| `list_by_project` | `SELECT` |  | Lists pools for a project |
| `create_or_update` | `INSERT` |  | Creates or updates a machine pool |
| `delete` | `DELETE` |  | Deletes a machine pool |
| `_list_by_project` | `EXEC` |  | Lists pools for a project |
| `run_health_checks` | `EXEC` | `poolName, projectName, resourceGroupName, subscriptionId` | Triggers a refresh of the pool status. |
| `update` | `EXEC` |  | Partially updates a machine pool |
