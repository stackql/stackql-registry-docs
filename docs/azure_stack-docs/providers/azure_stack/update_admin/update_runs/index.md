---
title: update_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - update_runs
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
<tr><td><b>Name</b></td><td><code>update_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.update_admin.update_runs</code></td></tr>
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
| `get` | `SELECT` | `resourceGroupName, runName, subscriptionId, updateLocation, updateName` | Get an instance of update run using the ID. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, updateLocation, updateName` | Get the list of update runs. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, updateLocation, updateName` | Get the list of update runs. |
| `rerun` | `EXEC` | `resourceGroupName, runName, subscriptionId, updateLocation, updateName` | Resume a failed update. |
