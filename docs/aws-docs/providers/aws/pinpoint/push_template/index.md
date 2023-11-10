---
title: push_template
hide_title: false
hide_table_of_contents: false
keywords:
  - push_template
  - pinpoint
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>push_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>push_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>push_template</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pinpoint.push_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>g_cm</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>baidu</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>template_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>a_dm</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>a_pn_s</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>template_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_substitutions</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
g_cm,
baidu,
template_name,
a_dm,
a_pn_s,
template_description,
default_substitutions,
id,
arn,
default,
tags
FROM aws.pinpoint.push_template
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
