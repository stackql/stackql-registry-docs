---
title: providers_at_tenant_scope
hide_title: false
hide_table_of_contents: false
keywords:
  - providers_at_tenant_scope
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
<tr><td><b>Name</b></td><td><code>providers_at_tenant_scope</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resources.providers_at_tenant_scope</code></td></tr>
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
| `get` | `SELECT` | `resourceProviderNamespace` | Gets the specified resource provider at the tenant level. |
| `list` | `SELECT` |  | Gets all resource providers for the tenant. |
| `_list` | `EXEC` |  | Gets all resource providers for the tenant. |
