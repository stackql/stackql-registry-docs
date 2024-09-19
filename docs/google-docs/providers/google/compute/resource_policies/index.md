---
title: resource_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policies
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

Creates, updates, deletes, gets or lists a <code>resource_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.resource_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="diskConsistencyGroupPolicy" /> | `object` | Resource policy for disk consistency groups. |
| <CopyableCode code="groupPlacementPolicy" /> | `object` | A GroupPlacementPolicy specifies resource placement configuration. It specifies the failure bucket separation |
| <CopyableCode code="instanceSchedulePolicy" /> | `object` | An InstanceSchedulePolicy specifies when and how frequent certain operations are performed on the instance. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#resource_policies for resource policies. |
| <CopyableCode code="region" /> | `string` |  |
| <CopyableCode code="resourceStatus" /> | `object` | Contains output only fields. Use this sub-message for all output fields set on ResourcePolicy. The internal structure of this "status" field should mimic the structure of ResourcePolicy proto specification. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined fully-qualified URL for this resource. |
| <CopyableCode code="snapshotSchedulePolicy" /> | `object` | A snapshot schedule policy specifies when and how frequently snapshots are to be created for the target disk. Also specifies how many and how long these scheduled snapshots should be retained. |
| <CopyableCode code="status" /> | `string` | [Output Only] The status of resource policy creation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of resource policies. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, region, resourcePolicy" /> | Retrieves all information of the specified resource policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | A list all the resource policies that have been configured for the specified project in specified region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a new resource policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, region, resourcePolicy" /> | Deletes the specified resource policy. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project, region, resourcePolicy" /> | Modify the specified resource policy. |

## `SELECT` examples

Retrieves an aggregated list of resource policies. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
creationTimestamp,
diskConsistencyGroupPolicy,
groupPlacementPolicy,
instanceSchedulePolicy,
kind,
region,
resourceStatus,
selfLink,
snapshotSchedulePolicy,
status
FROM google.compute.resource_policies
WHERE project = '{{ project }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_policies</code> resource.

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
INSERT INTO google.compute.resource_policies (
project,
region,
region,
description,
name,
snapshotSchedulePolicy,
groupPlacementPolicy,
instanceSchedulePolicy,
diskConsistencyGroupPolicy,
status,
resourceStatus
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ region }}',
'{{ description }}',
'{{ name }}',
'{{ snapshotSchedulePolicy }}',
'{{ groupPlacementPolicy }}',
'{{ instanceSchedulePolicy }}',
'{{ diskConsistencyGroupPolicy }}',
'{{ status }}',
'{{ resourceStatus }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: id
      value: string
    - name: creationTimestamp
      value: string
    - name: selfLink
      value: string
    - name: region
      value: string
    - name: description
      value: string
    - name: name
      value: string
    - name: snapshotSchedulePolicy
      value:
        - name: schedule
          value:
            - name: hourlySchedule
              value:
                - name: hoursInCycle
                  value: integer
                - name: startTime
                  value: string
                - name: duration
                  value: string
            - name: dailySchedule
              value:
                - name: daysInCycle
                  value: integer
                - name: startTime
                  value: string
                - name: duration
                  value: string
            - name: weeklySchedule
              value:
                - name: dayOfWeeks
                  value:
                    - - name: day
                        value: string
                      - name: startTime
                        value: string
                      - name: duration
                        value: string
        - name: retentionPolicy
          value:
            - name: maxRetentionDays
              value: integer
            - name: onSourceDiskDelete
              value: string
        - name: snapshotProperties
          value:
            - name: labels
              value: object
            - name: storageLocations
              value:
                - string
            - name: guestFlush
              value: boolean
            - name: chainName
              value: string
    - name: groupPlacementPolicy
      value:
        - name: vmCount
          value: integer
        - name: availabilityDomainCount
          value: integer
        - name: collocation
          value: string
    - name: instanceSchedulePolicy
      value:
        - name: vmStartSchedule
          value:
            - name: schedule
              value: string
        - name: timeZone
          value: string
        - name: startTime
          value: string
        - name: expirationTime
          value: string
    - name: diskConsistencyGroupPolicy
      value: []
    - name: status
      value: string
    - name: resourceStatus
      value:
        - name: instanceSchedulePolicy
          value:
            - name: nextRunStartTime
              value: string
            - name: lastRunStartTime
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>resource_policies</code> resource.

```sql
/*+ update */
UPDATE google.compute.resource_policies
SET 
region = '{{ region }}',
description = '{{ description }}',
name = '{{ name }}',
snapshotSchedulePolicy = '{{ snapshotSchedulePolicy }}',
groupPlacementPolicy = '{{ groupPlacementPolicy }}',
instanceSchedulePolicy = '{{ instanceSchedulePolicy }}',
diskConsistencyGroupPolicy = '{{ diskConsistencyGroupPolicy }}',
status = '{{ status }}',
resourceStatus = '{{ resourceStatus }}'
WHERE 
project = '{{ project }}'
AND region = '{{ region }}'
AND resourcePolicy = '{{ resourcePolicy }}';
```

## `DELETE` example

Deletes the specified <code>resource_policies</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.resource_policies
WHERE project = '{{ project }}'
AND region = '{{ region }}'
AND resourcePolicy = '{{ resourcePolicy }}';
```
