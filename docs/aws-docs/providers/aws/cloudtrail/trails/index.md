---
title: trails
hide_title: false
hide_table_of_contents: false
keywords:
  - trails
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
Retrieves a list of <code>trails</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trails</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudtrail.trails</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CloudWatchLogsLogGroupArn</code></td><td><code>string</code></td><td>Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. Not required unless you specify CloudWatchLogsRoleArn.</td></tr><tr><td><code>CloudWatchLogsRoleArn</code></td><td><code>string</code></td><td>Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.</td></tr><tr><td><code>EnableLogFileValidation</code></td><td><code>boolean</code></td><td>Specifies whether log file validation is enabled. The default is false.</td></tr><tr><td><code>EventSelectors</code></td><td><code>array</code></td><td>Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event. You can configure up to five event selectors for a trail.</td></tr><tr><td><code>IncludeGlobalServiceEvents</code></td><td><code>boolean</code></td><td>Specifies whether the trail is publishing events from global services such as IAM to the log files.</td></tr><tr><td><code>IsLogging</code></td><td><code>boolean</code></td><td>Whether the CloudTrail is currently logging AWS API calls.</td></tr><tr><td><code>IsMultiRegionTrail</code></td><td><code>boolean</code></td><td>Specifies whether the trail applies only to the current region or to all regions. The default is false. If the trail exists only in the current region and this value is set to true, shadow trails (replications of the trail) will be created in the other regions. If the trail exists in all regions and this value is set to false, the trail will remain in the region where it was created, and its shadow trails in other regions will be deleted. As a best practice, consider using trails that log events in all regions.</td></tr><tr><td><code>IsOrganizationTrail</code></td><td><code>boolean</code></td><td>Specifies whether the trail is created for all accounts in an organization in AWS Organizations, or only for the current AWS account. The default is false, and cannot be true unless the call is made on behalf of an AWS account that is the master account for an organization in AWS Organizations.</td></tr><tr><td><code>KMSKeyId</code></td><td><code>string</code></td><td>Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.</td></tr><tr><td><code>S3BucketName</code></td><td><code>string</code></td><td>Specifies the name of the Amazon S3 bucket designated for publishing log files. See Amazon S3 Bucket Naming Requirements.</td></tr><tr><td><code>S3KeyPrefix</code></td><td><code>string</code></td><td>Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your CloudTrail Log Files. The maximum length is 200 characters.</td></tr><tr><td><code>SnsTopicName</code></td><td><code>string</code></td><td>Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>TrailName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SnsTopicArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>InsightSelectors</code></td><td><code>array</code></td><td>Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing trail.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.cloudtrail.trails
WHERE region = 'us-east-1'
```
