---
title: key_encryption_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - key_encryption_keys
  - encryption_keys
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_kek" /> | `SELECT` | <CopyableCode code="name" /> |
| <CopyableCode code="create_kek" /> | `INSERT` |  |
| <CopyableCode code="delete_kek" /> | `DELETE` | <CopyableCode code="name" /> |
| <CopyableCode code="put_kek" /> | `REPLACE` | <CopyableCode code="name" /> |
| <CopyableCode code="get_kek_names" /> | `EXEC` |  |
| <CopyableCode code="undelete_kek" /> | `EXEC` | <CopyableCode code="name" /> |
