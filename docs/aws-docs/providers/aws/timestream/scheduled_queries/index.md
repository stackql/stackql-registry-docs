---
title: scheduled_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_queries
  - timestream
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

Creates, updates, deletes or gets a <code>scheduled_query</code> resource or lists <code>scheduled_queries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::ScheduledQuery resource creates a Timestream Scheduled Query.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.timestream.scheduled_queries" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name of the scheduled query that is generated upon creation.</td></tr>
<tr><td><CopyableCode code="scheduled_query_name" /></td><td><code>string</code></td><td>The name of the scheduled query. Scheduled query names must be unique within each Region.</td></tr>
<tr><td><CopyableCode code="query_string" /></td><td><code>string</code></td><td>The query string to run. Parameter names can be specified in the query string @ character followed by an identifier. The named Parameter @scheduled_runtime is reserved and can be used in the query to get the time at which the query is scheduled to run. The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of @scheduled_runtime paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the @scheduled_runtime parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.</td></tr>
<tr><td><CopyableCode code="schedule_configuration" /></td><td><code>object</code></td><td>Configuration for when the scheduled query is executed.</td></tr>
<tr><td><CopyableCode code="notification_configuration" /></td><td><code>object</code></td><td>Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.</td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td>Using a ClientToken makes the call to CreateScheduledQuery idempotent, in other words, making the same request repeatedly will produce the same result. Making multiple identical CreateScheduledQuery requests has the same effect as making a single request. If CreateScheduledQuery is called without a ClientToken, the Query SDK generates a ClientToken on your behalf. After 8 hours, any request with the same ClientToken is treated as a new request.</td></tr>
<tr><td><CopyableCode code="scheduled_query_execution_role_arn" /></td><td><code>string</code></td><td>The ARN for the IAM role that Timestream will assume when running the scheduled query.</td></tr>
<tr><td><CopyableCode code="target_configuration" /></td><td><code>object</code></td><td>Configuration of target store where scheduled query results are written to.</td></tr>
<tr><td><CopyableCode code="error_report_configuration" /></td><td><code>object</code></td><td>Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with alias/. If ErrorReportConfiguration uses SSE_KMS as encryption type, the same KmsKeyId is used to encrypt the error report at rest.</td></tr>
<tr><td><CopyableCode code="sq_name" /></td><td><code>string</code></td><td>The name of the scheduled query. Scheduled query names must be unique within each Region.</td></tr>
<tr><td><CopyableCode code="sq_query_string" /></td><td><code>string</code></td><td>The query string to run. Parameter names can be specified in the query string @ character followed by an identifier. The named Parameter @scheduled_runtime is reserved and can be used in the query to get the time at which the query is scheduled to run. The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of @scheduled_runtime paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the @scheduled_runtime parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.</td></tr>
<tr><td><CopyableCode code="sq_schedule_configuration" /></td><td><code>string</code></td><td>Configuration for when the scheduled query is executed.</td></tr>
<tr><td><CopyableCode code="sq_notification_configuration" /></td><td><code>string</code></td><td>Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.</td></tr>
<tr><td><CopyableCode code="sq_scheduled_query_execution_role_arn" /></td><td><code>string</code></td><td>The ARN for the IAM role that Timestream will assume when running the scheduled query.</td></tr>
<tr><td><CopyableCode code="sq_target_configuration" /></td><td><code>string</code></td><td>Configuration of target store where scheduled query results are written to.</td></tr>
<tr><td><CopyableCode code="sq_error_report_configuration" /></td><td><code>string</code></td><td>Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.</td></tr>
<tr><td><CopyableCode code="sq_kms_key_id" /></td><td><code>string</code></td><td>The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with alias/. If ErrorReportConfiguration uses SSE_KMS as encryption type, the same KmsKeyId is used to encrypt the error report at rest.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs to label the scheduled query.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html"><code>AWS::Timestream::ScheduledQuery</code></a>.

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
    <td><CopyableCode code="QueryString, ScheduleConfiguration, NotificationConfiguration, ScheduledQueryExecutionRoleArn, ErrorReportConfiguration, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>scheduled_queries</code> in a region.
