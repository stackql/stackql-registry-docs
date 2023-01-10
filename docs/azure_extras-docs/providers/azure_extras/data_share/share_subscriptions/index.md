---
title: share_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - share_subscriptions
  - data_share
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>share_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_share.share_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id of the azure resource |
| `name` | `string` | Name of the azure resource |
| `type` | `string` | Type of the azure resource |
| `properties` | `object` | Share subscription property bag. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ShareSubscriptions_Get` | `SELECT` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId` | Get a shareSubscription in an account |
| `ShareSubscriptions_ListByAccount` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | List share subscriptions in an account |
| `ShareSubscriptions_Create` | `INSERT` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId, data__properties` | Create a shareSubscription in an account |
| `ShareSubscriptions_Delete` | `DELETE` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId` | Delete a shareSubscription in an account |
| `ShareSubscriptions_CancelSynchronization` | `EXEC` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId, data__synchronizationId` | Request to cancel a synchronization. |
| `ShareSubscriptions_ListSourceShareSynchronizationSettings` | `EXEC` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId` | Get synchronization settings set on a share |
| `ShareSubscriptions_ListSynchronizationDetails` | `EXEC` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId, data__synchronizationId` | List synchronization details |
| `ShareSubscriptions_ListSynchronizations` | `EXEC` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId` | List synchronizations of a share subscription |
| `ShareSubscriptions_Synchronize` | `EXEC` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId` | Initiate a copy |
