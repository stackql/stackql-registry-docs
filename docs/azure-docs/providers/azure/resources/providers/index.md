---
title: providers
hide_title: false
hide_table_of_contents: false
keywords:
  - providers
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
<tr><td><b>Name</b></td><td><code>providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resources.providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The provider ID. |
| `namespace` | `string` | The namespace of the resource provider. |
| `providerAuthorizationConsentState` | `string` | The provider authorization consent state. |
| `registrationPolicy` | `string` | The registration policy of the resource provider. |
| `registrationState` | `string` | The registration state of the resource provider. |
| `resourceTypes` | `array` | The collection of provider resource types. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceProviderNamespace, subscriptionId` | Gets the specified resource provider. |
| `list` | `SELECT` | `subscriptionId` | Gets all resource providers for a subscription. |
| `_list` | `EXEC` | `subscriptionId` | Gets all resource providers for a subscription. |
| `_provider_permissions` | `EXEC` | `resourceProviderNamespace, subscriptionId` | Get the provider permissions. |
| `provider_permissions` | `EXEC` | `resourceProviderNamespace, subscriptionId` | Get the provider permissions. |
| `register` | `EXEC` | `resourceProviderNamespace, subscriptionId` | Registers a subscription with a resource provider. |
| `register_at_management_group_scope` | `EXEC` | `groupId, resourceProviderNamespace` | Registers a management group with a resource provider. Use this operation to register a resource provider with resource types that can be deployed at the management group scope. It does not recursively register subscriptions within the management group. Instead, you must register subscriptions individually. |
| `unregister` | `EXEC` | `resourceProviderNamespace, subscriptionId` | Unregisters a subscription from a resource provider. |
