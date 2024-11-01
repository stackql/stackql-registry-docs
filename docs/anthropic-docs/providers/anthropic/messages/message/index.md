---
title: message
hide_title: false
hide_table_of_contents: false
keywords:
  - message
  - messages
  - anthropic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Anthropic resources using SQL.
custom_edit_url: null
image: /img/providers/anthropic/stackql-anthropic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>message</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="anthropic.messages.message" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique object identifier. |
| <CopyableCode code="content" /> | `array` | The generated content blocks by the model. |
| <CopyableCode code="model" /> | `string` | The model that handled the request. |
| <CopyableCode code="role" /> | `string` | The conversational role of the generated message. |
| <CopyableCode code="stop_reason" /> | `string` | The reason the model stopped generating. |
| <CopyableCode code="stop_sequence" /> | `string` | The stop sequence that caused the model to stop, if applicable. |
| <CopyableCode code="type" /> | `string` | Object type, which is always "message" for Messages API. |
| <CopyableCode code="usage" /> | `object` | Information about token usage and rate limits. |

## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="create_message" /> | `SELECT` | <CopyableCode code="anthropic-version, data__max_tokens, data__messages, data__model" /> |

## Required Parameters for Message Creation
| Parameter | Description |
|:----------|:------------|
| `anthropic-version` | API version string (e.g., '2023-06-01') |
| `data__max_tokens` | Maximum number of tokens to generate |
| `data__messages` | Array of message objects with role and content |
| `data__model` | Model identifier (e.g., 'claude-3-5-sonnet-20240620') |

:::info Model Comparison Table
To help you choose the right model for your needs, we’ve compiled a table comparing the key features and capabilities of each model in the Claude family:

| Model                 | Claude 3.5 Sonnet                     | Claude 3 Opus               | Claude 3 Sonnet            | Claude 3 Haiku                               |
|-----------------------|---------------------------------------|-----------------------------|-----------------------------|----------------------------------------------|
| **Description**       | Most intelligent model               | Powerful model for highly complex tasks | Balance of intelligence and speed | Fastest and most compact model for near-instant responsiveness |
| **Strengths**         | Highest level of intelligence and capability | Top-level performance, intelligence, fluency, and understanding | Strong utility, balanced for scaled deployments | Quick and accurate targeted performance |
| **Multilingual**      | Yes                                   | Yes                         | Yes                         | Yes                                          |
| **Vision**            | Yes                                   | Yes                         | Yes                         | Yes                                          |
| **Message Batches API** | Yes                                 | Yes                         | No                          | Yes                                          |
| **API model name**    | Upgraded version: `claude-3-5-sonnet-20241022` <br /> Previous version: `claude-3-5-sonnet-20240620` | `claude-3-opus-20240229`    | `claude-3-sonnet-20240229`                   | `claude-3-haiku-20240307`                   |
| **Comparative latency** | Fast                                | Moderately fast             | Fast                        | Fastest                                      |
| **Context window**    | 200K                                  | 200K                        | 200K                        | 200K                                         |
| **Max output**        | 8192 tokens                           | 4096 tokens                 | 4096 tokens                 | 4096 tokens                                  |
| **Cost (Input / Output per MTok)** | $3.00 / $15.00               | $15.00 / $75.00            | $3.00 / $15.00              | $0.25 / $1.25                                |
| **Training data cut-off** | Apr 2024                           | Aug 2023                    | Aug 2023                    | Aug 2023                                     |

:::

## Query Examples

### Basic Message Generation
This example generates a one-sentence summary of StackQL:

```sql
SELECT
  model as model,
  role as role,
  stop_reason as stop_reason,
  stop_sequence as stop_sequence,
  JSON_EXTRACT(usage, '$.input_tokens') as input_tokens,
  JSON_EXTRACT(usage, '$.output_tokens') as output_tokens,
  JSON_EXTRACT(json_each.value, '$.text') as content
FROM
  anthropic.messages.message,
  JSON_EACH(content)
WHERE 
  "anthropic-version" = '2023-06-01'
  AND data__model = 'claude-3-5-sonnet-20240620'
  AND data__max_tokens = 1024
  AND data__messages = '[{"role": "user", "content": "one sentence summary of stackql"}]'
```

Example response:
```
|----------------------------|-----------|-------------|---------------|--------------|---------------|--------------------------------|
|           model            |   role    | stop_reason | stop_sequence | input_tokens | output_tokens |            content             |
|----------------------------|-----------|-------------|---------------|--------------|---------------|--------------------------------|
| claude-3-5-sonnet-20240620 | assistant | end_turn    | null          |           13 |            46 | StackQL is a SQL-like query    |
|                            |           |             |               |              |               | language and runtime for       |
|                            |           |             |               |              |               | cloud infrastructure, allowing |
|                            |           |             |               |              |               | users to query, analyze, and   |
|                            |           |             |               |              |               | manage cloud resources across  |
|                            |           |             |               |              |               | multiple providers using       |
|                            |           |             |               |              |               | familiar SQL syntax.           |
|----------------------------|-----------|-------------|---------------|--------------|---------------|--------------------------------|
```

### Multi-turn Conversation Example
This example shows how to conduct a multi-turn conversation:

