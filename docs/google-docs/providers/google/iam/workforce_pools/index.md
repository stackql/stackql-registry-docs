---
title: workforce_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - workforce_pools
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

Creates, updates, deletes, gets or lists a <code>workforce_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workforce_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iam.workforce_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the pool. Format: `locations/{location}/workforcePools/{workforce_pool_id}` |
| <CopyableCode code="description" /> | `string` | A user-specified description of the pool. Cannot exceed 256 characters. |
| <CopyableCode code="accessRestrictions" /> | `object` | Access related restrictions on the workforce pool. |
| <CopyableCode code="disabled" /> | `boolean` | Disables the workforce pool. You cannot use a disabled pool to exchange tokens, or use existing tokens to access resources. If the pool is re-enabled, existing tokens grant access again. |
| <CopyableCode code="displayName" /> | `string` | A user-specified display name of the pool in Google Cloud Console. Cannot exceed 32 characters. |
| <CopyableCode code="expireTime" /> | `string` | Output only. Time after which the workforce pool will be permanently purged and cannot be recovered. |
| <CopyableCode code="parent" /> | `string` | Immutable. The resource name of the parent. Format: `organizations/{org-id}`. |
| <CopyableCode code="sessionDuration" /> | `string` | Duration that the Google Cloud access tokens, console sign-in sessions, and `gcloud` sign-in sessions from this pool are valid. Must be greater than 15 minutes (900s) and less than 12 hours (43200s). If `session_duration` is not configured, minted credentials have a default duration of one hour (3600s). For SAML providers, the lifetime of the token is the minimum of the `session_duration` and the `SessionNotOnOrAfter` claim in the SAML assertion. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the pool. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, workforcePoolsId" /> | Gets an individual WorkforcePool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId" /> | Lists all non-deleted WorkforcePools under the specified parent. If `show_deleted` is set to `true`, then deleted pools are also listed. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId" /> | Creates a new WorkforcePool. You cannot reuse the name of a deleted pool until 30 days after deletion. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, workforcePoolsId" /> | Deletes a WorkforcePool. You cannot use a deleted WorkforcePool to exchange external credentials for Google Cloud credentials. However, deletion does not revoke credentials that have already been issued. Credentials issued for a deleted pool do not grant access to resources. If the pool is undeleted, and the credentials are not expired, they grant access again. You can undelete a pool for 30 days. After 30 days, deletion is permanent. You cannot update deleted pools. However, you can view and list them. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, workforcePoolsId" /> | Updates an existing WorkforcePool. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="locationsId, workforcePoolsId" /> | Undeletes a WorkforcePool, as long as it was deleted fewer than 30 days ago. |

## `SELECT` examples

Lists all non-deleted WorkforcePools under the specified parent. If `show_deleted` is set to `true`, then deleted pools are also listed.

```sql
SELECT
name,
description,
accessRestrictions,
disabled,
displayName,
expireTime,
parent,
sessionDuration,
state
FROM google.iam.workforce_pools
WHERE locationsId = '{{ locationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workforce_pools</code> resource.

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
INSERT INTO google.iam.workforce_pools (
locationsId,
parent,
displayName,
description,
disabled,
sessionDuration,
accessRestrictions
)
SELECT 
'{{ locationsId }}',
'{{ parent }}',
'{{ displayName }}',
'{{ description }}',
true|false,
'{{ sessionDuration }}',
'{{ accessRestrictions }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
parent: string
displayName: string
description: string
state: string
disabled: boolean
sessionDuration: string
expireTime: string
accessRestrictions:
  allowedServices:
    - domain: string
  disableProgrammaticSignin: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workforce_pools</code> resource.

```sql
/*+ update */
UPDATE google.iam.workforce_pools
SET 
parent = '{{ parent }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
disabled = true|false,
sessionDuration = '{{ sessionDuration }}',
accessRestrictions = '{{ accessRestrictions }}'
WHERE 
locationsId = '{{ locationsId }}'
AND workforcePoolsId = '{{ workforcePoolsId }}';
```

## `DELETE` example

Deletes the specified <code>workforce_pools</code> resource.

```sql
/*+ delete */
DELETE FROM google.iam.workforce_pools
WHERE locationsId = '{{ locationsId }}'
AND workforcePoolsId = '{{ workforcePoolsId }}';
```
