---
title: resource_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_skus
  - cognitive_services
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
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.resource_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of SKU. |
| `kind` | `string` | The Kind of resources that are supported in this SKU. |
| `locations` | `array` | The set of locations that the SKU is available. |
| `resourceType` | `string` | The type of resource the SKU applies to. |
| `restrictions` | `array` | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |
| `tier` | `string` | Specifies the tier of Cognitive Services account. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ResourceSkus_List` | `SELECT` | `subscriptionId` |
