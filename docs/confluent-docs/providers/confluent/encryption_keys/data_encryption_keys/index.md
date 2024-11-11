---
title: data_encryption_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - data_encryption_keys
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

Creates, updates, deletes, gets or lists a <code>data_encryption_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_encryption_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.encryption_keys.data_encryption_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="algorithm" /> | `string` | Algorithm of the dek |
| <CopyableCode code="deleted" /> | `boolean` | Whether the dek is deleted |
| <CopyableCode code="encryptedKeyMaterial" /> | `string` | Encrypted key material of the dek |
| <CopyableCode code="kekName" /> | `string` | Kek name of the dek |
| <CopyableCode code="keyMaterial" /> | `string` | Raw key material of the dek |
| <CopyableCode code="subject" /> | `string` | Subject of the dek |
| <CopyableCode code="ts" /> | `integer` | Timestamp of the dek |
| <CopyableCode code="version" /> | `integer` | Version of the dek |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_dek" /> | `SELECT` | <CopyableCode code="name, subject" /> |  |
| <CopyableCode code="get_dek_subjects" /> | `SELECT` | <CopyableCode code="name" /> |  |
| <CopyableCode code="create_dek" /> | `INSERT` | <CopyableCode code="name" /> |  |
| <CopyableCode code="delete_dek_versions" /> | `DELETE` | <CopyableCode code="name, subject" /> |  |
| <CopyableCode code="undelete_dek_versions" /> | `EXEC` | <CopyableCode code="name, subject" /> |  |

## `SELECT` examples




```sql
SELECT
algorithm,
deleted,
encryptedKeyMaterial,
kekName,
keyMaterial,
subject,
ts,
version
FROM confluent.encryption_keys.data_encryption_keys
WHERE name = '{{ name }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_encryption_keys</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO confluent.encryption_keys.data_encryption_keys (
data__subject,
data__version,
data__algorithm,
data__encryptedKeyMaterial,
data__deleted,
name
)
SELECT 
'{{ subject }}',
'{{ version }}',
'{{ algorithm }}',
'{{ encryptedKeyMaterial }}',
'{{ deleted }}',
'{{ name }}'
;
```
</TabItem>

    <TabItem value="required">

    ```sql
    /*+ create */
    INSERT INTO confluent.encryption_keys.data_encryption_keys (
    name
    )
    SELECT 
    '{{ name }}'
    ;
    ```
    </TabItem>
    
<TabItem value="manifest">

```yaml
- name: data_encryption_keys
  props:
    - name: name
      value: string
    - name: subject
      value: string
    - name: version
      value: integer
    - name: algorithm
      value: string
    - name: encryptedKeyMaterial
      value: string
    - name: deleted
      value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>data_encryption_keys</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.encryption_keys.data_encryption_keys
WHERE name = '{{ name }}'
AND subject = '{{ subject }}';
```
