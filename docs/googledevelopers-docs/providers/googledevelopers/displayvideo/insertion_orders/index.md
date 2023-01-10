---
title: insertion_orders
hide_title: false
hide_table_of_contents: false
keywords:
  - insertion_orders
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
<tr><td><b>Name</b></td><td><code>insertion_orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.insertion_orders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the insertion order. |
| `insertionOrderId` | `string` | Output only. The unique ID of the insertion order. Assigned by the system. |
| `campaignId` | `string` | Required. Immutable. The unique ID of the campaign that the insertion order belongs to. |
| `entityStatus` | `string` | Required. Controls whether or not the insertion order can spend its budget and bid on inventory. * For CreateInsertionOrder method, only `ENTITY_STATUS_DRAFT` is allowed. To activate an insertion order, use UpdateInsertionOrder method and update the status to `ENTITY_STATUS_ACTIVE` after creation. * An insertion order cannot be changed back to `ENTITY_STATUS_DRAFT` status from any other status. * An insertion order cannot be set to `ENTITY_STATUS_ACTIVE` if its parent campaign is not active. |
| `frequencyCap` | `object` | Settings that control the number of times a user may be shown with the same ad during a given time period. |
| `integrationDetails` | `object` | Integration details of an entry. |
| `reservationType` | `string` | Output only. The reservation type of the insertion order. |
| `pacing` | `object` | Settings that control the rate at which a budget is spent. |
| `billableOutcome` | `string` | Immutable. The billable outcome of the insertion order. |
| `updateTime` | `string` | Output only. The timestamp when the insertion order was last updated. Assigned by the system. |
| `bidStrategy` | `object` | Settings that control the bid strategy. Bid strategy determines the bid price. |
| `displayName` | `string` | Required. The display name of the insertion order. Must be UTF-8 encoded with a maximum size of 240 bytes. |
| `partnerCosts` | `array` | The partner costs associated with the insertion order. If absent or empty in CreateInsertionOrder method, the newly created insertion order will inherit partner costs from the partner settings. |
| `advertiserId` | `string` | Output only. The unique ID of the advertiser the insertion order belongs to. |
| `insertionOrderType` | `string` | The type of insertion order. If this field is unspecified in creation, the value defaults to `RTB`. |
| `performanceGoal` | `object` | Settings that control the performance goal of a campaign or insertion order. |
| `budget` | `object` | Settings that control how insertion order budget is allocated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `advertisers_insertionOrders_get` | `SELECT` | `advertisersId, insertionOrdersId` | Gets an insertion order. Returns error code `NOT_FOUND` if the insertion order does not exist. |
| `advertisers_insertionOrders_list` | `SELECT` | `advertisersId` | Lists insertion orders in an advertiser. The order is defined by the order_by parameter. If a filter by entity_status is not specified, insertion orders with `ENTITY_STATUS_ARCHIVED` will not be included in the results. |
| `advertisers_insertionOrders_create` | `INSERT` | `advertisersId` | Creates a new insertion order. Returns the newly created insertion order if successful. |
| `advertisers_insertionOrders_delete` | `DELETE` | `advertisersId, insertionOrdersId` | Deletes an insertion order. Returns error code `NOT_FOUND` if the insertion order does not exist. The insertion order should be archived first, i.e. set entity_status to `ENTITY_STATUS_ARCHIVED`, to be able to delete it. |
| `advertisers_insertionOrders_patch` | `EXEC` | `advertisersId, insertionOrdersId` | Updates an existing insertion order. Returns the updated insertion order if successful. |
