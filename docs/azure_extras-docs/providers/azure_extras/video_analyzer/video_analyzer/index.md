---
title: video_analyzer
hide_title: false
hide_table_of_contents: false
keywords:
  - video_analyzer
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
<tr><td><b>Name</b></td><td><code>video_analyzer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.video_analyzer.video_analyzer</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The properties of the Video Analyzer account. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | The managed identity for the Video Analyzer resource. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VideoAnalyzers_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Get the details of the specified Video Analyzer account |
| `VideoAnalyzers_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the Video Analyzer accounts in the specified resource group. |
| `VideoAnalyzers_ListBySubscription` | `SELECT` | `subscriptionId` | List all Video Analyzer accounts in the specified subscription. |
| `VideoAnalyzers_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Create or update an instance of a Video Analyzer account |
| `VideoAnalyzers_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Delete the specified Video Analyzer account |
| `VideoAnalyzers_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates an existing instance of Video Analyzer account |
