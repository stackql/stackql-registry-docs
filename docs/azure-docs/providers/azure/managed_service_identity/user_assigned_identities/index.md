---
title: user_assigned_identities
hide_title: false
hide_table_of_contents: false
keywords:
  - user_assigned_identities
  - managed_service_identity
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
<tr><td><b>Id</b></td><td><code>azure.managed_service_identity.user_assigned_identities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `type` | `string` | The identity type. |
| `principalId` | `string` | The principal ID of resource identity. |
| `tenantId` | `string` | The tenant ID of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `UserAssignedIdentities_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Gets the identity. |
| `UserAssignedIdentities_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the userAssignedIdentities available under the specified ResourceGroup. |
| `UserAssignedIdentities_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all the userAssignedIdentities available under the specified subscription. |
| `UserAssignedIdentities_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create or update an identity in the specified subscription and resource group. |
| `UserAssignedIdentities_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes the identity. |
| `UserAssignedIdentities_ListAssociatedResources` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Lists the associated resources for this identity. |
| `UserAssignedIdentities_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update an identity in the specified subscription and resource group. |
