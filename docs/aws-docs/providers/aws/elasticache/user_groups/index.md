---
title: user_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - user_groups
  - elasticache
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

Creates, updates, deletes or gets an <code>user_group</code> resource or lists <code>user_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElastiCache::UserGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticache.user_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Indicates user group status. Can be "creating", "active", "modifying", "deleting".</td></tr>
<tr><td><CopyableCode code="user_group_id" /></td><td><code>string</code></td><td>The ID of the user group.</td></tr>
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>Must be redis.</td></tr>
<tr><td><CopyableCode code="user_ids" /></td><td><code>array</code></td><td>List of users associated to this user group.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the user account.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this user.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html"><code>AWS::ElastiCache::UserGroup</code></a>.

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
    <td><CopyableCode code="UserGroupId, Engine, UserIds, region" /></td>
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
Gets all <code>user_groups</code> in a region.
```sql
SELECT
region,
status,
user_group_id,
engine,
user_ids,
arn,
tags
FROM aws.elasticache.user_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>user_group</code>.
```sql
SELECT
region,
status,
user_group_id,
engine,
user_ids,
arn,
tags
FROM aws.elasticache.user_groups
WHERE region = 'us-east-1' AND data__Identifier = '<UserGroupId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.elasticache.user_groups (
 UserGroupId,
 Engine,
 UserIds,
 region
)
SELECT 
'{{ UserGroupId }}',
 '{{ Engine }}',
 '{{ UserIds }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.elasticache.user_groups (
 UserGroupId,
 Engine,
 UserIds,
 Tags,
 region
)
SELECT 
 '{{ UserGroupId }}',
 '{{ Engine }}',
 '{{ UserIds }}',
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
  - name: user_group
    props:
      - name: UserGroupId
        value: '{{ UserGroupId }}'
      - name: Engine
        value: '{{ Engine }}'
      - name: UserIds
        value:
          - '{{ UserIds[0] }}'
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
DELETE FROM aws.elasticache.user_groups
WHERE data__Identifier = '<UserGroupId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_groups</code> resource, the following permissions are required:

### Create
```json
elasticache:CreateUserGroup,
elasticache:DescribeUserGroups,
elasticache:ListTagsForResource,
elasticache:AddTagsToResource
```

### Read
```json
elasticache:DescribeUserGroups,
elasticache:ListTagsForResource
```

### Update
```json
elasticache:ModifyUserGroup,
elasticache:DescribeUserGroups,
elasticache:ListTagsForResource,
elasticache:AddTagsToResource,
elasticache:RemoveTagsFromResource
```

### Delete
```json
elasticache:ModifyReplicationGroup,
elasticache:DeleteUserGroup,
elasticache:DescribeUserGroups,
elasticache:ListTagsForResource
```

### List
```json
elasticache:DescribeUserGroups,
elasticache:ListTagsForResource
```
