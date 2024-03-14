---
title: locationf_sx_ontap
hide_title: false
hide_table_of_contents: false
keywords:
  - locationf_sx_ontap
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
Gets an individual <code>locationf_sx_ontap</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locationf_sx_ontap</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>locationf_sx_ontap</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datasync.locationf_sx_ontap</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>storage_virtual_machine_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the FSx ONTAP SVM.</td></tr>
<tr><td><code>fsx_filesystem_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the FSx ONAP file system.</td></tr>
<tr><td><code>security_group_arns</code></td><td><code>array</code></td><td>The ARNs of the security groups that are to use to configure the FSx ONTAP file system.</td></tr>
<tr><td><code>protocol</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>subdirectory</code></td><td><code>string</code></td><td>A subdirectory in the location's path.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>location_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon FSx ONTAP file system location that is created.</td></tr>
<tr><td><code>location_uri</code></td><td><code>string</code></td><td>The URL of the FSx ONTAP file system that was described.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
storage_virtual_machine_arn,
fsx_filesystem_arn,
security_group_arns,
protocol,
subdirectory,
tags,
location_arn,
location_uri
FROM awscc.datasync.locationf_sx_ontap
WHERE data__Identifier = '<LocationArn>';
```

## Permissions

To operate on the <code>locationf_sx_ontap</code> resource, the following permissions are required:

### Read
```json
datasync:DescribeLocationFsxOntap,
datasync:ListTagsForResource
```

### Update
```json
datasync:DescribeLocationFsxOntap,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource
```

### Delete
```json
datasync:DeleteLocation
```

