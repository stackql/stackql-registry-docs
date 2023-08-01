---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - longview
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.longview.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID of this Subscription tier.<br /> |
| `clients_included` | `integer` | The number of Longview Clients that may be created with this Subscription tier.<br /> |
| `label` | `string` | A display name for this Subscription tier.<br /> |
| `price` | `object` | Pricing information about this Subscription tier.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getLongviewSubscription` | `SELECT` | `subscriptionId` | Get the Longview plan details as a single `LongviewSubscription` object for the provided subscription ID. This is a public endpoint and requires no authentication.<br /> |
| `getLongviewSubscriptions` | `SELECT` |  | Returns a paginated list of available Longview Subscriptions. This is a public endpoint and requires no authentication.<br /> |
| `_getLongviewSubscription` | `EXEC` | `subscriptionId` | Get the Longview plan details as a single `LongviewSubscription` object for the provided subscription ID. This is a public endpoint and requires no authentication.<br /> |
| `_getLongviewSubscriptions` | `EXEC` |  | Returns a paginated list of available Longview Subscriptions. This is a public endpoint and requires no authentication.<br /> |
