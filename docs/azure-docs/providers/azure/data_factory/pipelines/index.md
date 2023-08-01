---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
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
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.pipelines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `etag` | `string` | Etag identifies change in the resource. |
| `properties` | `object` | A data factory pipeline. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Pipelines_Get` | `SELECT` | `api-version, factoryName, pipelineName, resourceGroupName, subscriptionId` | Gets a pipeline. |
| `Pipelines_ListByFactory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists pipelines. |
| `Pipelines_CreateOrUpdate` | `INSERT` | `api-version, factoryName, pipelineName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a pipeline. |
| `Pipelines_Delete` | `DELETE` | `api-version, factoryName, pipelineName, resourceGroupName, subscriptionId` | Deletes a pipeline. |
| `Pipelines_CreateRun` | `EXEC` | `api-version, factoryName, pipelineName, resourceGroupName, subscriptionId` | Creates a run of a pipeline. |
