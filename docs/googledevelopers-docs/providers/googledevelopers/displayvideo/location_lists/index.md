---
title: location_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - location_lists
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
<tr><td><b>Name</b></td><td><code>location_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.location_lists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the location list. |
| `locationType` | `string` | Required. Immutable. The type of location. All locations in the list will share this type. |
| `advertiserId` | `string` | Required. Immutable. The unique ID of the advertiser the location list belongs to. |
| `displayName` | `string` | Required. The display name of the location list. Must be UTF-8 encoded with a maximum size of 240 bytes. |
| `locationListId` | `string` | Output only. The unique ID of the location list. Assigned by the system. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `advertisers_locationLists_get` | `SELECT` | `advertisersId, locationListsId` | Gets a location list. |
| `advertisers_locationLists_list` | `SELECT` | `advertisersId` | Lists location lists based on a given advertiser id. |
| `advertisers_locationLists_create` | `INSERT` | `advertisersId` | Creates a new location list. Returns the newly created location list if successful. |
| `advertisers_locationLists_patch` | `EXEC` | `advertisersId, locationListId` | Updates a location list. Returns the updated location list if successful. |
