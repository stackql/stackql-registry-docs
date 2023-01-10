---
title: inventory_items
hide_title: false
hide_table_of_contents: false
keywords:
  - inventory_items
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
<tr><td><b>Name</b></td><td><code>inventory_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.inventory_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this inventory item. |
| `name` | `string` | Name of this inventory item. For standalone inventory items, this is the same name as that of its only ad slot. For group inventory items, this can differ from the name of any of its ad slots. |
| `contentCategoryId` | `string` | Content category ID of this inventory item. |
| `accountId` | `string` | Account ID of this inventory item. |
| `estimatedClickThroughRate` | `string` | Estimated click-through rate of this inventory item. |
| `inPlan` | `boolean` | Whether this inventory item is in plan. |
| `type` | `string` | Type of inventory item. |
| `adSlots` | `array` | Ad slots of this inventory item. If this inventory item represents a standalone placement, there will be exactly one ad slot. If this inventory item represents a placement group, there will be more than one ad slot, each representing one child placement in that placement group. |
| `negotiationChannelId` | `string` | Negotiation channel ID of this inventory item. |
| `rfpId` | `string` | RFP ID of this inventory item. |
| `orderId` | `string` | Order ID of this inventory item. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#inventoryItem". |
| `siteId` | `string` | ID of the site this inventory item is associated with. |
| `advertiserId` | `string` | Advertiser ID of this inventory item. |
| `placementStrategyId` | `string` | Placement strategy ID of this inventory item. |
| `projectId` | `string` | Project ID of this inventory item. |
| `lastModifiedInfo` | `object` | Modification timestamp. |
| `estimatedConversionRate` | `string` | Estimated conversion rate of this inventory item. |
| `pricing` | `object` | Pricing Information |
| `subaccountId` | `string` | Subaccount ID of this inventory item. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `inventoryItems_get` | `SELECT` | `id, profileId, projectId` | Gets one inventory item by ID. |
| `inventoryItems_list` | `SELECT` | `profileId, projectId` | Retrieves a list of inventory items, possibly filtered. This method supports paging. |
