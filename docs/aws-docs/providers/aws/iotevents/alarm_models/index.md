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
<tr><td><b>Description</b></td><td>Represents an alarm model to monitor an ITE input attribute. You can use the alarm to get notified when the value is outside a specified range. For more information, see &#91;Create an alarm model&#93;(https://docs.aws.amazon.com/iotevents/latest/developerguide/create-alarms.html) in the *Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.alarm_models" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alarm_model_name" /></td><td><code>string</code></td><td>The name of the alarm model.</td></tr>
<tr><td><CopyableCode code="alarm_model_description" /></td><td><code>string</code></td><td>The description of the alarm model.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see &#91;Amazon Resource Names (ARNs)&#93;(https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *General Reference*.</td></tr>
<tr><td><CopyableCode code="key" /></td><td><code>string</code></td><td>An input attribute used as a key to create an alarm. ITE routes &#91;inputs&#93;(https://docs.aws.amazon.com/iotevents/latest/apireference/API_Input.html) associated with this key to the alarm.</td></tr>
<tr><td><CopyableCode code="severity" /></td><td><code>integer</code></td><td>A non-negative integer that reflects the severity level of the alarm.</td></tr>
<tr><td><CopyableCode code="alarm_rule" /></td><td><code>object</code></td><td>Defines when your alarm is invoked.</td></tr>
<tr><td><CopyableCode code="alarm_event_actions" /></td><td><code>object</code></td><td>Contains information about one or more alarm actions.</td></tr>
<tr><td><CopyableCode code="alarm_capabilities" /></td><td><code>object</code></td><td>Contains the configuration information of alarm state changes.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the alarm model. The tags help you manage the alarm model. For more information, see &#91;Tagging your resources&#93;(https://docs.aws.amazon.com/iotevents/latest/developerguide/tagging-iotevents.html) in the *Developer Guide*.<br />You can create up to 50 tags for one alarm model.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html"><code>AWS::IoTEvents::AlarmModel</code></a>.

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
Gets all <code>alarm_models</code> in a region.
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
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>alarm_model</code>.
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
