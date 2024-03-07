---
title: software_package_version
hide_title: false
hide_table_of_contents: false
keywords:
  - software_package_version
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>software_package_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>software_package_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>software_package_version</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.software_package_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>error_reason</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>package_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>package_version_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>version_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
attributes,
description,
error_reason,
package_name,
package_version_arn,
status,
tags,
version_name
FROM awscc.iot.software_package_version
WHERE region = 'us-east-1'
AND data__Identifier = '{PackageName}';
AND data__Identifier = '{VersionName}';
```

## Permissions

To operate on the <code>software_package_version</code> resource, the following permissions are required:

### Read
```json
iot:GetPackageVersion,
iot:ListTagsForResource
```

### Update
```json
iot:UpdatePackageVersion,
iot:GetPackageVersion,
iot:ListTagsForResource,
iot:TagResource,
iot:UntagResource,
iot:GetIndexingConfiguration
```

### Delete
```json
iot:DeletePackageVersion,
iot:UpdatePackageVersion,
iot:GetPackageVersion,
iot:GetIndexingConfiguration
```

