---
title: account_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - account_policy
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
Gets an individual <code>account_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>account_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.logs.account_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td>User account id</td></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td>The name of the account policy</td></tr>
<tr><td><code>policy_document</code></td><td><code>string</code></td><td>The body of the policy document you want to use for this topic.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;You can only add one policy per PolicyType.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;The policy must be in JSON string format.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Length Constraints: Maximum length of 30720</td></tr>
<tr><td><code>policy_type</code></td><td><code>string</code></td><td>Type of the policy.</td></tr>
<tr><td><code>scope</code></td><td><code>string</code></td><td>Scope for policy application</td></tr>
<tr><td><code>selection_criteria</code></td><td><code>string</code></td><td>Log group  selection criteria to apply policy only to a subset of log groups. SelectionCriteria string can be up to 25KB and cloudwatchlogs determines the length of selectionCriteria by using its UTF-8 bytes</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
account_id,
policy_name,
policy_document,
policy_type,
scope,
selection_criteria
FROM awscc.logs.account_policy
WHERE data__Identifier = '<AccountId>|<PolicyType>|<PolicyName>';
```

## Permissions

To operate on the <code>account_policy</code> resource, the following permissions are required:

### Read
```json
logs:DescribeAccountPolicies
```

### Update
```json
logs:PutAccountPolicy,
logs:PutDataProtectionPolicy,
logs:DescribeAccountPolicies,
logs:DeleteAccountPolicy,
logs:DeleteDataProtectionPolicy,
logs:CreateLogDelivery,
logs:PutSubscriptionFilter,
logs:DeleteSubscriptionFilter,
s3:REST.PUT.OBJECT,
firehose:TagDeliveryStream,
iam:PassRole
```

### Delete
```json
logs:DeleteAccountPolicy,
logs:DeleteDataProtectionPolicy,
logs:DescribeAccountPolicies,
logs:DeleteSubscriptionFilter,
iam:PassRole
```

