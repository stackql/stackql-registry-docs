---
title: location_nfs
hide_title: false
hide_table_of_contents: false
keywords:
  - location_nfs
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
Gets an individual <code>location_nfs</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_nfs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>location_nfs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datasync.location_nfs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>mount_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>on_prem_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>server_hostname</code></td><td><code>string</code></td><td>The name of the NFS server. This value is the IP address or DNS name of the NFS server.</td></tr>
<tr><td><code>subdirectory</code></td><td><code>string</code></td><td>The subdirectory in the NFS file system that is used to read data from the NFS source location or write data to the NFS destination.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>location_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the NFS location.</td></tr>
<tr><td><code>location_uri</code></td><td><code>string</code></td><td>The URL of the NFS location that was described.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
mount_options,
on_prem_config,
server_hostname,
subdirectory,
tags,
location_arn,
location_uri
FROM awscc.datasync.location_nfs
WHERE region = 'us-east-1'
AND data__Identifier = '{LocationArn}';
```

## Permissions

To operate on the <code>location_nfs</code> resource, the following permissions are required:

### Read
```json
datasync:DescribeLocationNfs,
datasync:ListTagsForResource
```

### Update
```json
datasync:DescribeLocationNfs,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource,
datasync:UpdateLocationNfs
```

### Delete
```json
datasync:DeleteLocation
```

