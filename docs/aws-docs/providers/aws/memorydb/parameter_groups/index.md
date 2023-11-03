---
title: parameter_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - parameter_groups
  - memorydb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>parameter_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>parameter_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.memorydb.parameter_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ParameterGroupName</code></td><td><code>string</code></td><td>The name of the parameter group.</td></tr><tr><td><code>Family</code></td><td><code>string</code></td><td>The name of the parameter group family that this parameter group is compatible with.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>A description of the parameter group.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this parameter group.</td></tr><tr><td><code>Parameters</code></td><td><code>object</code></td><td>An map of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional.</td></tr><tr><td><code>ARN</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the parameter group.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.memorydb.parameter_groups
WHERE region = 'us-east-1'
```
