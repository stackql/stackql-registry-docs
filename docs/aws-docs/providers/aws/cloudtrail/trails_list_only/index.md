---
title: trails_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - trails_list_only
  - cloudtrail
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

Lists <code>trails</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/trails/"><code>trails</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trails_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket. A maximum of five trails can exist in a region, irrespective of the region in which they were created.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudtrail.trails_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cloud_watch_logs_log_group_arn" /></td><td><code>string</code></td><td>Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. Not required unless you specify CloudWatchLogsRoleArn.</td></tr>
<tr><td><CopyableCode code="cloud_watch_logs_role_arn" /></td><td><code>string</code></td><td>Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.</td></tr>
<tr><td><CopyableCode code="enable_log_file_validation" /></td><td><code>boolean</code></td><td>Specifies whether log file validation is enabled. The default is false.</td></tr>
<tr><td><CopyableCode code="advanced_event_selectors" /></td><td><code>array</code></td><td>The advanced event selectors that were used to select events for the data store.</td></tr>
<tr><td><CopyableCode code="event_selectors" /></td><td><code>array</code></td><td>Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event. You can configure up to five event selectors for a trail.</td></tr>
<tr><td><CopyableCode code="include_global_service_events" /></td><td><code>boolean</code></td><td>Specifies whether the trail is publishing events from global services such as IAM to the log files.</td></tr>
<tr><td><CopyableCode code="is_logging" /></td><td><code>boolean</code></td><td>Whether the CloudTrail is currently logging AWS API calls.</td></tr>
<tr><td><CopyableCode code="is_multi_region_trail" /></td><td><code>boolean</code></td><td>Specifies whether the trail applies only to the current region or to all regions. The default is false. If the trail exists only in the current region and this value is set to true, shadow trails (replications of the trail) will be created in the other regions. If the trail exists in all regions and this value is set to false, the trail will remain in the region where it was created, and its shadow trails in other regions will be deleted. As a best practice, consider using trails that log events in all regions.</td></tr>
<tr><td><CopyableCode code="is_organization_trail" /></td><td><code>boolean</code></td><td>Specifies whether the trail is created for all accounts in an organization in AWS Organizations, or only for the current AWS account. The default is false, and cannot be true unless the call is made on behalf of an AWS account that is the master account for an organization in AWS Organizations.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.</td></tr>
<tr><td><CopyableCode code="s3_bucket_name" /></td><td><code>string</code></td><td>Specifies the name of the Amazon S3 bucket designated for publishing log files. See Amazon S3 Bucket Naming Requirements.</td></tr>
<tr><td><CopyableCode code="s3_key_prefix" /></td><td><code>string</code></td><td>Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your CloudTrail Log Files. The maximum length is 200 characters.</td></tr>
<tr><td><CopyableCode code="sns_topic_name" /></td><td><code>string</code></td><td>Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="trail_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sns_topic_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="insight_selectors" /></td><td><code>array</code></td><td>Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing trail.</td></tr>
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
Lists all <code>trails</code> in a region.
```sql
SELECT
region,
trail_name
FROM aws.cloudtrail.trails_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>trails_list_only</code> resource, see <a href="/providers/aws/cloudtrail/trails/#permissions"><code>trails</code></a>


