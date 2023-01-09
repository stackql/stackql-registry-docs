---
title: orders_bymerchantorderid
hide_title: false
hide_table_of_contents: false
keywords:
  - orders_bymerchantorderid
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
<tr><td><b>Name</b></td><td><code>orders_bymerchantorderid</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.orders_bymerchantorderid</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#ordersGetByMerchantOrderIdResponse`". |
| `order` | `object` | Order. Production access (all methods) requires the order manager role. Sandbox access does not. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `orders_getbymerchantorderid` | `SELECT` | `merchantId, merchantOrderId` |
