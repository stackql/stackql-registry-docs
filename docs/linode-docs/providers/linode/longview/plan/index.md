---
title: plan
hide_title: false
hide_table_of_contents: false
keywords:
  - plan
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
<tr><td><b>Name</b></td><td><code>plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.longview.plan</code></td></tr>
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
| `getLongviewPlan` | `SELECT` |  | Get the details of your current Longview plan. This returns a `LongviewSubscription` object for your current Longview Pro plan, or an empty set `&#123;&#125;` if your current plan is Longview Free.<br /><br />You must have at least one of the following `global` [User Grants](/docs/api/account/#users-grants-view) in order to access this endpoint:<br /><br />  - `"account_access": read_write`<br />  - `"account_access": read_only`<br />  - `"longview_subscription": true`<br />  - `"add_longview": true`<br /><br /><br />To update your subscription plan, send a request to [Update Longview Plan](/docs/api/longview/#longview-plan-update).<br /> |
| `_getLongviewPlan` | `EXEC` |  | Get the details of your current Longview plan. This returns a `LongviewSubscription` object for your current Longview Pro plan, or an empty set `&#123;&#125;` if your current plan is Longview Free.<br /><br />You must have at least one of the following `global` [User Grants](/docs/api/account/#users-grants-view) in order to access this endpoint:<br /><br />  - `"account_access": read_write`<br />  - `"account_access": read_only`<br />  - `"longview_subscription": true`<br />  - `"add_longview": true`<br /><br /><br />To update your subscription plan, send a request to [Update Longview Plan](/docs/api/longview/#longview-plan-update).<br /> |
| `updateLongviewPlan` | `EXEC` |  | Update your Longview plan to that of the given subcription ID. This returns a `LongviewSubscription` object for the updated Longview Pro plan, or an empty set `&#123;&#125;` if the updated plan is Longview Free.<br /><br />You must have `"longview_subscription": true` configured as a `global` [User Grant](/docs/api/account/#users-grants-view) in order to access this endpoint.<br /><br />You can send a request to the [List Longview Subscriptions](/docs/api/longview/#longview-subscriptions-list) endpoint to receive the details, including `id`'s, of each plan.<br /> |
