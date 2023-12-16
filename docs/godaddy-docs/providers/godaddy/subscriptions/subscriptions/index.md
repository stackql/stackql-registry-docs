---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - subscriptions
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>godaddy.subscriptions.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `addons` | `array` | An array of additional products that have been purchased to augment this Subscription |
| `billing` | `object` |  |
| `cancelable` | `boolean` | Whether or not the Subscription is allowed to be canceled |
| `createdAt` | `string` | When the Subscription was created |
| `expiresAt` | `string` | When the Subscription will expire |
| `label` | `string` | A human readable description of this Subscription |
| `launchUrl` | `string` | The url to use or manage this Subscription's active product |
| `paymentProfileId` | `integer` | Unique identifier of the payment profile that will be used to automatically renew this Subscription |
| `priceLocked` | `boolean` | Whether the renewal price will be based from the list price or a locked-in price for this shopper |
| `product` | `object` |  |
| `relations` | `object` |  |
| `renewAuto` | `boolean` | Whether or not the Subscription is set to be automatically renewed via the billing agent |
| `renewable` | `boolean` | Whether or not the Subscription is allowed to be renewed |
| `status` | `string` | Whether the Subscription is active or the specific non-active state |
| `subscriptionId` | `string` | Unique identifier of the Subscription |
| `upgradeable` | `boolean` | Whether or not the Subscription is allowed to be upgraded |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `subscription_id` | Retrieve details for the specified Subscription |
| `list` | `SELECT` |  | Retrieve a list of Subscriptions for the specified Shopper |
| `cancel` | `EXEC` | `subscription_id` | Cancel the specified Subscription |
| `update` | `EXEC` | `subscription_id` | Only Subscription properties that can be changed without immediate  financial impact can be modified via PATCH, whereas some properties  can be changed by purchasing a renewal  This endpoint only supports JWT authentication |
