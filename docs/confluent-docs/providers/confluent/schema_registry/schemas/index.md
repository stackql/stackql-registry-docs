---
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
  - schema_registry
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
| <CopyableCode code="get_schemas" /> | `SELECT` |  | Get the schemas matching the specified parameters. |
| <CopyableCode code="get_schema_only" /> | `EXEC` | <CopyableCode code="id" /> | Retrieves the schema identified by the input ID. |
| <CopyableCode code="get_subjects" /> | `EXEC` | <CopyableCode code="id" /> | Retrieves all the subjects associated with a particular schema ID. |
