---
title: promotions
hide_title: false
hide_table_of_contents: false
keywords:
  - promotions
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
<tr><td><b>Name</b></td><td><code>promotions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.promotions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Required. Output only. The REST promotion ID to uniquely identify the promotion. Content API methods that operate on promotions take this as their `promotionId` parameter. The REST ID for a promotion is of the form channel:contentLanguage:targetCountry:promotionId The `channel` field has a value of `"online"`, `"in_store"`, or `"online_in_store"`. |
| `brandExclusion` | `array` | Product filter by brand exclusion for the promotion. |
| `itemIdExclusion` | `array` | Product filter by item ID exclusion for the promotion. |
| `getThisQuantityDiscounted` | `integer` | The number of items discounted in the promotion. |
| `productApplicability` | `string` | Required. Applicability of the promotion to either all products or only specific products. |
| `promotionId` | `string` | Required. The user provided promotion ID to uniquely identify the promotion. |
| `moneyOffAmount` | `object` | The price represented as a number and currency. |
| `targetCountry` | `string` | Required. The target country used as part of the unique identifier. Can be `AU`, `CA`, `DE`, `FR`, `GB`, `IN` or `US`. |
| `minimumPurchaseAmount` | `object` | The price represented as a number and currency. |
| `limitQuantity` | `integer` | Maximum purchase quantity for the promotion. |
| `productTypeExclusion` | `array` | Product filter by product type exclusion for the promotion. |
| `genericRedemptionCode` | `string` | Generic redemption code for the promotion. To be used with the `offerType` field. |
| `itemGroupId` | `array` | Product filter by item group ID for the promotion. |
| `freeGiftItemId` | `string` | Free gift item ID for the promotion. |
| `storeCodeExclusion` | `array` | Store codes to exclude for the promotion. |
| `shippingServiceNames` | `array` | Shipping service names for the promotion. |
| `itemGroupIdExclusion` | `array` | Product filter by item group ID exclusion for the promotion. |
| `promotionDisplayDates` | `string` | String representation of the promotion display dates. Deprecated. Use `promotion_display_time_period` instead. |
| `orderLimit` | `integer` | Order limit for the promotion. |
| `percentOff` | `integer` | The percentage discount offered in the promotion. |
| `longTitle` | `string` | Required. Long title for the promotion. |
| `minimumPurchaseQuantity` | `integer` | Minimum purchase quantity for the promotion. |
| `freeGiftValue` | `object` | The price represented as a number and currency. |
| `redemptionChannel` | `array` | Required. Redemption channel for the promotion. At least one channel is required. |
| `promotionUrl` | `string` | URL to the page on the merchant's site where the promotion shows. Local Inventory ads promotions throw an error if no promo url is included. URL is used to confirm that the promotion is valid and can be redeemed. |
| `freeGiftDescription` | `string` | Free gift description for the promotion. |
| `promotionDestinationIds` | `array` | Destination ID for the promotion. |
| `couponValueType` | `string` | Required. Coupon value type for the promotion. |
| `offerType` | `string` | Required. Type of the promotion. |
| `promotionEffectiveTimePeriod` | `object` | A message that represents a time period. |
| `contentLanguage` | `string` | Required. The content language used as part of the unique identifier. `en` content language is available for all target countries. `fr` content language is available for `CA` and `FR` target countries, and `de` content language is available for `DE` target country. |
| `moneyBudget` | `object` | The price represented as a number and currency. |
| `limitValue` | `object` | The price represented as a number and currency. |
| `storeApplicability` | `string` | Whether the promotion applies to all stores, or only specified stores. Local Inventory ads promotions throw an error if no store applicability is included. An INVALID_ARGUMENT error is thrown if store_applicability is set to ALL_STORES and store_code or score_code_exclusion is set to a value. |
| `storeCode` | `array` | Store codes to include for the promotion. |
| `itemId` | `array` | Product filter by item ID for the promotion. |
| `promotionEffectiveDates` | `string` | String representation of the promotion effective dates. Deprecated. Use `promotion_effective_time_period` instead. |
| `brand` | `array` | Product filter by brand for the promotion. |
| `promotionDisplayTimePeriod` | `object` | A message that represents a time period. |
| `productType` | `array` | Product filter by product type for the promotion. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, merchantId` | Retrieves a promotion from your Merchant Center account. |
| `create` | `INSERT` | `merchantId` | Inserts a promotion for your Merchant Center account. If the promotion already exists, then it updates the promotion instead. To [end or delete] (https://developers.google.com/shopping-content/guides/promotions#end_a_promotion) a promotion update the time period of the promotion to a time that has already passed. |
