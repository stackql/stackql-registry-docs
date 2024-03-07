---
title: url
hide_title: false
hide_table_of_contents: false
keywords:
  - url
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
Gets an individual <code>url</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>url</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>url</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lambda.url</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>target_function_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the function associated with the Function URL.</td></tr>
<tr><td><code>qualifier</code></td><td><code>string</code></td><td>The alias qualifier for the target function. If TargetFunctionArn is unqualified then Qualifier must be passed.</td></tr>
<tr><td><code>auth_type</code></td><td><code>string</code></td><td>Can be either AWS_IAM if the requests are authorized via IAM, or NONE if no authorization is configured on the Function URL.</td></tr>
<tr><td><code>invoke_mode</code></td><td><code>string</code></td><td>The invocation mode for the function’s URL. Set to BUFFERED if you want to buffer responses before returning them to the client. Set to RESPONSE_STREAM if you want to stream responses, allowing faster time to first byte and larger response payload sizes. If not set, defaults to BUFFERED.</td></tr>
<tr><td><code>function_arn</code></td><td><code>string</code></td><td>The full Amazon Resource Name (ARN) of the function associated with the Function URL.</td></tr>
<tr><td><code>function_url</code></td><td><code>string</code></td><td>The generated url for this resource.</td></tr>
<tr><td><code>cors</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
target_function_arn,
qualifier,
auth_type,
invoke_mode,
function_arn,
function_url,
cors
FROM awscc.lambda.url
WHERE region = 'us-east-1'
AND data__Identifier = '{FunctionArn}';
```

## Permissions

To operate on the <code>url</code> resource, the following permissions are required:

### Read
```json
lambda:GetFunctionUrlConfig
```

### Update
```json
lambda:UpdateFunctionUrlConfig
```

### Delete
```json
lambda:DeleteFunctionUrlConfig
```

