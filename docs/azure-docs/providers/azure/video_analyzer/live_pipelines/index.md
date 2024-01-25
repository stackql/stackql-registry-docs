---
title: live_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - live_pipelines
  - video_analyzer
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
<tr><td><b>Name</b></td><td><code>live_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.video_analyzer.live_pipelines</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, livePipelineName, resourceGroupName, subscriptionId` | Retrieves a specific live pipeline by name. If a live pipeline with that name has been previously created, the call will return the JSON representation of that instance. |
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Retrieves a list of live pipelines that have been created, along with their JSON representations. |
| `create_or_update` | `INSERT` | `accountName, livePipelineName, resourceGroupName, subscriptionId` | Creates a new live pipeline or updates an existing one, with the given name. |
| `delete` | `DELETE` | `accountName, livePipelineName, resourceGroupName, subscriptionId` | Deletes a live pipeline with the given name. |
| `_list` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Retrieves a list of live pipelines that have been created, along with their JSON representations. |
| `activate` | `EXEC` | `accountName, livePipelineName, resourceGroupName, subscriptionId` | Activates a live pipeline with the given name. |
| `deactivate` | `EXEC` | `accountName, livePipelineName, resourceGroupName, subscriptionId` | Deactivates a live pipeline with the given name. |
| `update` | `EXEC` | `accountName, livePipelineName, resourceGroupName, subscriptionId` | Updates an existing live pipeline with the given name. Properties that can be updated include: description, bitrateKbps, and parameter definitions. Only the description can be updated while the live pipeline is active. |
