---
title: dek_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - dek_versions
  - encryption_keys
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>dek_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dek_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.encryption_keys.dek_versions" /></td></tr>
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
| <CopyableCode code="get_dek_by_version" /> | `SELECT` | <CopyableCode code="name, subject, version" /> |  |
| <CopyableCode code="get_dek_versions" /> | `SELECT` | <CopyableCode code="name, subject" /> |  |
| <CopyableCode code="delete_dek_version" /> | `DELETE` | <CopyableCode code="name, subject, version" /> |  |
| <CopyableCode code="undelete_dek_version" /> | `EXEC` | <CopyableCode code="name, subject, version" /> |  |

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
FROM confluent.encryption_keys.dek_versions
WHERE name = '{{ name }}'
AND subject = '{{ subject }}';
```
## `DELETE` example

Deletes the specified <code>dek_versions</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.encryption_keys.dek_versions
WHERE name = '{{ name }}'
AND subject = '{{ subject }}'
AND version = '{{ version }}';
```
