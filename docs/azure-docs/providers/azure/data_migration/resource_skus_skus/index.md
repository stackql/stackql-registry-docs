---
title: resource_skus_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_skus_skus
  - data_migration
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
<tr><td><b>Name</b></td><td><code>resource_skus_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_migration.resource_skus_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of SKU. |
| `apiVersions` | `array` | The api versions that support this SKU. |
| `capabilities` | `array` | A name value pair to describe the capability. |
| `capacity` | `object` | Describes scaling information of a SKU. |
| `costs` | `array` | Metadata for retrieving price info. |
| `family` | `string` | The Family of this particular SKU. |
| `kind` | `string` | The Kind of resources that are supported in this SKU. |
| `locations` | `array` | The set of locations that the SKU is available. |
| `resourceType` | `string` | The type of resource the SKU applies to. |
| `restrictions` | `array` | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |
| `size` | `string` | The Size of the SKU. |
| `tier` | `string` | Specifies the tier of DMS (classic) in a scale set. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `api-version, subscriptionId` |
| `_list` | `EXEC` | `api-version, subscriptionId` |
