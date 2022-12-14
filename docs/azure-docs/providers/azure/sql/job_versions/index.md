---
title: job_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_versions
  - sql
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
<tr><td><b>Name</b></td><td><code>job_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.job_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | Link to retrieve next page of results. |
| `value` | `array` | Array of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobVersions_ListByJob` | `SELECT` | `jobAgentName, jobName, resourceGroupName, serverName, subscriptionId` | Gets all versions of a job. |
| `JobVersions_Get` | `EXEC` | `jobAgentName, jobName, jobVersion, resourceGroupName, serverName, subscriptionId` | Gets a job version. |
