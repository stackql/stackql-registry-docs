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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.pipeline_runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="durationInMs" /> | `integer` | The duration of a pipeline run. |
| <CopyableCode code="invokedBy" /> | `object` | Provides entity name and id that started the pipeline run. |
| <CopyableCode code="isLatest" /> | `boolean` | Indicates if the recovered pipeline run is the latest in its group. |
| <CopyableCode code="lastUpdated" /> | `string` | The last updated timestamp for the pipeline run event in ISO8601 format. |
| <CopyableCode code="message" /> | `string` | The message from a pipeline run. |
| <CopyableCode code="parameters" /> | `object` | The full or partial list of parameter name, value pair used in the pipeline run. |
| <CopyableCode code="pipelineName" /> | `string` | The pipeline name. |
| <CopyableCode code="runDimensions" /> | `object` | Run dimensions emitted by Pipeline run. |
| <CopyableCode code="runEnd" /> | `string` | The end time of a pipeline run in ISO8601 format. |
| <CopyableCode code="runGroupId" /> | `string` | Identifier that correlates all the recovery runs of a pipeline run. |
| <CopyableCode code="runId" /> | `string` | Identifier of a run. |
| <CopyableCode code="runStart" /> | `string` | The start time of a pipeline run in ISO8601 format. |
| <CopyableCode code="status" /> | `string` | The status of a pipeline run. Possible values: Queued, InProgress, Succeeded, Failed, Canceling, Cancelled |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, factoryName, resourceGroupName, runId, subscriptionId" /> | Get a pipeline run by its run ID. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="api-version, factoryName, resourceGroupName, runId, subscriptionId" /> | Cancel a pipeline run by its run ID. |
| <CopyableCode code="query_by_factory" /> | `EXEC` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId, data__lastUpdatedAfter, data__lastUpdatedBefore" /> | Query pipeline runs in the factory based on input filter conditions. |
