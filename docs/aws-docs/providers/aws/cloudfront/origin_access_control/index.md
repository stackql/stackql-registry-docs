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
<tr><td><b>Id</b></td><td><code>aws.cloudfront.origin_access_control</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>origin_access_control_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
origin_access_control_config,
id
FROM aws.cloudfront.origin_access_control
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
