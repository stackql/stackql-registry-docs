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
<tr><td><b>Description</b></td><td>The AWS::Lambda::EventInvokeConfig resource configures options for asynchronous invocation on a version or an alias.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lambda.event_invoke_config</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
destination_config,
function_name,
maximum_event_age_in_seconds,
maximum_retry_attempts,
qualifier
FROM aws.lambda.event_invoke_config
WHERE data__Identifier = '<FunctionName>|<Qualifier>';
```

## Permissions

To operate on the <code>event_invoke_config</code> resource, the following permissions are required:

### Read
```json
lambda:GetFunctionEventInvokeConfig
```

### Update
```json
lambda:UpdateFunctionEventInvokeConfig
```

### Delete
```json
lambda:DeleteFunctionEventInvokeConfig
```

