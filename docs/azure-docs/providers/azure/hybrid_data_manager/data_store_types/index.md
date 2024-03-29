---
title: data_store_types
hide_title: false
hide_table_of_contents: false
keywords:
  - data_store_types
  - hybrid_data_manager
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
<tr><td><b>Name</b></td><td><code>data_store_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_data_manager.data_store_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the object. |
| `name` | `string` | Name of the object. |
| `properties` | `object` | Data Store Type properties. |
| `type` | `string` | Type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataManagerName, dataStoreTypeName, resourceGroupName, subscriptionId` | Gets the data store/repository type given its name. |
| `list_by_data_manager` | `SELECT` | `dataManagerName, resourceGroupName, subscriptionId` | Gets all the data store/repository types that the resource supports. |
| `_list_by_data_manager` | `EXEC` | `dataManagerName, resourceGroupName, subscriptionId` | Gets all the data store/repository types that the resource supports. |
