---
title: canaries
hide_title: false
hide_table_of_contents: false
keywords:
  - canaries
  - synthetics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>canaries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>canaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>canaries</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.synthetics.canaries</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the canary.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>canaries</code> resource, the following permissions are required:

### Create
<pre>
synthetics:CreateCanary,
synthetics:StartCanary,
synthetics:GetCanary,
synthetics:TagResource,
s3:CreateBucket,
s3:GetObject,
s3:GetObjectVersion,
s3:PutBucketEncryption,
s3:PutEncryptionConfiguration,
s3:GetBucketLocation,
lambda:CreateFunction,
lambda:AddPermission,
lambda:PublishVersion,
lambda:UpdateFunctionConfiguration,
lambda:GetFunctionConfiguration,
lambda:GetLayerVersionByArn,
lambda:GetLayerVersion,
lambda:PublishLayerVersion,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
iam:PassRole</pre>

### List
<pre>
synthetics:DescribeCanaries</pre>


## Example
```sql
SELECT
region,
name
FROM awscc.synthetics.canaries
WHERE region = 'us-east-1'
```
