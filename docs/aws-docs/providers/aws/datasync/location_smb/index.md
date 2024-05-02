---
title: location_smb
hide_title: false
hide_table_of_contents: false
keywords:
  - location_smb
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
Gets an individual <code>location_smb</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_smb</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationSMB.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.datasync.location_smb</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>agent_arns</code></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of agents to use for a Simple Message Block (SMB) location.</td></tr>
<tr><td><code>domain</code></td><td><code>string</code></td><td>The name of the Windows domain that the SMB server belongs to.</td></tr>
<tr><td><code>mount_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>password</code></td><td><code>string</code></td><td>The password of the user who can mount the share and has the permissions to access files and folders in the SMB share.</td></tr>
<tr><td><code>server_hostname</code></td><td><code>string</code></td><td>The name of the SMB server. This value is the IP address or Domain Name Service (DNS) name of the SMB server.</td></tr>
<tr><td><code>subdirectory</code></td><td><code>string</code></td><td>The subdirectory in the SMB file system that is used to read data from the SMB source location or write data to the SMB destination</td></tr>
<tr><td><code>user</code></td><td><code>string</code></td><td>The user who can mount the share, has the permissions to access files and folders in the SMB share.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>location_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the SMB location that is created.</td></tr>
<tr><td><code>location_uri</code></td><td><code>string</code></td><td>The URL of the SMB location that was described.</td></tr>
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
agent_arns,
domain,
mount_options,
password,
server_hostname,
subdirectory,
user,
tags,
location_arn,
location_uri
FROM aws.datasync.location_smb
WHERE data__Identifier = '<LocationArn>';
```

## Permissions

To operate on the <code>location_smb</code> resource, the following permissions are required:

### Read
```json
datasync:DescribeLocationSmb,
datasync:ListTagsForResource
```

### Update
```json
datasync:DescribeLocationSmb,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource,
datasync:UpdateLocationSmb
```

### Delete
```json
datasync:DeleteLocation
```

