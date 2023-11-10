---
title: listener
hide_title: false
hide_table_of_contents: false
keywords:
  - listener
  - vpclattice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>listener</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listener</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>listener</td></tr>
<tr><td><b>Id</b></td><td><code>aws.vpclattice.listener</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_action</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>protocol</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
default_action,
id,
name,
port,
protocol,
service_arn,
service_id,
service_identifier,
tags
FROM aws.vpclattice.listener
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
