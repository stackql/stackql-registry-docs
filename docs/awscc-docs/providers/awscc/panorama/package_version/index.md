---
title: package_version
hide_title: false
hide_table_of_contents: false
keywords:
  - package_version
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
Gets an individual <code>package_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>package_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>package_version</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.panorama.package_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>owner_account</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>package_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>package_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>package_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>patch_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>mark_latest</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>is_latest_patch</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>package_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>registered_time</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>updated_latest_patch_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
owner_account,
package_id,
package_arn,
package_version,
patch_version,
mark_latest,
is_latest_patch,
package_name,
status,
status_description,
registered_time,
updated_latest_patch_version
FROM awscc.panorama.package_version
WHERE region = 'us-east-1'
AND data__Identifier = '{PackageId}';
AND data__Identifier = '{PackageVersion}';
AND data__Identifier = '{PatchVersion}';
```

## Permissions

To operate on the <code>package_version</code> resource, the following permissions are required:

### Read
```json
panorama:DescribePackageVersion,
s3:ListBucket,
s3:GetObject,
s3:GetObjectVersion
```

### Update
```json
panorama:DescribePackageVersion,
panorama:RegisterPackageVersion,
s3:ListBucket,
s3:PutObject,
s3:GetObject,
s3:GetObjectVersion
```

### Delete
```json
panorama:DeregisterPackageVersion,
panorama:DescribePackageVersion,
s3:DeleteObject,
s3:DeleteObjectVersion,
s3:DeleteObjectVersionTagging,
s3:ListBucket,
s3:GetObject,
s3:GetObjectVersion
```

