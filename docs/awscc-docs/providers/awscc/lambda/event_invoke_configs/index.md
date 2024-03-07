---
title: event_invoke_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - event_invoke_configs
  - lambda
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>event_invoke_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_invoke_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_invoke_configs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lambda.event_invoke_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>function_name</code></td><td><code>string</code></td><td>The name of the Lambda function.</td></tr>
<tr><td><code>qualifier</code></td><td><code>string</code></td><td>The identifier of a version or alias.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>event_invoke_configs</code> resource, the following permissions are required:

### Create
<pre>
lambda:PutFunctionEventInvokeConfig</pre>

### List
<pre>
lambda:ListFunctionEventInvokeConfigs</pre>


## Example
```sql
SELECT
region,
function_name,
qualifier
FROM awscc.lambda.event_invoke_configs
WHERE region = 'us-east-1'
```
