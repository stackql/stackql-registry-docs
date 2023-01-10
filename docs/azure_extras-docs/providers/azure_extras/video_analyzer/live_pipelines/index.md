---
title: live_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - live_pipelines
  - video_analyzer
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
<tr><td><b>Name</b></td><td><code>live_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.video_analyzer.live_pipelines</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LivePipelines_Get` | `SELECT` | `accountName, livePipelineName, resourceGroupName, subscriptionId` | Retrieves a specific live pipeline by name. If a live pipeline with that name has been previously created, the call will return the JSON representation of that instance. |
| `LivePipelines_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Retrieves a list of live pipelines that have been created, along with their JSON representations. |
| `LivePipelines_CreateOrUpdate` | `INSERT` | `accountName, livePipelineName, resourceGroupName, subscriptionId` | Creates a new live pipeline or updates an existing one, with the given name. |
| `LivePipelines_Delete` | `DELETE` | `accountName, livePipelineName, resourceGroupName, subscriptionId` | Deletes a live pipeline with the given name. |
| `LivePipelines_Activate` | `EXEC` | `accountName, livePipelineName, resourceGroupName, subscriptionId` | Activates a live pipeline with the given name. |
| `LivePipelines_Deactivate` | `EXEC` | `accountName, livePipelineName, resourceGroupName, subscriptionId` | Deactivates a live pipeline with the given name. |
| `LivePipelines_Update` | `EXEC` | `accountName, livePipelineName, resourceGroupName, subscriptionId` | Updates an existing live pipeline with the given name. Properties that can be updated include: description, bitrateKbps, and parameter definitions. Only the description can be updated while the live pipeline is active. |
