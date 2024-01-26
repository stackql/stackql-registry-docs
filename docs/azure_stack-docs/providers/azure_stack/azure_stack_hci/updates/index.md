---
title: updates
hide_title: false
hide_table_of_contents: false
keywords:
  - updates
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
<tr><td><b>Name</b></td><td><code>updates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack_hci.updates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Details of a singular Update in HCI Cluster |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId, updateName` | Get specified Update |
| `list` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | List all Updates |
| `delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId, updateName` | Delete specified Update |
| `_list` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | List all Updates |
| `post` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, updateName` | Apply Update |
| `put` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, updateName` | Put specified Update |
