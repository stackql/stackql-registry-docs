---
title: user_assigned_identities
hide_title: false
hide_table_of_contents: false
keywords:
  - user_assigned_identities
  - managed_identity
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
<tr><td><b>Name</b></td><td><code>user_assigned_identities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_identity.user_assigned_identities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties associated with the user assigned identity. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Gets the identity. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the userAssignedIdentities available under the specified ResourceGroup. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all the userAssignedIdentities available under the specified subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create or update an identity in the specified subscription and resource group. |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes the identity. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the userAssignedIdentities available under the specified ResourceGroup. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all the userAssignedIdentities available under the specified subscription. |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update an identity in the specified subscription and resource group. |
