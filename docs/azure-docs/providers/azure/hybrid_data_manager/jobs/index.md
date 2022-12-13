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
| `properties` | `object` | Job Properties |
| `startTime` | `string` | Time at which the job was started in UTC ISO 8601 format. |
| `status` | `string` | Status of the job. |
| `type` | `string` | Type of the object. |
| `endTime` | `string` | Time at which the job ended in UTC ISO 8601 format. |
| `error` | `object` | Top level error for the job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Jobs_Get` | `SELECT` | `dataManagerName, dataServiceName, jobDefinitionName, jobId, resourceGroupName, subscriptionId` | This method gets a data manager job given the jobId. |
| `Jobs_ListByDataManager` | `SELECT` | `dataManagerName, resourceGroupName, subscriptionId` | This method gets all the jobs at the data manager resource level. |
| `Jobs_ListByDataService` | `SELECT` | `dataManagerName, dataServiceName, resourceGroupName, subscriptionId` | This method gets all the jobs of a data service type in a given resource. |
| `Jobs_ListByJobDefinition` | `SELECT` | `dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId` | This method gets all the jobs of a given job definition. |
| `Jobs_Cancel` | `EXEC` | `dataManagerName, dataServiceName, jobDefinitionName, jobId, resourceGroupName, subscriptionId` | Cancels the given job. |
| `Jobs_Resume` | `EXEC` | `dataManagerName, dataServiceName, jobDefinitionName, jobId, resourceGroupName, subscriptionId` | Resumes the given job. |
