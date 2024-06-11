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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>trail</code> resource or lists <code>trails</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trails</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket. A maximum of five trails can exist in a region, irrespective of the region in which they were created.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudtrail.trails" /></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="S3BucketName, IsLogging, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>trails</code> in a region.
```sql
SELECT
region,
trail_name
FROM aws.cloudtrail.trails
WHERE region = 'us-east-1';
```
Gets all properties from a <code>trail</code>.
```sql
SELECT
region,
cloud_watch_logs_log_group_arn,
cloud_watch_logs_role_arn,
enable_log_file_validation,
advanced_event_selectors,
event_selectors,
include_global_service_events,
is_logging,
is_multi_region_trail,
is_organization_trail,
kms_key_id,
s3_bucket_name,
s3_key_prefix,
sns_topic_name,
tags,
trail_name,
arn,
sns_topic_arn,
insight_selectors
FROM aws.cloudtrail.trails
WHERE region = 'us-east-1' AND data__Identifier = '<TrailName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>trail</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.cloudtrail.trails (
 IsLogging,
 S3BucketName,
 region
)
SELECT 
'{{ IsLogging }}',
 '{{ S3BucketName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudtrail.trails (
 CloudWatchLogsLogGroupArn,
 CloudWatchLogsRoleArn,
 EnableLogFileValidation,
 AdvancedEventSelectors,
 EventSelectors,
 IncludeGlobalServiceEvents,
 IsLogging,
 IsMultiRegionTrail,
 IsOrganizationTrail,
 KMSKeyId,
 S3BucketName,
 S3KeyPrefix,
 SnsTopicName,
 Tags,
 TrailName,
 InsightSelectors,
 region
)
SELECT 
 '{{ CloudWatchLogsLogGroupArn }}',
 '{{ CloudWatchLogsRoleArn }}',
 '{{ EnableLogFileValidation }}',
 '{{ AdvancedEventSelectors }}',
 '{{ EventSelectors }}',
 '{{ IncludeGlobalServiceEvents }}',
 '{{ IsLogging }}',
 '{{ IsMultiRegionTrail }}',
 '{{ IsOrganizationTrail }}',
 '{{ KMSKeyId }}',
 '{{ S3BucketName }}',
 '{{ S3KeyPrefix }}',
 '{{ SnsTopicName }}',
 '{{ Tags }}',
 '{{ TrailName }}',
 '{{ InsightSelectors }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: trail
    props:
      - name: CloudWatchLogsLogGroupArn
        value: '{{ CloudWatchLogsLogGroupArn }}'
      - name: CloudWatchLogsRoleArn
        value: '{{ CloudWatchLogsRoleArn }}'
      - name: EnableLogFileValidation
        value: '{{ EnableLogFileValidation }}'
      - name: AdvancedEventSelectors
        value:
          - Name: '{{ Name }}'
            FieldSelectors:
              - Field: '{{ Field }}'
                Equals:
                  - '{{ Equals[0] }}'
                StartsWith:
                  - '{{ StartsWith[0] }}'
                EndsWith:
                  - '{{ EndsWith[0] }}'
                NotEquals:
                  - '{{ NotEquals[0] }}'
                NotStartsWith:
                  - '{{ NotStartsWith[0] }}'
                NotEndsWith:
                  - '{{ NotEndsWith[0] }}'
      - name: EventSelectors
        value:
          - DataResources:
              - Type: '{{ Type }}'
                Values:
                  - '{{ Values[0] }}'
            IncludeManagementEvents: '{{ IncludeManagementEvents }}'
            ReadWriteType: '{{ ReadWriteType }}'
            ExcludeManagementEventSources:
              - '{{ ExcludeManagementEventSources[0] }}'
      - name: IncludeGlobalServiceEvents
        value: '{{ IncludeGlobalServiceEvents }}'
      - name: IsLogging
        value: '{{ IsLogging }}'
      - name: IsMultiRegionTrail
        value: '{{ IsMultiRegionTrail }}'
      - name: IsOrganizationTrail
        value: '{{ IsOrganizationTrail }}'
      - name: KMSKeyId
        value: '{{ KMSKeyId }}'
      - name: S3BucketName
        value: '{{ S3BucketName }}'
      - name: S3KeyPrefix
        value: '{{ S3KeyPrefix }}'
      - name: SnsTopicName
        value: '{{ SnsTopicName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TrailName
        value: '{{ TrailName }}'
      - name: InsightSelectors
        value:
          - InsightType: '{{ InsightType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cloudtrail.trails
WHERE data__Identifier = '<TrailName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>trails</code> resource, the following permissions are required:

### Create
```json
CloudTrail:CreateTrail,
CloudTrail:StartLogging,
CloudTrail:AddTags,
CloudTrail:PutEventSelectors,
CloudTrail:PutInsightSelectors,
iam:GetRole,
iam:PassRole,
iam:CreateServiceLinkedRole,
organizations:DescribeOrganization,
organizations:ListAWSServiceAccessForOrganization
```

### Read
```json
CloudTrail:GetTrail,
CloudTrail:GetTrailStatus,
CloudTrail:ListTags,
CloudTrail:GetEventSelectors,
CloudTrail:GetInsightSelectors,
CloudTrail:DescribeTrails
```

### Update
```json
CloudTrail:UpdateTrail,
CloudTrail:StartLogging,
CloudTrail:StopLogging,
CloudTrail:AddTags,
CloudTrail:RemoveTags,
CloudTrail:PutEventSelectors,
CloudTrail:PutInsightSelectors,
iam:GetRole,
iam:PassRole,
iam:CreateServiceLinkedRole,
organizations:DescribeOrganization,
organizations:ListAWSServiceAccessForOrganization,
CloudTrail:GetTrail,
CloudTrail:DescribeTrails
```

### Delete
```json
CloudTrail:DeleteTrail
```

### List
```json
CloudTrail:ListTrails,
CloudTrail:GetTrail,
CloudTrail:GetTrailStatus,
CloudTrail:ListTags,
CloudTrail:GetEventSelectors,
CloudTrail:GetInsightSelectors,
CloudTrail:DescribeTrails
```

