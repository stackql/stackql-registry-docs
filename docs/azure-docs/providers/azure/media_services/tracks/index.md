---
title: tracks
hide_title: false
hide_table_of_contents: false
keywords:
  - tracks
  - media_services
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
<tr><td><b>Name</b></td><td><code>tracks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.media_services.tracks</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, assetName, resourceGroupName, subscriptionId, trackName` | Get the details of a Track in the Asset |
| `list` | `SELECT` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Lists the Tracks in the asset |
| `create_or_update` | `INSERT` | `accountName, api-version, assetName, resourceGroupName, subscriptionId, trackName` | Create or update a Track in the asset |
| `delete` | `DELETE` | `accountName, api-version, assetName, resourceGroupName, subscriptionId, trackName` | Deletes a Track in the asset |
| `_list` | `EXEC` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Lists the Tracks in the asset |
| `update` | `EXEC` | `accountName, api-version, assetName, resourceGroupName, subscriptionId, trackName` | Updates an existing Track in the asset |
