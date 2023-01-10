---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - lab_services
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
<tr><td><b>Id</b></td><td><code>azure_extras.lab_services.skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the SKU. |
| `tier` | `string` | The tier of the SKU. |
| `capabilities` | `array` | The capabilities of the SKU. |
| `costs` | `array` | Metadata for retrieving price info of a lab services SKUs. |
| `size` | `string` | The SKU size. |
| `locations` | `array` | List of locations that are available for a size. |
| `resourceType` | `string` | The lab services resource type. |
| `restrictions` | `array` | Restrictions of a lab services SKUs. |
| `family` | `string` | The family of the SKU. |
| `capacity` | `object` | The scale out/in options of the SKU. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Skus_List` | `SELECT` |  |
