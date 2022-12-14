---
title: resource_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_skus
  - compute
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
<tr><td><b>Id</b></td><td><code>azure.compute.resource_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of SKU. |
| `locationInfo` | `array` | A list of locations and availability zones in those locations where the SKU is available. |
| `resourceType` | `string` | The type of resource the SKU applies to. |
| `apiVersions` | `array` | The api versions that support this SKU. |
| `capacity` | `object` | Describes scaling information of a SKU. |
| `capabilities` | `array` | A name value pair to describe the capability. |
| `family` | `string` | The Family of this particular SKU. |
| `tier` | `string` | Specifies the tier of virtual machines in a scale set.&lt;br /&gt;&lt;br /&gt; Possible Values:&lt;br /&gt;&lt;br /&gt; **Standard**&lt;br /&gt;&lt;br /&gt; **Basic** |
| `costs` | `array` | Metadata for retrieving price info. |
| `locations` | `array` | The set of locations that the SKU is available. |
| `kind` | `string` | The Kind of resources that are supported in this SKU. |
| `restrictions` | `array` | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |
| `size` | `string` | The Size of the SKU. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ResourceSkus_List` | `SELECT` | `subscriptionId` |
