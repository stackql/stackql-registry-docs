---
title: verified_access_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_access_instance
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
Gets an individual <code>verified_access_instance</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::VerifiedAccessInstance resource creates an AWS EC2 Verified Access Instance.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.verified_access_instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>verified_access_instance_id</code></td><td><code>string</code></td><td>The ID of the AWS Verified Access instance.</td></tr>
<tr><td><code>verified_access_trust_providers</code></td><td><code>array</code></td><td>AWS Verified Access trust providers.</td></tr>
<tr><td><code>verified_access_trust_provider_ids</code></td><td><code>array</code></td><td>The IDs of the AWS Verified Access trust providers.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>Time this Verified Access Instance was created.</td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td>Time this Verified Access Instance was last updated.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description for the AWS Verified Access instance.</td></tr>
<tr><td><code>logging_configurations</code></td><td><code>object</code></td><td>The configuration options for AWS Verified Access instances.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>fips_enabled</code></td><td><code>boolean</code></td><td>Indicates whether FIPS is enabled</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
verified_access_instance_id,
verified_access_trust_providers,
verified_access_trust_provider_ids,
creation_time,
last_updated_time,
description,
logging_configurations,
tags,
fips_enabled
FROM aws.ec2.verified_access_instance
WHERE data__Identifier = '<VerifiedAccessInstanceId>';
```

## Permissions

To operate on the <code>verified_access_instance</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeVerifiedAccessInstances,
ec2:DescribeVerifiedAccessInstanceLoggingConfigurations,
ec2:DescribeTags,
logs:GetLogDelivery,
logs:ListLogDeliveries
```

### Update
```json
ec2:ModifyVerifiedAccessInstance,
ec2:ModifyVerifiedAccessInstanceLoggingConfiguration,
ec2:DescribeVerifiedAccessInstances,
ec2:DescribeVerifiedAccessInstanceLoggingConfigurations,
ec2:DescribeTags,
ec2:AttachVerifiedAccessTrustProvider,
ec2:DetachVerifiedAccessTrustProvider,
ec2:DeleteTags,
ec2:CreateTags,
ec2:DescribeTags,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:PutDestination,
logs:PutLogEvents,
logs:DescribeLogStreams,
s3:listBuckets,
s3:PutObject,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
logs:DescribeLogGroups,
logs:PutResourcePolicy,
firehose:TagDeliveryStream,
iam:CreateServiceLinkedRole,
logs:DescribeResourcePolicies
```

### Delete
```json
ec2:DeleteVerifiedAccessInstance,
ec2:DeleteTags,
ec2:DescribeVerifiedAccessInstances,
ec2:DescribeVerifiedAccessInstanceLoggingConfigurations,
ec2:DetachVerifiedAccessTrustProvider,
ec2:GetVerifiedAccessGroupPolicy,
ec2:DescribeTags,
logs:ListLogDeliveries,
logs:GetLogDelivery,
logs:DeleteLogDelivery
```

