---
title: legacy_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - legacy_peerings
  - peering
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
<tr><td><b>Name</b></td><td><code>legacy_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.legacy_peerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `kind` | `string` | The kind of the peering. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | The properties that define connectivity to the Microsoft Cloud Edge. |
| `sku` | `object` | The SKU that defines the tier and kind of the peering. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `LegacyPeerings_List` | `SELECT` | `kind, peeringLocation, subscriptionId` |
