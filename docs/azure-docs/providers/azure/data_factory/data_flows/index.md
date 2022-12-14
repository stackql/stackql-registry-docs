---
title: data_flows
hide_title: false
hide_table_of_contents: false
keywords:
  - data_flows
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
<tr><td><b>Name</b></td><td><code>data_flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.data_flows</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | Azure Data Factory nested object which contains a flow with data movements and transformations. |
| `type` | `string` | The resource type. |
| `etag` | `string` | Etag identifies change in the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataFlows_Get` | `SELECT` | `api-version, dataFlowName, factoryName, resourceGroupName, subscriptionId` | Gets a data flow. |
| `DataFlows_ListByFactory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists data flows. |
| `DataFlows_CreateOrUpdate` | `INSERT` | `api-version, dataFlowName, factoryName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a data flow. |
| `DataFlows_Delete` | `DELETE` | `api-version, dataFlowName, factoryName, resourceGroupName, subscriptionId` | Deletes a data flow. |
