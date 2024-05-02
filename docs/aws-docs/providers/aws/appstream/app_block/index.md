---
title: app_block
hide_title: false
hide_table_of_contents: false
keywords:
  - app_block
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>app_block</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_block</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::AppBlock</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appstream.app_block</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_s3_location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>setup_script_details</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>packaging_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>post_setup_script_details</code></td><td><code>object</code></td><td></td></tr>
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
name,
arn,
description,
display_name,
source_s3_location,
setup_script_details,
tags,
created_time,
packaging_type,
post_setup_script_details
FROM aws.appstream.app_block
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>app_block</code> resource, the following permissions are required:

### Read
```json
appstream:DescribeAppBlocks
```

### Delete
```json
appstream:DeleteAppBlock
```

