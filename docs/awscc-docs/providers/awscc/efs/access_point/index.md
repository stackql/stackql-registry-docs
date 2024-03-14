---
title: access_point
hide_title: false
hide_table_of_contents: false
keywords:
  - access_point
  - efs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>access_point</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_point</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_point</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.efs.access_point</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_point_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>client_token</code></td><td><code>string</code></td><td>The opaque string specified in the request to ensure idempotent creation.</td></tr>
<tr><td><code>access_point_tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.&lt;br&#x2F;&gt; For more information, see &#91;Tag&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-resource-tags.html).</td></tr>
<tr><td><code>file_system_id</code></td><td><code>string</code></td><td>The ID of the EFS file system that the access point applies to. Accepts only the ID format for input when specifying a file system, for example ``fs-0123456789abcedf2``.</td></tr>
<tr><td><code>posix_user</code></td><td><code>object</code></td><td>The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point.</td></tr>
<tr><td><code>root_directory</code></td><td><code>object</code></td><td>The directory on the EFS file system that the access point exposes as the root directory to NFS clients using the access point.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
access_point_id,
arn,
client_token,
access_point_tags,
file_system_id,
posix_user,
root_directory
FROM awscc.efs.access_point
WHERE data__Identifier = '<AccessPointId>';
```

## Permissions

To operate on the <code>access_point</code> resource, the following permissions are required:

### Read
```json
elasticfilesystem:DescribeAccessPoints
```

### Delete
```json
elasticfilesystem:DeleteAccessPoint,
elasticfilesystem:DescribeAccessPoints
```

### Update
```json
elasticfilesystem:DescribeAccessPoints,
elasticfilesystem:ListTagsForResource,
elasticfilesystem:TagResource,
elasticfilesystem:UntagResource
```

