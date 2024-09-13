---
title: workload_identity_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_identity_pools
  - iam
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

Creates, updates, deletes or gets an <code>workload_identity_pool</code> resource or lists <code>workload_identity_pools</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workload_identity_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iam.workload_identity_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the pool. |
| <CopyableCode code="description" /> | `string` | A description of the pool. Cannot exceed 256 characters. |
| <CopyableCode code="disabled" /> | `boolean` | Whether the pool is disabled. You cannot use a disabled pool to exchange tokens, or use existing tokens to access resources. If the pool is re-enabled, existing tokens grant access again. |
| <CopyableCode code="displayName" /> | `string` | A display name for the pool. Cannot exceed 32 characters. |
| <CopyableCode code="expireTime" /> | `string` | Output only. Time after which the workload identity pool will be permanently purged and cannot be recovered. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the pool. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, workloadIdentityPoolsId" /> | Gets an individual WorkloadIdentityPool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all non-deleted WorkloadIdentityPools in a project. If `show_deleted` is set to `true`, then deleted pools are also listed. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new WorkloadIdentityPool. You cannot reuse the name of a deleted pool until 30 days after deletion. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, workloadIdentityPoolsId" /> | Deletes a WorkloadIdentityPool. You cannot use a deleted pool to exchange external credentials for Google Cloud credentials. However, deletion does not revoke credentials that have already been issued. Credentials issued for a deleted pool do not grant access to resources. If the pool is undeleted, and the credentials are not expired, they grant access again. You can undelete a pool for 30 days. After 30 days, deletion is permanent. You cannot update deleted pools. However, you can view and list them. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, workloadIdentityPoolsId" /> | Updates an existing WorkloadIdentityPool. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, workloadIdentityPoolsId" /> | Undeletes a WorkloadIdentityPool, as long as it was deleted fewer than 30 days ago. |

## `SELECT` examples

Lists all non-deleted WorkloadIdentityPools in a project. If `show_deleted` is set to `true`, then deleted pools are also listed.

```sql
SELECT
name,
description,
disabled,
displayName,
expireTime,
state
FROM google.iam.workload_identity_pools
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workload_identity_pools</code> resource.

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
INSERT INTO google.iam.workload_identity_pools (
locationsId,
projectsId,
name,
displayName,
description,
state,
disabled,
expireTime
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ state }}',
true|false,
'{{ expireTime }}'
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
      - name: state
        value: '{{ state }}'
      - name: disabled
        value: '{{ disabled }}'
      - name: expireTime
        value: '{{ expireTime }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a workload_identity_pool only if the necessary resources are available.

```sql
UPDATE google.iam.workload_identity_pools
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
state = '{{ state }}',
disabled = true|false,
expireTime = '{{ expireTime }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workloadIdentityPoolsId = '{{ workloadIdentityPoolsId }}';
```

## `DELETE` example

Deletes the specified workload_identity_pool resource.

```sql
DELETE FROM google.iam.workload_identity_pools
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workloadIdentityPoolsId = '{{ workloadIdentityPoolsId }}';
```
