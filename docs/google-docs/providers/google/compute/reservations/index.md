---
title: reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations
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

Creates, updates, deletes, gets or lists a <code>reservations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.reservations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="aggregateReservation" /> | `object` | This reservation type is specified by total resource amounts (e.g. total count of CPUs) and can account for multiple instance SKUs. In other words, one can create instances of varying shapes against this reservation. |
| <CopyableCode code="commitment" /> | `string` | [Output Only] Full or partial URL to a parent commitment. This field displays for reservations that are tied to a commitment. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#reservations for reservations. |
| <CopyableCode code="resourcePolicies" /> | `object` | Resource policies to be added to this reservation. The key is defined by user, and the value is resource policy url. This is to define placement policy with reservation. |
| <CopyableCode code="resourceStatus" /> | `object` | [Output Only] Contains output only fields. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | [Output Only] Reserved for future use. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined fully-qualified URL for this resource. |
| <CopyableCode code="shareSettings" /> | `object` | The share setting for reservations and sole tenancy node groups. |
| <CopyableCode code="specificReservation" /> | `object` | This reservation type allows to pre allocate specific instance configuration. |
| <CopyableCode code="specificReservationRequired" /> | `boolean` | Indicates whether the reservation can be consumed by VMs with affinity for "any" reservation. If the field is set, then only VMs that target the reservation by name can consume from this reservation. |
| <CopyableCode code="status" /> | `string` | [Output Only] The status of the reservation. |
| <CopyableCode code="zone" /> | `string` | Zone in which the reservation resides. A zone must be provided if the reservation is created within a commitment. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of reservations. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, reservation, zone" /> | Retrieves information about the specified reservation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, zone" /> | A list of all the reservations that have been configured for the specified project in specified zone. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, zone" /> | Creates a new reservation. For more information, read Reserving zonal resources. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, reservation, zone" /> | Deletes the specified reservation. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="project, reservation, zone" /> | Update share settings of the reservation. |
| <CopyableCode code="resize" /> | `EXEC` | <CopyableCode code="project, reservation, zone" /> | Resizes the reservation (applicable to standalone reservations only). For more information, read Modifying reservations. |

## `SELECT` examples

Retrieves an aggregated list of reservations. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
aggregateReservation,
commitment,
creationTimestamp,
kind,
resourcePolicies,
resourceStatus,
satisfiesPzs,
selfLink,
shareSettings,
specificReservation,
specificReservationRequired,
status,
zone
FROM google.compute.reservations
WHERE project = '{{ project }}'; 
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
INSERT INTO google.compute.reservations (
project,
zone,
zone,
description,
name,
specificReservation,
aggregateReservation,
commitment,
specificReservationRequired,
status,
shareSettings,
satisfiesPzs,
resourcePolicies,
resourceStatus
)
SELECT 
'{{ project }}',
'{{ zone }}',
'{{ zone }}',
'{{ description }}',
'{{ name }}',
'{{ specificReservation }}',
'{{ aggregateReservation }}',
'{{ commitment }}',
true|false,
'{{ status }}',
'{{ shareSettings }}',
true|false,
'{{ resourcePolicies }}',
'{{ resourceStatus }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: zone
      value: '{{ zone }}'
    - name: description
      value: '{{ description }}'
    - name: name
      value: '{{ name }}'
    - name: specificReservation
      value:
        - name: instanceProperties
          value:
            - name: machineType
              value: '{{ machineType }}'
            - name: guestAccelerators
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: minCpuPlatform
              value: '{{ minCpuPlatform }}'
            - name: localSsds
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: locationHint
              value: '{{ locationHint }}'
        - name: count
          value: '{{ count }}'
        - name: inUseCount
          value: '{{ inUseCount }}'
        - name: assuredCount
          value: '{{ assuredCount }}'
        - name: sourceInstanceTemplate
          value: '{{ sourceInstanceTemplate }}'
    - name: aggregateReservation
      value:
        - name: vmFamily
          value: '{{ vmFamily }}'
        - name: reservedResources
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: inUseResources
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: workloadType
          value: '{{ workloadType }}'
    - name: commitment
      value: '{{ commitment }}'
    - name: specificReservationRequired
      value: '{{ specificReservationRequired }}'
    - name: status
      value: '{{ status }}'
    - name: shareSettings
      value:
        - name: shareType
          value: '{{ shareType }}'
        - name: projectMap
          value: '{{ projectMap }}'
    - name: satisfiesPzs
      value: '{{ satisfiesPzs }}'
    - name: resourcePolicies
      value: '{{ resourcePolicies }}'
    - name: resourceStatus
      value:
        - name: specificSkuAllocation
          value:
            - name: sourceInstanceTemplateId
              value: '{{ sourceInstanceTemplateId }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>reservations</code> resource.

```sql
/*+ update */
UPDATE google.compute.reservations
SET 
zone = '{{ zone }}',
description = '{{ description }}',
name = '{{ name }}',
specificReservation = '{{ specificReservation }}',
aggregateReservation = '{{ aggregateReservation }}',
commitment = '{{ commitment }}',
specificReservationRequired = true|false,
status = '{{ status }}',
shareSettings = '{{ shareSettings }}',
satisfiesPzs = true|false,
resourcePolicies = '{{ resourcePolicies }}',
resourceStatus = '{{ resourceStatus }}'
WHERE 
project = '{{ project }}'
AND reservation = '{{ reservation }}'
AND zone = '{{ zone }}';
```

## `DELETE` example

Deletes the specified <code>reservations</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.reservations
WHERE project = '{{ project }}'
AND reservation = '{{ reservation }}'
AND zone = '{{ zone }}';
```
