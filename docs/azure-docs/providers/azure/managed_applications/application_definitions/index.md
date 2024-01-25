---
title: application_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - application_definitions
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
<tr><td><b>Name</b></td><td><code>application_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_applications.application_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `managedBy` | `string` | ID of the resource that manages this resource. |
| `properties` | `object` | The managed application definition properties. |
| `sku` | `object` | SKU for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationDefinitionName, resourceGroupName, subscriptionId` | Gets the managed application definition. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the managed application definitions in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all the application definitions within a subscription. |
| `create_or_update` | `INSERT` | `applicationDefinitionName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a managed application definition. |
| `delete` | `DELETE` | `applicationDefinitionName, resourceGroupName, subscriptionId` | Deletes the managed application definition. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists the managed application definitions in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all the application definitions within a subscription. |
| `update` | `EXEC` | `applicationDefinitionName, resourceGroupName, subscriptionId` | Updates the managed application definition. |
