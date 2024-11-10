---
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
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

Creates, updates, deletes, gets or lists a <code>schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="maxId" /> | `integer` | Maximum ID |
| <CopyableCode code="references" /> | `array` | References to other schemas |
| <CopyableCode code="schema" /> | `string` | Schema string identified by the ID |
| <CopyableCode code="schemaType" /> | `string` | Schema type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_schema" /> | `SELECT` | <CopyableCode code="id" /> | Retrieves the schema string identified by the input ID. |
| <CopyableCode code="get_schemas" /> | `SELECT` | <CopyableCode code="" /> | Get the schemas matching the specified parameters. |
| <CopyableCode code="get_schema_only" /> | `EXEC` | <CopyableCode code="id" /> | Retrieves the schema identified by the input ID. |

## `SELECT` examples

Get the schemas matching the specified parameters.


```sql
SELECT
maxId,
references,
schema,
schemaType
FROM confluent.schema_registry.schemas
;
```