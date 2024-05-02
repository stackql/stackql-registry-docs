---
title: view_version
hide_title: false
hide_table_of_contents: false
keywords:
  - view_version
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>view_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>view_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::ViewVersion</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connect.view_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>view_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the view for which a version is being created.</td></tr>
<tr><td><code>view_version_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the created view version.</td></tr>
<tr><td><code>version_description</code></td><td><code>string</code></td><td>The description for the view version.</td></tr>
<tr><td><code>view_content_sha256</code></td><td><code>string</code></td><td>The view content hash to be checked.</td></tr>
<tr><td><code>version</code></td><td><code>integer</code></td><td>The version of the view.</td></tr>
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
view_arn,
view_version_arn,
version_description,
view_content_sha256,
version
FROM aws.connect.view_version
WHERE data__Identifier = '<ViewVersionArn>';
```

## Permissions

To operate on the <code>view_version</code> resource, the following permissions are required:

### Read
```json
connect:DescribeView
```

### Delete
```json
connect:DeleteViewVersion
```

