---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - dev_center
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
<tr><td><b>Id</b></td><td><code>azure_extras.dev_center.skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the SKU. Ex - P3. It is typically a letter+number code |
| `capacity` | `integer` | If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted. |
| `family` | `string` | If the service has different generations of hardware, for the same SKU, then that can be captured here. |
| `locations` | `array` | SKU supported locations. |
| `resourceType` | `string` | The name of the resource type |
| `size` | `string` | The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code.  |
| `tier` | `string` | This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT. |
| `capabilities` | `array` | Collection of name/value pairs to describe the SKU capabilities. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Skus_ListBySubscription` | `SELECT` |  |
