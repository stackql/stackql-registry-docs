---
title: acls
hide_title: false
hide_table_of_contents: false
keywords:
  - acls
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

Creates, updates, deletes or gets an <code>acl</code> resource or lists <code>acls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>acls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MemoryDB::ACL</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.memorydb.acls" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Indicates acl status. Can be "creating", "active", "modifying", "deleting".</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ACLName, region" /></td>
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
List all <code>acls</code> in a region.
```sql
SELECT
region,
acl_name
FROM aws.memorydb.acls
WHERE region = 'us-east-1';
```
Gets all properties from an <code>acl</code>.
```sql
SELECT
region,
status,
acl_name,
user_names,
arn,
tags
FROM aws.memorydb.acls
WHERE region = 'us-east-1' AND data__Identifier = '<ACLName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>acl</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.memorydb.acls (
 ACLName,
 region
)
SELECT 
'{{ ACLName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.memorydb.acls (
 ACLName,
 UserNames,
 Tags,
 region
)
SELECT 
 '{{ ACLName }}',
 '{{ UserNames }}',
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
  - name: acl
    props:
      - name: ACLName
        value: '{{ ACLName }}'
      - name: UserNames
        value:
          - '{{ UserNames[0] }}'
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
DELETE FROM aws.memorydb.acls
WHERE data__Identifier = '<ACLName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>acls</code> resource, the following permissions are required:

### Create
```json
memorydb:CreateACL,
memorydb:DescribeACLs,
memorydb:TagResource,
memorydb:ListTags
```

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

### List
```json
memorydb:DescribeACLs,
memorydb:ListTags
```

