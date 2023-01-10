---
title: collections
hide_title: false
hide_table_of_contents: false
keywords:
  - collections
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
<tr><td><b>Name</b></td><td><code>collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.collections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Required. The REST ID of the collection. Content API methods that operate on collections take this as their collectionId parameter. The REST ID for a collection is of the form collectionId. [id attribute](https://support.google.com/merchants/answer/9649290) |
| `imageLink` | `array` | The URL of a collection’s image. [image_link attribute](https://support.google.com/merchants/answer/9703236) |
| `mobileLink` | `string` | A collection’s mobile-optimized landing page when you have a different URL for mobile and desktop traffic. [mobile_link attribute](https://support.google.com/merchants/answer/9646123) |
| `customLabel3` | `string` | Label that you assign to a collection to help organize bidding and reporting in Shopping campaigns. |
| `productCountry` | `string` | [product_country attribute](https://support.google.com/merchants/answer/9674155) |
| `language` | `string` | The language of a collection and the language of any featured products linked to the collection. [language attribute](https://support.google.com/merchants/answer/9673781) |
| `customLabel2` | `string` | Label that you assign to a collection to help organize bidding and reporting in Shopping campaigns. |
| `customLabel0` | `string` | Label that you assign to a collection to help organize bidding and reporting in Shopping campaigns. [Custom label](https://support.google.com/merchants/answer/9674217) |
| `customLabel4` | `string` | Label that you assign to a collection to help organize bidding and reporting in Shopping campaigns. |
| `featuredProduct` | `array` | This identifies one or more products associated with the collection. Used as a lookup to the corresponding product ID in your product feeds. Provide a maximum of 100 featuredProduct (for collections). Provide up to 10 featuredProduct (for Shoppable Images only) with ID and X and Y coordinates. [featured_product attribute](https://support.google.com/merchants/answer/9703736) |
| `link` | `string` | A collection’s landing page. URL directly linking to your collection's page on your website. [link attribute](https://support.google.com/merchants/answer/9673983) |
| `customLabel1` | `string` | Label that you assign to a collection to help organize bidding and reporting in Shopping campaigns. |
| `headline` | `array` | Your collection's name. [headline attribute](https://support.google.com/merchants/answer/9673580) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `collectionId, merchantId` | Retrieves a collection from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the collections in your Merchant Center account. The response might contain fewer items than specified by page_size. Rely on next_page_token to determine if there are more items to be requested. |
| `create` | `INSERT` | `merchantId` | Uploads a collection to your Merchant Center account. If a collection with the same collectionId already exists, this method updates that entry. In each update, the collection is completely replaced by the fields in the body of the update request. |
| `delete` | `DELETE` | `collectionId, merchantId` | Deletes a collection from your Merchant Center account. |
