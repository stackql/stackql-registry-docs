---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - subscriptions_admin
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
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.subscriptions_admin.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier. |
| `routingResourceManagerType` | `string` | Resource manager type. |
| `displayName` | `string` | Subscription name. |
| `externalReferenceId` | `string` | External reference identifier. |
| `owner` | `string` | Subscription owner. |
| `state` | `string` | Subscription notification state. |
| `tenantId` | `string` | Directory tenant identifier. |
| `subscriptionId` | `string` | Subscription identifier. |
| `delegatedProviderSubscriptionId` | `string` | Parent DelegatedProvider subscription identifier. |
| `offerId` | `string` | Identifier of the offer under the scope of a delegated provider. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Subscriptions_Get` | `SELECT` | `subscriptionId, targetSubscriptionId` | Get a specified subscription. |
| `Subscriptions_List` | `SELECT` | `subscriptionId` | Get the list of subscriptions. |
| `Subscriptions_CreateOrUpdate` | `INSERT` | `subscriptionId, targetSubscriptionId` | Creates or updates the specified subscription. |
| `Subscriptions_Delete` | `DELETE` | `subscriptionId, targetSubscriptionId` | Delete the specified subscription. |
| `Subscriptions_CheckIdentityHealth` | `EXEC` | `subscriptionId` | Checks the identity health |
| `Subscriptions_CheckNameAvailability` | `EXEC` | `subscriptionId` | Get the list of subscriptions. |
| `Subscriptions_MoveSubscriptions` | `EXEC` | `subscriptionId, data__resources` | Move subscriptions between delegated provider offers. |
| `Subscriptions_RestoreData` | `EXEC` | `subscriptionId` | Restores the data |
| `Subscriptions_UpdateEncryption` | `EXEC` | `subscriptionId` | Update the encryption settings. |
| `Subscriptions_ValidateMoveSubscriptions` | `EXEC` | `subscriptionId, data__resources` | Validate that user subscriptions can be moved between delegated provider offers. |
