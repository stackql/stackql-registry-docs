---
title: available_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - available_skus
  - data_box_edge
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
<tr><td><b>Name</b></td><td><code>available_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_box_edge.available_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The Sku name. |
| `resourceType` | `string` | The type of the resource. |
| `tier` | `string` | The Sku tier. |
| `capabilities` | `array` | The capability info of the SKU. |
| `size` | `string` | The Sku kind. |
| `family` | `string` | The Sku family. |
| `version` | `string` | Availability of the Sku as preview/stable. |
| `kind` | `string` | The Sku kind. |
| `shipmentTypes` | `array` | List of Shipment Types supported by this SKU |
| `apiVersions` | `array` | The API versions in which Sku is available. |
| `locationInfo` | `array` | Availability of the Sku for the location/zone/site. |
| `signupOption` | `string` | Sku can be signed up by customer or not. |
| `costs` | `array` | The pricing info of the Sku. |
| `availability` | `string` | Links to the next set of results |
| `locations` | `array` | Availability of the Sku for the region. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AvailableSkus_List` | `SELECT` | `subscriptionId` |
