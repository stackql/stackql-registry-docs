---
title: bucket_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_policy
  - s3
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>bucket_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bucket_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>bucket_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3.bucket_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>bucket</code></td><td><code>string</code></td><td>The name of the Amazon S3 bucket to which the policy applies.</td></tr>
<tr><td><code>policy_document</code></td><td><code>object</code></td><td>A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy &#91;PolicyDocument&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-iam-policy.html#cfn-iam-policy-policydocument) resource description in this guide and &#91;Access Policy Language Overview&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;access-policy-language-overview.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
bucket,
policy_document
FROM awscc.s3.bucket_policy
WHERE region = 'us-east-1'
AND data__Identifier = '{Bucket}';
```

## Permissions

To operate on the <code>bucket_policy</code> resource, the following permissions are required:

### Read
```json
s3:GetBucketPolicy
```

### Update
```json
s3:GetBucketPolicy,
s3:PutBucketPolicy
```

### Delete
```json
s3:GetBucketPolicy,
s3:DeleteBucketPolicy
```

