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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>url</code> resource, use <code>urls</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>url</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::Url</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.url" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="target_function_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the function associated with the Function URL.</td></tr>
<tr><td><CopyableCode code="qualifier" /></td><td><code>string</code></td><td>The alias qualifier for the target function. If TargetFunctionArn is unqualified then Qualifier must be passed.</td></tr>
<tr><td><CopyableCode code="auth_type" /></td><td><code>string</code></td><td>Can be either AWS_IAM if the requests are authorized via IAM, or NONE if no authorization is configured on the Function URL.</td></tr>
<tr><td><CopyableCode code="invoke_mode" /></td><td><code>string</code></td><td>The invocation mode for the function's URL. Set to BUFFERED if you want to buffer responses before returning them to the client. Set to RESPONSE_STREAM if you want to stream responses, allowing faster time to first byte and larger response payload sizes. If not set, defaults to BUFFERED.</td></tr>
<tr><td><CopyableCode code="function_arn" /></td><td><code>string</code></td><td>The full Amazon Resource Name (ARN) of the function associated with the Function URL.</td></tr>
<tr><td><CopyableCode code="function_url" /></td><td><code>string</code></td><td>The generated url for this resource.</td></tr>
<tr><td><CopyableCode code="cors" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.lambda.url
WHERE region = 'us-east-1' AND data__Identifier = '<FunctionArn>';
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

