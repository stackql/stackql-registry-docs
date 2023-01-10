---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - engagement_fabric
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
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.engagement_fabric.channels</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Channels_Get` | `SELECT` | `accountName, channelName, resourceGroupName, subscriptionId` |
| `Channels_ListByAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` |
| `Channels_CreateOrUpdate` | `INSERT` | `accountName, channelName, resourceGroupName, subscriptionId` |
| `Channels_Delete` | `DELETE` | `accountName, channelName, resourceGroupName, subscriptionId` |
