---
title: configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration
  - amazonmq
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configuration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.amazonmq.configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>revision</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>authentication_strategy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
engine_version,
description,
revision,
authentication_strategy,
engine_type,
data,
id,
arn,
tags,
name
FROM aws.amazonmq.configuration
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
