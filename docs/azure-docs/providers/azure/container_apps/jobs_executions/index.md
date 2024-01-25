---
title: jobs_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_executions
  - container_apps
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
<tr><td><b>Name</b></td><td><code>jobs_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.jobs_executions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Job execution Id. |
| `name` | `string` | Job execution Name. |
| `properties` | `object` | Container Apps Job execution specific properties. |
| `type` | `string` | Job execution type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `jobName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `jobName, resourceGroupName, subscriptionId` |
