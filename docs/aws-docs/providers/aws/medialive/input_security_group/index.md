---
title: input_security_group
hide_title: false
hide_table_of_contents: false
keywords:
  - input_security_group
  - medialive
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>input_security_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>input_security_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>input_security_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.medialive.input_security_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>whitelist_rules</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
arn,
whitelist_rules,
tags
FROM aws.medialive.input_security_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
