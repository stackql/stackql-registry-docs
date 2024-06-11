---
title: workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows
  - imagebuilder
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

Creates, updates, deletes or gets a <code>workflow</code> resource or lists <code>workflows</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::Workflow</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.workflows" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the workflow.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the workflow.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version of the workflow.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the workflow.</td></tr>
<tr><td><CopyableCode code="change_description" /></td><td><code>string</code></td><td>The change description of the workflow.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the workflow denotes whether the workflow is used to build, test, or distribute.</td></tr>
<tr><td><CopyableCode code="data" /></td><td><code>string</code></td><td>The data of the workflow.</td></tr>
<tr><td><CopyableCode code="uri" /></td><td><code>string</code></td><td>The uri of the workflow.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The KMS key identifier used to encrypt the workflow.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The tags associated with the workflow.</td></tr>
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
    <td><CopyableCode code="Name, Type, Version, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>workflows</code> in a region.
```sql
SELECT
region,
arn
FROM aws.imagebuilder.workflows
WHERE region = 'us-east-1';
```
Gets all properties from a <code>workflow</code>.
```sql
SELECT
region,
arn,
name,
version,
description,
change_description,
type,
data,
uri,
kms_key_id,
tags
FROM aws.imagebuilder.workflows
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workflow</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.imagebuilder.workflows (
 Name,
 Version,
 Type,
 region
)
SELECT 
'{{ Name }}',
 '{{ Version }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.imagebuilder.workflows (
 Name,
 Version,
 Description,
 ChangeDescription,
 Type,
 Data,
 Uri,
 KmsKeyId,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Version }}',
 '{{ Description }}',
 '{{ ChangeDescription }}',
 '{{ Type }}',
 '{{ Data }}',
 '{{ Uri }}',
 '{{ KmsKeyId }}',
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
  - name: workflow
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Version
        value: '{{ Version }}'
      - name: Description
        value: '{{ Description }}'
      - name: ChangeDescription
        value: '{{ ChangeDescription }}'
      - name: Type
        value: '{{ Type }}'
      - name: Data
        value: '{{ Data }}'
      - name: Uri
        value: '{{ Uri }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.imagebuilder.workflows
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>workflows</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
kms:GenerateDataKey*,
kms:Encrypt,
kms:Decrypt,
s3:GetObject,
s3:HeadBucket,
s3:GetBucketLocation,
imagebuilder:TagResource,
imagebuilder:GetWorkflow,
imagebuilder:CreateWorkflow
```

### Read
```json
imagebuilder:GetWorkflow
```

### Delete
```json
imagebuilder:GetWorkflow,
imagebuilder:UnTagResource,
imagebuilder:DeleteWorkflow
```

### List
```json
imagebuilder:ListWorkflows
```

