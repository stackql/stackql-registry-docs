---
title: skus_nested_resource_type_third
hide_title: false
hide_table_of_contents: false
keywords:
  - skus_nested_resource_type_third
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
<tr><td><b>Name</b></td><td><code>skus_nested_resource_type_third</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.provider_hub.skus_nested_resource_type_third</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `nestedResourceTypeFirst, nestedResourceTypeSecond, nestedResourceTypeThird, providerNamespace, resourceType, sku, subscriptionId` | Gets the sku details for the given resource type and sku name. |
| `create_or_update` | `INSERT` | `nestedResourceTypeFirst, nestedResourceTypeSecond, nestedResourceTypeThird, providerNamespace, resourceType, sku, subscriptionId` | Creates or updates the resource type skus in the given resource type. |
| `delete` | `DELETE` | `nestedResourceTypeFirst, nestedResourceTypeSecond, nestedResourceTypeThird, providerNamespace, resourceType, sku, subscriptionId` | Deletes a resource type sku. |
