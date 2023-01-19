---
title: subscriptionsv2
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptionsv2
  - androidpublisher
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
<tr><td><b>Name</b></td><td><code>subscriptionsv2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.subscriptionsv2</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `externalAccountIdentifiers` | `object` | User account identifier in the third-party service. |
| `kind` | `string` | This kind represents a SubscriptionPurchaseV2 object in the androidpublisher service. |
| `subscribeWithGoogleInfo` | `object` | Information associated with purchases made with 'Subscribe with Google'. |
| `lineItems` | `array` | Item-level info for a subscription purchase. The items in the same purchase should be either all with AutoRenewingPlan or all with PrepaidPlan. |
| `latestOrderId` | `string` | The order id of the latest order associated with the purchase of the subscription. For autoRenewing subscription, this is the order id of signup order if it is not renewed yet, or the last recurring order id (success, pending, or declined order). For prepaid subscription, this is the order id associated with the queried purchase token. |
| `subscriptionState` | `string` | The current state of the subscription. |
| `testPurchase` | `object` | Whether this subscription purchase is a test purchase. |
| `canceledStateContext` | `object` | Information specific to a subscription in canceled state. |
| `regionCode` | `string` | ISO 3166-1 alpha-2 billing country/region code of the user at the time the subscription was granted. |
| `linkedPurchaseToken` | `string` | The purchase token of the old subscription if this subscription is one of the following: * Re-signup of a canceled but non-lapsed subscription * Upgrade/downgrade from a previous subscription. * Convert from prepaid to auto renewing subscription. * Convert from an auto renewing subscription to prepaid. * Topup a prepaid subscription. |
| `startTime` | `string` | Time at which the subscription was granted. Not set for pending subscriptions (subscription was created but awaiting payment during signup). |
| `acknowledgementState` | `string` | The acknowledgement state of the subscription. |
| `pausedStateContext` | `object` | Information specific to a subscription in paused state. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `purchases_subscriptionsv2_get` | `SELECT` | `packageName, token` |
