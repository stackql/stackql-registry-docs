---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - managed_applications
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_applications.applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `kind` | `string` | The kind of the managed application. Allowed values are MarketPlace and ServiceCatalog. |
| `managedBy` | `string` | ID of the resource that manages this resource. |
| `plan` | `object` | Plan for the managed application. |
| `properties` | `object` | The managed application properties. |
| `sku` | `object` | SKU for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationName, resourceGroupName, subscriptionId` | Gets the managed application. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the applications within a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all the applications within a subscription. |
| `create_or_update` | `INSERT` | `applicationName, resourceGroupName, subscriptionId, data__kind, data__properties` | Creates or updates a managed application. |
| `delete` | `DELETE` | `applicationName, resourceGroupName, subscriptionId` | Deletes the managed application. |
| `delete_by_id` | `DELETE` | `applicationId` | Deletes the managed application. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the applications within a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all the applications within a subscription. |
| `create_or_update_by_id` | `EXEC` | `applicationId, data__kind, data__properties` | Creates or updates a managed application. |
| `get_by_id` | `EXEC` | `applicationId` | Gets the managed application. |
| `refresh_permissions` | `EXEC` | `applicationName, resourceGroupName, subscriptionId` | Refresh Permissions for application. |
| `update` | `EXEC` | `applicationName, resourceGroupName, subscriptionId` | Updates an existing managed application. |
| `update_by_id` | `EXEC` | `applicationId` | Updates an existing managed application. |
