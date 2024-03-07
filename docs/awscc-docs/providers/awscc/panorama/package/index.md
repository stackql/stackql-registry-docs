---
title: package
hide_title: false
hide_table_of_contents: false
keywords:
  - package
  - panorama
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>package</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>package</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>package</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.panorama.package</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>package_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>package_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>storage_location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
package_name,
package_id,
arn,
storage_location,
created_time,
tags
FROM awscc.panorama.package
WHERE region = 'us-east-1'
AND data__Identifier = '{PackageId}';
```

## Permissions

To operate on the <code>package</code> resource, the following permissions are required:

### Read
```json
panorama:DescribePackage,
panorama:ListTagsForResource,
s3:ListBucket,
s3:GetObject,
s3:GetObjectVersion
```

### Update
```json
panorama:DescribePackage,
panorama:ListTagsForResource,
panorama:TagResource,
panorama:UntagResource,
s3:PutObject,
s3:ListBucket,
s3:GetObject,
s3:GetObjectVersion
```

### Delete
```json
panorama:DeletePackage,
panorama:DescribePackage,
s3:DeleteObject,
s3:DeleteObjectVersion,
s3:DeleteObjectVersionTagging,
s3:ListObjects,
s3:ListObjectsV2,
s3:ListBucket,
s3:GetObject,
s3:GetObjectVersion
```

