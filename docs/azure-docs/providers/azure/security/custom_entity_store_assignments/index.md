---
title: custom_entity_store_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_entity_store_assignments
  - security
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
<tr><td><b>Name</b></td><td><code>custom_entity_store_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.custom_entity_store_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | describes the custom entity store assignment properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, customEntityStoreAssignmentName, resourceGroupName, subscriptionId` | Gets a single custom entity store assignment by name for the provided subscription and resource group. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List custom entity store assignments by a provided subscription and resource group |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | List custom entity store assignments by provided subscription |
| `create` | `INSERT` | `api-version, customEntityStoreAssignmentName, resourceGroupName, subscriptionId` | Creates a custom entity store assignment for the provided subscription, if not already exists. |
| `delete` | `DELETE` | `api-version, customEntityStoreAssignmentName, resourceGroupName, subscriptionId` | Delete a custom entity store assignment by name for a provided subscription |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | List custom entity store assignments by a provided subscription and resource group |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | List custom entity store assignments by provided subscription |
