---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - solutions
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.solutions.applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `plan` | `object` | Plan for the managed application. |
| `properties` | `object` | The managed application properties. |
| `sku` | `object` | SKU for the resource. |
| `identity` | `object` | Identity for the resource. |
| `kind` | `string` | The kind of the managed application. Allowed values are MarketPlace and ServiceCatalog. |
| `managedBy` | `string` | ID of the resource that manages this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Applications_Get` | `SELECT` | `applicationName, resourceGroupName, subscriptionId` | Gets the managed application. |
| `Applications_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the applications within a resource group. |
| `Applications_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all the applications within a subscription. |
| `Applications_CreateOrUpdate` | `INSERT` | `applicationName, resourceGroupName, subscriptionId, data__kind, data__properties` | Creates or updates a managed application. |
| `Applications_Delete` | `DELETE` | `applicationName, resourceGroupName, subscriptionId` | Deletes the managed application. |
| `Applications_DeleteById` | `DELETE` | `applicationId` | Deletes the managed application. |
| `Applications_CreateOrUpdateById` | `EXEC` | `applicationId, data__kind, data__properties` | Creates or updates a managed application. |
| `Applications_GetById` | `EXEC` | `applicationId` | Gets the managed application. |
| `Applications_ListAllowedUpgradePlans` | `EXEC` | `applicationName, resourceGroupName, subscriptionId` | List allowed upgrade plans for application. |
| `Applications_ListTokens` | `EXEC` | `applicationName, resourceGroupName, subscriptionId` | List tokens for application. |
| `Applications_RefreshPermissions` | `EXEC` | `applicationName, resourceGroupName, subscriptionId` | Refresh Permissions for application. |
| `Applications_Update` | `EXEC` | `applicationName, resourceGroupName, subscriptionId` | Updates an existing managed application. |
| `Applications_UpdateAccess` | `EXEC` | `applicationName, resourceGroupName, subscriptionId, data__metadata, data__status, data__subStatus` | Update access for application. |
| `Applications_UpdateById` | `EXEC` | `applicationId` | Updates an existing managed application. |
