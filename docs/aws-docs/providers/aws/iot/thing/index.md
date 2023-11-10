---
title: thing
hide_title: false
hide_table_of_contents: false
keywords:
  - thing
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>thing</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>thing</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>thing</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.thing</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>attribute_payload</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>thing_name</code></td><td><code>string</code></td><td></td></tr>
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
attribute_payload,
thing_name
FROM aws.iot.thing
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ThingName&gt;'
```
