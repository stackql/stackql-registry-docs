---
title: locationf_sx_windows
hide_title: false
hide_table_of_contents: false
keywords:
  - locationf_sx_windows
  - datasync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>locationf_sx_windows</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locationf_sx_windows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationFSxWindows.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.datasync.locationf_sx_windows</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain</code></td><td><code>string</code></td><td>The name of the Windows domain that the FSx for Windows server belongs to.</td></tr>
<tr><td><code>fsx_filesystem_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the FSx for Windows file system.</td></tr>
<tr><td><code>password</code></td><td><code>string</code></td><td>The password of the user who has the permissions to access files and folders in the FSx for Windows file system.</td></tr>
<tr><td><code>security_group_arns</code></td><td><code>array</code></td><td>The ARNs of the security groups that are to use to configure the FSx for Windows file system.</td></tr>
<tr><td><code>subdirectory</code></td><td><code>string</code></td><td>A subdirectory in the location's path.</td></tr>
<tr><td><code>user</code></td><td><code>string</code></td><td>The user who has the permissions to access files and folders in the FSx for Windows file system.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>location_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon FSx for Windows file system location that is created.</td></tr>
<tr><td><code>location_uri</code></td><td><code>string</code></td><td>The URL of the FSx for Windows location that was described.</td></tr>
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
domain,
fsx_filesystem_arn,
password,
security_group_arns,
subdirectory,
user,
tags,
location_arn,
location_uri
FROM aws.datasync.locationf_sx_windows
WHERE data__Identifier = '<LocationArn>';
```

## Permissions

To operate on the <code>locationf_sx_windows</code> resource, the following permissions are required:

### Read
```json
datasync:DescribeLocationFsxWindows,
datasync:ListTagsForResource
```

### Update
```json
datasync:DescribeLocationFsxWindows,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource
```

### Delete
```json
datasync:DeleteLocation
```

