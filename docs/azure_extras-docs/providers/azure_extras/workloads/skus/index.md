---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - workloads
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
<tr><td><b>Id</b></td><td><code>azure_extras.workloads.skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the SKU. |
| `size` | `string` | The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code.  |
| `tier` | `string` | This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT. |
| `restrictions` | `array` | The SKU restrictions. |
| `capacity` | `object` | If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted. |
| `capabilities` | `array` | The SKU capabilities. |
| `family` | `string` | If the service has different generations of hardware, for the same SKU, then that can be captured here. |
| `costs` | `array` | The SKU costs. |
| `locationInfo` | `array` | List of locations where this SKU is available. |
| `locations` | `array` | List of locations where this SKU is available. |
| `kind` | `string` | If the service has different kinds of hardware, for the same SKU, then that can be captured here. |
| `resourceType` | `string` | Resource type the SKU applicable for. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Skus_List` | `SELECT` | `subscriptionId` |
