---
title: customers__purchasable_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - customers__purchasable_skus
  - cloudchannel
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customers__purchasable_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudchannel.customers__purchasable_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token to retrieve the next page of results. |
| `purchasableSkus` | `array` | The list of SKUs requested. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `accounts_customers_listPurchasableSkus` | `SELECT` | `accountsId, customersId` |
