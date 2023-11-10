---
title: db_parameter_group
hide_title: false
hide_table_of_contents: false
keywords:
  - db_parameter_group
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
Gets an individual <code>db_parameter_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_parameter_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_parameter_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rds.db_parameter_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>d_bparameter_group_name</code></td><td><code>string</code></td><td>Specifies the name of the DB parameter group</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Provides the customer-specified description for this DB parameter group.</td></tr>
<tr><td><code>family</code></td><td><code>string</code></td><td>The DB parameter group family name.</td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td>An array of parameter names and values for the parameter update.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
d_bparameter_group_name,
description,
family,
parameters,
tags
FROM aws.rds.db_parameter_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DBParameterGroupName&gt;'
```
