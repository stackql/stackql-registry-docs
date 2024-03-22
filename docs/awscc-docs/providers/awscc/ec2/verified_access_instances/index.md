---
title: verified_access_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_access_instances
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>verified_access_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>verified_access_instances</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.verified_access_instances</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>verified_access_instance_id</code></td><td><code>string</code></td><td>The ID of the AWS Verified Access instance.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
verified_access_instance_id
FROM awscc.ec2.verified_access_instances
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>verified_access_instances</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVerifiedAccessInstance,
ec2:AttachVerifiedAccessTrustProvider,
ec2:ModifyVerifiedAccessInstanceLoggingConfiguration,
ec2:DescribeVerifiedAccessInstances,
ec2:DescribeVerifiedAccessInstanceLoggingConfigurations,
ec2:CreateTags,
ec2:DescribeTags,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:PutDestination,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
logs:PutLogEvents,
logs:DescribeLogStreams,
s3:listBuckets,
s3:PutObject,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
logs:DescribeLogGroups,
logs:PutResourcePolicy,
firehose:TagDeliveryStream,
logs:DescribeResourcePolicies,
iam:CreateServiceLinkedRole,
verified-access:AllowVerifiedAccess
```

### List
```json
ec2:DescribeVerifiedAccessInstances,
ec2:DescribeTags,
logs:ListLogDeliveries,
logs:GetLogDelivery
```

