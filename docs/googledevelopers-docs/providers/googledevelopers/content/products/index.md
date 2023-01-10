---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
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
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The REST ID of the product. Content API methods that operate on products take this as their `productId` parameter. The REST ID for a product is of the form channel:contentLanguage: targetCountry: offerId. |
| `description` | `string` | Description of the item. |
| `ageGroup` | `string` | Target age group of the item. |
| `costOfGoodsSold` | `object` |  |
| `title` | `string` | Title of the item. |
| `source` | `string` | The source of the offer, that is, how the offer was created. Acceptable values are: - "`api`" - "`crawl`" - "`feed`"  |
| `googleProductCategory` | `string` | Google's category of the item (see [Google product taxonomy](https://support.google.com/merchants/answer/1705911)). When querying products, this field will contain the user provided value. There is currently no way to get back the auto assigned google product categories through the API. |
| `energyEfficiencyClass` | `string` | The energy efficiency class as defined in EU directive 2010/30/EU. |
| `displayAdsTitle` | `string` | Title of an item for dynamic remarketing campaigns. |
| `taxCategory` | `string` | The tax category of the product, used to configure detailed tax nexus in account-level tax settings. |
| `identifierExists` | `boolean` | False when the item does not have unique product identifiers appropriate to its category, such as GTIN, MPN, and brand. Required according to the Unique Product Identifier Rules for all target countries except for Canada. |
| `maxHandlingTime` | `string` | Maximal product handling time (in business days). |
| `imageLink` | `string` | URL of an image of the item. |
| `multipack` | `string` | The number of identical products in a merchant-defined multipack. |
| `customLabel2` | `string` | Custom label 2 for custom grouping of items in a Shopping campaign. |
| `taxes` | `array` | Tax information. |
| `gender` | `string` | Target gender of the item. |
| `availability` | `string` | Availability status of the item. |
| `itemGroupId` | `string` | Shared identifier for all variants of the same product. |
| `displayAdsId` | `string` | An identifier for an item for dynamic remarketing campaigns. |
| `additionalSizeType` | `string` | Additional cut of the item. Used together with size_type to represent combined size types for apparel items. |
| `link` | `string` | URL directly linking to your item's page on your website. |
| `externalSellerId` | `string` | Required for multi-seller accounts. Use this attribute if you're a marketplace uploading products for various sellers to your multi-seller account. |
| `isBundle` | `boolean` | Whether the item is a merchant-defined bundle. A bundle is a custom grouping of different products sold by a merchant for a single price. |
| `minHandlingTime` | `string` | Minimal product handling time (in business days). |
| `adsRedirect` | `string` | Allows advertisers to override the item URL when the product is shown within the context of Product Ads. |
| `shippingLength` | `object` |  |
| `customLabel1` | `string` | Custom label 1 for custom grouping of items in a Shopping campaign. |
| `installment` | `object` |  |
| `adsGrouping` | `string` | Used to group items in an arbitrary way. Only for CPA%, discouraged otherwise. |
| `gtin` | `string` | Global Trade Item Number (GTIN) of the item. |
| `unitPricingMeasure` | `object` |  |
| `displayAdsSimilarIds` | `array` | Advertiser-specified recommendations. |
| `sizes` | `array` | Size of the item. Only one value is allowed. For variants with different sizes, insert a separate product for each size with the same `itemGroupId` value (see size definition). |
| `customLabel3` | `string` | Custom label 3 for custom grouping of items in a Shopping campaign. |
| `promotionIds` | `array` | The unique ID of a promotion. |
| `shipping` | `array` | Shipping rules. |
| `mobileLink` | `string` | URL for the mobile-optimized version of your item's landing page. |
| `offerId` | `string` | Required. A unique identifier for the item. Leading and trailing whitespaces are stripped and multiple whitespaces are replaced by a single whitespace upon submission. Only valid unicode characters are accepted. See the products feed specification for details. *Note:* Content API methods that operate on products take the REST ID of the product, *not* this identifier. |
| `sizeType` | `string` | The cut of the item. Recommended for apparel items. |
| `productWeight` | `object` |  |
| `condition` | `string` | Condition or state of the item. |
| `mpn` | `string` | Manufacturer Part Number (MPN) of the item. |
| `shoppingAdsExcludedCountries` | `array` | List of country codes (ISO 3166-1 alpha-2) to exclude the offer from Shopping Ads destination. Countries from this list are removed from countries configured in MC feed settings. |
| `maxEnergyEfficiencyClass` | `string` | The energy efficiency class as defined in EU directive 2010/30/EU. |
| `subscriptionCost` | `object` |  |
| `displayAdsLink` | `string` | URL directly to your item's landing page for dynamic remarketing campaigns. |
| `contentLanguage` | `string` | Required. The two-letter ISO 639-1 language code for the item. |
| `productDetails` | `array` | Technical specification or additional product details. |
| `unitPricingBaseMeasure` | `object` |  |
| `linkTemplate` | `string` | URL template for merchant hosted local storefront. |
| `adsLabels` | `array` | Similar to ads_grouping, but only works on CPC. |
| `adult` | `boolean` | Should be set to true if the item is targeted towards adults. |
| `additionalImageLinks` | `array` | Additional URLs of images of the item. |
| `salePriceEffectiveDate` | `string` | Date range during which the item is on sale (see products data specification ). |
| `shippingWeight` | `object` |  |
| `material` | `string` | The material of which the item is made. |
| `brand` | `string` | Brand of the item. |
| `pickupMethod` | `string` | The pick up option for the item. Acceptable values are: - "`buy`" - "`reserve`" - "`ship to store`" - "`not supported`"  |
| `productHighlights` | `array` | Bullet points describing the most relevant highlights of a product. |
| `includedDestinations` | `array` | The list of destinations to include for this target (corresponds to checked check boxes in Merchant Center). Default destinations are always included unless provided in `excludedDestinations`. |
| `targetCountry` | `string` | Required. The CLDR territory code for the item's country of sale. |
| `loyaltyPoints` | `object` |  |
| `availabilityDate` | `string` | The day a pre-ordered product becomes available for delivery, in ISO 8601 format. |
| `displayAdsValue` | `number` | Offer margin for dynamic remarketing campaigns. |
| `sellOnGoogleQuantity` | `string` | The quantity of the product that is available for selling on Google. Supported only for online products. |
| `canonicalLink` | `string` | URL for the canonical version of your item's landing page. |
| `salePrice` | `object` |  |
| `shippingLabel` | `string` | The shipping label of the product, used to group product in account-level shipping rules. |
| `channel` | `string` | Required. The item's channel (online or local). Acceptable values are: - "`local`" - "`online`"  |
| `transitTimeLabel` | `string` | The transit time label of the product, used to group product in account-level transit time tables. |
| `price` | `object` |  |
| `customAttributes` | `array` | A list of custom (merchant-provided) attributes. It can also be used for submitting any attribute of the feed specification in its generic form (for example, `&#123; "name": "size type", "value": "regular" &#125;`). This is useful for submitting attributes not explicitly exposed by the API, such as additional attributes used for Buy on Google (formerly known as Shopping Actions). |
| `shippingWidth` | `object` |  |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#product`" |
| `productWidth` | `object` |  |
| `minEnergyEfficiencyClass` | `string` | The energy efficiency class as defined in EU directive 2010/30/EU. |
| `excludedDestinations` | `array` | The list of destinations to exclude for this target (corresponds to cleared check boxes in Merchant Center). Products that are excluded from all destinations for more than 7 days are automatically deleted. |
| `customLabel4` | `string` | Custom label 4 for custom grouping of items in a Shopping campaign. |
| `mobileLinkTemplate` | `string` | URL template for merchant hosted local storefront optimized for mobile devices. |
| `customLabel0` | `string` | Custom label 0 for custom grouping of items in a Shopping campaign. |
| `productTypes` | `array` | Categories of the item (formatted as in products data specification). |
| `pause` | `string` | Publication of this item should be temporarily paused. Acceptable values are: - "`ads`"  |
| `color` | `string` | Color of the item. |
| `pickupSla` | `string` | Item store pickup timeline. Acceptable values are: - "`same day`" - "`next day`" - "`2-day`" - "`3-day`" - "`4-day`" - "`5-day`" - "`6-day`" - "`7-day`" - "`multi-week`"  |
| `productHeight` | `object` |  |
| `sizeSystem` | `string` | System in which the size is specified. Recommended for apparel items. |
| `pattern` | `string` | The item's pattern (for example, polka dots). |
| `feedLabel` | `string` | Feed label for the item. Either `targetCountry` or `feedLabel` is required. |
| `productLength` | `object` |  |
| `expirationDate` | `string` | Date on which the item should expire, as specified upon insertion, in ISO 8601 format. The actual expiration date in Google Shopping is exposed in `productstatuses` as `googleExpirationDate` and might be earlier if `expirationDate` is too far in the future. |
| `shippingHeight` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `merchantId, productId` | Retrieves a product from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the products in your Merchant Center account. The response might contain fewer items than specified by maxResults. Rely on nextPageToken to determine if there are more items to be requested. |
| `insert` | `INSERT` | `merchantId` | Uploads a product to your Merchant Center account. If an item with the same channel, contentLanguage, offerId, and targetCountry already exists, this method updates that entry. |
| `delete` | `DELETE` | `merchantId, productId` | Deletes a product from your Merchant Center account. |
| `custombatch` | `EXEC` |  | Retrieves, inserts, and deletes multiple products in a single request. |
| `update` | `EXEC` | `merchantId, productId` | Updates an existing product in your Merchant Center account. Only updates attributes provided in the request. |
