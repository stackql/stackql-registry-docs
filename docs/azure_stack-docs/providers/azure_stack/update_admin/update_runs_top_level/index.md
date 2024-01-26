---
title: update_runs_top_level
hide_title: false
hide_table_of_contents: false
keywords:
  - update_runs_top_level
  - update_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>update_runs_top_level</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.update_admin.update_runs_top_level</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Region location of resource. |
| `properties` | `object` | Properties of an update run. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, runName, subscriptionId, updateLocation` | Get an instance of update run using the ID. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, updateLocation` | Get the list of update runs. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, updateLocation` | Get the list of update runs. |
