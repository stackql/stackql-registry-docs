---
title: tracks
hide_title: false
hide_table_of_contents: false
keywords:
  - tracks
  - media_services
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
<tr><td><b>Name</b></td><td><code>tracks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.media_services.tracks</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Tracks_Get` | `SELECT` | `accountName, api-version, assetName, resourceGroupName, subscriptionId, trackName` | Get the details of a Track in the Asset |
| `Tracks_List` | `SELECT` | `accountName, api-version, assetName, resourceGroupName, subscriptionId` | Lists the Tracks in the asset |
| `Tracks_CreateOrUpdate` | `INSERT` | `accountName, api-version, assetName, resourceGroupName, subscriptionId, trackName` | Create or update a Track in the asset |
| `Tracks_Delete` | `DELETE` | `accountName, api-version, assetName, resourceGroupName, subscriptionId, trackName` | Deletes a Track in the asset |
| `Tracks_Update` | `EXEC` | `accountName, api-version, assetName, resourceGroupName, subscriptionId, trackName` | Updates an existing Track in the asset |
| `Tracks_UpdateTrackData` | `EXEC` | `accountName, api-version, assetName, resourceGroupName, subscriptionId, trackName` | Update the track data. Call this API after any changes are made to the track data stored in the asset container. For example, you have modified the WebVTT captions file in the Azure blob storage container for the asset, viewers will not see the new version of the captions unless this API is called. Note, the changes may not be reflected immediately. CDN cache may also need to be purged if applicable. |
