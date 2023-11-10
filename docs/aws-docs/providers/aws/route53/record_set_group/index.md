---
title: record_set_group
hide_title: false
hide_table_of_contents: false
keywords:
  - record_set_group
  - route53
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>record_set_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>record_set_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>record_set_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53.record_set_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>comment</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>hosted_zone_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>record_sets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>hosted_zone_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
comment,
id,
hosted_zone_name,
record_sets,
hosted_zone_id
FROM aws.route53.record_set_group
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
