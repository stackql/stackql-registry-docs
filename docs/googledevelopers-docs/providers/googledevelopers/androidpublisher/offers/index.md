---
title: offers
hide_title: false
hide_table_of_contents: false
keywords:
  - offers
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
<tr><td><b>Name</b></td><td><code>offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.offers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `offerId` | `string` | Required. Immutable. Unique ID of this subscription offer. Must be unique within the base plan. |
| `targeting` | `object` | Defines the rule a user needs to satisfy to receive this offer. |
| `offerTags` | `array` | List of up to 20 custom tags specified for this offer, and returned to the app through the billing library. |
| `packageName` | `string` | Required. Immutable. The package name of the app the parent subscription belongs to. |
| `phases` | `array` | Required. The phases of this subscription offer. Must contain at least one entry, and may contain at most five. Users will always receive all these phases in the specified order. Phases may not be added, removed, or reordered after initial creation. |
| `otherRegionsConfig` | `object` | Configuration for any new locations Play may launch in specified on a subscription offer. |
| `productId` | `string` | Required. Immutable. The ID of the parent subscription this offer belongs to. |
| `state` | `string` | Output only. The current state of this offer. Can be changed using Activate and Deactivate actions. NB: the base plan state supersedes this state, so an active offer may not be available if the base plan is not active. |
| `regionalConfigs` | `array` | Required. The region-specific configuration of this offer. Must contain at least one entry. |
| `basePlanId` | `string` | Required. Immutable. The ID of the base plan to which this offer is an extension. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `monetization_subscriptions_basePlans_offers_get` | `SELECT` | `basePlanId, offerId, packageName, productId` | Reads a single offer |
| `monetization_subscriptions_basePlans_offers_list` | `SELECT` | `basePlanId, packageName, productId` | Lists all offers under a given subscription. |
| `monetization_subscriptions_basePlans_offers_create` | `INSERT` | `basePlanId, packageName, productId` | Creates a new subscription offer. Only auto-renewing base plans can have subscription offers. The offer state will be DRAFT until it is activated. |
| `monetization_subscriptions_basePlans_offers_delete` | `DELETE` | `basePlanId, offerId, packageName, productId` | Deletes a subscription offer. Can only be done for draft offers. This action is irreversible. |
| `monetization_subscriptions_basePlans_offers_activate` | `EXEC` | `basePlanId, offerId, packageName, productId` | Activates a subscription offer. Once activated, subscription offers will be available to new subscribers. |
| `monetization_subscriptions_basePlans_offers_deactivate` | `EXEC` | `basePlanId, offerId, packageName, productId` | Deactivates a subscription offer. Once deactivated, existing subscribers will maintain their subscription, but the offer will become unavailable to new subscribers. |
| `monetization_subscriptions_basePlans_offers_patch` | `EXEC` | `basePlanId, offerId, packageName, productId` | Updates an existing subscription offer. |
