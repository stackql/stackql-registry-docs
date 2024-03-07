---
title: drt_access
hide_title: false
hide_table_of_contents: false
keywords:
  - drt_access
  - shield
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>drt_access</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>drt_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>drt_access</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.shield.drt_access</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>log_bucket_list</code></td><td><code>array</code></td><td>Authorizes the Shield Response Team (SRT) to access the specified Amazon S3 bucket containing log data such as Application Load Balancer access logs, CloudFront logs, or logs from third party sources. You can associate up to 10 Amazon S3 buckets with your subscription.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>Authorizes the Shield Response Team (SRT) using the specified role, to access your AWS account to assist with DDoS attack mitigation during potential attacks. This enables the SRT to inspect your AWS WAF configuration and create or update AWS WAF rules and web ACLs.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>drt_access</code> resource, the following permissions are required:

### Delete
<pre>
shield:DescribeDRTAccess,
shield:DisassociateDRTLogBucket,
shield:DisassociateDRTRole,
iam:PassRole,
iam:GetRole,
iam:ListAttachedRolePolicies,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
s3:DeleteBucketPolicy</pre>

### Read
<pre>
shield:DescribeDRTAccess</pre>

### Update
<pre>
shield:DescribeDRTAccess,
shield:AssociateDRTLogBucket,
shield:AssociateDRTRole,
shield:DisassociateDRTLogBucket,
shield:DisassociateDRTRole,
iam:PassRole,
iam:GetRole,
iam:ListAttachedRolePolicies,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
s3:DeleteBucketPolicy</pre>


## Example
```sql
SELECT
region,
account_id,
log_bucket_list,
role_arn
FROM awscc.shield.drt_access
WHERE data__Identifier = '&lt;AccountId&gt;'
```
