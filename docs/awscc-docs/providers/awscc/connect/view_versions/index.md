---
title: view_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - view_versions
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
Retrieves a list of <code>view_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>view_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>view_versions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.view_versions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>view_version_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the created view version.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>view_versions</code> resource, the following permissions are required:

### Create
<pre>
connect:CreateViewVersion</pre>

### List
<pre>
connect:ListViewVersions</pre>


## Example
```sql
SELECT
region,
view_version_arn
FROM awscc.connect.view_versions
WHERE region = 'us-east-1'
```
