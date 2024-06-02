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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="bigqueryreservation.reservations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the reservation, e.g., `projects/*/locations/*/reservations/team1-prod`. The reservation_id must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. |
| <CopyableCode code="autoscale" /> | `object` | Auto scaling settings. |
| <CopyableCode code="concurrency" /> | `string` | Job concurrency target which sets a soft upper bound on the number of jobs that can run concurrently in this reservation. This is a soft target due to asynchronous nature of the system and various optimizations for small queries. Default value is 0 which means that concurrency target will be automatically computed by the system. NOTE: this field is exposed as target job concurrency in the Information Schema, DDL and BQ CLI. |
| <CopyableCode code="creationTime" /> | `string` | Output only. Creation time of the reservation. |
| <CopyableCode code="edition" /> | `string` | Edition of the reservation. |
| <CopyableCode code="ignoreIdleSlots" /> | `boolean` | If false, any query or pipeline job using this reservation will use idle slots from other reservations within the same admin project. If true, a query or pipeline job using this reservation will execute with the slot capacity specified in the slot_capacity field at most. |
| <CopyableCode code="multiRegionAuxiliary" /> | `boolean` | Applicable only for reservations located within one of the BigQuery multi-regions (US or EU). If set to true, this reservation is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this reservation is placed in the organization's default region. NOTE: this is a preview feature. Project must be allow-listed in order to set this field. |
| <CopyableCode code="originalPrimaryLocation" /> | `string` | Optional. The original primary location of the reservation which is set only during its creation and remains unchanged afterwards. It can be used by the customer to answer questions about disaster recovery billing. The field is output only for customers and should not be specified, however, the google.api.field_behavior is not set to OUTPUT_ONLY since these fields are set in rerouted requests sent across regions. |
| <CopyableCode code="primaryLocation" /> | `string` | Optional. The primary location of the reservation. The field is only meaningful for reservation used for cross region disaster recovery. The field is output only for customers and should not be specified, however, the google.api.field_behavior is not set to OUTPUT_ONLY since these fields are set in rerouted requests sent across regions. |
| <CopyableCode code="secondaryLocation" /> | `string` | Optional. The secondary location of the reservation which is used for cross region disaster recovery purposes. Customer can set this in create/update reservation calls to create a failover reservation or convert a non-failover reservation to a failover reservation. |
| <CopyableCode code="slotCapacity" /> | `string` | Baseline slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the unit of parallelism. Queries using this reservation might use more slots during runtime if ignore_idle_slots is set to false, or autoscaling is enabled. If edition is EDITION_UNSPECIFIED and total slot_capacity of the reservation and its siblings exceeds the total slot_count of all capacity commitments, the request will fail with `google.rpc.Code.RESOURCE_EXHAUSTED`. If edition is any value but EDITION_UNSPECIFIED, then the above requirement is not needed. The total slot_capacity of the reservation and its siblings may exceed the total slot_count of capacity commitments. In that case, the exceeding slots will be charged with the autoscale SKU. You can increase the number of baseline slots in a reservation every few minutes. If you want to decrease your baseline slots, you are limited to once an hour if you have recently changed your baseline slot capacity and your baseline slots exceed your committed slots. Otherwise, you can decrease your baseline slots every few minutes. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of the reservation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, reservationsId" /> | Returns information about the reservation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the reservations for the project in the specified location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new reservation resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, reservationsId" /> | Deletes a reservation. Returns `google.rpc.Code.FAILED_PRECONDITION` when reservation has assignments. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all the reservations for the project in the specified location. |
| <CopyableCode code="failover_reservation" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, reservationsId" /> | Failover a reservation to the secondary location. The operation should be done in the current secondary location, which will be promoted to the new primary location for the reservation. Attempting to failover a reservation in the current primary location will fail with the error code `google.rpc.Code.FAILED_PRECONDITION`. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, reservationsId" /> | Updates an existing reservation resource. |
