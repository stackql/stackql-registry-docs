---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - stor_simple_8000_series
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
<tr><td><b>Id</b></td><td><code>azure_extras.stor_simple_8000_series.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `type` | `string` | The hierarchical type of the object. |
| `status` | `string` | The current status of the job. |
| `endTime` | `string` | The UTC time at which the job completed. |
| `error` | `object` | The job error details. Contains list of job error items. |
| `startTime` | `string` | The UTC time at which the job was started. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
| `properties` | `object` | The properties of the job. |
| `percentComplete` | `integer` | The percentage of the job that is already complete. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Jobs_Get` | `SELECT` | `deviceName, jobName, managerName, resourceGroupName, subscriptionId` | Gets the details of the specified job name. |
| `Jobs_ListByDevice` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Gets all the jobs for specified device. With optional OData query parameters, a filtered set of jobs is returned. |
| `Jobs_ListByManager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Gets all the jobs for the specified manager. With optional OData query parameters, a filtered set of jobs is returned. |
| `Jobs_Cancel` | `EXEC` | `deviceName, jobName, managerName, resourceGroupName, subscriptionId` | Cancels a job on the device. |
