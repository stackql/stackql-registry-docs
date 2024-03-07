---
title: response_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - response_plans
  - ssmincidents
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>response_plans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>response_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>response_plans</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ssmincidents.response_plans</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the response plan.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>response_plans</code> resource, the following permissions are required:

### Create
<pre>
ssm-incidents:CreateResponsePlan,
ssm-incidents:GetResponsePlan,
ssm-incidents:TagResource,
ssm-incidents:ListTagsForResource,
iam:PassRole,
secretsmanager:GetSecretValue,
kms:Decrypt,
kms:GenerateDataKey*</pre>

### List
<pre>
ssm-incidents:ListResponsePlans</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.ssmincidents.response_plans
WHERE region = 'us-east-1'
```
