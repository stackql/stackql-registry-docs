---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - spring_apps
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
<tr><td><b>Id</b></td><td><code>azure.spring_apps.skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Gets the name of SKU. |
| `capacity` | `object` | The SKU capacity |
| `locationInfo` | `array` | Gets a list of locations and availability zones in those locations where the SKU is available. |
| `locations` | `array` | Gets the set of locations that the SKU is available. |
| `resourceType` | `string` | Gets the type of resource the SKU applies to. |
| `restrictions` | `array` | Gets the restrictions because of which SKU cannot be used. This is<br />empty if there are no restrictions. |
| `tier` | `string` | Gets the tier of SKU. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `subscriptionId` |
| `_list` | `EXEC` | `subscriptionId` |
