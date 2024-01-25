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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `registryName, resourceGroupName, runId, subscriptionId` | Gets the detailed information for a given run. |
| `list` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Gets all the runs for a registry. |
| `_list` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Gets all the runs for a registry. |
| `cancel` | `EXEC` | `registryName, resourceGroupName, runId, subscriptionId` | Cancel an existing run. |
| `update` | `EXEC` | `registryName, resourceGroupName, runId, subscriptionId` | Patch the run properties. |
