---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
  - displayvideo
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the page_token field in the subsequent call to `ListSites` method to retrieve the next page of results. |
| `sites` | `array` | The list of sites. This list will be absent if empty. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `advertisers_channels_sites_list` | `SELECT` | `advertisersId, channelsId` | Lists sites in a channel. |
| `partners_channels_sites_list` | `SELECT` | `channelsId, partnersId` | Lists sites in a channel. |
| `advertisers_channels_sites_create` | `INSERT` | `advertiserId, channelsId` | Creates a site in a channel. |
| `partners_channels_sites_create` | `INSERT` | `channelsId, partnerId` | Creates a site in a channel. |
| `advertisers_channels_sites_delete` | `DELETE` | `advertiserId, channelsId, sitesId` | Deletes a site from a channel. |
| `partners_channels_sites_delete` | `DELETE` | `channelsId, partnerId, sitesId` | Deletes a site from a channel. |
| `advertisers_channels_sites_bulkEdit` | `EXEC` | `advertiserId, channelsId` | Bulk edits sites under a single channel. The operation will delete the sites provided in BulkEditSitesRequest.deleted_sites and then create the sites provided in BulkEditSitesRequest.created_sites. |
| `advertisers_channels_sites_replace` | `EXEC` | `advertiserId, channelsId` | Replaces all of the sites under a single channel. The operation will replace the sites under a channel with the sites provided in ReplaceSitesRequest.new_sites. |
| `partners_channels_sites_bulkEdit` | `EXEC` | `channelsId, partnerId` | Bulk edits sites under a single channel. The operation will delete the sites provided in BulkEditSitesRequest.deleted_sites and then create the sites provided in BulkEditSitesRequest.created_sites. |
| `partners_channels_sites_replace` | `EXEC` | `channelsId, partnerId` | Replaces all of the sites under a single channel. The operation will replace the sites under a channel with the sites provided in ReplaceSitesRequest.new_sites. |
