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


Used to retrieve a list of <code>user_groups</code> in a region or to create or delete a <code>user_groups</code> resource, use <code>user_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElastiCache::UserGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticache.user_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="user_group_id" /></td><td><code>string</code></td><td>The ID of the user group.</td></tr>
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
user_group_id
FROM aws.elasticache.user_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- user_group.iql (required properties only)
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
-- user_group.iql (all properties)
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

## `DELETE` Example

```sql
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

