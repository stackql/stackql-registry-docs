---
title: job_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_definitions
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
<tr><td><b>Name</b></td><td><code>job_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_data_manager.job_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the object. |
| `name` | `string` | Name of the object. |
| `type` | `string` | Type of the object. |
| `properties` | `object` | Job Definition |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobDefinitions_Get` | `SELECT` | `dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId` | This method gets job definition object by name. |
| `JobDefinitions_ListByDataManager` | `SELECT` | `dataManagerName, resourceGroupName, subscriptionId` | This method gets all the job definitions of the given data manager resource. |
| `JobDefinitions_ListByDataService` | `SELECT` | `dataManagerName, dataServiceName, resourceGroupName, subscriptionId` | This method gets all the job definitions of the given data service name. |
| `JobDefinitions_CreateOrUpdate` | `INSERT` | `dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a job definition. |
| `JobDefinitions_Delete` | `DELETE` | `dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId` | This method deletes the given job definition. |
| `JobDefinitions_Run` | `EXEC` | `dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId` | This method runs a job instance of the given job definition. |
