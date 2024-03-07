---
title: access_log_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_log_subscriptions
  - vpclattice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>access_log_subscriptions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_log_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_log_subscriptions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.vpclattice.access_log_subscriptions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>access_log_subscriptions</code> resource, the following permissions are required:

### Create
<pre>
vpc-lattice:CreateAccessLogSubscription,
vpc-lattice:TagResource,
vpc-lattice:GetAccessLogSubscription,
vpc-lattice:ListTagsForResource,
logs:CreateLogDelivery,
logs:CreateLogStream,
logs:PutDestination,
logs:PutDestinationPolicy,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
logs:GetLogDelivery,
s3:PutBucketLogging,
s3:GetBucketLogging,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
firehose:TagDeliveryStream,
firehose:CreateDeliveryStream,
firehose:DescribeDeliveryStream,
iam:CreateServiceLinkedRole</pre>

### List
<pre>
vpc-lattice:ListAccessLogSubscriptions</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.vpclattice.access_log_subscriptions
WHERE region = 'us-east-1'
```
