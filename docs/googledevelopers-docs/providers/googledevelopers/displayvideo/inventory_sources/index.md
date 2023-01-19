---
title: inventory_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - inventory_sources
  - displayvideo
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
<tr><td><b>Name</b></td><td><code>inventory_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.inventory_sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the inventory source. |
| `rateDetails` | `object` | The rate related settings of the inventory source. |
| `commitment` | `string` | Whether the inventory source has a guaranteed or non-guaranteed delivery. |
| `creativeConfigs` | `array` | The creative requirements of the inventory source. Not applicable for auction packages. |
| `deliveryMethod` | `string` | The delivery method of the inventory source. * For non-guaranteed inventory sources, the only acceptable value is `INVENTORY_SOURCE_DELIVERY_METHOD_PROGRAMMATIC`. * For guaranteed inventory sources, acceptable values are `INVENTORY_SOURCE_DELIVERY_METHOD_TAG` and `INVENTORY_SOURCE_DELIVERY_METHOD_PROGRAMMATIC`. |
| `status` | `object` | The status related settings of the inventory source. |
| `guaranteedOrderId` | `string` | Immutable. The ID of the guaranteed order that this inventory source belongs to. Only applicable when commitment is `INVENTORY_SOURCE_COMMITMENT_GUARANTEED`. |
| `readPartnerIds` | `array` | Output only. The IDs of partners with read-only access to the inventory source. All advertisers of partners in this field inherit read-only access to the inventory source. |
| `inventorySourceId` | `string` | Output only. The unique ID of the inventory source. Assigned by the system. |
| `publisherName` | `string` | The publisher/seller name of the inventory source. |
| `readAdvertiserIds` | `array` | Output only. The IDs of advertisers with read-only access to the inventory source. |
| `inventorySourceType` | `string` | Denotes the type of the inventory source. |
| `readWriteAccessors` | `object` | The partner or advertisers with access to the inventory source. |
| `displayName` | `string` | The display name of the inventory source. Must be UTF-8 encoded with a maximum size of 240 bytes. |
| `exchange` | `string` | The exchange to which the inventory source belongs. |
| `subSitePropertyId` | `string` | Immutable. The unique ID of the sub-site property assigned to this inventory source. |
| `inventorySourceProductType` | `string` | Output only. The product type of the inventory source, denoting the way through which it sells inventory. |
| `timeRange` | `object` | A time range. |
| `dealId` | `string` | The ID in the exchange space that uniquely identifies the inventory source. Must be unique across buyers within each exchange but not necessarily unique across exchanges. |
| `updateTime` | `string` | Output only. The timestamp when the inventory source was last updated. Assigned by the system. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `inventorySources_get` | `SELECT` | `inventorySourcesId` | Gets an inventory source. |
| `inventorySources_list` | `SELECT` |  | Lists inventory sources that are accessible to the current user. The order is defined by the order_by parameter. If a filter by entity_status is not specified, inventory sources with entity status `ENTITY_STATUS_ARCHIVED` will not be included in the results. |
| `inventorySources_create` | `INSERT` |  | Creates a new inventory source. Returns the newly created inventory source if successful. |
| `inventorySources_editInventorySourceReadWriteAccessors` | `EXEC` | `inventorySourcesId` | Edits read/write accessors of an inventory source. Returns the updated read_write_accessors for the inventory source. |
| `inventorySources_patch` | `EXEC` | `inventorySourcesId` | Updates an existing inventory source. Returns the updated inventory source if successful. |
