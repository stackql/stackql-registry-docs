---
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - runs
  - container_registry
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
<tr><td><b>Name</b></td><td><code>runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. |
| `properties` | `object` | The properties for a run. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Runs_Get` | `SELECT` | `registryName, resourceGroupName, runId, subscriptionId` | Gets the detailed information for a given run. |
| `Runs_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Gets all the runs for a registry. |
| `Runs_Cancel` | `EXEC` | `registryName, resourceGroupName, runId, subscriptionId` | Cancel an existing run. |
| `Runs_GetLogSasUrl` | `EXEC` | `registryName, resourceGroupName, runId, subscriptionId` | Gets a link to download the run logs. |
| `Runs_Update` | `EXEC` | `registryName, resourceGroupName, runId, subscriptionId` | Patch the run properties. |
