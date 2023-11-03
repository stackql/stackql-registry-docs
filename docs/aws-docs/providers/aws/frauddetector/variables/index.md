---
title: variables
hide_title: false
hide_table_of_contents: false
keywords:
  - variables
  - frauddetector
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>variables</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>variables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.frauddetector.variables</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the variable.</td></tr><tr><td><code>DataSource</code></td><td><code>string</code></td><td>The source of the data.</td></tr><tr><td><code>DataType</code></td><td><code>string</code></td><td>The data type.</td></tr><tr><td><code>DefaultValue</code></td><td><code>string</code></td><td>The default value for the variable when no value is received.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>The description.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>Tags associated with this variable.</td></tr><tr><td><code>VariableType</code></td><td><code>string</code></td><td>The variable type. For more information see https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the variable.</td></tr><tr><td><code>CreatedTime</code></td><td><code>string</code></td><td>The time when the variable was created.</td></tr><tr><td><code>LastUpdatedTime</code></td><td><code>string</code></td><td>The time when the variable was last updated.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.frauddetector.variables
WHERE region = 'us-east-1'
```
