---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - scheduler
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.scheduler.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets the job resource identifier. |
| `name` | `string` | Gets the job resource name. |
| `properties` | `object` |  |
| `type` | `string` | Gets the job resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Jobs_Get` | `SELECT` | `api-version, jobCollectionName, jobName, resourceGroupName, subscriptionId` | Gets a job. |
| `Jobs_List` | `SELECT` | `api-version, jobCollectionName, resourceGroupName, subscriptionId` | Lists all jobs under the specified job collection. |
| `Jobs_CreateOrUpdate` | `INSERT` | `api-version, jobCollectionName, jobName, resourceGroupName, subscriptionId` | Provisions a new job or updates an existing job. |
| `Jobs_Delete` | `DELETE` | `api-version, jobCollectionName, jobName, resourceGroupName, subscriptionId` | Deletes a job. |
| `Jobs_ListJobHistory` | `EXEC` | `api-version, jobCollectionName, jobName, resourceGroupName, subscriptionId` | Lists job history. |
| `Jobs_Patch` | `EXEC` | `api-version, jobCollectionName, jobName, resourceGroupName, subscriptionId` | Patches an existing job. |
| `Jobs_Run` | `EXEC` | `api-version, jobCollectionName, jobName, resourceGroupName, subscriptionId` | Runs a job. |
