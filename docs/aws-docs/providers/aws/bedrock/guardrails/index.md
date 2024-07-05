---
title: guardrails
hide_title: false
hide_table_of_contents: false
keywords:
  - guardrails
  - bedrock
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

Creates, updates, deletes or gets a <code>guardrail</code> resource or lists <code>guardrails</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>guardrails</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::Guardrail Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.guardrails" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="blocked_input_messaging" /></td><td><code>string</code></td><td>Messaging for when violations are detected in text</td></tr>
<tr><td><CopyableCode code="blocked_outputs_messaging" /></td><td><code>string</code></td><td>Messaging for when violations are detected in text</td></tr>
<tr><td><CopyableCode code="content_policy_config" /></td><td><code>object</code></td><td>Content policy config for a guardrail.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Time Stamp</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the guardrail or its version</td></tr>
<tr><td><CopyableCode code="failure_recommendations" /></td><td><code>array</code></td><td>List of failure recommendations</td></tr>
<tr><td><CopyableCode code="guardrail_arn" /></td><td><code>string</code></td><td>Arn representation for the guardrail</td></tr>
<tr><td><CopyableCode code="guardrail_id" /></td><td><code>string</code></td><td>Unique id for the guardrail</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>The KMS key with which the guardrail was encrypted at rest</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the guardrail</td></tr>
<tr><td><CopyableCode code="sensitive_information_policy_config" /></td><td><code>object</code></td><td>Sensitive information policy config for a guardrail.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Status of the guardrail</td></tr>
<tr><td><CopyableCode code="status_reasons" /></td><td><code>array</code></td><td>List of status reasons</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>List of Tags</td></tr>
<tr><td><CopyableCode code="topic_policy_config" /></td><td><code>object</code></td><td>Topic policy config for a guardrail.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Time Stamp</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>Guardrail version</td></tr>
<tr><td><CopyableCode code="word_policy_config" /></td><td><code>object</code></td><td>Word policy config for a guardrail.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

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
    <td><CopyableCode code="Name, BlockedInputMessaging, BlockedOutputsMessaging, region" /></td>
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
Gets all <code>guardrails</code> in a region.
```sql
SELECT
region,
blocked_input_messaging,
blocked_outputs_messaging,
content_policy_config,
created_at,
description,
failure_recommendations,
guardrail_arn,
guardrail_id,
kms_key_arn,
name,
sensitive_information_policy_config,
status,
status_reasons,
tags,
topic_policy_config,
updated_at,
version,
word_policy_config
FROM aws.bedrock.guardrails
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>guardrail</code>.
```sql
SELECT
region,
blocked_input_messaging,
blocked_outputs_messaging,
content_policy_config,
created_at,
description,
failure_recommendations,
guardrail_arn,
guardrail_id,
kms_key_arn,
name,
sensitive_information_policy_config,
status,
status_reasons,
tags,
topic_policy_config,
updated_at,
version,
word_policy_config
FROM aws.bedrock.guardrails
WHERE region = 'us-east-1' AND data__Identifier = '<GuardrailArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>guardrail</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.bedrock.guardrails (
 BlockedInputMessaging,
 BlockedOutputsMessaging,
 Name,
 region
)
SELECT 
'{{ BlockedInputMessaging }}',
 '{{ BlockedOutputsMessaging }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.bedrock.guardrails (
 BlockedInputMessaging,
 BlockedOutputsMessaging,
 ContentPolicyConfig,
 Description,
 KmsKeyArn,
 Name,
 SensitiveInformationPolicyConfig,
 Tags,
 TopicPolicyConfig,
 WordPolicyConfig,
 region
)
SELECT 
 '{{ BlockedInputMessaging }}',
 '{{ BlockedOutputsMessaging }}',
 '{{ ContentPolicyConfig }}',
 '{{ Description }}',
 '{{ KmsKeyArn }}',
 '{{ Name }}',
 '{{ SensitiveInformationPolicyConfig }}',
 '{{ Tags }}',
 '{{ TopicPolicyConfig }}',
 '{{ WordPolicyConfig }}',
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
  - name: guardrail
    props:
      - name: BlockedInputMessaging
        value: '{{ BlockedInputMessaging }}'
      - name: BlockedOutputsMessaging
        value: '{{ BlockedOutputsMessaging }}'
      - name: ContentPolicyConfig
        value:
          FiltersConfig:
            - Type: '{{ Type }}'
              InputStrength: '{{ InputStrength }}'
              OutputStrength: null
      - name: Description
        value: '{{ Description }}'
      - name: KmsKeyArn
        value: '{{ KmsKeyArn }}'
      - name: Name
        value: '{{ Name }}'
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
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TopicPolicyConfig
        value:
          TopicsConfig:
            - Name: '{{ Name }}'
              Definition: '{{ Definition }}'
              Examples:
                - '{{ Examples[0] }}'
              Type: '{{ Type }}'
      - name: WordPolicyConfig
        value:
          WordsConfig:
            - Text: '{{ Text }}'
          ManagedWordListsConfig:
            - Type: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.bedrock.guardrails
WHERE data__Identifier = '<GuardrailArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>guardrails</code> resource, the following permissions are required:

### Create
```json
bedrock:CreateGuardrail,
bedrock:GetGuardrail,
kms:DescribeKey,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt,
bedrock:TagResource,
bedrock:ListTagsForResource
```

### Read
```json
bedrock:GetGuardrail,
kms:Decrypt,
bedrock:ListTagsForResource
```

### Update
```json
bedrock:UpdateGuardrail,
bedrock:GetGuardrail,
bedrock:ListTagsForResource,
bedrock:TagResource,
bedrock:UntagResource,
kms:DescribeKey,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
bedrock:DeleteGuardrail,
bedrock:GetGuardrail,
kms:Decrypt,
kms:RetireGrant
```

### List
```json
bedrock:ListGuardrails
```

