---
title: assistants
hide_title: false
hide_table_of_contents: false
keywords:
  - assistants
  - assistants
  - openai    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage OpenAI and ChatGPT resources using SQL.
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




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
| <CopyableCode code="name" /> | `string` | The name of the assistant. The maximum length is 256 characters.<br /> |
| <CopyableCode code="description" /> | `string` | The description of the assistant. The maximum length is 512 characters.<br /> |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) for when the assistant was created. |
| <CopyableCode code="instructions" /> | `string` | The system instructions that the assistant uses. The maximum length is 256,000 characters.<br /> |
| <CopyableCode code="metadata" /> | `object` | Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long.<br /> |
| <CopyableCode code="model" /> | `string` | ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.<br /> |
| <CopyableCode code="object" /> | `string` | The object type, which is always `assistant`. |
| <CopyableCode code="response_format" /> | `` | Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models/gpt-4o), [GPT-4 Turbo](/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.<br /><br />Setting to `&#123; "type": "json_schema", "json_schema": &#123;...&#125; &#125;` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs).<br /><br />Setting to `&#123; "type": "json_object" &#125;` enables JSON mode, which ensures the message the model generates is valid JSON.<br /><br />**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.<br /> |
| <CopyableCode code="temperature" /> | `number` | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.<br /> |
| <CopyableCode code="tool_resources" /> | `object` | A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.<br /> |
| <CopyableCode code="tools" /> | `array` | A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.<br /> |
| <CopyableCode code="top_p" /> | `number` | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.<br /><br />We generally recommend altering this or temperature but not both.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_assistant" /> | `SELECT` | <CopyableCode code="assistant_id" /> |
| <CopyableCode code="list_assistants" /> | `SELECT` |  |
| <CopyableCode code="create_assistant" /> | `INSERT` | <CopyableCode code="data__model" /> |
| <CopyableCode code="delete_assistant" /> | `DELETE` | <CopyableCode code="assistant_id" /> |
| <CopyableCode code="modify_assistant" /> | `UPDATE` | <CopyableCode code="assistant_id" /> |
