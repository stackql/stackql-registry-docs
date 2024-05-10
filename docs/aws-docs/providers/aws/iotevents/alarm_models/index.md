---
title: alarm_models
hide_title: false
hide_table_of_contents: false
keywords:
  - alarm_models
  - iotevents
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


Used to retrieve a list of <code>alarm_models</code> in a region or to create or delete a <code>alarm_models</code> resource, use <code>alarm_model</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarm_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::AlarmModel resource creates a alarm model. AWS IoT Events alarms help you monitor your data for changes. The data can be metrics that you measure for your equipment and processes. You can create alarms that send notifications when a threshold is breached. Alarms help you detect issues, streamline maintenance, and optimize performance of your equipment and processes.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Alarms are instances of alarm models. The alarm model specifies what to detect, when to send notifications, who gets notified, and more. You can also specify one or more supported actions that occur when the alarm state changes. AWS IoT Events routes input attributes derived from your data to the appropriate alarms. If the data that you're monitoring is outside the specified range, the alarm is invoked. You can also acknowledge the alarms or set them to the snooze mode.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.alarm_models" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="alarm_model_name" /></td><td><code>string</code></td><td>The name of the alarm model.</td></tr>
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
alarm_model_name
FROM aws.iotevents.alarm_models
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>alarm_model</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- alarm_model.iql (required properties only)
INSERT INTO aws.iotevents.alarm_models (
 RoleArn,
 AlarmRule,
 region
)
SELECT 
'{{ RoleArn }}',
 '{{ AlarmRule }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- alarm_model.iql (all properties)
INSERT INTO aws.iotevents.alarm_models (
 AlarmModelName,
 AlarmModelDescription,
 RoleArn,
 Key,
 Severity,
 AlarmRule,
 AlarmEventActions,
 AlarmCapabilities,
 Tags,
 region
)
SELECT 
 '{{ AlarmModelName }}',
 '{{ AlarmModelDescription }}',
 '{{ RoleArn }}',
 '{{ Key }}',
 '{{ Severity }}',
 '{{ AlarmRule }}',
 '{{ AlarmEventActions }}',
 '{{ AlarmCapabilities }}',
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
  - name: alarm_model
    props:
      - name: AlarmModelName
        value: '{{ AlarmModelName }}'
      - name: AlarmModelDescription
        value: '{{ AlarmModelDescription }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Key
        value: '{{ Key }}'
      - name: Severity
        value: '{{ Severity }}'
      - name: AlarmRule
        value:
          SimpleRule:
            InputProperty: '{{ InputProperty }}'
            ComparisonOperator: '{{ ComparisonOperator }}'
            Threshold: '{{ Threshold }}'
      - name: AlarmEventActions
        value:
          AlarmActions:
            - DynamoDB:
                HashKeyField: '{{ HashKeyField }}'
                HashKeyType: '{{ HashKeyType }}'
                HashKeyValue: '{{ HashKeyValue }}'
                Operation: '{{ Operation }}'
                Payload:
                  ContentExpression: '{{ ContentExpression }}'
                  Type: '{{ Type }}'
                PayloadField: '{{ PayloadField }}'
                RangeKeyField: '{{ RangeKeyField }}'
                RangeKeyType: '{{ RangeKeyType }}'
                RangeKeyValue: '{{ RangeKeyValue }}'
                TableName: '{{ TableName }}'
              DynamoDBv2:
                Payload: null
                TableName: '{{ TableName }}'
              Firehose:
                DeliveryStreamName: '{{ DeliveryStreamName }}'
                Payload: null
                Separator: '{{ Separator }}'
              IotEvents:
                InputName: '{{ InputName }}'
                Payload: null
              IotSiteWise:
                AssetId: '{{ AssetId }}'
                EntryId: '{{ EntryId }}'
                PropertyAlias: '{{ PropertyAlias }}'
                PropertyId: '{{ PropertyId }}'
                PropertyValue:
                  Quality: '{{ Quality }}'
                  Timestamp:
                    OffsetInNanos: '{{ OffsetInNanos }}'
                    TimeInSeconds: '{{ TimeInSeconds }}'
                  Value:
                    BooleanValue: '{{ BooleanValue }}'
                    DoubleValue: '{{ DoubleValue }}'
                    IntegerValue: '{{ IntegerValue }}'
                    StringValue: '{{ StringValue }}'
              IotTopicPublish:
                MqttTopic: '{{ MqttTopic }}'
                Payload: null
              Lambda:
                FunctionArn: '{{ FunctionArn }}'
                Payload: null
              Sns:
                Payload: null
                TargetArn: '{{ TargetArn }}'
              Sqs:
                Payload: null
                QueueUrl: '{{ QueueUrl }}'
                UseBase64: '{{ UseBase64 }}'
      - name: AlarmCapabilities
        value:
          InitializationConfiguration:
            DisabledOnInitialization: '{{ DisabledOnInitialization }}'
          AcknowledgeFlow:
            Enabled: '{{ Enabled }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotevents.alarm_models
WHERE data__Identifier = '<AlarmModelName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>alarm_models</code> resource, the following permissions are required:

### Create
```json
iotevents:CreateAlarmModel,
iotevents:UpdateInputRouting,
iotevents:DescribeAlarmModel,
iotevents:ListTagsForResource,
iotevents:TagResource,
iam:PassRole
```

### Delete
```json
iotevents:DeleteAlarmModel,
iotevents:DescribeAlarmModel
```

### List
```json
iotevents:ListAlarmModels
```

