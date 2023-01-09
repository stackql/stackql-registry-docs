---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - androidpublisher
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
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `regionCode` | `string` | ISO 3166-1 alpha-2 billing region code of the user at the time the product was granted. |
| `purchaseType` | `integer` | The type of purchase of the inapp product. This field is only set if this purchase was not made using the standard in-app billing flow. Possible values are: 0. Test (i.e. purchased from a license testing account) 1. Promo (i.e. purchased using a promo code) 2. Rewarded (i.e. from watching a video ad instead of paying) |
| `purchaseState` | `integer` | The purchase state of the order. Possible values are: 0. Purchased 1. Canceled 2. Pending |
| `purchaseTimeMillis` | `string` | The time the product was purchased, in milliseconds since the epoch (Jan 1, 1970). |
| `acknowledgementState` | `integer` | The acknowledgement state of the inapp product. Possible values are: 0. Yet to be acknowledged 1. Acknowledged |
| `purchaseToken` | `string` | The purchase token generated to identify this purchase. May not be present. |
| `productId` | `string` | The inapp product SKU. May not be present. |
| `kind` | `string` | This kind represents an inappPurchase object in the androidpublisher service. |
| `consumptionState` | `integer` | The consumption state of the inapp product. Possible values are: 0. Yet to be consumed 1. Consumed |
| `developerPayload` | `string` | A developer-specified string that contains supplemental information about an order. |
| `obfuscatedExternalProfileId` | `string` | An obfuscated version of the id that is uniquely associated with the user's profile in your app. Only present if specified using https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedprofileid when the purchase was made. |
| `obfuscatedExternalAccountId` | `string` | An obfuscated version of the id that is uniquely associated with the user's account in your app. Only present if specified using https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedaccountid when the purchase was made. |
| `quantity` | `integer` | The quantity associated with the purchase of the inapp product. If not present, the quantity is 1. |
| `orderId` | `string` | The order id associated with the purchase of the inapp product. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `purchases_products_get` | `SELECT` | `packageName, productId, token` | Checks the purchase and consumption status of an inapp item. |
| `purchases_products_acknowledge` | `EXEC` | `packageName, productId, token` | Acknowledges a purchase of an inapp item. |
