---
title: ssh_public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - ssh_public_keys
  - oslogin
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

Creates, updates, deletes, gets or lists a <code>ssh_public_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ssh_public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.oslogin.ssh_public_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The canonical resource name. |
| <CopyableCode code="expirationTimeUsec" /> | `string` | An expiration time in microseconds since epoch. |
| <CopyableCode code="fingerprint" /> | `string` | Output only. The SHA-256 fingerprint of the SSH public key. |
| <CopyableCode code="key" /> | `string` | Public key text in SSH format, defined by RFC4253 section 6.6. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="sshPublicKeysId, usersId" /> | Retrieves an SSH public key. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="usersId" /> | Create an SSH public key |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="sshPublicKeysId, usersId" /> | Deletes an SSH public key. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="sshPublicKeysId, usersId" /> | Updates an SSH public key and returns the profile information. This method supports patch semantics. |

## `SELECT` examples

Retrieves an SSH public key.

```sql
SELECT
name,
expirationTimeUsec,
fingerprint,
key
FROM google.oslogin.ssh_public_keys
WHERE sshPublicKeysId = '{{ sshPublicKeysId }}'
AND usersId = '{{ usersId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ssh_public_keys</code> resource.

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
INSERT INTO google.oslogin.ssh_public_keys (
usersId,
key,
expirationTimeUsec,
fingerprint,
name
)
SELECT 
'{{ usersId }}',
'{{ key }}',
'{{ expirationTimeUsec }}',
'{{ fingerprint }}',
'{{ name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: key
      value: '{{ key }}'
    - name: expirationTimeUsec
      value: '{{ expirationTimeUsec }}'
    - name: fingerprint
      value: '{{ fingerprint }}'
    - name: name
      value: '{{ name }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>ssh_public_keys</code> resource.

```sql
/*+ update */
UPDATE google.oslogin.ssh_public_keys
SET 
key = '{{ key }}',
expirationTimeUsec = '{{ expirationTimeUsec }}',
fingerprint = '{{ fingerprint }}',
name = '{{ name }}'
WHERE 
sshPublicKeysId = '{{ sshPublicKeysId }}'
AND usersId = '{{ usersId }}';
```

## `DELETE` example

Deletes the specified <code>ssh_public_keys</code> resource.

```sql
/*+ delete */
DELETE FROM google.oslogin.ssh_public_keys
WHERE sshPublicKeysId = '{{ sshPublicKeysId }}'
AND usersId = '{{ usersId }}';
```
