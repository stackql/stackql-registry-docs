---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
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
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appstream.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>launch_path</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>launch_parameters</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>working_directory</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_families</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>icon_s3_location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>app_block_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>platforms</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>attributes_to_delete</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
<pre>
appstream:DescribeApplications</pre>

### Update
<pre>
appstream:UpdateApplication,
s3:GetObject</pre>

### Delete
<pre>
appstream:DeleteApplication</pre>


## Example
```sql
SELECT
region,
name,
display_name,
description,
launch_path,
launch_parameters,
working_directory,
instance_families,
icon_s3_location,
arn,
app_block_arn,
platforms,
tags,
attributes_to_delete,
created_time
FROM awscc.appstream.application
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
