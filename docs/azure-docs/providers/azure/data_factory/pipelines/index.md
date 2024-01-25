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
| `get` | `SELECT` | `api-version, factoryName, pipelineName, resourceGroupName, subscriptionId` | Gets a pipeline. |
| `list_by_factory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists pipelines. |
| `create_or_update` | `INSERT` | `api-version, factoryName, pipelineName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a pipeline. |
| `delete` | `DELETE` | `api-version, factoryName, pipelineName, resourceGroupName, subscriptionId` | Deletes a pipeline. |
| `_list_by_factory` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists pipelines. |
