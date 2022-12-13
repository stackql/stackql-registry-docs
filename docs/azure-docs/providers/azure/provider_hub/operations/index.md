---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - provider_hub
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.provider_hub.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the operation. |
| `origin` | `string` |  |
| `properties` | `` |  |
| `actionType` | `string` |  |
| `display` | `object` | Display information of the operation. |
| `isDataAction` | `boolean` | Indicates whether the operation applies to data-plane. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Operations_List` | `SELECT` |  | Lists all the operations supported by Microsoft.ProviderHub. |
| `Operations_ListByProviderRegistration` | `SELECT` | `providerNamespace, subscriptionId` | Gets the operations supported by the given provider. |
| `Operations_CreateOrUpdate` | `INSERT` | `providerNamespace, subscriptionId, data__contents` | Creates or updates the operation supported by the given provider. |
| `Operations_Delete` | `DELETE` | `providerNamespace, subscriptionId` | Deletes an operation. |
