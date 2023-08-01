---
title: reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations
  - pubsublite
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsublite.reservations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token that can be sent as `page_token` to retrieve the next page of results. If this field is omitted, there are no more results. |
| `reservations` | `array` | The list of reservation in the requested parent. The order of the reservations is unspecified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `admin_projects_locations_reservations_get` | `SELECT` | `locationsId, projectsId, reservationsId` | Returns the reservation configuration. |
| `admin_projects_locations_reservations_list` | `SELECT` | `locationsId, projectsId` | Returns the list of reservations for the given project. |
| `admin_projects_locations_reservations_create` | `INSERT` | `locationsId, projectsId` | Creates a new reservation. |
| `admin_projects_locations_reservations_delete` | `DELETE` | `locationsId, projectsId, reservationsId` | Deletes the specified reservation. |
| `admin_projects_locations_reservations_patch` | `EXEC` | `locationsId, projectsId, reservationsId` | Updates properties of the specified reservation. |
