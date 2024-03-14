---
title: view
hide_title: false
hide_table_of_contents: false
keywords:
  - view
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
Gets an individual <code>view</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>view</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>view</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.view</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the instance.</td></tr>
<tr><td><code>view_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the view.</td></tr>
<tr><td><code>view_id</code></td><td><code>string</code></td><td>The view id of the view.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the view.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the view.</td></tr>
<tr><td><code>template</code></td><td><code>object</code></td><td>The template of the view as JSON.</td></tr>
<tr><td><code>actions</code></td><td><code>array</code></td><td>The actions of the view in an array.</td></tr>
<tr><td><code>view_content_sha256</code></td><td><code>string</code></td><td>The view content hash.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
instance_arn,
view_arn,
view_id,
name,
description,
template,
actions,
view_content_sha256,
tags
FROM awscc.connect.view
WHERE data__Identifier = '<ViewArn>';
```

## Permissions

To operate on the <code>view</code> resource, the following permissions are required:

### Read
```json
connect:DescribeView
```

### Delete
```json
connect:DeleteView,
connect:UntagResource
```

### Update
```json
connect:UpdateViewMetadata,
connect:UpdateViewContent,
connect:TagResource,
connect:UntagResource
```

