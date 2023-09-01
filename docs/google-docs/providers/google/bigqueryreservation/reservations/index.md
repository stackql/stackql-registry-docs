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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `edition` | `string` | Edition of the reservation. |
| `ignoreIdleSlots` | `boolean` | If false, any query or pipeline job using this reservation will use idle slots from other reservations within the same admin project. If true, a query or pipeline job using this reservation will execute with the slot capacity specified in the slot_capacity field at most. |
| `creationTime` | `string` | Output only. Creation time of the reservation. |
| `slotCapacity` | `string` | Baseline slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the unit of parallelism. Queries using this reservation might use more slots during runtime if ignore_idle_slots is set to false, or autoscaling is enabled. If edition is EDITION_UNSPECIFIED and total slot_capacity of the reservation and its siblings exceeds the total slot_count of all capacity commitments, the request will fail with `google.rpc.Code.RESOURCE_EXHAUSTED`. If edition is any value but EDITION_UNSPECIFIED, then the above requirement is not needed. The total slot_capacity of the reservation and its siblings may exceed the total slot_count of capacity commitments. In that case, the exceeding slots will be charged with the autoscale SKU. You can increase the number of baseline slots in a reservation every few minutes. If you want to decrease your baseline slots, you are limited to once an hour if you have recently changed your baseline slot capacity and your baseline slots exceed your committed slots. Otherwise, you can decrease your baseline slots every few minutes. |
| `autoscale` | `object` | Auto scaling settings. |
| `concurrency` | `string` | Job concurrency target which sets a soft upper bound on the number of jobs that can run concurrently in this reservation. This is a soft target due to asynchronous nature of the system and various optimizations for small queries. Default value is 0 which means that concurrency target will be automatically computed by the system. NOTE: this field is exposed as `target_job_concurrency` in the Information Schema, DDL and BQ CLI. |
| `multiRegionAuxiliary` | `boolean` | Applicable only for reservations located within one of the BigQuery multi-regions (US or EU). If set to true, this reservation is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this reservation is placed in the organization's default region. NOTE: this is a preview feature. Project must be allow-listed in order to set this field. |
| `updateTime` | `string` | Output only. Last update time of the reservation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, reservationsId` | Returns information about the reservation. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all the reservations for the project in the specified location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new reservation resource. |
| `delete` | `DELETE` | `locationsId, projectsId, reservationsId` | Deletes a reservation. Returns `google.rpc.Code.FAILED_PRECONDITION` when reservation has assignments. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists all the reservations for the project in the specified location. |
| `patch` | `EXEC` | `locationsId, projectsId, reservationsId` | Updates an existing reservation resource. |
