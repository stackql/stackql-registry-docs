---
title: pipeline_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_jobs
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
<tr><td><b>Name</b></td><td><code>pipeline_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.video_analyzer.pipeline_jobs</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PipelineJobs_Get` | `SELECT` | `accountName, pipelineJobName, resourceGroupName, subscriptionId` | Retrieves a specific pipeline job by name. If a pipeline job with that name has been previously created, the call will return the JSON representation of that instance. |
| `PipelineJobs_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Retrieves a list of all live pipelines that have been created, along with their JSON representations. |
| `PipelineJobs_CreateOrUpdate` | `INSERT` | `accountName, pipelineJobName, resourceGroupName, subscriptionId` | Creates a new pipeline job or updates an existing one, with the given name. |
| `PipelineJobs_Delete` | `DELETE` | `accountName, pipelineJobName, resourceGroupName, subscriptionId` | Deletes a pipeline job with the given name. |
| `PipelineJobs_Cancel` | `EXEC` | `accountName, pipelineJobName, resourceGroupName, subscriptionId` | Cancels a pipeline job with the given name. |
| `PipelineJobs_Update` | `EXEC` | `accountName, pipelineJobName, resourceGroupName, subscriptionId` | Updates an existing pipeline job with the given name. Properties that can be updated include: description. |
