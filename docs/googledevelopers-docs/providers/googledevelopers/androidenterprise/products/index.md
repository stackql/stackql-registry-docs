---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - androidenterprise
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
<tr><td><b>Id</b></td><td><code>googledevelopers.androidenterprise.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The localized promotional description, if available. |
| `appTracks` | `array` | The tracks visible to the enterprise. |
| `smallIconUrl` | `string` | A link to a smaller image that can be used as an icon for the product. This image is suitable for use at up to 128px x 128px. |
| `distributionChannel` | `string` | How and to whom the package is made available. The value publicGoogleHosted means that the package is available through the Play store and not restricted to a specific enterprise. The value privateGoogleHosted means that the package is a private app (restricted to an enterprise) but hosted by Google. The value privateSelfHosted means that the package is a private app (restricted to an enterprise) and is privately hosted. |
| `lastUpdatedTimestampMillis` | `string` | The approximate time (within 7 days) the app was last published, expressed in milliseconds since epoch. |
| `contentRating` | `string` | The content rating for this app. |
| `productId` | `string` | A string of the form *app:&lt;package name&gt;*. For example, app:com.google.android.gm represents the Gmail app. |
| `screenshotUrls` | `array` | A list of screenshot links representing the app. |
| `recentChanges` | `string` | A description of the recent changes made to the app. |
| `authorName` | `string` | The name of the author of the product (for example, the app developer). |
| `appVersion` | `array` | App versions currently available for this product. |
| `title` | `string` | The name of the product. |
| `productPricing` | `string` | Whether this product is free, free with in-app purchases, or paid. If the pricing is unknown, this means the product is not generally available anymore (even though it might still be available to people who own it). |
| `minAndroidSdkVersion` | `integer` | The minimum Android SDK necessary to run the app. |
| `category` | `string` | The app category (e.g. RACING, SOCIAL, etc.) |
| `appRestrictionsSchema` | `object` | Represents the list of app restrictions available to be pre-configured for the product. |
| `requiresContainerApp` | `boolean` | Deprecated. |
| `signingCertificate` | `object` |  |
| `permissions` | `array` | A list of permissions required by the app. |
| `availableTracks` | `array` | Deprecated, use appTracks instead. |
| `availableCountries` | `array` | The countries which this app is available in. |
| `iconUrl` | `string` | A link to an image that can be used as an icon for the product. This image is suitable for use at up to 512px x 512px. |
| `detailsUrl` | `string` | A link to the (consumer) Google Play details page for the product. |
| `workDetailsUrl` | `string` | A link to the managed Google Play details page for the product, for use by an Enterprise admin. |
| `features` | `array` | Noteworthy features (if any) of this product. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `enterpriseId, productId` | Retrieves details of a product for display to an enterprise admin. |
| `list` | `SELECT` | `enterpriseId` | Finds approved products that match a query, or all approved products if there is no query. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.  |
| `approve` | `EXEC` | `enterpriseId, productId` |  Approves the specified product and the relevant app permissions, if any. The maximum number of products that you can approve per enterprise customer is 1,000. To learn how to use managed Google Play to design and create a store layout to display approved products to your users, see Store Layout Design. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.  |
| `generateApprovalUrl` | `EXEC` | `enterpriseId, productId` | Generates a URL that can be rendered in an iframe to display the permissions (if any) of a product. An enterprise admin must view these permissions and accept them on behalf of their organization in order to approve that product. Admins should accept the displayed permissions by interacting with a separate UI element in the EMM console, which in turn should trigger the use of this URL as the approvalUrlInfo.approvalUrl property in a Products.approve call to approve the product. This URL can only be used to display permissions for up to 1 day. **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations.  |
| `unapprove` | `EXEC` | `enterpriseId, productId` | Unapproves the specified product (and the relevant app permissions, if any) **Note:** This item has been deprecated. New integrations cannot use this method and can refer to our new recommendations. |
