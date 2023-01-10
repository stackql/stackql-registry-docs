---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - test_base
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
<tr><td><b>Name</b></td><td><code>skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the SKU. This is typically a letter + number code, such as B0 or S0. |
| `capabilities` | `array` | The capabilities of a SKU. |
| `locations` | `array` | The locations that the SKU is available. |
| `resourceType` | `string` | The type of resource the SKU applies to. |
| `tier` | `string` | The tier of this particular SKU. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Skus_List` | `SELECT` | `subscriptionId` |
