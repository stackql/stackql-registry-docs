---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - storsimple_8000_series
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_8000_series.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `endTime` | `string` | The UTC time at which the job completed. |
| `error` | `object` | The job error details. Contains list of job error items. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
| `percentComplete` | `integer` | The percentage of the job that is already complete. |
| `properties` | `object` | The properties of the job. |
| `startTime` | `string` | The UTC time at which the job was started. |
| `status` | `string` | The current status of the job. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, jobName, managerName, resourceGroupName, subscriptionId` | Gets the details of the specified job name. |
| `list_by_device` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Gets all the jobs for specified device. With optional OData query parameters, a filtered set of jobs is returned. |
| `list_by_manager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Gets all the jobs for the specified manager. With optional OData query parameters, a filtered set of jobs is returned. |
| `_list_by_device` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Gets all the jobs for specified device. With optional OData query parameters, a filtered set of jobs is returned. |
| `_list_by_manager` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Gets all the jobs for the specified manager. With optional OData query parameters, a filtered set of jobs is returned. |
| `cancel` | `EXEC` | `deviceName, jobName, managerName, resourceGroupName, subscriptionId` | Cancels a job on the device. |
