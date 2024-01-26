---
title: offer_delegations
hide_title: false
hide_table_of_contents: false
keywords:
  - offer_delegations
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
<tr><td><b>Name</b></td><td><code>offer_delegations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.subscriptions_admin.offer_delegations</code></td></tr>
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
| `get` | `SELECT` | `offer, offerDelegationName, resourceGroupName, subscriptionId` | Get the specified offer delegation. |
| `list` | `SELECT` | `offer, resourceGroupName, subscriptionId` | Get the list of offer delegations. |
| `create_or_update` | `INSERT` | `offer, offerDelegationName, resourceGroupName, subscriptionId` | Create or update the offer delegation. |
| `delete` | `DELETE` | `offer, offerDelegationName, resourceGroupName, subscriptionId` | Delete the specified offer delegation. |
| `_list` | `EXEC` | `offer, resourceGroupName, subscriptionId` | Get the list of offer delegations. |
