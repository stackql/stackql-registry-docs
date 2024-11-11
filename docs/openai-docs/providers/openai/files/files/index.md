---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - files
  - openai
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage openai resources using SQL
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.files.files" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` | The `File` object represents a document that has been uploaded to OpenAI. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_files" /> | `SELECT` | <CopyableCode code="" /> |  |
| <CopyableCode code="retrieve_file" /> | `SELECT` | <CopyableCode code="file_id" /> |  |
| <CopyableCode code="create_file" /> | `INSERT` | <CopyableCode code="" /> |  |
| <CopyableCode code="delete_file" /> | `DELETE` | <CopyableCode code="file_id" /> |  |
| <CopyableCode code="download_file" /> | `EXEC` | <CopyableCode code="file_id" /> |  |

## `SELECT` examples




```sql
SELECT
column_anon
FROM openai.files.files
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>files</code> resource.

<Tabs
    defaultValue="all"
    values={[
        
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO openai.files.files (

)
SELECT 

;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: files
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>files</code> resource.

```sql
/*+ delete */
DELETE FROM openai.files.files
WHERE file_id = '{{ file_id }}';
```
