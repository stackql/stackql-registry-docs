---
title: ai_prompts
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_prompts
  - wisdom
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>ai_prompt</code> resource or lists <code>ai_prompts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ai_prompts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Wisdom::AIPrompt Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wisdom.ai_prompts" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="a_iprompt_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="a_iprompt_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="api_format" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="assistant_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="assistant_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="template_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="template_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="modified_time_seconds" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html"><code>AWS::Wisdom::AIPrompt</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ApiFormat, ModelId, TemplateConfiguration, TemplateType, Type, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>ai_prompts</code> in a region.
```sql
SELECT
region,
a_iprompt_id,
a_iprompt_arn,
api_format,
assistant_id,
assistant_arn,
description,
model_id,
name,
tags,
template_configuration,
template_type,
type,
modified_time_seconds
FROM aws.wisdom.ai_prompts
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>ai_prompt</code>.
```sql
SELECT
region,
a_iprompt_id,
a_iprompt_arn,
api_format,
assistant_id,
assistant_arn,
description,
model_id,
name,
tags,
template_configuration,
template_type,
type,
modified_time_seconds
FROM aws.wisdom.ai_prompts
WHERE region = 'us-east-1' AND data__Identifier = '<AIPromptId>|<AssistantId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ai_prompt</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.wisdom.ai_prompts (
 ApiFormat,
 ModelId,
 TemplateConfiguration,
 TemplateType,
 Type,
 region
)
SELECT 
'{{ ApiFormat }}',
 '{{ ModelId }}',
 '{{ TemplateConfiguration }}',
 '{{ TemplateType }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.wisdom.ai_prompts (
 ApiFormat,
 AssistantId,
 Description,
 ModelId,
 Name,
 Tags,
 TemplateConfiguration,
 TemplateType,
 Type,
 region
)
SELECT 
 '{{ ApiFormat }}',
 '{{ AssistantId }}',
 '{{ Description }}',
 '{{ ModelId }}',
 '{{ Name }}',
 '{{ Tags }}',
 '{{ TemplateConfiguration }}',
 '{{ TemplateType }}',
 '{{ Type }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: ai_prompt
    props:
      - name: ApiFormat
        value: '{{ ApiFormat }}'
      - name: AssistantId
        value: '{{ AssistantId }}'
      - name: Description
        value: '{{ Description }}'
      - name: ModelId
        value: '{{ ModelId }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value: {}
      - name: TemplateConfiguration
        value: {}
      - name: TemplateType
        value: '{{ TemplateType }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.wisdom.ai_prompts
WHERE data__Identifier = '<AIPromptId|AssistantId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ai_prompts</code> resource, the following permissions are required:

### Create
```json
wisdom:CreateAIPrompt,
wisdom:TagResource
```

### Read
```json
wisdom:GetAIPrompt
```

### Update
```json
wisdom:UpdateAIPrompt
```

### Delete
```json
wisdom:DeleteAIPrompt
```

### List
```json
wisdom:ListAIPrompts
```
