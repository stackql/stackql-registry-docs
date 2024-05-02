---
title: acl
hide_title: false
hide_table_of_contents: false
keywords:
  - acl
  - memorydb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>acl</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>acl</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MemoryDB::ACL</td></tr>
<tr><td><b>Id</b></td><td><code>aws.memorydb.acl</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>Indicates acl status. Can be "creating", "active", "modifying", "deleting".</td></tr>
<tr><td><code>acl_name</code></td><td><code>string</code></td><td>The name of the acl.</td></tr>
<tr><td><code>user_names</code></td><td><code>array</code></td><td>List of users associated to this acl.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the acl.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this cluster.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
status,
acl_name,
user_names,
arn,
tags
FROM aws.memorydb.acl
WHERE data__Identifier = '<ACLName>';
```

## Permissions

To operate on the <code>acl</code> resource, the following permissions are required:

### Read
```json
memorydb:DescribeACLs,
memorydb:ListTags
```

### Update
```json
memorydb:UpdateACL,
memorydb:DescribeACLs,
memorydb:ListTags,
memorydb:TagResource,
memorydb:UntagResource
```

### Delete
```json
memorydb:ModifyReplicationGroup,
memorydb:DeleteACL,
memorydb:DescribeACLs
```

