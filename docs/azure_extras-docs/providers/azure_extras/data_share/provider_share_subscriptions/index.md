---
title: provider_share_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_share_subscriptions
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
<tr><td><b>Name</b></td><td><code>provider_share_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_share.provider_share_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id of the azure resource |
| `name` | `string` | Name of the azure resource |
| `type` | `string` | Type of the azure resource |
| `properties` | `object` | Provider share subscription properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProviderShareSubscriptions_ListByShare` | `SELECT` | `accountName, api-version, resourceGroupName, shareName, subscriptionId` | List share subscriptions in a provider share |
| `ProviderShareSubscriptions_Adjust` | `EXEC` | `accountName, api-version, providerShareSubscriptionId, resourceGroupName, shareName, subscriptionId` | Adjust a share subscription's expiration date in a provider share |
| `ProviderShareSubscriptions_GetByShare` | `EXEC` | `accountName, api-version, providerShareSubscriptionId, resourceGroupName, shareName, subscriptionId` | Get share subscription in a provider share |
| `ProviderShareSubscriptions_Reinstate` | `EXEC` | `accountName, api-version, providerShareSubscriptionId, resourceGroupName, shareName, subscriptionId` | Reinstate share subscription in a provider share |
| `ProviderShareSubscriptions_Revoke` | `EXEC` | `accountName, api-version, providerShareSubscriptionId, resourceGroupName, shareName, subscriptionId` | Revoke share subscription in a provider share |
