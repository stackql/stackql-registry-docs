---
title: assigned_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - assigned_locations
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
<tr><td><b>Name</b></td><td><code>assigned_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.assigned_locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `assignedLocations` | `array` | The list of assigned locations. This list will be absent if empty. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the page_token field in the subsequent call to `ListAssignedLocations` method to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `advertisers_locationLists_assignedLocations_list` | `SELECT` | `advertiserId, locationListId` | Lists locations assigned to a location list. |
| `advertisers_locationLists_assignedLocations_create` | `INSERT` | `advertiserId, locationListId` | Creates an assignment between a location and a location list. |
| `advertisers_locationLists_assignedLocations_delete` | `DELETE` | `advertiserId, assignedLocationsId, locationListId` | Deletes the assignment between a location and a location list. |
| `advertisers_locationLists_assignedLocations_bulkEdit` | `EXEC` | `advertiserId, locationListsId` | Bulk edits multiple assignments between locations and a single location list. The operation will delete the assigned locations provided in BulkEditAssignedLocationsRequest.deleted_assigned_locations and then create the assigned locations provided in BulkEditAssignedLocationsRequest.created_assigned_locations. |
