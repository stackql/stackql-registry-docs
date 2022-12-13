---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - storage_cache
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
<tr><td><b>Id</b></td><td><code>azure.storage_cache.skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of this SKU. |
| `restrictions` | `array` | The restrictions preventing this SKU from being used. This is empty if there are no restrictions. |
| `capabilities` | `array` | A list of capabilities of this SKU, such as throughput or ops/sec. |
| `locationInfo` | `array` | The set of locations where the SKU is available. |
| `locations` | `array` | The set of locations where the SKU is available. This is the supported and registered Azure Geo Regions (e.g., West US, East US, Southeast Asia, etc.). |
| `resourceType` | `string` | The type of resource the SKU applies to. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Skus_List` | `SELECT` | `subscriptionId` |
