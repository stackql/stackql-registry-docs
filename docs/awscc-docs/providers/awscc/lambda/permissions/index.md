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
Retrieves a list of <code>permissions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>permissions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lambda.permissions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>function_name</code></td><td><code>string</code></td><td>The name of the Lambda function, version, or alias.&lt;br&#x2F;&gt;  **Name formats**&lt;br&#x2F;&gt; +   *Function name* – ``my-function`` (name-only), ``my-function:v1`` (with alias).&lt;br&#x2F;&gt;  +   *Function ARN* – ``arn:aws:lambda:us-west-2:123456789012:function:my-function``.&lt;br&#x2F;&gt;  +   *Partial ARN* – ``123456789012:function:my-function``.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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


## Example
```sql
SELECT
region,
function_name,
id
FROM awscc.lambda.permissions
WHERE region = 'us-east-1'
```
