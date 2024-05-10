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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>access_log_subscription</code> resource, use <code>access_log_subscriptions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_log_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner will only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.access_log_subscription" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="destination_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.vpclattice.access_log_subscription
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>access_log_subscription</code> resource, the following permissions are required:

### Read
```json
vpc-lattice:GetAccessLogSubscription,
vpc-lattice:ListTagsForResource,
logs:GetLogDelivery
```

### Update
```json
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
firehose:DescribeDeliveryStream
```

