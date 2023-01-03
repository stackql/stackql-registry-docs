---
title: reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations
  - bigqueryreservation
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
<tr><td><b>Id</b></td><td><code>google.bigqueryreservation.reservations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the reservation, e.g., `projects/*/locations/*/reservations/team1-prod`. The reservation_id must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. |
| `slotCapacity` | `string` | Minimum slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the unit of parallelism. Queries using this reservation might use more slots during runtime if ignore_idle_slots is set to false. If total slot_capacity of the reservation and its siblings exceeds the total slot_count of all capacity commitments, the request will fail with `google.rpc.Code.RESOURCE_EXHAUSTED`. NOTE: for reservations in US or EU multi-regions, slot capacity constraints are checked separately for default and auxiliary regions. See multi_region_auxiliary flag for more details. |
| `updateTime` | `string` | Output only. Last update time of the reservation. |
| `concurrency` | `string` | Maximum number of queries that are allowed to run concurrently in this reservation. This is a soft limit due to asynchronous nature of the system and various optimizations for small queries. Default value is 0 which means that concurrency will be automatically set based on the reservation size. |
| `creationTime` | `string` | Output only. Creation time of the reservation. |
| `ignoreIdleSlots` | `boolean` | If false, any query or pipeline job using this reservation will use idle slots from other reservations within the same admin project. If true, a query or pipeline job using this reservation will execute with the slot capacity specified in the slot_capacity field at most. |
| `multiRegionAuxiliary` | `boolean` | Applicable only for reservations located within one of the BigQuery multi-regions (US or EU). If set to true, this reservation is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this reservation is placed in the organization's default region. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_reservations_get` | `SELECT` | `locationsId, projectsId, reservationsId` | Returns information about the reservation. |
| `projects_locations_reservations_list` | `SELECT` | `locationsId, projectsId` | Lists all the reservations for the project in the specified location. |
| `projects_locations_reservations_create` | `INSERT` | `locationsId, projectsId` | Creates a new reservation resource. |
| `projects_locations_reservations_delete` | `DELETE` | `locationsId, projectsId, reservationsId` | Deletes a reservation. Returns `google.rpc.Code.FAILED_PRECONDITION` when reservation has assignments. |
| `projects_locations_reservations_patch` | `EXEC` | `locationsId, projectsId, reservationsId` | Updates an existing reservation resource. |
