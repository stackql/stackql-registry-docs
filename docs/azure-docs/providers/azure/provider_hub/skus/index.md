---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - provider_hub
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
<tr><td><b>Name</b></td><td><code>skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.provider_hub.skus</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `providerNamespace, resourceType, sku, subscriptionId` | Gets the sku details for the given resource type and sku name. |
| `list_by_resource_type_registrations` | `SELECT` | `providerNamespace, resourceType, subscriptionId` | Gets the list of skus for the given resource type. |
| `list_by_resource_type_registrations_nested_resource_type_first` | `SELECT` | `nestedResourceTypeFirst, providerNamespace, resourceType, subscriptionId` | Gets the list of skus for the given resource type. |
| `list_by_resource_type_registrations_nested_resource_type_second` | `SELECT` | `nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, subscriptionId` | Gets the list of skus for the given resource type. |
| `list_by_resource_type_registrations_nested_resource_type_third` | `SELECT` | `nestedResourceTypeFirst, nestedResourceTypeSecond, nestedResourceTypeThird, providerNamespace, resourceType, subscriptionId` | Gets the list of skus for the given resource type. |
| `create_or_update` | `INSERT` | `providerNamespace, resourceType, sku, subscriptionId` | Creates or updates the resource type skus in the given resource type. |
| `delete` | `DELETE` | `providerNamespace, resourceType, sku, subscriptionId` | Deletes a resource type sku. |
| `_list_by_resource_type_registrations` | `EXEC` | `providerNamespace, resourceType, subscriptionId` | Gets the list of skus for the given resource type. |
| `_list_by_resource_type_registrations_nested_resource_type_first` | `EXEC` | `nestedResourceTypeFirst, providerNamespace, resourceType, subscriptionId` | Gets the list of skus for the given resource type. |
| `_list_by_resource_type_registrations_nested_resource_type_second` | `EXEC` | `nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, subscriptionId` | Gets the list of skus for the given resource type. |
| `_list_by_resource_type_registrations_nested_resource_type_third` | `EXEC` | `nestedResourceTypeFirst, nestedResourceTypeSecond, nestedResourceTypeThird, providerNamespace, resourceType, subscriptionId` | Gets the list of skus for the given resource type. |
