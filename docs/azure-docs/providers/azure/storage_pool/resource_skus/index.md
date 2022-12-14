---
title: resource_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_skus
  - storage_pool
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
<tr><td><b>Name</b></td><td><code>resource_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_pool.resource_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Sku name |
| `capabilities` | `array` | List of additional capabilities for StoragePool resource. |
| `locationInfo` | `object` | Zone and capability info for resource sku |
| `resourceType` | `string` | StoragePool resource type |
| `restrictions` | `array` | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |
| `tier` | `string` | Sku tier |
| `apiVersion` | `string` | StoragePool RP API version |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ResourceSkus_List` | `SELECT` | `location, subscriptionId` |
