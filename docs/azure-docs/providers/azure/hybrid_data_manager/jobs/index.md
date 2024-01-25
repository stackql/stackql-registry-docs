---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - hybrid_data_manager
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
<tr><td><b>Id</b></td><td><code>azure.hybrid_data_manager.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the object. |
| `name` | `string` | Name of the object. |
| `endTime` | `string` | Time at which the job ended in UTC ISO 8601 format. |
| `error` | `object` | Top level error for the job. |
| `properties` | `object` | Job Properties |
| `startTime` | `string` | Time at which the job was started in UTC ISO 8601 format. |
| `status` | `string` | Status of the job. |
| `type` | `string` | Type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataManagerName, dataServiceName, jobDefinitionName, jobId, resourceGroupName, subscriptionId` | This method gets a data manager job given the jobId. |
| `list_by_data_manager` | `SELECT` | `dataManagerName, resourceGroupName, subscriptionId` | This method gets all the jobs at the data manager resource level. |
| `list_by_data_service` | `SELECT` | `dataManagerName, dataServiceName, resourceGroupName, subscriptionId` | This method gets all the jobs of a data service type in a given resource. |
| `list_by_job_definition` | `SELECT` | `dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId` | This method gets all the jobs of a given job definition. |
| `_list_by_data_manager` | `EXEC` | `dataManagerName, resourceGroupName, subscriptionId` | This method gets all the jobs at the data manager resource level. |
| `_list_by_data_service` | `EXEC` | `dataManagerName, dataServiceName, resourceGroupName, subscriptionId` | This method gets all the jobs of a data service type in a given resource. |
| `_list_by_job_definition` | `EXEC` | `dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId` | This method gets all the jobs of a given job definition. |
| `cancel` | `EXEC` | `dataManagerName, dataServiceName, jobDefinitionName, jobId, resourceGroupName, subscriptionId` | Cancels the given job. |
| `resume` | `EXEC` | `dataManagerName, dataServiceName, jobDefinitionName, jobId, resourceGroupName, subscriptionId` | Resumes the given job. |
