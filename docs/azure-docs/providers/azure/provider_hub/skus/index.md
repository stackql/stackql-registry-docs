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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Skus_Get` | `SELECT` | `providerNamespace, resourceType, sku, subscriptionId` | Gets the sku details for the given resource type and sku name. |
| `Skus_ListByResourceTypeRegistrations` | `SELECT` | `providerNamespace, resourceType, subscriptionId` | Gets the list of skus for the given resource type. |
| `Skus_ListByResourceTypeRegistrationsNestedResourceTypeFirst` | `SELECT` | `nestedResourceTypeFirst, providerNamespace, resourceType, subscriptionId` | Gets the list of skus for the given resource type. |
| `Skus_ListByResourceTypeRegistrationsNestedResourceTypeSecond` | `SELECT` | `nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, subscriptionId` | Gets the list of skus for the given resource type. |
| `Skus_ListByResourceTypeRegistrationsNestedResourceTypeThird` | `SELECT` | `nestedResourceTypeFirst, nestedResourceTypeSecond, nestedResourceTypeThird, providerNamespace, resourceType, subscriptionId` | Gets the list of skus for the given resource type. |
| `Skus_CreateOrUpdate` | `INSERT` | `providerNamespace, resourceType, sku, subscriptionId` | Creates or updates the resource type skus in the given resource type. |
| `Skus_Delete` | `DELETE` | `providerNamespace, resourceType, sku, subscriptionId` | Deletes a resource type sku. |
| `Skus_CreateOrUpdateNestedResourceTypeFirst` | `EXEC` | `nestedResourceTypeFirst, providerNamespace, resourceType, sku, subscriptionId` | Creates or updates the resource type skus in the given resource type. |
| `Skus_CreateOrUpdateNestedResourceTypeSecond` | `EXEC` | `nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, sku, subscriptionId` | Creates or updates the resource type skus in the given resource type. |
| `Skus_CreateOrUpdateNestedResourceTypeThird` | `EXEC` | `nestedResourceTypeFirst, nestedResourceTypeSecond, nestedResourceTypeThird, providerNamespace, resourceType, sku, subscriptionId` | Creates or updates the resource type skus in the given resource type. |
| `Skus_DeleteNestedResourceTypeFirst` | `EXEC` | `nestedResourceTypeFirst, providerNamespace, resourceType, sku, subscriptionId` | Deletes a resource type sku. |
| `Skus_DeleteNestedResourceTypeSecond` | `EXEC` | `nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, sku, subscriptionId` | Deletes a resource type sku. |
| `Skus_DeleteNestedResourceTypeThird` | `EXEC` | `nestedResourceTypeFirst, nestedResourceTypeSecond, nestedResourceTypeThird, providerNamespace, resourceType, sku, subscriptionId` | Deletes a resource type sku. |
| `Skus_GetNestedResourceTypeFirst` | `EXEC` | `nestedResourceTypeFirst, providerNamespace, resourceType, sku, subscriptionId` | Gets the sku details for the given resource type and sku name. |
| `Skus_GetNestedResourceTypeSecond` | `EXEC` | `nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, sku, subscriptionId` | Gets the sku details for the given resource type and sku name. |
| `Skus_GetNestedResourceTypeThird` | `EXEC` | `nestedResourceTypeFirst, nestedResourceTypeSecond, nestedResourceTypeThird, providerNamespace, resourceType, sku, subscriptionId` | Gets the sku details for the given resource type and sku name. |
