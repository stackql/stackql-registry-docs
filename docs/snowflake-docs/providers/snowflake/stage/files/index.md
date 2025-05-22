---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - stage
  - snowflake
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage snowflake resources using SQL
custom_edit_url: null
image: /img/providers/snowflake/stackql-snowflake-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.stage.files" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the file. |
| <CopyableCode code="last_modified" /> | `string` | Date and time when the file was last modified. |
| <CopyableCode code="md5" /> | `string` | md5 hash of the file. |
| <CopyableCode code="size" /> | `string` | Size of the file. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="list_files" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="pattern" /> | List files in the stage -- this is equivalent to LIST @stage. |
<br />

<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="pattern" /> | A query parameter that filters the command output by a regular expression pattern. | `string` | `-` |

</details>

## `SELECT` examples

List files in the stage -- this is equivalent to LIST @stage.


```sql
SELECT
name,
last_modified,
md5,
size
FROM snowflake.stage.files
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```