---
title: log_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - log_groups
  - cloudwatch
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

Represents a log group.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a log group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.log_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="log_group_name" /></td><td><code>string</code></td><td>The name of the log group.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>integer</code></td><td>The creation time of the log group, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</td></tr>
<tr><td><CopyableCode code="retention_in_days" /></td><td><code>integer</code></td><td><p>The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, and 3653.</p> <p>To set a log group so that its log events do not expire, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.html">DeleteRetentionPolicy</a>. </p></td></tr>
<tr><td><CopyableCode code="metric_filter_count" /></td><td><code>integer</code></td><td>The number of metric filters.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the log group.</td></tr>
<tr><td><CopyableCode code="stored_bytes" /></td><td><code>integer</code></td><td>The number of bytes stored.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the KMS key to use when encrypting log data.</td></tr>
<tr><td><CopyableCode code="data_protection_status" /></td><td><code>string</code></td><td>Displays whether this log group has a protection policy, or whether it had one in the past. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDataProtectionPolicy.html">PutDataProtectionPolicy</a>.</td></tr>
<tr><td><CopyableCode code="inherited_properties" /></td><td><code>array</code></td><td>Displays all the properties that this log group has inherited from account-level settings.</td></tr>
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
    <td><CopyableCode code="DescribeLogGroups" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="CreateLogGroup" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__logGroupName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="DeleteLogGroup" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__logGroupName, region" /></td>
  </tr>
</tbody></table>








