---
title: account_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - account_policies
  - logs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>account_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>account_policies</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.logs.account_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td>User account id</td></tr>
<tr><td><code>policy_type</code></td><td><code>string</code></td><td>Type of the policy.</td></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td>The name of the account policy</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
account_id,
policy_type,
policy_name
FROM awscc.logs.account_policies
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>account_policies</code> resource, the following permissions are required:

### Create
```json
logs:PutAccountPolicy,
logs:PutDataProtectionPolicy,
logs:DescribeAccountPolicies,
logs:CreateLogDelivery,
s3:REST.PUT.OBJECT,
firehose:TagDeliveryStream,
logs:PutSubscriptionFilter,
logs:DeleteSubscriptionFilter,
iam:PassRole
```

### List
```json
logs:DescribeAccountPolicies
```

