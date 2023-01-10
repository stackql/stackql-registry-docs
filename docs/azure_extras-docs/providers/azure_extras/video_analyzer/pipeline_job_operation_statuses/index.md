---
title: pipeline_job_operation_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_job_operation_statuses
  - video_analyzer
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>pipeline_job_operation_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.video_analyzer.pipeline_job_operation_statuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the pipeline job operation. |
| `error` | `object` | The error detail. |
| `status` | `string` | The status of the pipeline job operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PipelineJobOperationStatuses_Get` | `SELECT` | `accountName, operationId, pipelineJobName, resourceGroupName, subscriptionId` |
