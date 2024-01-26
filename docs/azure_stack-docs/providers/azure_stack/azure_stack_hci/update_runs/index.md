---
title: update_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - update_runs
  - azure_stack_hci
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
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack_hci.update_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Details of an Update run |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId, updateName, updateRunName` | Get the Update run for a specified update |
| `list` | `SELECT` | `clusterName, resourceGroupName, subscriptionId, updateName` | List all Update runs for a specified update |
| `delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId, updateName, updateRunName` | Delete specified Update Run |
| `_list` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, updateName` | List all Update runs for a specified update |
| `put` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, updateName, updateRunName` | Put Update runs for a specified update |
