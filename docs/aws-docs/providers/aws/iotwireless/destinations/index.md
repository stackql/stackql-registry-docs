---
title: destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - destinations
  - iotwireless
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

Creates, updates, deletes or gets a <code>destination</code> resource or lists <code>destinations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Destination's resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.destinations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Unique name of destination</td></tr>
<tr><td><CopyableCode code="expression" /></td><td><code>string</code></td><td>Destination expression</td></tr>
<tr><td><CopyableCode code="expression_type" /></td><td><code>string</code></td><td>Must be RuleName</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Destination description</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the destination.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>AWS role ARN that grants access</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Destination arn. Returned after successful create.</td></tr>
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
    <td><CopyableCode code="Name, Expression, ExpressionType, region" /></td>
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
Gets all <code>destinations</code> in a region.
```sql
SELECT
region,
name,
expression,
expression_type,
description,
tags,
role_arn,
arn
FROM aws.iotwireless.destinations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>destination</code>.
```sql
SELECT
region,
name,
expression,
expression_type,
description,
tags,
role_arn,
arn
FROM aws.iotwireless.destinations
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>destination</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotwireless.destinations (
 Name,
 Expression,
 ExpressionType,
 region
)
SELECT 
'{{ Name }}',
 '{{ Expression }}',
 '{{ ExpressionType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotwireless.destinations (
 Name,
 Expression,
 ExpressionType,
 Description,
 Tags,
 RoleArn,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Expression }}',
 '{{ ExpressionType }}',
 '{{ Description }}',
 '{{ Tags }}',
 '{{ RoleArn }}',
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
  - name: destination
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Expression
        value: '{{ Expression }}'
      - name: ExpressionType
        value: '{{ ExpressionType }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: RoleArn
        value: '{{ RoleArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iotwireless.destinations
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>destinations</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
iotwireless:CreateDestination,
iotwireless:TagResource,
iotwireless:ListTagsForResource
```

### Read
```json
iotwireless:GetDestination,
iotwireless:ListTagsForResource
```

### Update
```json
iam:PassRole,
iotwireless:UpdateDestination,
iotwireless:UntagResource,
iotwireless:ListTagsForResource
```

### Delete
```json
iotwireless:DeleteDestination
```

### List
```json
iotwireless:ListDestinations,
iotwireless:ListTagsForResource
```

