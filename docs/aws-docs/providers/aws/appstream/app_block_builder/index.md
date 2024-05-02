---
title: app_block_builder
hide_title: false
hide_table_of_contents: false
keywords:
  - app_block_builder
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>app_block_builder</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_block_builder</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::AppBlockBuilder.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appstream.app_block_builder</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>platform</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>access_endpoints</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>vpc_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>enable_default_internet_access</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>iam_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>app_block_arns</code></td><td><code>array</code></td><td></td></tr>
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
name,
arn,
description,
display_name,
platform,
access_endpoints,
tags,
vpc_config,
enable_default_internet_access,
iam_role_arn,
created_time,
instance_type,
app_block_arns
FROM aws.appstream.app_block_builder
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>app_block_builder</code> resource, the following permissions are required:

### Read
```json
appstream:DescribeAppBlockBuilders
```

### Update
```json
appstream:UpdateAppBlockBuilder,
appstream:DescribeAppBlockBuilders,
appstream:StartAppBlockBuilder,
appstream:StopAppBlockBuilder,
appstream:AssociateAppBlockBuilderAppBlock,
appstream:DisassociateAppBlockBuilderAppBlock,
appstream:DescribeAppBlockBuilderAppBlockAssociations,
appstream:ListTagsForResource,
appstream:TagResource,
appstream:UntagResource,
iam:PassRole
```

### Delete
```json
appstream:DescribeAppBlockBuilders,
appstream:DeleteAppBlockBuilder,
appstream:DisassociateAppBlockBuilderAppBlock,
appstream:DescribeAppBlockBuilderAppBlockAssociations
```

