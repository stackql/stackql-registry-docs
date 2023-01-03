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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | The name of the reservation. Structured like: projects/{project_number}/locations/{location}/reservations/{reservation_id} |
| `throughputCapacity` | `string` | The reserved throughput capacity. Every unit of throughput capacity is equivalent to 1 MiB/s of published messages or 2 MiB/s of subscribed messages. Any topics which are declared as using capacity from a Reservation will consume resources from this reservation instead of being charged individually. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `admin_projects_locations_reservations_get` | `SELECT` | `locationsId, projectsId, reservationsId` | Returns the reservation configuration. |
| `admin_projects_locations_reservations_list` | `SELECT` | `locationsId, projectsId` | Returns the list of reservations for the given project. |
| `admin_projects_locations_reservations_create` | `INSERT` | `locationsId, projectsId` | Creates a new reservation. |
| `admin_projects_locations_reservations_delete` | `DELETE` | `locationsId, projectsId, reservationsId` | Deletes the specified reservation. |
| `admin_projects_locations_reservations_patch` | `EXEC` | `locationsId, projectsId, reservationsId` | Updates properties of the specified reservation. |
