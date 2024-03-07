---
title: access_point
hide_title: false
hide_table_of_contents: false
keywords:
  - access_point
  - s3objectlambda
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>access_point</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_point</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_point</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3objectlambda.access_point</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name you want to assign to this Object lambda Access Point.</td></tr>
<tr><td><code>alias</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_date</code></td><td><code>string</code></td><td>The date and time when the Object lambda Access Point was created.</td></tr>
<tr><td><code>public_access_block_configuration</code></td><td><code>object</code></td><td>The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.</td></tr>
<tr><td><code>policy_status</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>object_lambda_configuration</code></td><td><code>object</code></td><td>The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
alias,
arn,
creation_date,
public_access_block_configuration,
policy_status,
object_lambda_configuration
FROM awscc.s3objectlambda.access_point
WHERE region = 'us-east-1'
AND data__Identifier = '{Name}';
```

## Permissions

To operate on the <code>access_point</code> resource, the following permissions are required:

### Read
```json
s3:GetAccessPointForObjectLambda,
s3:GetAccessPointPolicyStatusForObjectLambda,
s3:GetAccessPointConfigurationForObjectLambda
```

### Update
```json
s3:PutAccessPointConfigurationForObjectLambda,
s3:GetAccessPointForObjectLambda,
s3:GetAccessPointPolicyStatusForObjectLambda,
s3:GetAccessPointConfigurationForObjectLambda
```

### Delete
```json
s3:DeleteAccessPointForObjectLambda
```

