---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - subscription
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
<tr><td><b>Id</b></td><td><code>azure.subscription.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The fully qualified ID for the subscription. For example, /subscriptions/00000000-0000-0000-0000-000000000000. |
| `authorizationSource` | `string` | The authorization source of the request. Valid values are one or more combinations of Legacy, RoleBased, Bypassed, Direct and Management. For example, 'Legacy, RoleBased'. |
| `displayName` | `string` | The subscription display name. |
| `state` | `string` | The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted. |
| `subscriptionId` | `string` | The subscription ID. |
| `subscriptionPolicies` | `object` | Subscription policies. |
| `tags` | `object` | Tags for the subscription |
| `tenantId` | `string` | The tenant ID. For example, 00000000-0000-0000-0000-000000000000. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `subscriptionId` | Gets details about a specified subscription. |
| `list` | `SELECT` |  | Gets all subscriptions for a tenant. |
| `_list` | `EXEC` |  | Gets all subscriptions for a tenant. |
