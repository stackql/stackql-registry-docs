---
title: modes
hide_title: false
hide_table_of_contents: false
keywords:
  - modes
  - schema_registry
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

Creates, updates, deletes, gets or lists a <code>modes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>modes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.modes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="mode" /> | `string` | Schema Registry operating mode |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_mode" /> | `SELECT` | <CopyableCode code="subject" /> | Retrieves the subject mode. |
| <CopyableCode code="get_top_level_mode" /> | `SELECT` | <CopyableCode code="" /> | Retrieves global mode. |
| <CopyableCode code="delete_subject_mode" /> | `DELETE` | <CopyableCode code="subject" /> | Deletes the specified subject-level mode and reverts to the global default. |
| <CopyableCode code="update_mode" /> | `EXEC` | <CopyableCode code="subject" /> | Update mode for the specified subject. On success, echoes the original request back to the client. |
| <CopyableCode code="update_top_level_mode" /> | `EXEC` | <CopyableCode code="" /> | Update global mode. On success, echoes the original request back to the client. |

## `SELECT` examples

Retrieves global mode.


```sql
SELECT
mode
FROM confluent.schema_registry.modes
;
```
## `DELETE` example

Deletes the specified <code>modes</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.schema_registry.modes
WHERE subject = '{{ subject }}';
```
