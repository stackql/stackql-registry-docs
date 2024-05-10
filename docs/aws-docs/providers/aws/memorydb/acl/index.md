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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>acl</code> resource, use <code>acls</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>acl</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MemoryDB::ACL</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.memorydb.acl" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Indicates acl status. Can be "creating", "active", "modifying", "deleting".</td></tr>
<tr><td><CopyableCode code="acl_name" /></td><td><code>string</code></td><td>The name of the acl.</td></tr>
<tr><td><CopyableCode code="user_names" /></td><td><code>array</code></td><td>List of users associated to this acl.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the acl.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this cluster.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
WHERE region = 'us-east-1' AND data__Identifier = '<ACLName>';
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

