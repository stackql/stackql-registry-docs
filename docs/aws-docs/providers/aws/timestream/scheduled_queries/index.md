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


Used to retrieve a list of <code>scheduled_queries</code> in a region or to create or delete a <code>scheduled_queries</code> resource, use <code>scheduled_query</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::ScheduledQuery resource creates a Timestream Scheduled Query.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.timestream.scheduled_queries" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.timestream.scheduled_queries
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "QueryString": "{{ QueryString }}",
 "ScheduleConfiguration": {
  "ScheduleExpression": "{{ ScheduleExpression }}"
 },
 "NotificationConfiguration": {
  "SnsConfiguration": {
   "TopicArn": "{{ TopicArn }}"
  }
 },
 "ScheduledQueryExecutionRoleArn": "{{ ScheduledQueryExecutionRoleArn }}",
 "ErrorReportConfiguration": {
  "S3Configuration": {
   "BucketName": "{{ BucketName }}",
   "ObjectKeyPrefix": "{{ ObjectKeyPrefix }}",
   "EncryptionOption": "{{ EncryptionOption }}"
  }
 }
}
>>>
--required properties only
INSERT INTO aws.timestream.scheduled_queries (
 QueryString,
 ScheduleConfiguration,
 NotificationConfiguration,
 ScheduledQueryExecutionRoleArn,
 ErrorReportConfiguration,
 region
)
SELECT 
{{ .QueryString }},
 {{ .ScheduleConfiguration }},
 {{ .NotificationConfiguration }},
 {{ .ScheduledQueryExecutionRoleArn }},
 {{ .ErrorReportConfiguration }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ScheduledQueryName": "{{ ScheduledQueryName }}",
 "QueryString": "{{ QueryString }}",
 "ScheduleConfiguration": {
  "ScheduleExpression": "{{ ScheduleExpression }}"
 },
 "NotificationConfiguration": {
  "SnsConfiguration": {
   "TopicArn": "{{ TopicArn }}"
  }
 },
 "ClientToken": "{{ ClientToken }}",
 "ScheduledQueryExecutionRoleArn": "{{ ScheduledQueryExecutionRoleArn }}",
 "TargetConfiguration": {
  "TimestreamConfiguration": {
   "DatabaseName": "{{ DatabaseName }}",
   "TableName": "{{ TableName }}",
   "TimeColumn": "{{ TimeColumn }}",
   "DimensionMappings": [
    {
     "Name": "{{ Name }}",
     "DimensionValueType": "{{ DimensionValueType }}"
    }
   ],
   "MultiMeasureMappings": {
    "TargetMultiMeasureName": "{{ TargetMultiMeasureName }}",
    "MultiMeasureAttributeMappings": [
     {
      "SourceColumn": "{{ SourceColumn }}",
      "MeasureValueType": "{{ MeasureValueType }}",
      "TargetMultiMeasureAttributeName": "{{ TargetMultiMeasureAttributeName }}"
     }
    ]
   },
   "MixedMeasureMappings": [
    {
     "MeasureName": "{{ MeasureName }}",
     "SourceColumn": "{{ SourceColumn }}",
     "TargetMeasureName": "{{ TargetMeasureName }}",
     "MeasureValueType": "{{ MeasureValueType }}",
     "MultiMeasureAttributeMappings": null
    }
   ],
   "MeasureNameColumn": "{{ MeasureNameColumn }}"
  }
 },
 "ErrorReportConfiguration": {
  "S3Configuration": {
   "BucketName": "{{ BucketName }}",
   "ObjectKeyPrefix": "{{ ObjectKeyPrefix }}",
   "EncryptionOption": "{{ EncryptionOption }}"
  }
 },
 "KmsKeyId": "{{ KmsKeyId }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ .ScheduledQueryName }},
 {{ .QueryString }},
 {{ .ScheduleConfiguration }},
 {{ .NotificationConfiguration }},
 {{ .ClientToken }},
 {{ .ScheduledQueryExecutionRoleArn }},
 {{ .TargetConfiguration }},
 {{ .ErrorReportConfiguration }},
 {{ .KmsKeyId }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

