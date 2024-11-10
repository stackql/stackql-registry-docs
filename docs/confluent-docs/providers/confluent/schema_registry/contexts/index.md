---
title: contexts
hide_title: false
hide_table_of_contents: false
keywords:
  - contexts
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

Creates, updates, deletes, gets or lists a <code>contexts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contexts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.contexts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_contexts" /> | `SELECT` | <CopyableCode code="" /> | Retrieves a list of contexts. |

## `SELECT` examples

Retrieves a list of contexts.


```sql
SELECT
column_anon
FROM confluent.schema_registry.contexts
;
```