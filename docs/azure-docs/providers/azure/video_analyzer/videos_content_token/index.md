---
title: videos_content_token
hide_title: false
hide_table_of_contents: false
keywords:
  - videos_content_token
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
<tr><td><b>Name</b></td><td><code>videos_content_token</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.video_analyzer.videos_content_token</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `expirationDate` | `string` | The content token expiration date in ISO8601 format (eg. 2021-01-01T00:00:00Z). |
| `token` | `string` | The content token value to be added to the video content URL as the value for the "token" query string parameter. The token is specific to a single video. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId, videoName` |
