---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - paymentsresellersubscription
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
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.paymentsresellersubscription.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is empty, there are no subsequent pages. |
| `products` | `array` | The products for the specified partner. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `partners_products_list` | `SELECT` | `partnersId` |
