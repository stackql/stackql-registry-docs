---
title: db_security_group
hide_title: false
hide_table_of_contents: false
keywords:
  - db_security_group
  - rds
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>db_security_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_security_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_security_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rds.db_security_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>d_bsecurity_group_ingress</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>e_c2_vpc_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>group_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
d_bsecurity_group_ingress,
e_c2_vpc_id,
group_description,
tags
FROM aws.rds.db_security_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
