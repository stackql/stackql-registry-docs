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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>bucket_policy</code> resource, use <code>bucket_policies</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bucket_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Applies an Amazon S3 bucket policy to an Amazon S3 bucket. If you are using an identity other than the root user of the AWS-account that owns the bucket, the calling identity must have the <code>PutBucketPolicy</code> permissions on the specified bucket and belong to the bucket owner's account in order to use this operation.&lt;br&#x2F;&gt; If you don't have <code>PutBucketPolicy</code> permissions, Amazon S3 returns a <code>403 Access Denied</code> error. If you have the correct permissions, but you're not using an identity that belongs to the bucket owner's account, Amazon S3 returns a <code>405 Method Not Allowed</code> error.&lt;br&#x2F;&gt;   As a security precaution, the root user of the AWS-account that owns a bucket can always use this operation, even if the policy explicitly denies the root user the ability to perform this action. &lt;br&#x2F;&gt;  For more information, see &#91;Bucket policy examples&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;userguide&#x2F;example-bucket-policies.html).&lt;br&#x2F;&gt; The following operations are related to <code>PutBucketPolicy</code>:&lt;br&#x2F;&gt;  +   &#91;CreateBucket&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;API&#x2F;API_CreateBucket.html) &lt;br&#x2F;&gt;  +   &#91;DeleteBucket&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;API&#x2F;API_DeleteBucket.html)</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.bucket_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="bucket" /></td><td><code>string</code></td><td>The name of the Amazon S3 bucket to which the policy applies.</td></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>object</code></td><td>A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy &#91;PolicyDocument&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-iam-policy.html#cfn-iam-policy-policydocument) resource description in this guide and &#91;Access Policy Language Overview&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;access-policy-language-overview.html) in the *Amazon S3 User Guide*.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
bucket,
policy_document
FROM aws.s3.bucket_policy
WHERE region = 'us-east-1' AND data__Identifier = '<Bucket>';
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

