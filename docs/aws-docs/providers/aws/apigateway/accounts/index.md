---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
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
Retrieves a list of <code>accounts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::Account`` resource specifies the IAM role that Amazon API Gateway uses to write API logs to Amazon CloudWatch Logs. To avoid overwriting other roles, you should only have one ``AWS::ApiGateway::Account`` resource per region per account.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigateway.accounts</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.apigateway.accounts
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>accounts</code> resource, the following permissions are required:

### Create
```json
apigateway:PATCH,
iam:GetRole,
iam:PassRole
```

