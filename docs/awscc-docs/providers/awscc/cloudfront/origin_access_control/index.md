---
title: origin_access_control
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_access_control
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>origin_access_control</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_access_control</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>origin_access_control</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudfront.origin_access_control</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>origin_access_control_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>origin_access_control</code> resource, the following permissions are required:

### Delete
<pre>
cloudfront:DeleteOriginAccessControl,
cloudfront:GetOriginAccessControl</pre>

### Read
<pre>
cloudfront:GetOriginAccessControl</pre>

### Update
<pre>
cloudfront:UpdateOriginAccessControl,
cloudfront:GetOriginAccessControl</pre>


## Example
```sql
SELECT
region,
id,
origin_access_control_config
FROM awscc.cloudfront.origin_access_control
WHERE data__Identifier = '&lt;Id&gt;'
```