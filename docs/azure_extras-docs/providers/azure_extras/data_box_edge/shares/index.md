---
title: shares
hide_title: false
hide_table_of_contents: false
keywords:
  - shares
  - data_box_edge
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
<tr><td><b>Name</b></td><td><code>shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_box_edge.shares</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `properties` | `object` | The share properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Shares_Get` | `SELECT` | `deviceName, name, resourceGroupName, subscriptionId` |  |
| `Shares_ListByDataBoxEdgeDevice` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` |  |
| `Shares_CreateOrUpdate` | `INSERT` | `deviceName, name, resourceGroupName, subscriptionId, data__properties` |  |
| `Shares_Delete` | `DELETE` | `deviceName, name, resourceGroupName, subscriptionId` | Deletes the share on the Data Box Edge/Data Box Gateway device. |
| `Shares_Refresh` | `EXEC` | `deviceName, name, resourceGroupName, subscriptionId` |  |
