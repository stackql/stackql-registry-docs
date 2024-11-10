---
title: key_encryption_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - key_encryption_keys
  - encryption_keys
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>key_encryption_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_encryption_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.encryption_keys.key_encryption_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the kek |
| <CopyableCode code="deleted" /> | `boolean` | Whether the kek is deleted |
| <CopyableCode code="doc" /> | `string` | Description of the kek |
| <CopyableCode code="kmsKeyId" /> | `string` | KMS key ID of the kek |
| <CopyableCode code="kmsProps" /> | `object` | Properties of the kek |
| <CopyableCode code="kmsType" /> | `string` | KMS type of the kek |
| <CopyableCode code="shared" /> | `boolean` | Whether the kek is shared |
| <CopyableCode code="ts" /> | `integer` | Timestamp of the kek |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kek" /> | `SELECT` | <CopyableCode code="name" /> |  |
| <CopyableCode code="get_kek_names" /> | `SELECT` | <CopyableCode code="" /> |  |
| <CopyableCode code="create_kek" /> | `INSERT` | <CopyableCode code="" /> |  |
| <CopyableCode code="delete_kek" /> | `DELETE` | <CopyableCode code="name" /> |  |
| <CopyableCode code="put_kek" /> | `REPLACE` | <CopyableCode code="name" /> |  |
| <CopyableCode code="undelete_kek" /> | `EXEC` | <CopyableCode code="name" /> |  |

## `SELECT` examples




```sql
SELECT
name,
deleted,
doc,
kmsKeyId,
kmsProps,
kmsType,
shared,
ts
FROM confluent.encryption_keys.key_encryption_keys
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>key_encryption_keys</code> resource.

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
INSERT INTO confluent.encryption_keys.key_encryption_keys (

)
SELECT 

;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: key_encryption_keys
  props:
    - name: name
      value: string
    - name: kmsType
      value: string
    - name: kmsKeyId
      value: string
    - name: kmsProps
      value: object
    - name: doc
      value: string
    - name: shared
      value: boolean
    - name: deleted
      value: boolean

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>key_encryption_keys</code> resource.

```sql
/*+ update */
REPLACE confluent.encryption_keys.key_encryption_keys
SET 

WHERE 
name = '{{ name }}';
```

## `DELETE` example

Deletes the specified <code>key_encryption_keys</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.encryption_keys.key_encryption_keys
WHERE name = '{{ name }}';
```
