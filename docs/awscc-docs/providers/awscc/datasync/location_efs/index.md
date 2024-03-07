---
title: location_efs
hide_title: false
hide_table_of_contents: false
keywords:
  - location_efs
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
Gets an individual <code>location_efs</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_efs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>location_efs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datasync.location_efs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ec2_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>efs_filesystem_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the Amazon EFS file system.</td></tr>
<tr><td><code>access_point_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the Amazon EFS Access point that DataSync uses when accessing the EFS file system.</td></tr>
<tr><td><code>file_system_access_role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AWS IAM role that the DataSync will assume when mounting the EFS file system.</td></tr>
<tr><td><code>in_transit_encryption</code></td><td><code>string</code></td><td>Protocol that is used for encrypting the traffic exchanged between the DataSync Agent and the EFS file system.</td></tr>
<tr><td><code>subdirectory</code></td><td><code>string</code></td><td>A subdirectory in the location's path. This subdirectory in the EFS file system is used to read data from the EFS source location or write data to the EFS destination.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>location_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.</td></tr>
<tr><td><code>location_uri</code></td><td><code>string</code></td><td>The URL of the EFS location that was described.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
ec2_config,
efs_filesystem_arn,
access_point_arn,
file_system_access_role_arn,
in_transit_encryption,
subdirectory,
tags,
location_arn,
location_uri
FROM awscc.datasync.location_efs
WHERE region = 'us-east-1'
AND data__Identifier = '{LocationArn}';
```

## Permissions

To operate on the <code>location_efs</code> resource, the following permissions are required:

### Read
```json
datasync:DescribeLocationEfs,
datasync:ListTagsForResource
```

### Update
```json
datasync:DescribeLocationEfs,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource
```

### Delete
```json
datasync:DeleteLocation
```

