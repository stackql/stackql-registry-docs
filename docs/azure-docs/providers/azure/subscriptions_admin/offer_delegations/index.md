---
title: offer_delegations
hide_title: false
hide_table_of_contents: false
keywords:
  - offer_delegations
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
<tr><td><b>Name</b></td><td><code>offer_delegations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.subscriptions_admin.offer_delegations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource |
| `properties` | `object` | Properties for an offer delegation. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `OfferDelegations_Get` | `SELECT` | `offer, offerDelegationName, resourceGroupName, subscriptionId` | Get the specified offer delegation. |
| `OfferDelegations_List` | `SELECT` | `offer, resourceGroupName, subscriptionId` | Get the list of offer delegations. |
| `OfferDelegations_CreateOrUpdate` | `INSERT` | `offer, offerDelegationName, resourceGroupName, subscriptionId` | Create or update the offer delegation. |
| `OfferDelegations_Delete` | `DELETE` | `offer, offerDelegationName, resourceGroupName, subscriptionId` | Delete the specified offer delegation. |
