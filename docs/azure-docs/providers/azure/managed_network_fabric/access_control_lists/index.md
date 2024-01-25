---
title: access_control_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - access_control_lists
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>access_control_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.access_control_lists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Access Control List Properties defines the resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accessControlListName, resourceGroupName, subscriptionId` | Implements Access Control List GET method. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Implements AccessControlLists list by resource group GET method. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Implements AccessControlLists list by subscription GET method. |
| `create` | `INSERT` | `accessControlListName, resourceGroupName, subscriptionId, data__location, data__properties` | Implements Access Control List PUT method. |
| `delete` | `DELETE` | `accessControlListName, resourceGroupName, subscriptionId` | Implements Access Control List DELETE method. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Implements AccessControlLists list by resource group GET method. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Implements AccessControlLists list by subscription GET method. |
| `resync` | `EXEC` | `accessControlListName, resourceGroupName, subscriptionId` | Implements the operation to the underlying resources. |
| `update` | `EXEC` | `accessControlListName, resourceGroupName, subscriptionId` | API to update certain properties of the Access Control List resource. |
| `validate_configuration` | `EXEC` | `accessControlListName, resourceGroupName, subscriptionId` | Implements the operation to the underlying resources. |
