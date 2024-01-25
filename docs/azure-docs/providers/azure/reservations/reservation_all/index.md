---
title: reservation_all
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_all
  - reservations
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
<tr><td><b>Name</b></td><td><code>reservation_all</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.reservations.reservation_all</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `integer` |  |
| `kind` | `string` | Resource Provider type to be reserved. |
| `location` | `string` | The Azure region where the reserved resource lives. |
| `properties` | `object` | The properties of the reservations |
| `sku` | `object` | The name of sku |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
| `_list` | `EXEC` |  |
