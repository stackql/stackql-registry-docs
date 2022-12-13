---
title: price_sheet
hide_title: false
hide_table_of_contents: false
keywords:
  - price_sheet
  - consumption
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>price_sheet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.consumption.price_sheet</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The full qualified ARM ID of an event. |
| `name` | `string` | The ID that uniquely identifies an event.  |
| `properties` | `object` | price sheet result. It contains the pricesheet associated with billing period |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | The etag for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PriceSheet_Get` | `SELECT` | `subscriptionId` | Gets the price sheet for a subscription. Price sheet is available via this API only for May 1, 2014 or later. |
| `PriceSheet_GetByBillingPeriod` | `EXEC` | `billingPeriodName, subscriptionId` | Get the price sheet for a scope by subscriptionId and billing period. Price sheet is available via this API only for May 1, 2014 or later. |
