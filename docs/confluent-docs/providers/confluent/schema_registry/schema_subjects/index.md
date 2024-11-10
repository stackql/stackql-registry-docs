---
title: schema_subjects
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_subjects
  - schema_registry
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

Creates, updates, deletes, gets or lists a <code>schema_subjects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_subjects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.schema_subjects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_subjects" /> | `SELECT` | <CopyableCode code="id" /> | Retrieves all the subjects associated with a particular schema ID. |

## `SELECT` examples

Retrieves all the subjects associated with a particular schema ID.


```sql
SELECT
column_anon
FROM confluent.schema_registry.schema_subjects
WHERE id = '{{ id }}';
```