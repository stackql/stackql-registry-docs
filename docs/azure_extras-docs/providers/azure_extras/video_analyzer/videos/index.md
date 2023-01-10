---
title: videos
hide_title: false
hide_table_of_contents: false
keywords:
  - videos
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
<tr><td><b>Name</b></td><td><code>videos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.video_analyzer.videos</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Videos_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId, videoName` | Retrieves an existing video resource with the given name. |
| `Videos_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Retrieves a list of video resources that have been created, along with their JSON representations. |
| `Videos_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId, videoName` | Creates a new video resource or updates an existing video resource with the given name. |
| `Videos_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId, videoName` | Deletes an existing video resource and its underlying data. This operation is irreversible. |
| `Videos_ListContentToken` | `EXEC` | `accountName, resourceGroupName, subscriptionId, videoName` | Generates a streaming token which can be used for accessing content from video content URLs, for a video resource with the given name. |
| `Videos_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId, videoName` | Updates individual properties of an existing video resource with the given name. |
