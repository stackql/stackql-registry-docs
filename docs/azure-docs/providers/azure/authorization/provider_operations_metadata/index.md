---
title: provider_operations_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_operations_metadata
  - authorization
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
<tr><td><b>Name</b></td><td><code>provider_operations_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.provider_operations_metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The provider id. |
| `name` | `string` | The provider name. |
| `displayName` | `string` | The provider display name. |
| `operations` | `array` | The provider operations. |
| `resourceTypes` | `array` | The provider resource types |
| `type` | `string` | The provider type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceProviderNamespace` | Gets provider operations metadata for the specified resource provider. |
| `list` | `SELECT` |  | Gets provider operations metadata for all resource providers. |
| `_list` | `EXEC` |  | Gets provider operations metadata for all resource providers. |
