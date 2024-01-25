---
title: clusters_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_skus
  - data_explorer
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
<tr><td><b>Name</b></td><td><code>clusters_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_explorer.clusters_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the SKU |
| `locationInfo` | `array` | Locations and zones |
| `locations` | `array` | The set of locations that the SKU is available |
| `resourceType` | `string` | The resource type |
| `restrictions` | `array` | The restrictions because of which SKU cannot be used |
| `tier` | `string` | The tier of the SKU |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `subscriptionId` |
| `_list` | `EXEC` | `subscriptionId` |
