---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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

Creates, updates, deletes, gets or lists a <code>keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iam.keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the key. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The time after which the key will be permanently deleted and cannot be recovered. Note that the key may get purged before this time if the total limit of keys per provider is exceeded. |
| <CopyableCode code="keyData" /> | `object` | Represents a public key data along with its format. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the key. |
| <CopyableCode code="use" /> | `string` | Required. The purpose of the key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keysId, locationsId, providersId, workforcePoolsId" /> | Gets a WorkforcePoolProviderKey. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, providersId, workforcePoolsId" /> | Lists all non-deleted WorkforcePoolProviderKeys in a WorkforcePoolProvider. If `show_deleted` is set to `true`, then deleted keys are also listed. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, providersId, workforcePoolsId" /> | Creates a new WorkforcePoolProviderKey in a WorkforcePoolProvider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keysId, locationsId, providersId, workforcePoolsId" /> | Deletes a WorkforcePoolProviderKey. You can undelete a key for 30 days. After 30 days, deletion is permanent. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="keysId, projectsId, serviceAccountsId" /> | Disable a ServiceAccountKey. A disabled service account key can be re-enabled with EnableServiceAccountKey. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="keysId, projectsId, serviceAccountsId" /> | Enable a ServiceAccountKey. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="keysId, locationsId, providersId, workforcePoolsId" /> | Undeletes a WorkforcePoolProviderKey, as long as it was deleted fewer than 30 days ago. |
| <CopyableCode code="upload" /> | `EXEC` | <CopyableCode code="projectsId, serviceAccountsId" /> | Uploads the public key portion of a key pair that you manage, and associates the public key with a ServiceAccount. After you upload the public key, you can use the private key from the key pair as a service account key. |

## `SELECT` examples

Lists all non-deleted WorkforcePoolProviderKeys in a WorkforcePoolProvider. If `show_deleted` is set to `true`, then deleted keys are also listed.

```sql
SELECT
name,
expireTime,
keyData,
state,
use
FROM google.iam.keys
WHERE locationsId = '{{ locationsId }}'
AND providersId = '{{ providersId }}'
AND workforcePoolsId = '{{ workforcePoolsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>keys</code> resource.

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
INSERT INTO google.iam.keys (
locationsId,
providersId,
workforcePoolsId,
keyData,
use
)
SELECT 
'{{ locationsId }}',
'{{ providersId }}',
'{{ workforcePoolsId }}',
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

Deletes the specified <code>keys</code> resource.

```sql
/*+ delete */
DELETE FROM google.iam.keys
WHERE keysId = '{{ keysId }}'
AND locationsId = '{{ locationsId }}'
AND providersId = '{{ providersId }}'
AND workforcePoolsId = '{{ workforcePoolsId }}';
```
