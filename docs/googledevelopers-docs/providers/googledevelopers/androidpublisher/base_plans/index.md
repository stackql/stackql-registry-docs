---
title: base_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - base_plans
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
<tr><td><b>Name</b></td><td><code>base_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.base_plans</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `monetization_subscriptions_basePlans_delete` | `DELETE` | `basePlanId, packageName, productId` | Deletes a base plan. Can only be done for draft base plans. This action is irreversible. |
| `monetization_subscriptions_basePlans_activate` | `EXEC` | `basePlanId, packageName, productId` | Activates a base plan. Once activated, base plans will be available to new subscribers. |
| `monetization_subscriptions_basePlans_deactivate` | `EXEC` | `basePlanId, packageName, productId` | Deactivates a base plan. Once deactivated, the base plan will become unavailable to new subscribers, but existing subscribers will maintain their subscription |
| `monetization_subscriptions_basePlans_migratePrices` | `EXEC` | `basePlanId, packageName, productId` | Migrates subscribers who are receiving an historical subscription price to the currently-offered price for the specified region. Requests will cause price change notifications to be sent to users who are currently receiving an historical price older than the supplied timestamp. Subscribers who do not agree to the new price will have their subscription ended at the next renewal. |
