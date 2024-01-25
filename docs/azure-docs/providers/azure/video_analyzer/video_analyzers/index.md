---
title: video_analyzers
hide_title: false
hide_table_of_contents: false
keywords:
  - video_analyzers
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
<tr><td><b>Name</b></td><td><code>video_analyzers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.video_analyzer.video_analyzers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | The managed identity for the Video Analyzer resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of the Video Analyzer account. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Get the details of the specified Video Analyzer account |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the Video Analyzer accounts in the specified resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all Video Analyzer accounts in the specified subscription. |
| `create_or_update` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Create or update an instance of a Video Analyzer account |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Delete the specified Video Analyzer account |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Lists the Video Analyzer accounts in the specified resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all Video Analyzer accounts in the specified subscription. |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates an existing instance of Video Analyzer account |
