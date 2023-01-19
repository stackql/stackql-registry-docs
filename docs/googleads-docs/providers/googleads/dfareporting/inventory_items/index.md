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
| `estimatedClickThroughRate` | `string` | Estimated click-through rate of this inventory item. |
| `projectId` | `string` | Project ID of this inventory item. |
| `pricing` | `object` | Pricing Information |
| `rfpId` | `string` | RFP ID of this inventory item. |
| `lastModifiedInfo` | `object` | Modification timestamp. |
| `advertiserId` | `string` | Advertiser ID of this inventory item. |
| `subaccountId` | `string` | Subaccount ID of this inventory item. |
| `contentCategoryId` | `string` | Content category ID of this inventory item. |
| `negotiationChannelId` | `string` | Negotiation channel ID of this inventory item. |
| `adSlots` | `array` | Ad slots of this inventory item. If this inventory item represents a standalone placement, there will be exactly one ad slot. If this inventory item represents a placement group, there will be more than one ad slot, each representing one child placement in that placement group. |
| `accountId` | `string` | Account ID of this inventory item. |
| `estimatedConversionRate` | `string` | Estimated conversion rate of this inventory item. |
| `siteId` | `string` | ID of the site this inventory item is associated with. |
| `inPlan` | `boolean` | Whether this inventory item is in plan. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#inventoryItem". |
| `type` | `string` | Type of inventory item. |
| `orderId` | `string` | Order ID of this inventory item. |
| `placementStrategyId` | `string` | Placement strategy ID of this inventory item. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `inventoryItems_get` | `SELECT` | `id, profileId, projectId` | Gets one inventory item by ID. |
| `inventoryItems_list` | `SELECT` | `profileId, projectId` | Retrieves a list of inventory items, possibly filtered. This method supports paging. |
