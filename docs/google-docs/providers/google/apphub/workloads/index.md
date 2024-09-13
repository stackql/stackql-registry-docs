---
title: workloads
hide_title: false
hide_table_of_contents: false
keywords:
  - workloads
  - apphub
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

Creates, updates, deletes, gets or lists a <code>workloads</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workloads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apphub.workloads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the Workload. Format: "projects/{host-project-id}/locations/{location}/applications/{application-id}/workloads/{workload-id}" |
| <CopyableCode code="description" /> | `string` | Optional. User-defined description of a Workload. Can have a maximum length of 2048 characters. |
| <CopyableCode code="attributes" /> | `object` | Consumer provided attributes. |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time. |
| <CopyableCode code="discoveredWorkload" /> | `string` | Required. Immutable. The resource name of the original discovered workload. |
| <CopyableCode code="displayName" /> | `string` | Optional. User-defined name for the Workload. Can have a maximum length of 63 characters. |
| <CopyableCode code="state" /> | `string` | Output only. Workload state. |
| <CopyableCode code="uid" /> | `string` | Output only. A universally unique identifier (UUID) for the `Workload` in the UUID4 format. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time. |
| <CopyableCode code="workloadProperties" /> | `object` | Properties of an underlying compute resource represented by the Workload. |
| <CopyableCode code="workloadReference" /> | `object` | Reference of an underlying compute resource represented by the Workload. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationsId, locationsId, projectsId, workloadsId" /> | Gets a Workload in an Application. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Lists Workloads in an Application. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Creates a Workload in an Application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationsId, locationsId, projectsId, workloadsId" /> | Deletes a Workload from an Application. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="applicationsId, locationsId, projectsId, workloadsId" /> | Updates a Workload in an Application. |

## `SELECT` examples

Lists Workloads in an Application.

```sql
SELECT
name,
description,
attributes,
createTime,
discoveredWorkload,
displayName,
state,
uid,
updateTime,
workloadProperties,
workloadReference
FROM google.apphub.workloads
WHERE applicationsId = '{{ applicationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workloads</code> resource.

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
INSERT INTO google.apphub.workloads (
applicationsId,
locationsId,
projectsId,
name,
displayName,
description,
workloadReference,
workloadProperties,
discoveredWorkload,
attributes,
createTime,
updateTime,
uid,
state
)
SELECT 
'{{ applicationsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ workloadReference }}',
'{{ workloadProperties }}',
'{{ discoveredWorkload }}',
'{{ attributes }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ uid }}',
'{{ state }}'
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
      - name: displayName
        value: '{{ displayName }}'
      - name: description
        value: '{{ description }}'
      - name: workloadReference
        value: '{{ workloadReference }}'
      - name: workloadProperties
        value: '{{ workloadProperties }}'
      - name: discoveredWorkload
        value: '{{ discoveredWorkload }}'
      - name: attributes
        value: '{{ attributes }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: uid
        value: '{{ uid }}'
      - name: state
        value: '{{ state }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workloads</code> resource.

```sql
/*+ update */
UPDATE google.apphub.workloads
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
workloadReference = '{{ workloadReference }}',
workloadProperties = '{{ workloadProperties }}',
discoveredWorkload = '{{ discoveredWorkload }}',
attributes = '{{ attributes }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
uid = '{{ uid }}',
state = '{{ state }}'
WHERE 
applicationsId = '{{ applicationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workloadsId = '{{ workloadsId }}';
```

## `DELETE` example

Deletes the specified <code>workloads</code> resource.

```sql
/*+ delete */
DELETE FROM google.apphub.workloads
WHERE applicationsId = '{{ applicationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workloadsId = '{{ workloadsId }}';
```
