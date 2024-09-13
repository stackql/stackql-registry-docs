
---
title: capacity_commitments
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_commitments
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>capacity_commitment</code> resource or lists <code>capacity_commitments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_commitments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigqueryreservation.capacity_commitments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the capacity commitment, e.g., `projects/myproject/locations/US/capacityCommitments/123` The commitment_id must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. |
| <CopyableCode code="commitmentEndTime" /> | `string` | Output only. The end of the current commitment period. It is applicable only for ACTIVE capacity commitments. |
| <CopyableCode code="commitmentStartTime" /> | `string` | Output only. The start of the current commitment period. It is applicable only for ACTIVE capacity commitments. |
| <CopyableCode code="edition" /> | `string` | Edition of the capacity commitment. |
| <CopyableCode code="failureStatus" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="isFlatRate" /> | `boolean` | Output only. If true, the commitment is a flat-rate commitment, otherwise, it's an edition commitment. |
| <CopyableCode code="multiRegionAuxiliary" /> | `boolean` | Applicable only for commitments located within one of the BigQuery multi-regions (US or EU). If set to true, this commitment is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this commitment is placed in the organization's default region. NOTE: this is a preview feature. Project must be allow-listed in order to set this field. |
| <CopyableCode code="plan" /> | `string` | Capacity commitment commitment plan. |
| <CopyableCode code="renewalPlan" /> | `string` | The plan this capacity commitment is converted to after commitment_end_time passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable for ANNUAL and TRIAL commitments. |
| <CopyableCode code="slotCount" /> | `string` | Number of slots in this commitment. |
| <CopyableCode code="state" /> | `string` | Output only. State of the commitment. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="capacityCommitmentsId, locationsId, projectsId" /> | Returns information about the capacity commitment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the capacity commitments for the admin project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new capacity commitment resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="capacityCommitmentsId, locationsId, projectsId" /> | Deletes a capacity commitment. Attempting to delete capacity commitment before its commitment_end_time will fail with the error code `google.rpc.Code.FAILED_PRECONDITION`. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="capacityCommitmentsId, locationsId, projectsId" /> | Updates an existing capacity commitment. Only `plan` and `renewal_plan` fields can be updated. Plan can only be changed to a plan of a longer commitment period. Attempting to change to a plan with shorter commitment period will fail with the error code `google.rpc.Code.FAILED_PRECONDITION`. |
| <CopyableCode code="merge" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Merges capacity commitments of the same plan into a single commitment. The resulting capacity commitment has the greater commitment_end_time out of the to-be-merged capacity commitments. Attempting to merge capacity commitments of different plan will fail with the error code `google.rpc.Code.FAILED_PRECONDITION`. |
| <CopyableCode code="split" /> | `EXEC` | <CopyableCode code="capacityCommitmentsId, locationsId, projectsId" /> | Splits capacity commitment to two commitments of the same plan and `commitment_end_time`. A common use case is to enable downgrading commitments. For example, in order to downgrade from 10000 slots to 8000, you might split a 10000 capacity commitment into commitments of 2000 and 8000. Then, you delete the first one after the commitment end time passes. |

## `SELECT` examples

Lists all the capacity commitments for the admin project.

```sql
SELECT
name,
commitmentEndTime,
commitmentStartTime,
edition,
failureStatus,
isFlatRate,
multiRegionAuxiliary,
plan,
renewalPlan,
slotCount,
state
FROM google.bigqueryreservation.capacity_commitments
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>capacity_commitments</code> resource.

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
INSERT INTO google.bigqueryreservation.capacity_commitments (
locationsId,
projectsId,
name,
slotCount,
plan,
state,
commitmentStartTime,
commitmentEndTime,
failureStatus,
renewalPlan,
multiRegionAuxiliary,
edition,
isFlatRate
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ slotCount }}',
'{{ plan }}',
'{{ state }}',
'{{ commitmentStartTime }}',
'{{ commitmentEndTime }}',
'{{ failureStatus }}',
'{{ renewalPlan }}',
true|false,
'{{ edition }}',
true|false
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
      - name: slotCount
        value: '{{ slotCount }}'
      - name: plan
        value: '{{ plan }}'
      - name: state
        value: '{{ state }}'
      - name: commitmentStartTime
        value: '{{ commitmentStartTime }}'
      - name: commitmentEndTime
        value: '{{ commitmentEndTime }}'
      - name: failureStatus
        value: '{{ failureStatus }}'
      - name: renewalPlan
        value: '{{ renewalPlan }}'
      - name: multiRegionAuxiliary
        value: '{{ multiRegionAuxiliary }}'
      - name: edition
        value: '{{ edition }}'
      - name: isFlatRate
        value: '{{ isFlatRate }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a capacity_commitment only if the necessary resources are available.

```sql
UPDATE google.bigqueryreservation.capacity_commitments
SET 
name = '{{ name }}',
slotCount = '{{ slotCount }}',
plan = '{{ plan }}',
state = '{{ state }}',
commitmentStartTime = '{{ commitmentStartTime }}',
commitmentEndTime = '{{ commitmentEndTime }}',
failureStatus = '{{ failureStatus }}',
renewalPlan = '{{ renewalPlan }}',
multiRegionAuxiliary = true|false,
edition = '{{ edition }}',
isFlatRate = true|false
WHERE 
capacityCommitmentsId = '{{ capacityCommitmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified capacity_commitment resource.

```sql
DELETE FROM google.bigqueryreservation.capacity_commitments
WHERE capacityCommitmentsId = '{{ capacityCommitmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
