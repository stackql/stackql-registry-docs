---
title: ai_guardrails
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_guardrails
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

Creates, updates, deletes or gets an <code>ai_guardrail</code> resource or lists <code>ai_guardrails</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ai_guardrails</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Wisdom::AIGuardrail Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wisdom.ai_guardrails" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="assistant_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="assistant_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="a_iguardrail_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="a_iguardrail_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="blocked_input_messaging" /></td><td><code>string</code></td><td>Messaging for when violations are detected in text</td></tr>
<tr><td><CopyableCode code="blocked_outputs_messaging" /></td><td><code>string</code></td><td>Messaging for when violations are detected in text</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the guardrail or its version</td></tr>
<tr><td><CopyableCode code="topic_policy_config" /></td><td><code>object</code></td><td>Topic policy config for a guardrail.</td></tr>
<tr><td><CopyableCode code="content_policy_config" /></td><td><code>object</code></td><td>Content policy config for a guardrail.</td></tr>
<tr><td><CopyableCode code="word_policy_config" /></td><td><code>object</code></td><td>Word policy config for a guardrail.</td></tr>
<tr><td><CopyableCode code="sensitive_information_policy_config" /></td><td><code>object</code></td><td>Sensitive information policy config for a guardrail.</td></tr>
<tr><td><CopyableCode code="contextual_grounding_policy_config" /></td><td><code>object</code></td><td>Contextual grounding policy config for a guardrail.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html"><code>AWS::Wisdom::AIGuardrail</code></a>.

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
    <td><CopyableCode code="AssistantId, BlockedInputMessaging, BlockedOutputsMessaging, region" /></td>
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
Gets all <code>ai_guardrails</code> in a region.
```sql
SELECT
region,
assistant_id,
assistant_arn,
a_iguardrail_arn,
a_iguardrail_id,
name,
blocked_input_messaging,
blocked_outputs_messaging,
description,
topic_policy_config,
content_policy_config,
word_policy_config,
sensitive_information_policy_config,
contextual_grounding_policy_config,
tags
FROM aws.wisdom.ai_guardrails
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>ai_guardrail</code>.
```sql
SELECT
region,
assistant_id,
assistant_arn,
a_iguardrail_arn,
a_iguardrail_id,
name,
blocked_input_messaging,
blocked_outputs_messaging,
description,
topic_policy_config,
content_policy_config,
word_policy_config,
sensitive_information_policy_config,
contextual_grounding_policy_config,
tags
FROM aws.wisdom.ai_guardrails
WHERE region = 'us-east-1' AND data__Identifier = '<AIGuardrailId>|<AssistantId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ai_guardrail</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.wisdom.ai_guardrails (
 AssistantId,
 BlockedInputMessaging,
 BlockedOutputsMessaging,
 region
)
SELECT 
'{{ AssistantId }}',
 '{{ BlockedInputMessaging }}',
 '{{ BlockedOutputsMessaging }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.wisdom.ai_guardrails (
 AssistantId,
 Name,
 BlockedInputMessaging,
 BlockedOutputsMessaging,
 Description,
 TopicPolicyConfig,
 ContentPolicyConfig,
 WordPolicyConfig,
 SensitiveInformationPolicyConfig,
 ContextualGroundingPolicyConfig,
 Tags,
 region
)
SELECT 
 '{{ AssistantId }}',
 '{{ Name }}',
 '{{ BlockedInputMessaging }}',
 '{{ BlockedOutputsMessaging }}',
 '{{ Description }}',
 '{{ TopicPolicyConfig }}',
 '{{ ContentPolicyConfig }}',
 '{{ WordPolicyConfig }}',
 '{{ SensitiveInformationPolicyConfig }}',
 '{{ ContextualGroundingPolicyConfig }}',
 '{{ Tags }}',
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
  - name: ai_guardrail
    props:
      - name: AssistantId
        value: '{{ AssistantId }}'
      - name: Name
        value: '{{ Name }}'
      - name: BlockedInputMessaging
        value: '{{ BlockedInputMessaging }}'
      - name: BlockedOutputsMessaging
        value: '{{ BlockedOutputsMessaging }}'
      - name: Description
        value: '{{ Description }}'
      - name: TopicPolicyConfig
        value:
          TopicsConfig:
            - Name: '{{ Name }}'
              Definition: '{{ Definition }}'
              Examples:
                - '{{ Examples[0] }}'
              Type: '{{ Type }}'
      - name: ContentPolicyConfig
        value:
          FiltersConfig:
            - Type: '{{ Type }}'
              InputStrength: '{{ InputStrength }}'
              OutputStrength: null
      - name: WordPolicyConfig
        value:
          WordsConfig:
            - Text: '{{ Text }}'
          ManagedWordListsConfig:
            - Type: '{{ Type }}'
      - name: SensitiveInformationPolicyConfig
        value:
          PiiEntitiesConfig:
            - Type: '{{ Type }}'
              Action: '{{ Action }}'
          RegexesConfig:
            - Name: '{{ Name }}'
              Description: '{{ Description }}'
              Pattern: '{{ Pattern }}'
              Action: null
      - name: ContextualGroundingPolicyConfig
        value:
          FiltersConfig:
            - Type: '{{ Type }}'
              Threshold: null
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.wisdom.ai_guardrails
WHERE data__Identifier = '<AIGuardrailId|AssistantId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ai_guardrails</code> resource, the following permissions are required:

### Create
```json
wisdom:CreateAIGuardrail,
wisdom:TagResource
```

### Read
```json
wisdom:GetAIGuardrail
```

### Update
```json
wisdom:UpdateAIGuardrail
```

### Delete
```json
wisdom:DeleteAIGuardrail
```

### List
```json
wisdom:ListAIGuardrails
```