```sql
SELECT
region,
arn,
scheduled_query_name,
query_string,
schedule_configuration,
notification_configuration,
client_token,
scheduled_query_execution_role_arn,
target_configuration,
error_report_configuration,
kms_key_id,
sq_name,
sq_query_string,
sq_schedule_configuration,
sq_notification_configuration,
sq_scheduled_query_execution_role_arn,
sq_target_configuration,
sq_error_report_configuration,
sq_kms_key_id,
tags
FROM aws.timestream.scheduled_queries
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>scheduled_query</code>.
```sql
SELECT
region,
arn,
scheduled_query_name,
query_string,
schedule_configuration,
notification_configuration,
client_token,
scheduled_query_execution_role_arn,
target_configuration,
error_report_configuration,
kms_key_id,
sq_name,
sq_query_string,
sq_schedule_configuration,
sq_notification_configuration,
sq_scheduled_query_execution_role_arn,
sq_target_configuration,
sq_error_report_configuration,
sq_kms_key_id,
tags
FROM aws.timestream.scheduled_queries
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scheduled_query</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.timestream.scheduled_queries (
 QueryString,
 ScheduleConfiguration,
 NotificationConfiguration,
 ScheduledQueryExecutionRoleArn,
 ErrorReportConfiguration,
 region
)
SELECT 
'{{ QueryString }}',
 '{{ ScheduleConfiguration }}',
 '{{ NotificationConfiguration }}',
 '{{ ScheduledQueryExecutionRoleArn }}',
 '{{ ErrorReportConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.timestream.scheduled_queries (
 ScheduledQueryName,
 QueryString,
 ScheduleConfiguration,
 NotificationConfiguration,
 ClientToken,
 ScheduledQueryExecutionRoleArn,
 TargetConfiguration,
 ErrorReportConfiguration,
 KmsKeyId,
 Tags,
 region
)
SELECT 
 '{{ ScheduledQueryName }}',
 '{{ QueryString }}',
 '{{ ScheduleConfiguration }}',
 '{{ NotificationConfiguration }}',
 '{{ ClientToken }}',
 '{{ ScheduledQueryExecutionRoleArn }}',
 '{{ TargetConfiguration }}',
 '{{ ErrorReportConfiguration }}',
 '{{ KmsKeyId }}',
 '{{ Tags }}',
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
  - name: scheduled_query
    props:
      - name: ScheduledQueryName
        value: '{{ ScheduledQueryName }}'
      - name: QueryString
        value: '{{ QueryString }}'
      - name: ScheduleConfiguration
        value:
          ScheduleExpression: '{{ ScheduleExpression }}'
      - name: NotificationConfiguration
        value:
          SnsConfiguration:
            TopicArn: '{{ TopicArn }}'
      - name: ClientToken
        value: '{{ ClientToken }}'
      - name: ScheduledQueryExecutionRoleArn
        value: '{{ ScheduledQueryExecutionRoleArn }}'
      - name: TargetConfiguration
        value:
          TimestreamConfiguration:
            DatabaseName: '{{ DatabaseName }}'
            TableName: '{{ TableName }}'
            TimeColumn: '{{ TimeColumn }}'
            DimensionMappings:
              - Name: '{{ Name }}'
                DimensionValueType: '{{ DimensionValueType }}'
            MultiMeasureMappings:
              TargetMultiMeasureName: '{{ TargetMultiMeasureName }}'
              MultiMeasureAttributeMappings:
                - SourceColumn: '{{ SourceColumn }}'
                  MeasureValueType: '{{ MeasureValueType }}'
                  TargetMultiMeasureAttributeName: '{{ TargetMultiMeasureAttributeName }}'
            MixedMeasureMappings:
              - MeasureName: '{{ MeasureName }}'
                SourceColumn: '{{ SourceColumn }}'
                TargetMeasureName: '{{ TargetMeasureName }}'
                MeasureValueType: '{{ MeasureValueType }}'
                MultiMeasureAttributeMappings: null
            MeasureNameColumn: '{{ MeasureNameColumn }}'
      - name: ErrorReportConfiguration
        value:
          S3Configuration:
            BucketName: '{{ BucketName }}'
            ObjectKeyPrefix: '{{ ObjectKeyPrefix }}'
            EncryptionOption: '{{ EncryptionOption }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.timestream.scheduled_queries
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>scheduled_queries</code> resource, the following permissions are required:

### Create
```json
timestream:CreateScheduledQuery,
timestream:DescribeEndpoints
```

### Read
```json
timestream:DescribeScheduledQuery,
timestream:ListTagsForResource,
timestream:DescribeEndpoints
```

### Update
```json
timestream:UpdateScheduledQuery,
timestream:TagResource,
timestream:UntagResource,
timestream:DescribeEndpoints
```

### Delete
```json
timestream:DeleteScheduledQuery,
timestream:DescribeEndpoints
```

### List
```json
timestream:ListScheduledQueries,
timestream:DescribeEndpoints
```
