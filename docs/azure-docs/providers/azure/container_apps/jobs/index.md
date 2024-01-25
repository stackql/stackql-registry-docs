---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | The complex type of the extended location. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Container Apps Job resource specific properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobName, resourceGroupName, subscriptionId` |  |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` |  |
| `list_by_subscription` | `SELECT` | `subscriptionId` |  |
| `create_or_update` | `INSERT` | `jobName, resourceGroupName, subscriptionId` | Create or Update a Container Apps Job. |
| `delete` | `DELETE` | `jobName, resourceGroupName, subscriptionId` | Delete a Container Apps Job. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` |  |
| `_list_by_subscription` | `EXEC` | `subscriptionId` |  |
| `jobs` | `EXEC` | `jobExecutionName, jobName, resourceGroupName, subscriptionId` |  |
| `proxy_get` | `EXEC` | `apiName, jobName, resourceGroupName, subscriptionId` | Get the properties of a Container App Job. |
| `start` | `EXEC` | `jobName, resourceGroupName, subscriptionId` |  |
| `stop_execution` | `EXEC` | `jobExecutionName, jobName, resourceGroupName, subscriptionId` |  |
| `stop_multiple_executions` | `EXEC` | `jobName, resourceGroupName, subscriptionId` |  |
| `update` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Patches a Container Apps Job using JSON Merge Patch |
