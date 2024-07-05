---
title: urls_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - urls_list_only
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

Lists <code>urls</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/urls/"><code>urls</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>urls_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::Url</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.urls_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="target_function_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the function associated with the Function URL.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>urls</code> in a region.
```sql
SELECT
region,
function_arn
FROM aws.lambda.urls_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>urls_list_only</code> resource, see <a href="/providers/aws/lambda/urls/#permissions"><code>urls</code></a>


