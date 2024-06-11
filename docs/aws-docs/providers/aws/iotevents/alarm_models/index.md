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

Creates, updates, deletes or gets an <code>alarm_model</code> resource or lists <code>alarm_models</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarm_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::AlarmModel resource creates a alarm model. AWS IoT Events alarms help you monitor your data for changes. The data can be metrics that you measure for your equipment and processes. You can create alarms that send notifications when a threshold is breached. Alarms help you detect issues, streamline maintenance, and optimize performance of your equipment and processes.<br/><br/>Alarms are instances of alarm models. The alarm model specifies what to detect, when to send notifications, who gets notified, and more. You can also specify one or more supported actions that occur when the alarm state changes. AWS IoT Events routes input attributes derived from your data to the appropriate alarms. If the data that you're monitoring is outside the specified range, the alarm is invoked. You can also acknowledge the alarms or set them to the snooze mode.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.alarm_models" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alarm_model_name" /></td><td><code>string</code></td><td>The name of the alarm model.</td></tr>
<tr><td><CopyableCode code="alarm_model_description" /></td><td><code>string</code></td><td>A brief description of the alarm model.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</td></tr>
<tr><td><CopyableCode code="key" /></td><td><code>string</code></td><td>The value used to identify a alarm instance. When a device or system sends input, a new alarm instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding alarm instance based on this identifying information.<br/><br/>This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct alarm instance, the device must send a message payload that contains the same attribute-value.</td></tr>
<tr><td><CopyableCode code="severity" /></td><td><code>integer</code></td><td>A non-negative integer that reflects the severity level of the alarm.<br/><br/></td></tr>
<tr><td><CopyableCode code="alarm_rule" /></td><td><code>Defines when your alarm is invoked.</code></td><td></td></tr>
<tr><td><CopyableCode code="alarm_event_actions" /></td><td><code>Contains information about one or more alarm actions.</code></td><td></td></tr>
<tr><td><CopyableCode code="alarm_capabilities" /></td><td><code>Contains the configuration information of alarm state changes</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.<br/><br/>For more information, see &#91;Tag&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).</td></tr>
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
    <td><CopyableCode code="RoleArn, AlarmRule, region" /></td>
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
List all <code>alarm_models</code> in a region.
```sql
SELECT
region,
alarm_model_name
FROM aws.iotevents.alarm_models
WHERE region = 'us-east-1';
```
Gets all properties from an <code>alarm_model</code>.
```sql
SELECT
region,
alarm_model_name,
alarm_model_description,
role_arn,
key,
severity,
alarm_rule,
alarm_event_actions,
alarm_capabilities,
tags
FROM aws.iotevents.alarm_models
WHERE region = 'us-east-1' AND data__Identifier = '<AlarmModelName>';
```


## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
iotevents:DescribeAlarmModel,
iotevents:ListTagsForResource
```

### Update
```json
iotevents:UpdateAlarmModel,
iotevents:UpdateInputRouting,
iotevents:DescribeAlarmModel,
iotevents:ListTagsForResource,
iotevents:UntagResource,
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

