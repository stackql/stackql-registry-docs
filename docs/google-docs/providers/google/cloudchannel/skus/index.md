---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - cloudchannel
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudchannel.skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `skus` | `array` | The list of SKUs requested. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `products_skus_list` | `SELECT` | `productsId` |
