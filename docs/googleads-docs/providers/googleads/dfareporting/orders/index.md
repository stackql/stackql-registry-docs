---
title: orders
hide_title: false
hide_table_of_contents: false
keywords:
  - orders
  - dfareporting
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
<tr><td><b>Name</b></td><td><code>orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.orders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this order. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this order. |
| `buyerOrganizationName` | `string` | Name of the buyer organization. |
| `siteNames` | `array` | Free-form site names this order is associated with. |
| `sellerOrderId` | `string` | Seller order ID associated with this order. |
| `approverUserProfileIds` | `array` | IDs for users that have to approve documents created for this order. |
| `buyerInvoiceId` | `string` | Buyer invoice ID associated with this order. |
| `projectId` | `string` | Project ID of this order. |
| `contacts` | `array` | Contacts for this order. |
| `sellerOrganizationName` | `string` | Name of the seller organization. |
| `termsAndConditions` | `string` | Terms and conditions of this order. |
| `advertiserId` | `string` | Advertiser ID of this order. |
| `lastModifiedInfo` | `object` | Modification timestamp. |
| `accountId` | `string` | Account ID of this order. |
| `siteId` | `array` | Site IDs this order is associated with. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#order". |
| `notes` | `string` | Notes of this order. |
| `comments` | `string` | Comments in this order. |
| `subaccountId` | `string` | Subaccount ID of this order. |
| `planningTermId` | `string` | ID of the terms and conditions template used in this order. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, profileId, projectId` | Gets one order by ID. |
| `list` | `SELECT` | `profileId, projectId` | Retrieves a list of orders, possibly filtered. This method supports paging. |
