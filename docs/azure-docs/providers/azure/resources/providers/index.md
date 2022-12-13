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
| `resourceTypes` | `array` | The collection of provider resource types. |
| `namespace` | `string` | The namespace of the resource provider. |
| `providerAuthorizationConsentState` | `string` | The provider authorization consent state. |
| `registrationPolicy` | `string` | The registration policy of the resource provider. |
| `registrationState` | `string` | The registration state of the resource provider. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Providers_Get` | `SELECT` | `resourceProviderNamespace, subscriptionId` | Gets the specified resource provider. |
| `Providers_List` | `SELECT` | `subscriptionId` | Gets all resource providers for a subscription. |
| `Providers_GetAtTenantScope` | `EXEC` | `resourceProviderNamespace` | Gets the specified resource provider at the tenant level. |
| `Providers_ListAtTenantScope` | `EXEC` |  | Gets all resource providers for the tenant. |
| `Providers_ProviderPermissions` | `EXEC` | `resourceProviderNamespace, subscriptionId` | Get the provider permissions. |
| `Providers_Register` | `EXEC` | `resourceProviderNamespace, subscriptionId` | Registers a subscription with a resource provider. |
| `Providers_RegisterAtManagementGroupScope` | `EXEC` | `groupId, resourceProviderNamespace` | Registers a management group with a resource provider. Use this operation to register a resource provider with resource types that can be deployed at the management group scope. It does not recursively register subscriptions within the management group. Instead, you must register subscriptions individually. |
| `Providers_Unregister` | `EXEC` | `resourceProviderNamespace, subscriptionId` | Unregisters a subscription from a resource provider. |
