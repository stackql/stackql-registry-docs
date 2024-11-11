---
title: threads
hide_title: false
hide_table_of_contents: false
keywords:
  - threads
  - assistants
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

Creates, updates, deletes, gets or lists a <code>threads</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>threads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.assistants.threads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints. |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) for when the thread was created. |
| <CopyableCode code="metadata" /> | `object` | Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long. |
| <CopyableCode code="object" /> | `string` | The object type, which is always `thread`. |
| <CopyableCode code="tool_resources" /> | `object` | A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_thread" /> | `SELECT` | <CopyableCode code="thread_id" /> |  |
| <CopyableCode code="create_thread" /> | `INSERT` | <CopyableCode code="" /> |  |
| <CopyableCode code="delete_thread" /> | `DELETE` | <CopyableCode code="thread_id" /> |  |
| <CopyableCode code="modify_thread" /> | `UPDATE` | <CopyableCode code="thread_id" /> |  |
| <CopyableCode code="create_thread_and_run" /> | `EXEC` | <CopyableCode code="data__assistant_id" /> |  |

## `SELECT` examples




```sql
SELECT
id,
created_at,
metadata,
object,
tool_resources
FROM openai.assistants.threads
WHERE thread_id = '{{ thread_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>threads</code> resource.

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
INSERT INTO openai.assistants.threads (
data__messages,
data__tool_resources,
data__metadata
)
SELECT 
'{{ messages }}',
'{{ tool_resources }}',
'{{ metadata }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: threads
  props:
    - name: messages
      value: array
      props:
        - name: role
          value: string
        - name: content
          value: string
        - name: attachments
          value: array
          props:
            - name: file_id
              value: string
            - name: tools
              value: array
              props:
                - name: type
                  value: string
        - name: metadata
          value: object
    - name: tool_resources
      props:
        - name: code_interpreter
          props:
            - name: file_ids
              value: array
        - name: file_search
          value: string
    - name: metadata
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>threads</code> resource.

```sql
/*+ update */
UPDATE openai.assistants.threads
SET 
tool_resources = '{{ tool_resources }}',
metadata = '{{ metadata }}'
WHERE 
thread_id = '{{ thread_id }}';
```

## `DELETE` example

Deletes the specified <code>threads</code> resource.

```sql
/*+ delete */
DELETE FROM openai.assistants.threads
WHERE thread_id = '{{ thread_id }}';
```
