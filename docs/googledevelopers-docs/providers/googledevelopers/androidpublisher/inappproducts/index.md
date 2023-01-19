---
title: inappproducts
hide_title: false
hide_table_of_contents: false
keywords:
  - inappproducts
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
<tr><td><b>Name</b></td><td><code>inappproducts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.inappproducts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `listings` | `object` | List of localized title and description data. Map key is the language of the localized data, as defined by BCP-47, e.g. "en-US". |
| `purchaseType` | `string` | The type of the product, e.g. a recurring subscription. |
| `sku` | `string` | Stock-keeping-unit (SKU) of the product, unique within an app. |
| `trialPeriod` | `string` | Trial period, specified in ISO 8601 format. Acceptable values are anything between P7D (seven days) and P999D (999 days). |
| `gracePeriod` | `string` | Grace period of the subscription, specified in ISO 8601 format. Allows developers to give their subscribers a grace period when the payment for the new recurrence period is declined. Acceptable values are P0D (zero days), P3D (three days), P7D (seven days), P14D (14 days), and P30D (30 days). |
| `packageName` | `string` | Package name of the parent app. |
| `prices` | `object` | Prices per buyer region. None of these can be zero, as in-app products are never free. Map key is region code, as defined by ISO 3166-2. |
| `subscriptionPeriod` | `string` | Subscription period, specified in ISO 8601 format. Acceptable values are P1W (one week), P1M (one month), P3M (three months), P6M (six months), and P1Y (one year). |
| `subscriptionTaxesAndComplianceSettings` | `object` | Details about taxation, Google Play policy and legal compliance for subscription products. |
| `status` | `string` | The status of the product, e.g. whether it's active. |
| `defaultLanguage` | `string` | Default language of the localized data, as defined by BCP-47. e.g. "en-US". |
| `defaultPrice` | `object` | Definition of a price, i.e. currency and units. |
| `managedProductTaxesAndComplianceSettings` | `object` | Details about taxation and legal compliance for managed products. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `packageName, sku` | Gets an in-app product, which can be a managed product or a subscription. |
| `list` | `SELECT` | `packageName` | Lists all in-app products - both managed products and subscriptions. If an app has a large number of in-app products, the response may be paginated. In this case the response field `tokenPagination.nextPageToken` will be set and the caller should provide its value as a `token` request parameter to retrieve the next page. |
| `insert` | `INSERT` | `packageName` | Creates an in-app product (i.e. a managed product or a subscriptions). |
| `delete` | `DELETE` | `packageName, sku` | Deletes an in-app product (i.e. a managed product or a subscriptions). |
| `patch` | `EXEC` | `packageName, sku` | Patches an in-app product (i.e. a managed product or a subscriptions). |
| `update` | `EXEC` | `packageName, sku` | Updates an in-app product (i.e. a managed product or a subscriptions). |
