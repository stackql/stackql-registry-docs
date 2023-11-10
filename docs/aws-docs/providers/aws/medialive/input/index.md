---
title: input
hide_title: false
hide_table_of_contents: false
keywords:
  - input
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
Gets an individual <code>input</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>input</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>input</td></tr>
<tr><td><b>Id</b></td><td><code>aws.medialive.input</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>destinations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>vpc</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>media_connect_flows</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>input_security_groups</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>sources</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>input_devices</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
type,
destinations,
vpc,
media_connect_flows,
id,
arn,
input_security_groups,
sources,
input_devices,
role_arn,
tags,
name
FROM aws.medialive.input
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
