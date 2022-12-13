---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - api_management
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
<tr><td><b>Id</b></td><td><code>azure.api_management.skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of SKU. |
| `capabilities` | `array` | A name value pair to describe the capability. |
| `capacity` | `object` | Describes scaling information of a SKU. |
| `locations` | `array` | The set of locations that the SKU is available. |
| `resourceType` | `string` | The type of resource the SKU applies to. |
| `kind` | `string` | The Kind of resources that are supported in this SKU. |
| `tier` | `string` | Specifies the tier of virtual machines in a scale set.&lt;br /&gt;&lt;br /&gt; Possible Values:&lt;br /&gt;&lt;br /&gt; **Standard**&lt;br /&gt;&lt;br /&gt; **Basic** |
| `costs` | `array` | Metadata for retrieving price info. |
| `family` | `string` | The Family of this particular SKU. |
| `restrictions` | `array` | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |
| `locationInfo` | `array` | A list of locations and availability zones in those locations where the SKU is available. |
| `apiVersions` | `array` | The api versions that support this SKU. |
| `size` | `string` | The Size of the SKU. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ApiManagementSkus_List` | `SELECT` | `subscriptionId` |
