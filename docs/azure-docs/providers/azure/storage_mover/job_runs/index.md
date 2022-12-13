---
title: job_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - job_runs
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
<tr><td><b>Name</b></td><td><code>job_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_mover.job_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Job run properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobRuns_Get` | `SELECT` | `jobDefinitionName, jobRunName, projectName, resourceGroupName, storageMoverName, subscriptionId` | Gets a Job Run resource. |
| `JobRuns_List` | `SELECT` | `jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId` | Lists all Job Runs in a Job Definition. |
