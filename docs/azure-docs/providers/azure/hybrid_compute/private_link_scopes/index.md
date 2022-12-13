---
title: private_link_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_scopes
  - hybrid_compute
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
<tr><td><b>Name</b></td><td><code>private_link_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_compute.private_link_scopes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Azure resource type |
| `location` | `string` | Resource location |
| `properties` | `object` | Properties that define a Azure Arc PrivateLinkScope resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateLinkScopes_Get` | `SELECT` | `resourceGroupName, scopeName, subscriptionId` | Returns a Azure Arc PrivateLinkScope. |
| `PrivateLinkScopes_List` | `SELECT` | `subscriptionId` | Gets a list of all Azure Arc PrivateLinkScopes within a subscription. |
| `PrivateLinkScopes_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of Azure Arc PrivateLinkScopes within a resource group. |
| `PrivateLinkScopes_CreateOrUpdate` | `INSERT` | `resourceGroupName, scopeName, subscriptionId` | Creates (or updates) a Azure Arc PrivateLinkScope. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation. |
| `PrivateLinkScopes_Delete` | `DELETE` | `resourceGroupName, scopeName, subscriptionId` | Deletes a Azure Arc PrivateLinkScope. |
| `PrivateLinkScopes_GetValidationDetails` | `EXEC` | `location, privateLinkScopeId, subscriptionId` | Returns a Azure Arc PrivateLinkScope's validation details. |
| `PrivateLinkScopes_GetValidationDetailsForMachine` | `EXEC` | `machineName, resourceGroupName, subscriptionId` | Returns a Azure Arc PrivateLinkScope's validation details for a given machine. |
| `PrivateLinkScopes_UpdateTags` | `EXEC` | `resourceGroupName, scopeName, subscriptionId` | Updates an existing PrivateLinkScope's tags. To update other fields use the CreateOrUpdate method. |
