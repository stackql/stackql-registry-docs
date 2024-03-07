---
title: event_invoke_config
hide_title: false
hide_table_of_contents: false
keywords:
  - event_invoke_config
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
Gets an individual <code>event_invoke_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_invoke_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_invoke_config</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lambda.event_invoke_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>destination_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>function_name</code></td><td><code>string</code></td><td>The name of the Lambda function.</td></tr>
<tr><td><code>maximum_event_age_in_seconds</code></td><td><code>integer</code></td><td>The maximum age of a request that Lambda sends to a function for processing.</td></tr>
<tr><td><code>maximum_retry_attempts</code></td><td><code>integer</code></td><td>The maximum number of times to retry when the function returns an error.</td></tr>
<tr><td><code>qualifier</code></td><td><code>string</code></td><td>The identifier of a version or alias.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>event_invoke_config</code> resource, the following permissions are required:

### Read
<pre>
lambda:GetFunctionEventInvokeConfig</pre>

### Update
<pre>
lambda:UpdateFunctionEventInvokeConfig</pre>

### Delete
<pre>
lambda:DeleteFunctionEventInvokeConfig</pre>


## Example
```sql
SELECT
region,
destination_config,
function_name,
maximum_event_age_in_seconds,
maximum_retry_attempts,
qualifier
FROM awscc.lambda.event_invoke_config
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;FunctionName&gt;'
AND data__Identifier = '&lt;Qualifier&gt;'
```
