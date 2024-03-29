---
title: global_parameters
hide_title: false
hide_table_of_contents: false
keywords:
  - global_parameters
  - data_factory
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
<tr><td><b>Name</b></td><td><code>global_parameters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.global_parameters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `etag` | `string` | Etag identifies change in the resource. |
| `properties` | `object` | Global parameters associated with the Azure Data Factory |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, factoryName, globalParameterName, resourceGroupName, subscriptionId` | Gets a Global parameter |
| `list_by_factory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists Global parameters |
| `create_or_update` | `INSERT` | `api-version, factoryName, globalParameterName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a Global parameter |
| `delete` | `DELETE` | `api-version, factoryName, globalParameterName, resourceGroupName, subscriptionId` | Deletes a Global parameter |
| `_list_by_factory` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists Global parameters |
