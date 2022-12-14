---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - resources
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
<tr><td><b>Id</b></td><td><code>azure.resources.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The fully qualified ID for the subscription. For example, /subscriptions/00000000-0000-0000-0000-000000000000. |
| `subscriptionId` | `string` | The subscription ID. |
| `displayName` | `string` | The subscription display name. |
| `managedByTenants` | `array` | An array containing the tenants managing the subscription. |
| `subscriptionPolicies` | `object` | Subscription policies. |
| `tags` | `object` | The tags attached to the subscription. |
| `tenantId` | `string` | The subscription tenant ID. |
| `authorizationSource` | `string` | The authorization source of the request. Valid values are one or more combinations of Legacy, RoleBased, Bypassed, Direct and Management. For example, 'Legacy, RoleBased'. |
| `state` | `string` | The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Subscriptions_Get` | `SELECT` | `subscriptionId` | Gets details about a specified subscription. |
| `Subscriptions_List` | `SELECT` |  | Gets all subscriptions for a tenant. |
| `Subscriptions_CheckZonePeers` | `EXEC` | `subscriptionId` | Compares a subscriptions logical zone mapping |
| `Subscriptions_ListLocations` | `EXEC` | `subscriptionId` | This operation provides all the locations that are available for resource providers; however, each resource provider may support a subset of this list. |
