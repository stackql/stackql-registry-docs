---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - storsimple_1200_series
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
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier. |
| `name` | `string` | The name. |
| `endTime` | `string` | The UTC time at which the job completed |
| `error` | `object` | The job error information containing List of JobErrorItem. |
| `percentComplete` | `integer` | The percentage of the job that is already complete |
| `properties` | `object` | properties for the job |
| `startTime` | `string` | The UTC time at which the job was started |
| `status` | `string` | Current status of the job |
| `type` | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, jobName, managerName, resourceGroupName, subscriptionId` | Returns the properties of the specified job name. |
| `list_by_device` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the jobs in a device. |
| `list_by_manager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the jobs in a manager. |
| `_list_by_device` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the jobs in a device. |
| `_list_by_manager` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the jobs in a manager. |
