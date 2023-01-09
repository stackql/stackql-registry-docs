---
title: productdeliverytime
hide_title: false
hide_table_of_contents: false
keywords:
  - productdeliverytime
  - content
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>productdeliverytime</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.productdeliverytime</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `areaDeliveryTimes` | `array` | Required. A set of associations between `DeliveryArea` and `DeliveryTime` entries. The total number of `areaDeliveryTimes` can be at most 100. |
| `productId` | `object` | The Content API ID of the product. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `merchantId, productId` | Gets `productDeliveryTime` by `productId`. |
| `create` | `INSERT` | `merchantId` | Creates or updates the delivery time of a product. |
| `delete` | `DELETE` | `merchantId, productId` | Deletes the delivery time of a product. |
