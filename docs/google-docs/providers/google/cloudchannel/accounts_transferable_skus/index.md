---
title: accounts_transferable_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_transferable_skus
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
<tr><td><b>Name</b></td><td><code>accounts_transferable_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudchannel.accounts_transferable_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `transferableSkus` | `array` | Information about existing SKUs for a customer that needs a transfer. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass to ListTransferableSkusRequest.page_token to obtain that page. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `accounts_listTransferableSkus` | `SELECT` | `accountsId` |
