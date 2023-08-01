---
title: sk_us
hide_title: false
hide_table_of_contents: false
keywords:
  - sk_us
  - engagement_fabric
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
<tr><td><b>Name</b></td><td><code>sk_us</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.engagement_fabric.sk_us</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the SKU |
| `resourceType` | `string` | The fully qualified resource type |
| `restrictions` | `array` | The restrictions because of which SKU cannot be used |
| `tier` | `string` | The price tier of the SKU |
| `locationInfo` | `array` | Locations and zones |
| `locations` | `array` | The set of locations that the SKU is available |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SKUs_List` | `SELECT` | `subscriptionId` |
