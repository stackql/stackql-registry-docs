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
| `restrictions` | `array` | The SKU restrictions. |
| `capabilities` | `array` | The SKU capabilities. |
| `locationInfo` | `array` | List of locations where this SKU is available. |
| `resourceType` | `string` | Resource type the SKU applicable for. |
| `tier` | `string` | This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT. |
| `family` | `string` | If the service has different generations of hardware, for the same SKU, then that can be captured here. |
| `capacity` | `object` | If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted. |
| `kind` | `string` | If the service has different kinds of hardware, for the same SKU, then that can be captured here. |
| `locations` | `array` | List of locations where this SKU is available. |
| `costs` | `array` | The SKU costs. |
| `size` | `string` | The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code.  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Skus_List` | `SELECT` | `subscriptionId` |
