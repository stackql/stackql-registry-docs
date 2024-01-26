---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - user_subscriptions
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
<tr><td><b>Id</b></td><td><code>azure_stack.user_subscriptions.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier. |
| `displayName` | `string` | Subscription name. |
| `offerId` | `string` | Identifier of the offer under the scope of a delegated provider. |
| `state` | `string` | Subscription notification state. |
| `subscriptionId` | `string` | Subscription identifier. |
| `tenantId` | `string` | Directory tenant identifier. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `subscriptionId` | Gets details about particular subscription. |
| `list` | `SELECT` |  | Get the list of subscriptions. |
| `create_or_update` | `INSERT` | `subscriptionId` | Create or updates a subscription. |
| `delete` | `DELETE` | `subscriptionId` | Delete the specified subscription. |
| `_list` | `EXEC` |  | Get the list of subscriptions. |
