---
title: prompts
hide_title: false
hide_table_of_contents: false
keywords:
  - prompts
  - connect
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

Creates, updates, deletes or gets a <code>prompt</code> resource or lists <code>prompts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prompts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::Prompt</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.prompts" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the prompt.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the prompt.</td></tr>
<tr><td><CopyableCode code="s3_uri" /></td><td><code>string</code></td><td>S3 URI of the customer's audio file for creating prompts resource..</td></tr>
<tr><td><CopyableCode code="prompt_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the prompt.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html"><code>AWS::Connect::Prompt</code></a>.

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
    <td><CopyableCode code="InstanceArn, Name, region" /></td>
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
Gets all <code>prompts</code> in a region.
```sql
SELECT
region,
instance_arn,
name,
description,
s3_uri,
prompt_arn,
tags
FROM aws.connect.prompts
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>prompt</code>.
```sql
SELECT
region,
instance_arn,
name,
description,
s3_uri,
prompt_arn,
tags
FROM aws.connect.prompts
WHERE region = 'us-east-1' AND data__Identifier = '<PromptArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>prompt</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.prompts (
 InstanceArn,
 Name,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.prompts (
 InstanceArn,
 Name,
 Description,
 S3Uri,
 Tags,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ Name }}',
 '{{ Description }}',
 '{{ S3Uri }}',
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
  - name: prompt
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: S3Uri
        value: '{{ S3Uri }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.prompts
WHERE data__Identifier = '<PromptArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>prompts</code> resource, the following permissions are required:

### Create
```json
connect:CreatePrompt,
connect:TagResource,
s3:GetObject,
kms:Decrypt,
s3:GetObjectAcl
```

### Read
```json
connect:DescribePrompt
```

### Update
```json
connect:UpdatePrompt,
connect:TagResource,
connect:UntagResource
```

### Delete
```json
connect:DeletePrompt
```

### List
```json
connect:ListPrompts
```
