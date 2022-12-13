---
title: key_values
hide_title: false
hide_table_of_contents: false
keywords:
  - key_values
  - app_configuration
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
<tr><td><b>Name</b></td><td><code>key_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_configuration.key_values</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | All key-value properties. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `KeyValues_Get` | `SELECT` | `configStoreName, keyValueName, resourceGroupName, subscriptionId` | Gets the properties of the specified key-value. |
| `KeyValues_ListByConfigurationStore` | `SELECT` | `configStoreName, resourceGroupName, subscriptionId` | Lists the key-values for a given configuration store. |
| `KeyValues_CreateOrUpdate` | `INSERT` | `configStoreName, keyValueName, resourceGroupName, subscriptionId` | Creates a key-value. |
| `KeyValues_Delete` | `DELETE` | `configStoreName, keyValueName, resourceGroupName, subscriptionId` | Deletes a key-value. |
