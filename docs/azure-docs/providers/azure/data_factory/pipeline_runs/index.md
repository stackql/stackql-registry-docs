---
title: pipeline_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_runs
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
<tr><td><b>Name</b></td><td><code>pipeline_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.pipeline_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `durationInMs` | `integer` | The duration of a pipeline run. |
| `invokedBy` | `object` | Provides entity name and id that started the pipeline run. |
| `isLatest` | `boolean` | Indicates if the recovered pipeline run is the latest in its group. |
| `lastUpdated` | `string` | The last updated timestamp for the pipeline run event in ISO8601 format. |
| `message` | `string` | The message from a pipeline run. |
| `parameters` | `object` | The full or partial list of parameter name, value pair used in the pipeline run. |
| `pipelineName` | `string` | The pipeline name. |
| `runDimensions` | `object` | Run dimensions emitted by Pipeline run. |
| `runEnd` | `string` | The end time of a pipeline run in ISO8601 format. |
| `runGroupId` | `string` | Identifier that correlates all the recovery runs of a pipeline run. |
| `runId` | `string` | Identifier of a run. |
| `runStart` | `string` | The start time of a pipeline run in ISO8601 format. |
| `status` | `string` | The status of a pipeline run. Possible values: Queued, InProgress, Succeeded, Failed, Canceling, Cancelled |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, factoryName, resourceGroupName, runId, subscriptionId` | Get a pipeline run by its run ID. |
| `cancel` | `EXEC` | `api-version, factoryName, resourceGroupName, runId, subscriptionId` | Cancel a pipeline run by its run ID. |
| `query_by_factory` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, data__lastUpdatedAfter, data__lastUpdatedBefore` | Query pipeline runs in the factory based on input filter conditions. |
