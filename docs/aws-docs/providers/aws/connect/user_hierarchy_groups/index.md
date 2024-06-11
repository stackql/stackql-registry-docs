---
title: user_hierarchy_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - user_hierarchy_groups
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

Creates, updates, deletes or gets an <code>user_hierarchy_group</code> resource or lists <code>user_hierarchy_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_hierarchy_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::UserHierarchyGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.user_hierarchy_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="user_hierarchy_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the user hierarchy group.</td></tr>
<tr><td><CopyableCode code="parent_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the parent user hierarchy group.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the user hierarchy group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
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
    <td><CopyableCode code="Name, InstanceArn, region" /></td>
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
List all <code>user_hierarchy_groups</code> in a region.
```sql
SELECT
region,
user_hierarchy_group_arn
FROM aws.connect.user_hierarchy_groups
WHERE region = 'us-east-1';
```
Gets all properties from an <code>user_hierarchy_group</code>.
```sql
SELECT
region,
instance_arn,
user_hierarchy_group_arn,
parent_group_arn,
name,
tags
FROM aws.connect.user_hierarchy_groups
WHERE region = 'us-east-1' AND data__Identifier = '<UserHierarchyGroupArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_hierarchy_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.user_hierarchy_groups (
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
INSERT INTO aws.connect.user_hierarchy_groups (
 InstanceArn,
 ParentGroupArn,
 Name,
 Tags,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ ParentGroupArn }}',
 '{{ Name }}',
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
  - name: user_hierarchy_group
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: ParentGroupArn
        value: '{{ ParentGroupArn }}'
      - name: Name
        value: '{{ Name }}'
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
DELETE FROM aws.connect.user_hierarchy_groups
WHERE data__Identifier = '<UserHierarchyGroupArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_hierarchy_groups</code> resource, the following permissions are required:

### Create
```json
connect:CreateUserHierarchyGroup,
connect:TagResource
```

### Read
```json
connect:DescribeUserHierarchyGroup
```

### Delete
```json
connect:DeleteUserHierarchyGroup,
connect:UntagResource
```

### Update
```json
connect:UpdateUserHierarchyGroupName,
connect:TagResource,
connect:UntagResource
```

### List
```json
connect:ListUserHierarchyGroups
```

