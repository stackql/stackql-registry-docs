---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - adexchangebuyer2
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `availableStartTime` | `string` | Inventory availability dates. The start time will be truncated to seconds during serving. Thus, a field specified as 3:23:34.456 (HH:mm:ss.SSS) will be truncated to 3:23:34 when serving. |
| `seller` | `object` | Represents a seller of inventory. Each seller is identified by a unique Ad Manager account ID. |
| `createTime` | `string` | Creation time. |
| `updateTime` | `string` | Time of last update. |
| `syndicationProduct` | `string` | The syndication product associated with the deal. |
| `creatorContacts` | `array` | Optional contact information for the creator of this product. |
| `targetingCriterion` | `array` | Targeting that is shared between the buyer and the seller. Each targeting criterion has a specified key and for each key there is a list of inclusion value or exclusion values. |
| `hasCreatorSignedOff` | `boolean` | If the creator has already signed off on the product, then the buyer can finalize the deal by accepting the product as is. When copying to a proposal, if any of the terms are changed, then auto_finalize is automatically set to false. |
| `productRevision` | `string` | The revision number of the product (auto-assigned by Marketplace). |
| `terms` | `object` | The deal terms specify the details of a Product/deal. They specify things like price per buyer, the type of pricing model (for example, fixed price, auction) and expected impressions from the publisher. |
| `displayName` | `string` | The display name for this product as set by the seller. |
| `productId` | `string` | The unique ID for the product. |
| `availableEndTime` | `string` | The proposed end time for the deal. The field will be truncated to the order of seconds during serving. |
| `publisherProfileId` | `string` | An ID which can be used by the Publisher Profile API to get more information about the seller that created this product. |
| `webPropertyCode` | `string` | The web-property code for the seller. This needs to be copied as is when adding a new deal to a proposal. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_products_get` | `SELECT` | `accountId, productId` | Gets the requested product by ID. |
| `accounts_products_list` | `SELECT` | `accountId` | List all products visible to the buyer (optionally filtered by the specified PQL query). |
