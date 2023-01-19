---
title: guaranteed_orders
hide_title: false
hide_table_of_contents: false
keywords:
  - guaranteed_orders
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
<tr><td><b>Name</b></td><td><code>guaranteed_orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.guaranteed_orders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the guaranteed order. |
| `status` | `object` | The status settings of the guaranteed order. |
| `defaultCampaignId` | `string` | The ID of the default campaign that is assigned to the guaranteed order. The default campaign must belong to the default advertiser. |
| `guaranteedOrderId` | `string` | Output only. The unique identifier of the guaranteed order. The guaranteed order IDs have the format `&#123;exchange&#125;-&#123;legacy_guaranteed_order_id&#125;`. |
| `defaultAdvertiserId` | `string` | Output only. The ID of default advertiser of the guaranteed order. The default advertiser is either the read_write_advertiser_id or, if that is not set, the first advertiser listed in read_advertiser_ids. Otherwise, there is no default advertiser. |
| `readAccessInherited` | `boolean` | Whether all advertisers of read_write_partner_id have read access to the guaranteed order. Only applicable if read_write_partner_id is set. If True, overrides read_advertiser_ids. |
| `publisherName` | `string` | Required. The publisher name of the guaranteed order. Must be UTF-8 encoded with a maximum size of 240 bytes. |
| `readAdvertiserIds` | `array` | The IDs of advertisers with read access to the guaranteed order. This field must not include the advertiser assigned to read_write_advertiser_id if it is set. All advertisers in this field must belong to read_write_partner_id or the same partner as read_write_advertiser_id. |
| `readWritePartnerId` | `string` | The partner with read/write access to the guaranteed order. |
| `exchange` | `string` | Required. Immutable. The exchange where the guaranteed order originated. |
| `legacyGuaranteedOrderId` | `string` | Output only. The legacy ID of the guaranteed order. Assigned by the original exchange. The legacy ID is unique within one exchange, but is not guaranteed to be unique across all guaranteed orders. This ID is used in SDF and UI. |
| `readWriteAdvertiserId` | `string` | The advertiser with read/write access to the guaranteed order. This is also the default advertiser of the guaranteed order. |
| `displayName` | `string` | Required. The display name of the guaranteed order. Must be UTF-8 encoded with a maximum size of 240 bytes. |
| `updateTime` | `string` | Output only. The timestamp when the guaranteed order was last updated. Assigned by the system. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `guaranteedOrders_get` | `SELECT` | `guaranteedOrdersId` | Gets a guaranteed order. |
| `guaranteedOrders_list` | `SELECT` |  | Lists guaranteed orders that are accessible to the current user. The order is defined by the order_by parameter. If a filter by entity_status is not specified, guaranteed orders with entity status `ENTITY_STATUS_ARCHIVED` will not be included in the results. |
| `guaranteedOrders_create` | `INSERT` |  | Creates a new guaranteed order. Returns the newly created guaranteed order if successful. |
| `guaranteedOrders_editGuaranteedOrderReadAccessors` | `EXEC` | `guaranteedOrdersId` | Edits read advertisers of a guaranteed order. |
| `guaranteedOrders_patch` | `EXEC` | `guaranteedOrdersId` | Updates an existing guaranteed order. Returns the updated guaranteed order if successful. |
