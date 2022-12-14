---
title: data_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - data_stores
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
<tr><td><b>Name</b></td><td><code>data_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_data_manager.data_stores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the object. |
| `name` | `string` | Name of the object. |
| `type` | `string` | Type of the object. |
| `properties` | `object` | Data Store for sources and sinks |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataStores_Get` | `SELECT` | `dataManagerName, dataStoreName, resourceGroupName, subscriptionId` | This method gets the data store/repository by name. |
| `DataStores_ListByDataManager` | `SELECT` | `dataManagerName, resourceGroupName, subscriptionId` | Gets all the data stores/repositories in the given resource. |
| `DataStores_CreateOrUpdate` | `INSERT` | `dataManagerName, dataStoreName, resourceGroupName, subscriptionId, data__properties` | Creates or updates the data store/repository in the data manager. |
| `DataStores_Delete` | `DELETE` | `dataManagerName, dataStoreName, resourceGroupName, subscriptionId` | This method deletes the given data store/repository. |
