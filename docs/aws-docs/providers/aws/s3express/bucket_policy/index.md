---
title: bucket_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_policy
  - s3express
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

Gets or operates on an individual <code>bucket_policy</code> resource, use <code>bucket_policies</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bucket_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::S3Express::BucketPolicy.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3express.bucket_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="bucket" /></td><td><code>string</code></td><td>The name of the S3 directory bucket to which the policy applies.</td></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>object</code></td><td>A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
FROM aws.s3express.bucket_policy
WHERE data__Identifier = '<Bucket>';
```

## Permissions

To operate on the <code>bucket_policy</code> resource, the following permissions are required:

### Read
```json
s3express:GetBucketPolicy
```

### Update
```json
s3express:GetBucketPolicy,
s3express:PutBucketPolicy
```

### Delete
```json
s3express:GetBucketPolicy,
s3express:DeleteBucketPolicy
```

