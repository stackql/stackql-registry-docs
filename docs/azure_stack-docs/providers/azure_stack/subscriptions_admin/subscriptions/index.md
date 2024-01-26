---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - subscriptions_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.subscriptions_admin.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier. |
| `delegatedProviderSubscriptionId` | `string` | Parent DelegatedProvider subscription identifier. |
| `displayName` | `string` | Subscription name. |
| `externalReferenceId` | `string` | External reference identifier. |
| `offerId` | `string` | Identifier of the offer under the scope of a delegated provider. |
| `owner` | `string` | Subscription owner. |
| `routingResourceManagerType` | `string` | Resource manager type. |
| `state` | `string` | Subscription notification state. |
| `subscriptionId` | `string` | Subscription identifier. |
| `tenantId` | `string` | Directory tenant identifier. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `subscriptionId, targetSubscriptionId` | Get a specified subscription. |
| `list` | `SELECT` | `subscriptionId` | Get the list of subscriptions. |
| `create_or_update` | `INSERT` | `subscriptionId, targetSubscriptionId` | Creates or updates the specified subscription. |
| `delete` | `DELETE` | `subscriptionId, targetSubscriptionId` | Delete the specified subscription. |
| `_list` | `EXEC` | `subscriptionId` | Get the list of subscriptions. |
| `check_identity_health` | `EXEC` | `subscriptionId` | Checks the identity health |
| `check_name_availability` | `EXEC` | `subscriptionId` | Get the list of subscriptions. |
| `move_subscriptions` | `EXEC` | `subscriptionId, data__resources` | Move subscriptions between delegated provider offers. |
| `restore_data` | `EXEC` | `subscriptionId` | Restores the data |
| `validate_move_subscriptions` | `EXEC` | `subscriptionId, data__resources` | Validate that user subscriptions can be moved between delegated provider offers. |
