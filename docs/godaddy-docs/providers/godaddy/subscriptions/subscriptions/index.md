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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="godaddy.subscriptions.subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="addons" /> | `array` | An array of additional products that have been purchased to augment this Subscription |
| <CopyableCode code="billing" /> | `object` |  |
| <CopyableCode code="cancelable" /> | `boolean` | Whether or not the Subscription is allowed to be canceled |
| <CopyableCode code="createdAt" /> | `string` | When the Subscription was created |
| <CopyableCode code="expiresAt" /> | `string` | When the Subscription will expire |
| <CopyableCode code="label" /> | `string` | A human readable description of this Subscription |
| <CopyableCode code="launchUrl" /> | `string` | The url to use or manage this Subscription's active product |
| <CopyableCode code="paymentProfileId" /> | `integer` | Unique identifier of the payment profile that will be used to automatically renew this Subscription |
| <CopyableCode code="priceLocked" /> | `boolean` | Whether the renewal price will be based from the list price or a locked-in price for this shopper |
| <CopyableCode code="product" /> | `object` |  |
| <CopyableCode code="relations" /> | `object` |  |
| <CopyableCode code="renewAuto" /> | `boolean` | Whether or not the Subscription is set to be automatically renewed via the billing agent |
| <CopyableCode code="renewable" /> | `boolean` | Whether or not the Subscription is allowed to be renewed |
| <CopyableCode code="status" /> | `string` | Whether the Subscription is active or the specific non-active state |
| <CopyableCode code="subscriptionId" /> | `string` | Unique identifier of the Subscription |
| <CopyableCode code="upgradeable" /> | `boolean` | Whether or not the Subscription is allowed to be upgraded |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscription_id" /> | Retrieve details for the specified Subscription |
| <CopyableCode code="list" /> | `SELECT` |  | Retrieve a list of Subscriptions for the specified Shopper |
| <CopyableCode code="_list" /> | `EXEC` |  | Retrieve a list of Subscriptions for the specified Shopper |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="subscription_id" /> | Cancel the specified Subscription |
| <CopyableCode code="product_groups" /> | `EXEC` |  | Retrieve a list of ProductGroups for the specified Shopper |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="subscription_id" /> | Only Subscription properties that can be changed without immediate  financial impact can be modified via PATCH, whereas some properties  can be changed by purchasing a renewal  This endpoint only supports JWT authentication |
