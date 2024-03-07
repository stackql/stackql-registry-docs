---
title: access_log_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - access_log_subscription
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
Gets an individual <code>access_log_subscription</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_log_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_log_subscription</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.vpclattice.access_log_subscription</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>destination_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>access_log_subscription</code> resource, the following permissions are required:

### Read
<pre>
vpc-lattice:GetAccessLogSubscription,
vpc-lattice:ListTagsForResource,
logs:GetLogDelivery</pre>

### Update
<pre>
vpc-lattice:GetAccessLogSubscription,
vpc-lattice:UpdateAccessLogSubscription,
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
logs:UpdateLogDelivery,
firehose:UpdateDestination,
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
firehose:DescribeDeliveryStream</pre>

### Delete
<pre>
vpc-lattice:DeleteAccessLogSubscription,
vpc-lattice:UntagResource,
logs:DeleteLogDelivery,
logs:DeleteLogStream,
logs:GetLogDelivery,
logs:DeleteDestination,
s3:PutBucketLogging,
iam:GetServiceLinkedRoleDeletionStatus,
iam:DeleteServiceLinkedRole,
firehose:DeleteDeliveryStream,
firehose:UntagDeliveryStream</pre>


## Example
```sql
SELECT
region,
arn,
destination_arn,
id,
resource_arn,
resource_id,
resource_identifier,
tags
FROM awscc.vpclattice.access_log_subscription
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
