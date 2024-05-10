---
title: delivery_destination
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_destination
  - logs
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


Gets or updates an individual <code>delivery_destination</code> resource, use <code>delivery_destinations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This structure contains information about one delivery destination in your account.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;A delivery destination is an AWS resource that represents an AWS service that logs can be sent to CloudWatch Logs, Amazon S3, are supported as Kinesis Data Firehose delivery destinations.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.delivery_destination" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of this delivery destination.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that uniquely identifies this delivery destination.</td></tr>
<tr><td><CopyableCode code="destination_resource_arn" /></td><td><code>string</code></td><td>The ARN of the AWS resource that will receive the logs.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags that have been assigned to this delivery destination.</td></tr>
<tr><td><CopyableCode code="delivery_destination_type" /></td><td><code>string</code></td><td>Displays whether this delivery destination is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.</td></tr>
<tr><td><CopyableCode code="delivery_destination_policy" /></td><td><code>object</code></td><td>IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;The policy must be in JSON string format.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Length Constraints: Maximum length of 51200</td></tr>
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
name,
arn,
destination_resource_arn,
tags,
delivery_destination_type,
delivery_destination_policy
FROM aws.logs.delivery_destination
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## Permissions

To operate on the <code>delivery_destination</code> resource, the following permissions are required:

### Read
```json
logs:GetDeliveryDestination,
logs:ListTagsForResource,
logs:GetDeliveryDestinationPolicy
```

### Update
```json
logs:PutDeliveryDestination,
logs:GetDeliveryDestination,
logs:ListTagsForResource,
logs:TagResource,
logs:UntagResource,
logs:DeleteDeliveryDestinationPolicy,
logs:PutDeliveryDestinationPolicy,
logs:GetDeliveryDestinationPolicy
```

