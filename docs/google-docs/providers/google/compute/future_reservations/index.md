---
title: future_reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - future_reservations
  - compute
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

Creates, updates, deletes, gets or lists a <code>future_reservations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>future_reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.future_reservations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] A unique identifier for this future reservation. The server defines this identifier. |
| <CopyableCode code="name" /> | `string` | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the future reservation. |
| <CopyableCode code="autoCreatedReservationsDeleteTime" /> | `string` | Future timestamp when the FR auto-created reservations will be deleted by Compute Engine. Format of this field must be a valid href="https://www.ietf.org/rfc/rfc3339.txt">RFC3339 value. |
| <CopyableCode code="autoCreatedReservationsDuration" /> | `object` | A Duration represents a fixed-length span of time represented as a count of seconds and fractions of seconds at nanosecond resolution. It is independent of any calendar and concepts like "day" or "month". Range is approximately 10,000 years. |
| <CopyableCode code="autoDeleteAutoCreatedReservations" /> | `boolean` | Setting for enabling or disabling automatic deletion for auto-created reservation. If set to true, auto-created reservations will be deleted at Future Reservation's end time (default) or at user's defined timestamp if any of the [auto_created_reservations_delete_time, auto_created_reservations_duration] values is specified. For keeping auto-created reservation indefinitely, this value should be set to false. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] The creation timestamp for this future reservation in RFC3339 text format. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#futureReservation for future reservations. |
| <CopyableCode code="namePrefix" /> | `string` | Name prefix for the reservations to be created at the time of delivery. The name prefix must comply with RFC1035. Maximum allowed length for name prefix is 20. Automatically created reservations name format will be -date-####. |
| <CopyableCode code="planningStatus" /> | `string` | Planning state before being submitted for evaluation |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined fully-qualified URL for this resource. |
| <CopyableCode code="selfLinkWithId" /> | `string` | [Output Only] Server-defined URL for this resource with the resource id. |
| <CopyableCode code="shareSettings" /> | `object` | The share setting for reservations and sole tenancy node groups. |
| <CopyableCode code="specificSkuProperties" /> | `object` |  |
| <CopyableCode code="status" /> | `object` | [Output only] Represents status related to the future reservation. |
| <CopyableCode code="timeWindow" /> | `object` |  |
| <CopyableCode code="zone" /> | `string` | [Output Only] URL of the Zone where this future reservation resides. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of future reservations. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="futureReservation, project, zone" /> | Retrieves information about the specified future reservation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, zone" /> | A list of all the future reservations that have been configured for the specified project in specified zone. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, zone" /> | Creates a new Future Reservation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="futureReservation, project, zone" /> | Deletes the specified future reservation. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="futureReservation, project, zone" /> | Updates the specified future reservation. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="futureReservation, project, zone" /> | Cancel the specified future reservation. |

## `SELECT` examples

Retrieves an aggregated list of future reservations. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
autoCreatedReservationsDeleteTime,
autoCreatedReservationsDuration,
autoDeleteAutoCreatedReservations,
creationTimestamp,
kind,
namePrefix,
planningStatus,
selfLink,
selfLinkWithId,
shareSettings,
specificSkuProperties,
status,
timeWindow,
zone
FROM google.compute.future_reservations
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>future_reservations</code> resource.

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
INSERT INTO google.compute.future_reservations (
project,
zone,
kind,
id,
creationTimestamp,
selfLink,
selfLinkWithId,
zone,
description,
name,
specificSkuProperties,
timeWindow,
shareSettings,
namePrefix,
status,
planningStatus,
autoCreatedReservationsDeleteTime,
autoCreatedReservationsDuration,
autoDeleteAutoCreatedReservations
)
SELECT 
'{{ project }}',
'{{ zone }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ selfLink }}',
'{{ selfLinkWithId }}',
'{{ zone }}',
'{{ description }}',
'{{ name }}',
'{{ specificSkuProperties }}',
'{{ timeWindow }}',
'{{ shareSettings }}',
'{{ namePrefix }}',
'{{ status }}',
'{{ planningStatus }}',
'{{ autoCreatedReservationsDeleteTime }}',
'{{ autoCreatedReservationsDuration }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: kind
        value: '{{ kind }}'
      - name: id
        value: '{{ id }}'
      - name: creationTimestamp
        value: '{{ creationTimestamp }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: selfLinkWithId
        value: '{{ selfLinkWithId }}'
      - name: zone
        value: '{{ zone }}'
      - name: description
        value: '{{ description }}'
      - name: name
        value: '{{ name }}'
      - name: specificSkuProperties
        value: '{{ specificSkuProperties }}'
      - name: timeWindow
        value: '{{ timeWindow }}'
      - name: shareSettings
        value: '{{ shareSettings }}'
      - name: namePrefix
        value: '{{ namePrefix }}'
      - name: status
        value: '{{ status }}'
      - name: planningStatus
        value: '{{ planningStatus }}'
      - name: autoCreatedReservationsDeleteTime
        value: '{{ autoCreatedReservationsDeleteTime }}'
      - name: autoCreatedReservationsDuration
        value: '{{ autoCreatedReservationsDuration }}'
      - name: autoDeleteAutoCreatedReservations
        value: '{{ autoDeleteAutoCreatedReservations }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>future_reservations</code> resource.

```sql
/*+ update */
UPDATE google.compute.future_reservations
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
selfLink = '{{ selfLink }}',
selfLinkWithId = '{{ selfLinkWithId }}',
zone = '{{ zone }}',
description = '{{ description }}',
name = '{{ name }}',
specificSkuProperties = '{{ specificSkuProperties }}',
timeWindow = '{{ timeWindow }}',
shareSettings = '{{ shareSettings }}',
namePrefix = '{{ namePrefix }}',
status = '{{ status }}',
planningStatus = '{{ planningStatus }}',
autoCreatedReservationsDeleteTime = '{{ autoCreatedReservationsDeleteTime }}',
autoCreatedReservationsDuration = '{{ autoCreatedReservationsDuration }}',
autoDeleteAutoCreatedReservations = true|false
WHERE 
futureReservation = '{{ futureReservation }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```

## `DELETE` example

Deletes the specified <code>future_reservations</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.future_reservations
WHERE futureReservation = '{{ futureReservation }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```
