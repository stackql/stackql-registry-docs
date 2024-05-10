---
title: bucket_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_policies
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


Used to retrieve a list of <code>bucket_policies</code> in a region or to create or delete a <code>bucket_policies</code> resource, use <code>bucket_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bucket_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Applies an Amazon S3 bucket policy to an Amazon S3 bucket. If you are using an identity other than the root user of the AWS-account that owns the bucket, the calling identity must have the ``PutBucketPolicy`` permissions on the specified bucket and belong to the bucket owner's account in order to use this operation.&lt;br&#x2F;&gt; If you don't have ``PutBucketPolicy`` permissions, Amazon S3 returns a ``403 Access Denied`` error. If you have the correct permissions, but you're not using an identity that belongs to the bucket owner's account, Amazon S3 returns a ``405 Method Not Allowed`` error.&lt;br&#x2F;&gt;   As a security precaution, the root user of the AWS-account that owns a bucket can always use this operation, even if the policy explicitly denies the root user the ability to perform this action. &lt;br&#x2F;&gt;  For more information, see &#91;Bucket policy examples&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;userguide&#x2F;example-bucket-policies.html).&lt;br&#x2F;&gt; The following operations are related to ``PutBucketPolicy``:&lt;br&#x2F;&gt;  +   &#91;CreateBucket&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;API&#x2F;API_CreateBucket.html) &lt;br&#x2F;&gt;  +   &#91;DeleteBucket&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;API&#x2F;API_DeleteBucket.html)</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.bucket_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="bucket" /></td><td><code>string</code></td><td>The name of the Amazon S3 bucket to which the policy applies.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
bucket
FROM aws.s3.bucket_policies
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>bucket_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- bucket_policy.iql (required properties only)
INSERT INTO aws.s3.bucket_policies (
 Bucket,
 PolicyDocument,
 region
)
SELECT 
'{{ Bucket }}',
 '{{ PolicyDocument }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- bucket_policy.iql (all properties)
INSERT INTO aws.s3.bucket_policies (
 Bucket,
 PolicyDocument,
 region
)
SELECT 
 '{{ Bucket }}',
 '{{ PolicyDocument }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: bucket_policy
    props:
      - name: Bucket
        value: '{{ Bucket }}'
      - name: PolicyDocument
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.s3.bucket_policies
WHERE data__Identifier = '<Bucket>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>bucket_policies</code> resource, the following permissions are required:

### Create
```json
s3:GetBucketPolicy,
s3:PutBucketPolicy
```

### List
```json
s3:GetBucketPolicy,
s3:ListAllMyBuckets
```

### Delete
```json
s3:GetBucketPolicy,
s3:DeleteBucketPolicy
```

