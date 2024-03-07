---
title: permission
hide_title: false
hide_table_of_contents: false
keywords:
  - permission
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
Gets an individual <code>permission</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>permission</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lambda.permission</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>action</code></td><td><code>string</code></td><td>The action that the principal can use on the function. For example, ``lambda:InvokeFunction`` or ``lambda:GetFunction``.</td></tr>
<tr><td><code>event_source_token</code></td><td><code>string</code></td><td>For Alexa Smart Home functions, a token that the invoker must supply.</td></tr>
<tr><td><code>function_name</code></td><td><code>string</code></td><td>The name of the Lambda function, version, or alias.&lt;br&#x2F;&gt;  **Name formats**&lt;br&#x2F;&gt; +   *Function name* – ``my-function`` (name-only), ``my-function:v1`` (with alias).&lt;br&#x2F;&gt;  +   *Function ARN* – ``arn:aws:lambda:us-west-2:123456789012:function:my-function``.&lt;br&#x2F;&gt;  +   *Partial ARN* – ``123456789012:function:my-function``.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</td></tr>
<tr><td><code>function_url_auth_type</code></td><td><code>string</code></td><td>The type of authentication that your function URL uses. Set to ``AWS_IAM`` if you want to restrict access to authenticated users only. Set to ``NONE`` if you want to bypass IAM authentication to create a public endpoint. For more information, see &#91;Security and auth model for Lambda function URLs&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;urls-auth.html).</td></tr>
<tr><td><code>principal</code></td><td><code>string</code></td><td>The AWS-service or AWS-account that invokes the function. If you specify a service, use ``SourceArn`` or ``SourceAccount`` to limit who can invoke the function through that service.</td></tr>
<tr><td><code>principal_org_id</code></td><td><code>string</code></td><td>The identifier for your organization in AOlong. Use this to grant permissions to all the AWS-accounts under this organization.</td></tr>
<tr><td><code>source_account</code></td><td><code>string</code></td><td>For AWS-service, the ID of the AWS-account that owns the resource. Use this together with ``SourceArn`` to ensure that the specified account owns the resource. It is possible for an Amazon S3 bucket to be deleted by its owner and recreated by another account.</td></tr>
<tr><td><code>source_arn</code></td><td><code>string</code></td><td>For AWS-services, the ARN of the AWS resource that invokes the function. For example, an Amazon S3 bucket or Amazon SNS topic.&lt;br&#x2F;&gt; Note that Lambda configures the comparison using the ``StringLike`` operator.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>permission</code> resource, the following permissions are required:

### Read
```json
lambda:GetPolicy
```

### Delete
```json
lambda:RemovePermission
```


## Example
```sql
SELECT
region,
id,
action,
event_source_token,
function_name,
function_url_auth_type,
principal,
principal_org_id,
source_account,
source_arn
FROM awscc.lambda.permission
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;FunctionName&gt;'
AND data__Identifier = '&lt;Id&gt;'
```
