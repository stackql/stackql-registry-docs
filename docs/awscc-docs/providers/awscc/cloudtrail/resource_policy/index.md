---
title: resource_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policy
  - cloudtrail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>resource_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudtrail.resource_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td>The ARN of the AWS CloudTrail resource to which the policy applies.</td></tr>
<tr><td><code>resource_policy</code></td><td><code>object</code></td><td>A policy document containing permissions to add to the specified resource. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
resource_arn,
resource_policy
FROM awscc.cloudtrail.resource_policy
WHERE data__Identifier = '<ResourceArn>';
```

## Permissions

To operate on the <code>resource_policy</code> resource, the following permissions are required:

### Read
```json
CloudTrail:GetResourcePolicy
```

### Update
```json
CloudTrail:PutResourcePolicy,
CloudTrail:GetResourcePolicy
```

### Delete
```json
CloudTrail:DeleteResourcePolicy
```