```sql
SELECT
  JSON_EXTRACT(json_each.value, '$.text') as content
FROM
  anthropic.messages.message,
  JSON_EACH(content)
WHERE 
  "anthropic-version" = '2023-06-01'
  AND data__model = 'claude-3-5-sonnet-20240620'
  AND data__max_tokens = 1024
  AND data__messages = '[
    {"role": "user", "content": "What is cloud infrastructure?"},
    {"role": "assistant", "content": "Cloud infrastructure refers to the hardware and software components needed for cloud computing, including servers, storage, and networking resources."},
    {"role": "user", "content": "How can StackQL help manage it?"}
  ]'
```

### Using System Prompts
Example showing how to include a system prompt:

```sql
SELECT
  JSON_EXTRACT(json_each.value, '$.text') as content
FROM
  anthropic.messages.message,
  JSON_EACH(content)
WHERE 
  "anthropic-version" = '2023-06-01'
  AND data__model = 'claude-3-5-sonnet-20240620'
  AND data__max_tokens = 1024
  AND data__system = 'You are a cloud infrastructure expert focusing on technical details.'
  AND data__messages = '[{"role": "user", "content": "Explain how StackQL helps with cloud resource management"}]'
```

## Usage Notes

### Token Usage
- The `usage` object contains information about token consumption:
  - `input_tokens`: Number of tokens in the input
  - `output_tokens`: Number of tokens generated in the response
- Token usage affects billing and rate limits
- Token counts may not exactly match visible content due to internal processing

### Response Processing
- Use `JSON_EACH` to process the content array
- Content is returned as blocks with type and text
- Use `JSON_EXTRACT` to access nested JSON fields like usage statistics

### Best Practices
1. Always specify an appropriate `max_tokens` value
2. Include the correct `anthropic-version` header
3. Format message arrays properly as JSON strings
4. Use system prompts for specialized behavior
5. Monitor token usage for cost optimization

## Error Handling
Common error scenarios to handle:
- Invalid model specification
- Malformed message JSON
- Token limit exceeded
- Rate limiting
- Authentication failures

## Rate Limits
- Token-based rate limiting
- Monitored through the usage object
- Consider implementing backoff strategies for heavy usage

## Version Compatibility
- Specify API version using `anthropic-version`
- Current supported version: '2023-06-01'
- Check Anthropic's documentation for version updates

## Advanced Usage Examples

### Temperature Control
Adjust response randomness with the temperature parameter:

```sql
/* Lower temperature for more focused responses */
SELECT
  JSON_EXTRACT(json_each.value, '$.text') as content
FROM
  anthropic.messages.message,
  JSON_EACH(content)
WHERE 
  "anthropic-version" = '2023-06-01'
  AND data__model = 'claude-3-5-sonnet-20240620'
  AND data__max_tokens = 1024
  AND data__temperature = 1  
  AND data__messages = '[{"role": "user", "content": "List 3 key benefits of using StackQL"}]'
```

### Using Stop Sequences
Configure custom stop sequences to control response length:

```sql
SELECT
  JSON_EXTRACT(json_each.value, '$.text') as content,
  stop_reason,
  stop_sequence
FROM
  anthropic.messages.message,
  JSON_EACH(content)
WHERE 
  "anthropic-version" = '2023-06-01'
  AND data__model = 'claude-3-5-sonnet-20240620'
  AND data__max_tokens = 1024
  AND data__stop_sequences = '["END", "STOP"]'
  AND data__messages = '[{"role": "user", "content": "Describe StackQL until you reach a natural conclusion END"}]'
```

### Metadata Tracking
Include metadata for request tracking:

```sql
SELECT
  JSON_EXTRACT(json_each.value, '$.text') as content,
  JSON_EXTRACT(usage, '$.input_tokens') as input_tokens,
  JSON_EXTRACT(usage, '$.output_tokens') as output_tokens
FROM
  anthropic.messages.message,
  JSON_EACH(content)
WHERE 
  "anthropic-version" = '2023-06-01'
  AND data__model = 'claude-3-5-sonnet-20240620'
  AND data__max_tokens = 1024
  AND data__metadata = '{"user_id": "u123"}'
  AND data__messages = '[{"role": "user", "content": "What is StackQL?"}]'
```

## Working with Response Data

### Content Block Structure
The content field returns an array of blocks with this structure:

```json
{
  "type": "text",
  "text": "The actual content..."
}
```

Access specific parts using JSON functions:
```sql
-- Get just the text content
JSON_EXTRACT(json_each.value, '$.text')

-- Get the content type
JSON_EXTRACT(json_each.value, '$.type')
```

### Usage Statistics Processing
Extract detailed usage information:

```sql
SELECT
  JSON_EXTRACT(usage, '$.input_tokens') as input_tokens,
  JSON_EXTRACT(usage, '$.output_tokens') as output_tokens,
  JSON_EXTRACT(usage, '$.cache_creation_input_tokens') as cache_creation_tokens,
  JSON_EXTRACT(usage, '$.cache_read_input_tokens') as cache_read_tokens
FROM
  anthropic.messages.message
WHERE
  -- query conditions
```

## Performance Optimization

### Token Usage Optimization
Tips for minimizing token usage:
1. Use precise prompts
2. Set appropriate max_tokens
3. Use system prompts effectively
4. Leverage stop sequences
5. Monitor and analyze usage patterns

### Response Processing Optimization
Strategies for efficient response handling:
1. Use appropriate JSON extraction
2. Implement efficient error handling
3. Process responses asynchronously when possible
4. Cache frequently used responses
5. Implement retry logic with exponential backoff