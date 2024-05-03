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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>package_version</code> resource, use <code>package_versions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>package_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for PackageVersion Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.panorama.package_version" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="owner_account" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="package_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="package_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="package_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="patch_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="mark_latest" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="is_latest_patch" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="package_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="registered_time" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_latest_patch_version" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
FROM aws.panorama.package_version
WHERE data__Identifier = '<PackageId>|<PackageVersion>|<PatchVersion>';
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

