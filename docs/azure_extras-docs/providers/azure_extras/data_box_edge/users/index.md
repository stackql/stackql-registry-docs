---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_box_edge.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `properties` | `object` | The user properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Users_Get` | `SELECT` | `deviceName, name, resourceGroupName, subscriptionId` | Gets the properties of the specified user. |
| `Users_ListByDataBoxEdgeDevice` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` | Gets all the users registered on a Data Box Edge/Data Box Gateway device. |
| `Users_CreateOrUpdate` | `INSERT` | `deviceName, name, resourceGroupName, subscriptionId, data__properties` | Creates a new user or updates an existing user's information on a Data Box Edge/Data Box Gateway device. |
| `Users_Delete` | `DELETE` | `deviceName, name, resourceGroupName, subscriptionId` | Deletes the user on a databox edge/gateway device. |
