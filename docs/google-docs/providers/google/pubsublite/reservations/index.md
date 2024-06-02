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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pubsublite.reservations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the reservation. Structured like: projects/&#123;project_number&#125;/locations/&#123;location&#125;/reservations/&#123;reservation_id&#125; |
| <CopyableCode code="throughputCapacity" /> | `string` | The reserved throughput capacity. Every unit of throughput capacity is equivalent to 1 MiB/s of published messages or 2 MiB/s of subscribed messages. Any topics which are declared as using capacity from a Reservation will consume resources from this reservation instead of being charged individually. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="admin_projects_locations_reservations_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, reservationsId" /> | Returns the reservation configuration. |
| <CopyableCode code="admin_projects_locations_reservations_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns the list of reservations for the given project. |
| <CopyableCode code="admin_projects_locations_reservations_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new reservation. |
| <CopyableCode code="admin_projects_locations_reservations_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, reservationsId" /> | Deletes the specified reservation. |
| <CopyableCode code="_admin_projects_locations_reservations_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Returns the list of reservations for the given project. |
| <CopyableCode code="admin_projects_locations_reservations_patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, reservationsId" /> | Updates properties of the specified reservation. |
