---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
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
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_box_edge.triggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The hierarchical type of the object. |
| `kind` | `string` | Trigger Kind. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Triggers_Get` | `SELECT` | `deviceName, name, resourceGroupName, subscriptionId` | Get a specific trigger by name. |
| `Triggers_ListByDataBoxEdgeDevice` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` | Lists all the triggers configured in the device. |
| `Triggers_CreateOrUpdate` | `INSERT` | `deviceName, name, resourceGroupName, subscriptionId, data__kind` | Creates or updates a trigger. |
| `Triggers_Delete` | `DELETE` | `deviceName, name, resourceGroupName, subscriptionId` | Deletes the trigger on the gateway device. |
