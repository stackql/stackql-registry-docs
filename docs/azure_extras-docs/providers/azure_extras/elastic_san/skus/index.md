---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - elastic_san
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
<tr><td><b>Id</b></td><td><code>azure_extras.elastic_san.skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The sku name. |
| `locationInfo` | `array` | Availability of the SKU for the location/zone |
| `locations` | `array` | The set of locations that the SKU is available. This will be supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). |
| `resourceType` | `string` | The type of the resource. |
| `tier` | `string` | The sku tier. |
| `capabilities` | `array` | The capability information in the specified SKU. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Skus_List` | `SELECT` | `subscriptionId` |
