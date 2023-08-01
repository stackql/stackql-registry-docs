---
title: job_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_definitions
  - storage_mover
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
<tr><td><b>Id</b></td><td><code>azure.storage_mover.job_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | Job definition properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobDefinitions_Get` | `SELECT` | `jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId` | Gets a Job Definition resource. |
| `JobDefinitions_List` | `SELECT` | `projectName, resourceGroupName, storageMoverName, subscriptionId` | Lists all Job Definitions in a Project. |
| `JobDefinitions_CreateOrUpdate` | `INSERT` | `jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId, data__properties` | Creates or updates a Job Definition resource, which contains configuration for a single unit of managed data transfer. |
| `JobDefinitions_Delete` | `DELETE` | `jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId` | Deletes a Job Definition resource. |
| `JobDefinitions_StartJob` | `EXEC` | `jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId` | Requests an Agent to start a new instance of this Job Definition, generating a new Job Run resource. |
| `JobDefinitions_StopJob` | `EXEC` | `jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId` | Requests the Agent of any active instance of this Job Definition to stop. |
| `JobDefinitions_Update` | `EXEC` | `jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId` | Updates properties for a Job Definition resource. Properties not specified in the request body will be unchanged. |
