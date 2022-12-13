---
title: streaming_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_jobs
  - stream_analytics
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
<tr><td><b>Name</b></td><td><code>streaming_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.stream_analytics.streaming_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Describes how identity is verified |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties that are associated with a streaming job. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StreamingJobs_Get` | `SELECT` | `jobName, resourceGroupName, subscriptionId` | Gets details about the specified streaming job. |
| `StreamingJobs_List` | `SELECT` | `subscriptionId` | Lists all of the streaming jobs in the given subscription. |
| `StreamingJobs_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the streaming jobs in the specified resource group. |
| `StreamingJobs_CreateOrReplace` | `INSERT` | `jobName, resourceGroupName, subscriptionId` | Creates a streaming job or replaces an already existing streaming job. |
| `StreamingJobs_Delete` | `DELETE` | `jobName, resourceGroupName, subscriptionId` | Deletes a streaming job. |
| `StreamingJobs_Scale` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Scales a streaming job when the job is running. |
| `StreamingJobs_Start` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Starts a streaming job. Once a job is started it will start processing input events and produce output. |
| `StreamingJobs_Stop` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Stops a running streaming job. This will cause a running streaming job to stop processing input events and producing output. |
| `StreamingJobs_Update` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Updates an existing streaming job. This can be used to partially update (ie. update one or two properties) a streaming job without affecting the rest the job definition. |
