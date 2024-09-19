---
title: workload_identity_pool_provider_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_identity_pool_provider_keys
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

Creates, updates, deletes, gets or lists a <code>workload_identity_pool_provider_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workload_identity_pool_provider_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iam.workload_identity_pool_provider_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the key. |
| <CopyableCode code="expireTime" /> | `string` | Output only. Time after which the key will be permanently purged and cannot be recovered. Note that the key may get purged before this timestamp if the total limit of keys per provider is crossed. |
| <CopyableCode code="keyData" /> | `object` | Represents a public key data along with its format. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the key. |
| <CopyableCode code="use" /> | `string` | Required. The purpose of the key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keysId, locationsId, projectsId, providersId, workloadIdentityPoolsId" /> | Gets an individual WorkloadIdentityPoolProviderKey. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, providersId, workloadIdentityPoolsId" /> | Lists all non-deleted WorkloadIdentityPoolProviderKeys in a project. If show_deleted is set to `true`, then deleted pools are also listed. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, providersId, workloadIdentityPoolsId" /> | Create a new WorkloadIdentityPoolProviderKey in a WorkloadIdentityPoolProvider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keysId, locationsId, projectsId, providersId, workloadIdentityPoolsId" /> | Deletes an WorkloadIdentityPoolProviderKey. You can undelete a key for 30 days. After 30 days, deletion is permanent. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="keysId, locationsId, projectsId, providersId, workloadIdentityPoolsId" /> | Undeletes an WorkloadIdentityPoolProviderKey, as long as it was deleted fewer than 30 days ago. |

## `SELECT` examples

Lists all non-deleted WorkloadIdentityPoolProviderKeys in a project. If show_deleted is set to `true`, then deleted pools are also listed.

```sql
SELECT
name,
expireTime,
keyData,
state,
use
FROM google.iam.workload_identity_pool_provider_keys
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND providersId = '{{ providersId }}'
AND workloadIdentityPoolsId = '{{ workloadIdentityPoolsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workload_identity_pool_provider_keys</code> resource.

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
INSERT INTO google.iam.workload_identity_pool_provider_keys (
locationsId,
projectsId,
providersId,
workloadIdentityPoolsId,
keyData,
use
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ providersId }}',
'{{ workloadIdentityPoolsId }}',
'{{ keyData }}',
'{{ use }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
keyData:
  format: string
  notBeforeTime: string
  notAfterTime: string
  key: string
  keySpec: string
state: string
use: string
expireTime: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>workload_identity_pool_provider_keys</code> resource.

```sql
/*+ delete */
DELETE FROM google.iam.workload_identity_pool_provider_keys
WHERE keysId = '{{ keysId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND providersId = '{{ providersId }}'
AND workloadIdentityPoolsId = '{{ workloadIdentityPoolsId }}';
```
