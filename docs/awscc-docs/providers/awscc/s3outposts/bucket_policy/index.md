---
title: bucket_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_policy
  - s3outposts
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
<tr><td><b>Id</b></td><td><code>awscc.s3outposts.bucket_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>bucket</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified bucket.</td></tr>
<tr><td><code>policy_document</code></td><td><code>object</code></td><td>A policy document containing permissions to add to the specified bucket.</td></tr>
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
FROM awscc.s3outposts.bucket_policy
WHERE data__Identifier = '<Bucket>';
```

## Permissions

To operate on the <code>bucket_policy</code> resource, the following permissions are required:

### Read
```json
s3-outposts:GetBucketPolicy
```

### Update
```json
s3-outposts:PutBucketPolicy,
s3-outposts:GetBucketPolicy
```

### Delete
```json
s3-outposts:DeleteBucketPolicy,
s3-outposts:GetBucketPolicy
```

