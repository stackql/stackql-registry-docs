---
title: functions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - functions_list_only
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

Lists <code>functions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/functions/"><code>functions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::Lambda::Function</code> resource creates a Lambda function. To create a function, you need a &#91;deployment package&#93;(https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html) and an &#91;execution role&#93;(https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html). The deployment package is a .zip file archive or container image that contains your function code. The execution role grants the function permission to use AWS services, such as Amazon CloudWatch Logs for log streaming and AWS X-Ray for request tracing.<br />You set the package type to <code>Image</code> if the deployment package is a &#91;container image&#93;(https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html). For these functions, include the URI of the container image in the ECR registry in the &#91;ImageUri property of the Code property&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-imageuri). You do not need to specify the handler and runtime properties. <br />You set the package type to <code>Zip</code> if the deployment package is a &#91;.zip file archive&#93;(https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html#gettingstarted-package-zip). For these functions, specify the S3 location of your .zip file in the <code>Code</code> property. Alternatively, for Node.js and Python functions, you can define your function inline in the &#91;ZipFile property of the Code property&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-zipfile). In both cases, you must also specify the handler and runtime properties.<br />You can use &#91;code signing&#93;(https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html) if your deployment package is a .zip file archive. To enable code signing for this function, specify the ARN of a code-signing configuration. When a user attempts to deploy a code package with <code>UpdateFunctionCode</code>, Lambda checks that the code package has a valid signature from a trusted publisher. The code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.<br />When you update a <code>AWS::Lambda::Function</code> resource, CFNshort calls the &#91;UpdateFunctionConfiguration&#93;(https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionConfiguration.html) and &#91;UpdateFunctionCode&#93;(https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionCode.html) LAM APIs under the hood. Because these calls happen sequentially, and invocations can happen between these calls, your function may encounter errors in the time between the calls. For example, if you remove an environment variable, and the code that references that environment variable in the same CFNshort update, you may see invocation errors related to a missing environment variable. To work around this, you can invoke your function against a version or alias by default, rather than the <code>$LATEST</code> version.<br />Note that you configure &#91;provisioned concurrency&#93;(https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) on a <code>AWS::Lambda::Version</code> or a <code>AWS::Lambda::Alias</code>.<br />For a complete introduction to Lambda functions, see &#91;What is Lambda?&#93;(https://docs.aws.amazon.com/lambda/latest/dg/lambda-welcome.html) in the *Lambda developer guide.*</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.functions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="function_name" /></td><td><code>string</code></td><td>The name of the Lambda function, up to 64 characters in length. If you don't specify a name, CFN generates one.<br />If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
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
Lists all <code>functions</code> in a region.
```sql
SELECT
region,
function_name
FROM aws.lambda.functions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>functions_list_only</code> resource, see <a href="/providers/aws/lambda/functions/#permissions"><code>functions</code></a>

