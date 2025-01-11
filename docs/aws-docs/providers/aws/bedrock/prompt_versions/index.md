---
title: prompt_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - prompt_versions
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

Creates, updates, deletes or gets a <code>prompt_version</code> resource or lists <code>prompt_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prompt_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::PromptVersion Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.prompt_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="prompt_arn" /></td><td><code>string</code></td><td>ARN of a prompt resource possibly with a version</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN of a prompt version resource</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="prompt_id" /></td><td><code>string</code></td><td>Identifier for a Prompt</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>Version.</td></tr>
<tr><td><CopyableCode code="variants" /></td><td><code>array</code></td><td>List of prompt variants</td></tr>
<tr><td><CopyableCode code="default_variant" /></td><td><code>string</code></td><td>Name for a variant.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description for a prompt version resource.</td></tr>
<tr><td><CopyableCode code="customer_encryption_key_arn" /></td><td><code>string</code></td><td>A KMS key ARN</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name for a prompt resource.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of tag keys and values</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-promptversion.html"><code>AWS::Bedrock::PromptVersion</code></a>.

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
    <td><CopyableCode code="PromptArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>prompt_versions</code> in a region.
```sql
SELECT
region,
prompt_arn,
arn,
created_at,
prompt_id,
updated_at,
version,
variants,
default_variant,
description,
customer_encryption_key_arn,
name,
tags
FROM aws.bedrock.prompt_versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>prompt_version</code>.
```sql
SELECT
region,
prompt_arn,
arn,
created_at,
prompt_id,
updated_at,
version,
variants,
default_variant,
description,
customer_encryption_key_arn,
name,
tags
FROM aws.bedrock.prompt_versions
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>prompt_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.bedrock.prompt_versions (
 PromptArn,
 region
)
SELECT 
'{{ PromptArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.bedrock.prompt_versions (
 PromptArn,
 Description,
 Tags,
 region
)
SELECT 
 '{{ PromptArn }}',
 '{{ Description }}',
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
  - name: prompt_version
    props:
      - name: PromptArn
        value: '{{ PromptArn }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.bedrock.prompt_versions
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>prompt_versions</code> resource, the following permissions are required:

### Create
```json
bedrock:CreatePromptVersion,
bedrock:GetPrompt,
bedrock:TagResource,
bedrock:ListTagsForResource,
kms:GenerateDataKey,
kms:Decrypt
```

### Read
```json
bedrock:GetPrompt,
bedrock:ListTagsForResource,
kms:Decrypt
```

### Delete
```json
bedrock:DeletePrompt,
bedrock:GetPrompt
```

### List
```json
bedrock:ListPrompts
```
