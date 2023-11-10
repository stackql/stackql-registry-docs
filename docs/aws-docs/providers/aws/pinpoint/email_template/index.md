---
title: email_template
hide_title: false
hide_table_of_contents: false
keywords:
  - email_template
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
Gets an individual <code>email_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>email_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>email_template</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pinpoint.email_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>html_part</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>text_part</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>template_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>template_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_substitutions</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subject</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
html_part,
text_part,
template_name,
template_description,
default_substitutions,
id,
arn,
subject,
tags
FROM aws.pinpoint.email_template
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
