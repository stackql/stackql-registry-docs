---
title: stack_set_constraint
hide_title: false
hide_table_of_contents: false
keywords:
  - stack_set_constraint
  - servicecatalog
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>stack_set_constraint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stack_set_constraint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stack_set_constraint</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicecatalog.stack_set_constraint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_instance_control</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>accept_language</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>portfolio_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>product_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region_list</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>admin_role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>account_list</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>execution_role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
description,
stack_instance_control,
accept_language,
portfolio_id,
product_id,
region_list,
admin_role,
account_list,
execution_role
FROM aws.servicecatalog.stack_set_constraint
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
