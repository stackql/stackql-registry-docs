---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
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

Used to retrieve a list of <code>permissions</code> in a region or create a <code>permissions</code> resource, use <code>permission</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::Lambda::Permission`` resource grants an AWS service or another account permission to use a function. You can apply the policy at the function level, or specify a qualifier to restrict access to a single version or alias. If you use a qualifier, the invoker must use the full Amazon Resource Name (ARN) of that version or alias to invoke the function.&lt;br&#x2F;&gt; To grant permission to another account, specify the account ID as the ``Principal``. To grant permission to an organization defined in AOlong, specify the organization ID as the ``PrincipalOrgID``. For AWS services, the principal is a domain-style identifier defined by the service, like ``s3.amazonaws.com`` or ``sns.amazonaws.com``. For AWS services, you can also specify the ARN of the associated resource as the ``SourceArn``. If you grant permission to a service principal without specifying the source, other accounts could potentially configure resources in their account to invoke your Lambda function.&lt;br&#x2F;&gt; If your function has a fu</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.permissions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="function_name" /></td><td><code>string</code></td><td>The name of the Lambda function, version, or alias.&lt;br&#x2F;&gt;  **Name formats**&lt;br&#x2F;&gt; +   *Function name* – ``my-function`` (name-only), ``my-function:v1`` (with alias).&lt;br&#x2F;&gt;  +   *Function ARN* – ``arn:aws:lambda:us-west-2:123456789012:function:my-function``.&lt;br&#x2F;&gt;  +   *Partial ARN* – ``123456789012:function:my-function``.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
function_name,
id
FROM aws.lambda.permissions
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>permissions</code> resource, the following permissions are required:

### Create
```json
lambda:AddPermission
```

### List
```json
lambda:GetPolicy
```

