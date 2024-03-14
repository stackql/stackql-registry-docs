---
title: account
hide_title: false
hide_table_of_contents: false
keywords:
  - account
  - apigateway
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>account</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>account</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.account</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cloud_watch_role_arn</code></td><td><code>string</code></td><td>The ARN of an Amazon CloudWatch role for the current Account.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
cloud_watch_role_arn
FROM awscc.apigateway.account
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>account</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:PATCH,
iam:GetRole,
iam:PassRole
```

