---
title: assistants
hide_title: false
hide_table_of_contents: false
keywords:
  - assistants
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

Creates, updates, deletes, gets or lists a <code>assistants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assistants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.assistants.assistants" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints. |
| <CopyableCode code="name" /> | `string` | The name of the assistant. The maximum length is 256 characters. |
| <CopyableCode code="description" /> | `string` | The description of the assistant. The maximum length is 512 characters. |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) for when the assistant was created. |
| <CopyableCode code="instructions" /> | `string` | The system instructions that the assistant uses. The maximum length is 256,000 characters. |
| <CopyableCode code="metadata" /> | `object` | Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long. |
| <CopyableCode code="model" /> | `string` | ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them. |
| <CopyableCode code="object" /> | `string` | The object type, which is always `assistant`. |
| <CopyableCode code="response_format" /> | `` | Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`. Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs). Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON. **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length. |
| <CopyableCode code="temperature" /> | `number` | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. |
| <CopyableCode code="tool_resources" /> | `object` | A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs. |
| <CopyableCode code="tools" /> | `array` | A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`. |
| <CopyableCode code="top_p" /> | `number` | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_assistant" /> | `SELECT` | <CopyableCode code="assistant_id" /> |  |
| <CopyableCode code="list_assistants" /> | `SELECT` | <CopyableCode code="" /> |  |
| <CopyableCode code="create_assistant" /> | `INSERT` | <CopyableCode code="data__model" /> |  |
| <CopyableCode code="delete_assistant" /> | `DELETE` | <CopyableCode code="assistant_id" /> |  |
| <CopyableCode code="modify_assistant" /> | `UPDATE` | <CopyableCode code="assistant_id" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
description,
created_at,
instructions,
metadata,
model,
object,
response_format,
temperature,
tool_resources,
tools,
top_p
FROM openai.assistants.assistants
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assistants</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO openai.assistants.assistants (
data__model,
data__name,
data__description,
data__instructions,
data__tools,
data__tool_resources,
data__metadata,
data__temperature,
data__top_p,
data__response_format
)
SELECT 
'{{ model }}',
'{{ name }}',
'{{ description }}',
'{{ instructions }}',
'{{ tools }}',
'{{ tool_resources }}',
'{{ metadata }}',
'{{ temperature }}',
'{{ top_p }}',
'{{ response_format }}'
;
```
</TabItem>

    <TabItem value="required">

    ```sql
    /*+ create */
    INSERT INTO openai.assistants.assistants (
    data__model
    )
    SELECT 
    '{{ model }}'
    ;
    ```
    </TabItem>
    
<TabItem value="manifest">

```yaml
- name: assistants
  props:
    - name: data__model
      value: string
    - name: model
      value: string
    - name: name
      value: string
    - name: description
      value: string
    - name: instructions
      value: string
    - name: tools
      value: array
      props:
        - name: type
          value: string
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
    - name: temperature
      value: number
    - name: top_p
      value: number
    - name: response_format
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>assistants</code> resource.

```sql
/*+ update */
UPDATE openai.assistants.assistants
SET 
model = '{{ model }}',
name = '{{ name }}',
description = '{{ description }}',
instructions = '{{ instructions }}',
tools = '{{ tools }}',
tool_resources = '{{ tool_resources }}',
metadata = '{{ metadata }}',
temperature = number,
top_p = number,
response_format = '{{ response_format }}'
WHERE 
assistant_id = '{{ assistant_id }}';
```

## `DELETE` example

Deletes the specified <code>assistants</code> resource.

```sql
/*+ delete */
DELETE FROM openai.assistants.assistants
WHERE assistant_id = '{{ assistant_id }}';
```
