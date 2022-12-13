---
title: delegated_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_providers
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
<tr><td><b>Name</b></td><td><code>delegated_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.subscriptions_admin.delegated_providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier. |
| `subscriptionId` | `string` | Subscription identifier. |
| `tenantId` | `string` | Directory tenant identifier. |
| `state` | `string` | Subscription notification state. |
| `delegatedProviderSubscriptionId` | `string` | Parent DelegatedProvider subscription identifier. |
| `displayName` | `string` | Subscription name. |
| `externalReferenceId` | `string` | External reference identifier. |
| `owner` | `string` | Subscription owner. |
| `offerId` | `string` | Identifier of the offer under the scope of a delegated provider. |
| `routingResourceManagerType` | `string` | Resource manager type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DelegatedProviders_Get` | `SELECT` | `delegatedProvider, subscriptionId` | Get the specified delegated provider. |
| `DelegatedProviders_List` | `SELECT` | `subscriptionId` | Get the list of delegatedProviders. |
