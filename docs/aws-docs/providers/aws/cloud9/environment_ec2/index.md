---
title: environment_ec2
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_ec2
  - cloud9
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>environment_ec2</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_ec2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environment_ec2</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloud9.environment_ec2</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>repositories</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>owner_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>connection_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>automatic_stop_time_minutes</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>image_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_type</code></td><td><code>string</code></td><td></td></tr>
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
repositories,
owner_arn,
description,
connection_type,
automatic_stop_time_minutes,
image_id,
subnet_id,
id,
arn,
instance_type,
tags,
name
FROM aws.cloud9.environment_ec2
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
