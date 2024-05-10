---
title: job_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - job_templates
  - iot
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


Used to retrieve a list of <code>job_templates</code> in a region or to create or delete a <code>job_templates</code> resource, use <code>job_template</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Job templates enable you to preconfigure jobs so that you can deploy them to multiple sets of target devices.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.job_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="job_template_id" /></td><td><code>string</code></td><td></td></tr>
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
job_template_id
FROM aws.iot.job_templates
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>job_template</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- job_template.iql (required properties only)
INSERT INTO aws.iot.job_templates (
 JobTemplateId,
 Description,
 region
)
SELECT 
'{{ JobTemplateId }}',
 '{{ Description }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- job_template.iql (all properties)
INSERT INTO aws.iot.job_templates (
 JobArn,
 JobTemplateId,
 Description,
 Document,
 DocumentSource,
 TimeoutConfig,
 JobExecutionsRolloutConfig,
 AbortConfig,
 PresignedUrlConfig,
 JobExecutionsRetryConfig,
 MaintenanceWindows,
 DestinationPackageVersions,
 Tags,
 region
)
SELECT 
 '{{ JobArn }}',
 '{{ JobTemplateId }}',
 '{{ Description }}',
 '{{ Document }}',
 '{{ DocumentSource }}',
 '{{ TimeoutConfig }}',
 '{{ JobExecutionsRolloutConfig }}',
 '{{ AbortConfig }}',
 '{{ PresignedUrlConfig }}',
 '{{ JobExecutionsRetryConfig }}',
 '{{ MaintenanceWindows }}',
 '{{ DestinationPackageVersions }}',
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
  - name: job_template
    props:
      - name: JobArn
        value: '{{ JobArn }}'
      - name: JobTemplateId
        value: '{{ JobTemplateId }}'
      - name: Description
        value: '{{ Description }}'
      - name: Document
        value: '{{ Document }}'
      - name: DocumentSource
        value: '{{ DocumentSource }}'
      - name: TimeoutConfig
        value:
          InProgressTimeoutInMinutes: '{{ InProgressTimeoutInMinutes }}'
      - name: JobExecutionsRolloutConfig
        value:
          ExponentialRolloutRate:
            BaseRatePerMinute: '{{ BaseRatePerMinute }}'
            IncrementFactor: null
            RateIncreaseCriteria:
              NumberOfNotifiedThings: '{{ NumberOfNotifiedThings }}'
              NumberOfSucceededThings: '{{ NumberOfSucceededThings }}'
          MaximumPerMinute: '{{ MaximumPerMinute }}'
      - name: AbortConfig
        value:
          CriteriaList:
            - Action:
                CloudwatchAlarm:
                  StateValue: '{{ StateValue }}'
                  AlarmName: '{{ AlarmName }}'
                  StateReason: '{{ StateReason }}'
                  RoleArn: '{{ RoleArn }}'
                CloudwatchLogs:
                  LogGroupName: '{{ LogGroupName }}'
                  RoleArn: '{{ RoleArn }}'
                  BatchMode: '{{ BatchMode }}'
                CloudwatchMetric:
                  MetricName: '{{ MetricName }}'
                  MetricValue: '{{ MetricValue }}'
                  MetricNamespace: '{{ MetricNamespace }}'
                  MetricUnit: '{{ MetricUnit }}'
                  RoleArn: '{{ RoleArn }}'
                  MetricTimestamp: '{{ MetricTimestamp }}'
                DynamoDB:
                  TableName: '{{ TableName }}'
                  PayloadField: '{{ PayloadField }}'
                  RangeKeyField: '{{ RangeKeyField }}'
                  HashKeyField: '{{ HashKeyField }}'
                  RangeKeyValue: '{{ RangeKeyValue }}'
                  RangeKeyType: '{{ RangeKeyType }}'
                  HashKeyType: '{{ HashKeyType }}'
                  HashKeyValue: '{{ HashKeyValue }}'
                  RoleArn: '{{ RoleArn }}'
                DynamoDBv2:
                  PutItem:
                    TableName: '{{ TableName }}'
                  RoleArn: '{{ RoleArn }}'
                Elasticsearch:
                  Type: '{{ Type }}'
                  Index: '{{ Index }}'
                  Id: '{{ Id }}'
                  Endpoint: '{{ Endpoint }}'
                  RoleArn: '{{ RoleArn }}'
                Firehose:
                  DeliveryStreamName: '{{ DeliveryStreamName }}'
                  RoleArn: '{{ RoleArn }}'
                  Separator: '{{ Separator }}'
                  BatchMode: '{{ BatchMode }}'
                Http:
                  ConfirmationUrl: '{{ ConfirmationUrl }}'
                  Headers:
                    - Value: '{{ Value }}'
                      Key: '{{ Key }}'
                  Url: '{{ Url }}'
                  Auth:
                    Sigv4:
                      ServiceName: '{{ ServiceName }}'
                      SigningRegion: '{{ SigningRegion }}'
                      RoleArn: '{{ RoleArn }}'
                IotAnalytics:
                  RoleArn: '{{ RoleArn }}'
                  ChannelName: '{{ ChannelName }}'
                  BatchMode: '{{ BatchMode }}'
                IotEvents:
                  InputName: '{{ InputName }}'
                  RoleArn: '{{ RoleArn }}'
                  MessageId: '{{ MessageId }}'
                  BatchMode: '{{ BatchMode }}'
                IotSiteWise:
                  RoleArn: '{{ RoleArn }}'
                  PutAssetPropertyValueEntries:
                    - PropertyAlias: '{{ PropertyAlias }}'
                      PropertyValues:
                        - Value:
                            StringValue: '{{ StringValue }}'
                            DoubleValue: '{{ DoubleValue }}'
                            BooleanValue: '{{ BooleanValue }}'
                            IntegerValue: '{{ IntegerValue }}'
                          Timestamp:
                            TimeInSeconds: '{{ TimeInSeconds }}'
                            OffsetInNanos: '{{ OffsetInNanos }}'
                          Quality: '{{ Quality }}'
                      AssetId: '{{ AssetId }}'
                      EntryId: '{{ EntryId }}'
                      PropertyId: '{{ PropertyId }}'
                Kafka:
                  DestinationArn: '{{ DestinationArn }}'
                  Topic: '{{ Topic }}'
                  Key: '{{ Key }}'
                  Partition: '{{ Partition }}'
                  ClientProperties: {}
                  Headers:
                    - Value: '{{ Value }}'
                      Key: '{{ Key }}'
                Kinesis:
                  PartitionKey: '{{ PartitionKey }}'
                  StreamName: '{{ StreamName }}'
                  RoleArn: '{{ RoleArn }}'
                Lambda:
                  FunctionArn: '{{ FunctionArn }}'
                Location:
                  RoleArn: '{{ RoleArn }}'
                  TrackerName: '{{ TrackerName }}'
                  DeviceId: '{{ DeviceId }}'
                  Latitude: '{{ Latitude }}'
                  Longitude: '{{ Longitude }}'
                  Timestamp:
                    Value: '{{ Value }}'
                    Unit: '{{ Unit }}'
                OpenSearch:
                  Type: '{{ Type }}'
                  Index: '{{ Index }}'
                  Id: '{{ Id }}'
                  Endpoint: '{{ Endpoint }}'
                  RoleArn: '{{ RoleArn }}'
                Republish:
                  Qos: '{{ Qos }}'
                  Topic: '{{ Topic }}'
                  RoleArn: '{{ RoleArn }}'
                  Headers:
                    PayloadFormatIndicator: '{{ PayloadFormatIndicator }}'
                    ContentType: '{{ ContentType }}'
                    ResponseTopic: '{{ ResponseTopic }}'
                    CorrelationData: '{{ CorrelationData }}'
                    MessageExpiry: '{{ MessageExpiry }}'
                    UserProperties:
                      - Key: '{{ Key }}'
                        Value: '{{ Value }}'
                S3:
                  BucketName: '{{ BucketName }}'
                  Key: '{{ Key }}'
                  RoleArn: '{{ RoleArn }}'
                  CannedAcl: '{{ CannedAcl }}'
                Sns:
                  TargetArn: '{{ TargetArn }}'
                  MessageFormat: '{{ MessageFormat }}'
                  RoleArn: '{{ RoleArn }}'
                Sqs:
                  RoleArn: '{{ RoleArn }}'
                  UseBase64: '{{ UseBase64 }}'
                  QueueUrl: '{{ QueueUrl }}'
                StepFunctions:
                  ExecutionNamePrefix: '{{ ExecutionNamePrefix }}'
                  StateMachineName: '{{ StateMachineName }}'
                  RoleArn: '{{ RoleArn }}'
                Timestream:
                  RoleArn: '{{ RoleArn }}'
                  DatabaseName: '{{ DatabaseName }}'
                  TableName: '{{ TableName }}'
                  Dimensions:
                    - Name: '{{ Name }}'
                      Value: '{{ Value }}'
                  Timestamp:
                    Value: '{{ Value }}'
                    Unit: '{{ Unit }}'
              FailureType: '{{ FailureType }}'
              MinNumberOfExecutedThings: '{{ MinNumberOfExecutedThings }}'
              ThresholdPercentage: null
      - name: PresignedUrlConfig
        value:
          RoleArn: '{{ RoleArn }}'
          ExpiresInSec: '{{ ExpiresInSec }}'
      - name: JobExecutionsRetryConfig
        value:
          RetryCriteriaList:
            - NumberOfRetries: '{{ NumberOfRetries }}'
              FailureType: '{{ FailureType }}'
      - name: MaintenanceWindows
        value:
          - StartTime: '{{ StartTime }}'
            DurationInMinutes: '{{ DurationInMinutes }}'
      - name: DestinationPackageVersions
        value:
          - '{{ DestinationPackageVersions[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iot.job_templates
WHERE data__Identifier = '<JobTemplateId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>job_templates</code> resource, the following permissions are required:

### Create
```json
iot:CreateJobTemplate,
iam:PassRole,
s3:GetObject,
iot:TagResource
```

### Delete
```json
iot:DeleteJobTemplate
```

### List
```json
iot:ListJobTemplates
```

