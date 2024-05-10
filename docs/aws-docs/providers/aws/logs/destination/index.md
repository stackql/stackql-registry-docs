---
title: destination
hide_title: false
hide_table_of_contents: false
keywords:
  - destination
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


Gets or updates an individual <code>destination</code> resource, use <code>destinations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Logs::Destination resource specifies a CloudWatch Logs destination. A destination encapsulates a physical resource (such as an Amazon Kinesis data stream) and enables you to subscribe that resource to a stream of log events.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.destination" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="destination_name" /></td><td><code>string</code></td><td>The name of the destination resource</td></tr>
<tr><td><CopyableCode code="destination_policy" /></td><td><code>string</code></td><td>An IAM policy document that governs which AWS accounts can create subscription filters against this destination.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource</td></tr>
<tr><td><CopyableCode code="target_arn" /></td><td><code>string</code></td><td>The ARN of the physical target where the log events are delivered (for example, a Kinesis stream)</td></tr>
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
destination_name,
destination_policy,
role_arn,
target_arn
FROM aws.logs.destination
WHERE region = 'us-east-1' AND data__Identifier = '<DestinationName>';
```


## Permissions

To operate on the <code>destination</code> resource, the following permissions are required:

### Read
```json
logs:DescribeDestinations
```

### Update
```json
logs:PutDestination,
logs:PutDestinationPolicy,
logs:DescribeDestinations,
iam:PassRole
```

