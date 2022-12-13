---
title: data_services
hide_title: false
hide_table_of_contents: false
keywords:
  - data_services
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
<tr><td><b>Name</b></td><td><code>data_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_data_manager.data_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the object. |
| `name` | `string` | Name of the object. |
| `properties` | `object` | Data Service properties. |
| `type` | `string` | Type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataServices_Get` | `SELECT` | `dataManagerName, dataServiceName, resourceGroupName, subscriptionId` | Gets the data service that matches the data service name given. |
| `DataServices_ListByDataManager` | `SELECT` | `dataManagerName, resourceGroupName, subscriptionId` | This method gets all the data services. |
