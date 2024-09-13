
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>reservation</code> resource or lists <code>reservations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.pubsublite.reservations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the reservation. Structured like: projects/{project_number}/locations/{location}/reservations/{reservation_id} |
| <CopyableCode code="throughputCapacity" /> | `string` | The reserved throughput capacity. Every unit of throughput capacity is equivalent to 1 MiB/s of published messages or 2 MiB/s of subscribed messages. Any topics which are declared as using capacity from a Reservation will consume resources from this reservation instead of being charged individually. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="admin_projects_locations_reservations_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, reservationsId" /> | Returns the reservation configuration. |
| <CopyableCode code="admin_projects_locations_reservations_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns the list of reservations for the given project. |
| <CopyableCode code="admin_projects_locations_reservations_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new reservation. |
| <CopyableCode code="admin_projects_locations_reservations_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, reservationsId" /> | Deletes the specified reservation. |
| <CopyableCode code="admin_projects_locations_reservations_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, reservationsId" /> | Updates properties of the specified reservation. |

## `SELECT` examples

Returns the list of reservations for the given project.

```sql
SELECT
name,
throughputCapacity
FROM google.pubsublite.reservations
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>reservations</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.pubsublite.reservations (
locationsId,
projectsId,
name,
throughputCapacity
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ throughputCapacity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: throughputCapacity
        value: '{{ throughputCapacity }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a reservation only if the necessary resources are available.

```sql
UPDATE google.pubsublite.reservations
SET 
name = '{{ name }}',
throughputCapacity = '{{ throughputCapacity }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND reservationsId = '{{ reservationsId }}';
```

## `DELETE` example

Deletes the specified reservation resource.

```sql
DELETE FROM google.pubsublite.reservations
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND reservationsId = '{{ reservationsId }}';
```
