---
title: user_group
hide_title: false
hide_table_of_contents: false
keywords:
  - user_group
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
Gets an individual <code>user_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.elasticache.user_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>Indicates user group status. Can be "creating", "active", "modifying", "deleting".</td></tr>
<tr><td><code>user_group_id</code></td><td><code>string</code></td><td>The ID of the user group.</td></tr>
<tr><td><code>engine</code></td><td><code>string</code></td><td>Must be redis.</td></tr>
<tr><td><code>user_ids</code></td><td><code>array</code></td><td>List of users associated to this user group.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the user account.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this user.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
status,
user_group_id,
engine,
user_ids,
arn,
tags
FROM awscc.elasticache.user_group
WHERE region = 'us-east-1'
AND data__Identifier = '{UserGroupId}';
```

## Permissions

To operate on the <code>user_group</code> resource, the following permissions are required:

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

