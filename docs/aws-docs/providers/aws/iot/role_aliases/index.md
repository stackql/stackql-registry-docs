---
title: role_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - role_aliases
  - iot
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

Creates, updates, deletes or gets a <code>role_alias</code> resource or lists <code>role_aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Use the AWS::IoT::RoleAlias resource to declare an AWS IoT RoleAlias.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.role_aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="role_alias" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_alias_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="credential_duration_seconds" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="RoleArn, region" /></td>
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
List all <code>role_aliases</code> in a region.
```sql
SELECT
region,
role_alias
FROM aws.iot.role_aliases
WHERE region = 'us-east-1';
```
Gets all properties from a <code>role_alias</code>.
```sql
SELECT
region,
role_alias,
role_alias_arn,
role_arn,
credential_duration_seconds,
tags
FROM aws.iot.role_aliases
WHERE region = 'us-east-1' AND data__Identifier = '<RoleAlias>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>role_alias</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.role_aliases (
 RoleArn,
 region
)
SELECT 
'{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.role_aliases (
 RoleAlias,
 RoleArn,
 CredentialDurationSeconds,
 Tags,
 region
)
SELECT 
 '{{ RoleAlias }}',
 '{{ RoleArn }}',
 '{{ CredentialDurationSeconds }}',
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
  - name: role_alias
    props:
      - name: RoleAlias
        value: '{{ RoleAlias }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: CredentialDurationSeconds
        value: '{{ CredentialDurationSeconds }}'
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
DELETE FROM aws.iot.role_aliases
WHERE data__Identifier = '<RoleAlias>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>role_aliases</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:PassRole,
iot:CreateRoleAlias,
iot:DescribeRoleAlias,
iot:TagResource,
iot:ListTagsForResource
```

### Read
```json
iam:GetRole,
iam:PassRole,
iot:DescribeRoleAlias,
iot:ListTagsForResource
```

### Update
```json
iam:GetRole,
iam:PassRole,
iot:UpdateRoleAlias,
iot:DescribeRoleAlias,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

### Delete
```json
iot:DeleteRoleAlias,
iot:DescribeRoleAlias
```

### List
```json
iot:ListRoleAliases
```

