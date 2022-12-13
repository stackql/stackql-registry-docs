---
title: pipeline_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_runs
  - container_registry
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
<tr><td><b>Name</b></td><td><code>pipeline_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.pipeline_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `type` | `string` | The type of the resource. |
| `properties` | `object` | The properties of a pipeline run. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PipelineRuns_Get` | `SELECT` | `pipelineRunName, registryName, resourceGroupName, subscriptionId` | Gets the detailed information for a given pipeline run. |
| `PipelineRuns_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all the pipeline runs for the specified container registry. |
| `PipelineRuns_Create` | `INSERT` | `pipelineRunName, registryName, resourceGroupName, subscriptionId` | Creates a pipeline run for a container registry with the specified parameters |
| `PipelineRuns_Delete` | `DELETE` | `pipelineRunName, registryName, resourceGroupName, subscriptionId` | Deletes a pipeline run from a container registry. |
