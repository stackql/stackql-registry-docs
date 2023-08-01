---
title: delegated_provider_offers
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_provider_offers
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
<tr><td><b>Name</b></td><td><code>delegated_provider_offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.subscriptions_admin.delegated_provider_offers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource |
| `properties` | `object` | Properties for an delegated provider. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DelegatedProviderOffers_Get` | `SELECT` | `delegatedProviderSubscriptionId, offer, subscriptionId` | Get the specified delegated provider offer. |
| `DelegatedProviderOffers_List` | `SELECT` | `delegatedProviderSubscriptionId, subscriptionId` | Get the list of delegated provider offers. |
