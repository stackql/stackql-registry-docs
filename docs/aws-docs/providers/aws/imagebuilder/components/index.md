---
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
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


Used to retrieve a list of <code>components</code> in a region or to create or delete a <code>components</code> resource, use <code>component</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::Component</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.components" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the component.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
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
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.imagebuilder.components
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>component</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- component.iql (required properties only)
INSERT INTO aws.imagebuilder.components (
 Name,
 Version,
 Platform,
 region
)
SELECT 
'{{ Name }}',
 '{{ Version }}',
 '{{ Platform }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- component.iql (all properties)
INSERT INTO aws.imagebuilder.components (
 Name,
 Version,
 Description,
 ChangeDescription,
 Platform,
 Data,
 KmsKeyId,
 Tags,
 Uri,
 SupportedOsVersions,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Version }}',
 '{{ Description }}',
 '{{ ChangeDescription }}',
 '{{ Platform }}',
 '{{ Data }}',
 '{{ KmsKeyId }}',
 '{{ Tags }}',
 '{{ Uri }}',
 '{{ SupportedOsVersions }}',
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
  - name: component
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Version
        value: '{{ Version }}'
      - name: Description
        value: '{{ Description }}'
      - name: ChangeDescription
        value: '{{ ChangeDescription }}'
      - name: Platform
        value: '{{ Platform }}'
      - name: Data
        value: '{{ Data }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: Tags
        value: {}
      - name: Uri
        value: '{{ Uri }}'
      - name: SupportedOsVersions
        value:
          - '{{ SupportedOsVersions[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.imagebuilder.components
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>components</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
iam:GetRole,
kms:GenerateDataKey*,
kms:Encrypt,
kms:Decrypt,
s3:GetObject,
s3:HeadBucket,
s3:GetBucketLocation,
imagebuilder:TagResource,
imagebuilder:GetComponent,
imagebuilder:CreateComponent
```

### Delete
```json
imagebuilder:GetComponent,
imagebuilder:UnTagResource,
imagebuilder:DeleteComponent
```

### List
```json
imagebuilder:ListComponents
```

