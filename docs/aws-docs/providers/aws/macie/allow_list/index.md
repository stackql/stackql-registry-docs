---
title: allow_list
hide_title: false
hide_table_of_contents: false
keywords:
  - allow_list
  - macie
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>allow_list</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>allow_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>allow_list</td></tr>
<tr><td><b>Id</b></td><td><code>aws.macie.allow_list</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of AllowList.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of AllowList.</td></tr>
<tr><td><code>criteria</code></td><td><code>object</code></td><td>AllowList criteria.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>AllowList ID.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>AllowList ARN.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>AllowList status.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
description,
criteria,
id,
arn,
status,
tags
FROM aws.macie.allow_list
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
