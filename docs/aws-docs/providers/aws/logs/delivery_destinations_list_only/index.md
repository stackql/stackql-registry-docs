---
title: delivery_destinations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_destinations_list_only
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

Lists <code>delivery_destinations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/delivery_destinations/"><code>delivery_destinations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_destinations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This structure contains information about one delivery destination in your account.<br />A delivery destination is an AWS resource that represents an AWS service that logs can be sent to CloudWatch Logs, Amazon S3, are supported as Kinesis Data Firehose delivery destinations.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.delivery_destinations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of this delivery destination.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that uniquely identifies this delivery destination.</td></tr>
<tr><td><CopyableCode code="destination_resource_arn" /></td><td><code>string</code></td><td>The ARN of the AWS resource that will receive the logs.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags that have been assigned to this delivery destination.</td></tr>
<tr><td><CopyableCode code="delivery_destination_type" /></td><td><code>string</code></td><td>Displays whether this delivery destination is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.</td></tr>
<tr><td><CopyableCode code="delivery_destination_policy" /></td><td><code>object</code></td><td>IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.<br />The policy must be in JSON string format.<br />Length Constraints: Maximum length of 51200</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>delivery_destinations</code> in a region.
```sql
SELECT
region,
name
FROM aws.logs.delivery_destinations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>delivery_destinations_list_only</code> resource, see <a href="/providers/aws/logs/delivery_destinations/#permissions"><code>delivery_destinations</code></a>


