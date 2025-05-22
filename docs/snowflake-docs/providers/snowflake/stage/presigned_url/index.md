---
title: presigned_url
hide_title: false
hide_table_of_contents: false
keywords:
  - presigned_url
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

Creates, updates, deletes, gets or lists a <code>presigned_url</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>presigned_url</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.stage.presigned_url" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="presigned_url" /> | `string` | Presigned url for file transfer, only works for Server Side Encrypted Stages. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_presigned_url" /> | `SELECT` | <CopyableCode code="database_name, filePath, name, schema_name, endpoint" /> | Generate a presigned url and optionally encryption materials for uploading and downloading files. |
<br />
## `SELECT` examples

Generate a presigned url and optionally encryption materials for uploading and downloading files.


```sql
SELECT
presigned_url
FROM snowflake.stage.presigned_url
WHERE database_name = '{{ database_name }}'
AND filePath = '{{ filePath }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```