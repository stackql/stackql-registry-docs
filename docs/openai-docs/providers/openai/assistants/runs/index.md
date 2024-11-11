---
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - runs
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

Creates, updates, deletes, gets or lists a <code>runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.assistants.runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints. |
| <CopyableCode code="assistant_id" /> | `string` | The ID of the [assistant](/docs/api-reference/assistants) used for execution of this run. |
| <CopyableCode code="cancelled_at" /> | `integer` | The Unix timestamp (in seconds) for when the run was cancelled. |
| <CopyableCode code="completed_at" /> | `integer` | The Unix timestamp (in seconds) for when the run was completed. |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) for when the run was created. |
| <CopyableCode code="expires_at" /> | `integer` | The Unix timestamp (in seconds) for when the run will expire. |
| <CopyableCode code="failed_at" /> | `integer` | The Unix timestamp (in seconds) for when the run failed. |
| <CopyableCode code="incomplete_details" /> | `object` | Details on why the run is incomplete. Will be `null` if the run is not incomplete. |
| <CopyableCode code="instructions" /> | `string` | The instructions that the [assistant](/docs/api-reference/assistants) used for this run. |
| <CopyableCode code="last_error" /> | `object` | The last error associated with this run. Will be `null` if there are no errors. |
| <CopyableCode code="max_completion_tokens" /> | `integer` | The maximum number of completion tokens specified to have been used over the course of the run. |
| <CopyableCode code="max_prompt_tokens" /> | `integer` | The maximum number of prompt tokens specified to have been used over the course of the run. |
| <CopyableCode code="metadata" /> | `object` | Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long. |
| <CopyableCode code="model" /> | `string` | The model that the [assistant](/docs/api-reference/assistants) used for this run. |
| <CopyableCode code="object" /> | `string` | The object type, which is always `thread.run`. |
| <CopyableCode code="parallel_tool_calls" /> | `boolean` | Whether to enable [parallel function calling](/docs/guides/function-calling/parallel-function-calling) during tool use. |
| <CopyableCode code="required_action" /> | `object` | Details on the action required to continue the run. Will be `null` if no action is required. |
| <CopyableCode code="response_format" /> | `` | Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`. Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs). Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON. **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length. |
| <CopyableCode code="started_at" /> | `integer` | The Unix timestamp (in seconds) for when the run was started. |
| <CopyableCode code="status" /> | `string` | The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`. |
| <CopyableCode code="temperature" /> | `number` | The sampling temperature used for this run. If not set, defaults to 1. |
| <CopyableCode code="thread_id" /> | `string` | The ID of the [thread](/docs/api-reference/threads) that was executed on as a part of this run. |
| <CopyableCode code="tool_choice" /> | `` | Controls which (if any) tool is called by the model. `none` means the model will not call any tools and instead generates a message. `auto` is the default value and means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user. Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool. |
| <CopyableCode code="tools" /> | `array` | The list of tools that the [assistant](/docs/api-reference/assistants) used for this run. |
| <CopyableCode code="top_p" /> | `number` | The nucleus sampling value used for this run. If not set, defaults to 1. |
| <CopyableCode code="truncation_strategy" /> | `object` | Controls for how a thread will be truncated prior to the run. Use this to control the intial context window of the run. |
| <CopyableCode code="usage" /> | `object` | Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_run" /> | `SELECT` | <CopyableCode code="run_id, thread_id" /> |  |
| <CopyableCode code="list_runs" /> | `SELECT` | <CopyableCode code="thread_id" /> |  |
| <CopyableCode code="create_run" /> | `INSERT` | <CopyableCode code="thread_id, data__assistant_id" /> |  |
| <CopyableCode code="modify_run" /> | `UPDATE` | <CopyableCode code="run_id, thread_id" /> |  |
| <CopyableCode code="cancel_run" /> | `EXEC` | <CopyableCode code="run_id, thread_id" /> |  |
| <CopyableCode code="submit_tool_ouputs_to_run" /> | `EXEC` | <CopyableCode code="run_id, thread_id, data__tool_outputs" /> |  |

## `SELECT` examples




```sql
SELECT
id,
assistant_id,
cancelled_at,
completed_at,
created_at,
expires_at,
failed_at,
incomplete_details,
instructions,
last_error,
max_completion_tokens,
max_prompt_tokens,
metadata,
model,
object,
parallel_tool_calls,
required_action,
response_format,
started_at,
status,
temperature,
thread_id,
tool_choice,
tools,
top_p,
truncation_strategy,
usage
FROM openai.assistants.runs
WHERE thread_id = '{{ thread_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>runs</code> resource.

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
INSERT INTO openai.assistants.runs (
data__assistant_id,
data__model,
data__instructions,
data__additional_instructions,
data__additional_messages,
data__tools,
data__metadata,
data__temperature,
data__top_p,
data__stream,
data__max_prompt_tokens,
data__max_completion_tokens,
data__truncation_strategy,
data__tool_choice,
data__parallel_tool_calls,
data__response_format,
thread_id
)
SELECT 
'{{ assistant_id }}',
'{{ model }}',
'{{ instructions }}',
'{{ additional_instructions }}',
'{{ additional_messages }}',
'{{ tools }}',
'{{ metadata }}',
'{{ temperature }}',
'{{ top_p }}',
'{{ stream }}',
'{{ max_prompt_tokens }}',
'{{ max_completion_tokens }}',
'{{ truncation_strategy }}',
'{{ tool_choice }}',
'{{ parallel_tool_calls }}',
'{{ response_format }}',
'{{ thread_id }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO openai.assistants.runs (
data__assistant_id,
thread_id
)
SELECT 
'{{ assistant_id }}',
'{{ thread_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: runs
  props:
    - name: thread_id
      value: string
    - name: data__assistant_id
      value: string
    - name: assistant_id
      value: string
    - name: model
      value: string
    - name: instructions
      value: string
    - name: additional_instructions
      value: string
    - name: additional_messages
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
    - name: tools
      value: array
      props:
        - name: type
          value: string
    - name: metadata
      value: object
    - name: temperature
      value: number
    - name: top_p
      value: number
    - name: stream
      value: boolean
    - name: max_prompt_tokens
      value: integer
    - name: max_completion_tokens
      value: integer
    - name: truncation_strategy
      props:
        - name: type
          value: string
        - name: last_messages
          value: integer
    - name: tool_choice
      value: string
    - name: parallel_tool_calls
      value: boolean
    - name: response_format
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>runs</code> resource.

```sql
/*+ update */
UPDATE openai.assistants.runs
SET 
metadata = '{{ metadata }}'
WHERE 
run_id = '{{ run_id }}'
AND thread_id = '{{ thread_id }}';
```
