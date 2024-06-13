---
title: detector_models
hide_title: false
hide_table_of_contents: false
keywords:
  - detector_models
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

Creates, updates, deletes or gets a <code>detector_model</code> resource or lists <code>detector_models</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detector_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::DetectorModel resource creates a detector model. You create a *detector model* (a model of your equipment or process) using *states*. For each state, you define conditional (Boolean) logic that evaluates the incoming inputs to detect significant events. When an event is detected, it can change the state or trigger custom-built or predefined actions using other AWS services. You can define additional events that trigger actions when entering or exiting a state and, optionally, when a condition is met. For more information, see &#91;How to Use AWS IoT Events&#93;(https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.detector_models" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="detector_model_definition" /></td><td><code>object</code></td><td>Information that defines how a detector operates.</td></tr>
<tr><td><CopyableCode code="detector_model_description" /></td><td><code>string</code></td><td>A brief description of the detector model.</td></tr>
<tr><td><CopyableCode code="detector_model_name" /></td><td><code>string</code></td><td>The name of the detector model.</td></tr>
<tr><td><CopyableCode code="evaluation_method" /></td><td><code>string</code></td><td>Information about the order in which events are evaluated and how actions are executed.</td></tr>
<tr><td><CopyableCode code="key" /></td><td><code>string</code></td><td>The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.<br />This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.<br />For more information, see &#91;Tag&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).</td></tr>
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
    <td><CopyableCode code="DetectorModelDefinition, RoleArn, region" /></td>
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
List all <code>detector_models</code> in a region.
```sql
SELECT
region,
detector_model_name
FROM aws.iotevents.detector_models
WHERE region = 'us-east-1';
```
Gets all properties from a <code>detector_model</code>.
```sql
SELECT
region,
detector_model_definition,
detector_model_description,
detector_model_name,
evaluation_method,
key,
role_arn,
tags
FROM aws.iotevents.detector_models
WHERE region = 'us-east-1' AND data__Identifier = '<DetectorModelName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>detector_model</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotevents.detector_models (
 DetectorModelDefinition,
 RoleArn,
 region
)
SELECT 
'{{ DetectorModelDefinition }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotevents.detector_models (
 DetectorModelDefinition,
 DetectorModelDescription,
 DetectorModelName,
 EvaluationMethod,
 Key,
 RoleArn,
 Tags,
 region
)
SELECT 
 '{{ DetectorModelDefinition }}',
 '{{ DetectorModelDescription }}',
 '{{ DetectorModelName }}',
 '{{ EvaluationMethod }}',
 '{{ Key }}',
 '{{ RoleArn }}',
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
  - name: detector_model
    props:
      - name: DetectorModelDefinition
        value:
          InitialStateName: '{{ InitialStateName }}'
          States:
            - OnEnter:
                Events:
                  - Actions:
                      - ClearTimer:
                          TimerName: '{{ TimerName }}'
                        DynamoDB:
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
                        ResetTimer:
                          TimerName: '{{ TimerName }}'
                        SetTimer:
                          DurationExpression: '{{ DurationExpression }}'
                          Seconds: '{{ Seconds }}'
                          TimerName: '{{ TimerName }}'
                        SetVariable:
                          Value: '{{ Value }}'
                          VariableName: '{{ VariableName }}'
                        Sns:
                          Payload: null
                          TargetArn: '{{ TargetArn }}'
                        Sqs:
                          Payload: null
                          QueueUrl: '{{ QueueUrl }}'
                          UseBase64: '{{ UseBase64 }}'
                    Condition: '{{ Condition }}'
                    EventName: '{{ EventName }}'
              OnExit:
                Events:
                  - null
              OnInput:
                Events:
                  - null
                TransitionEvents:
                  - Actions:
                      - null
                    Condition: '{{ Condition }}'
                    EventName: '{{ EventName }}'
                    NextState: '{{ NextState }}'
              StateName: '{{ StateName }}'
      - name: DetectorModelDescription
        value: '{{ DetectorModelDescription }}'
      - name: DetectorModelName
        value: '{{ DetectorModelName }}'
      - name: EvaluationMethod
        value: '{{ EvaluationMethod }}'
      - name: Key
        value: '{{ Key }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
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
DELETE FROM aws.iotevents.detector_models
WHERE data__Identifier = '<DetectorModelName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>detector_models</code> resource, the following permissions are required:

### Create
```json
iotevents:CreateDetectorModel,
iotevents:UpdateInputRouting,
iotevents:DescribeDetectorModel,
iotevents:ListTagsForResource,
iotevents:TagResource,
iam:PassRole
```

### Read
```json
iotevents:DescribeDetectorModel,
iotevents:ListTagsForResource
```

### Update
```json
iotevents:UpdateDetectorModel,
iotevents:UpdateInputRouting,
iotevents:DescribeDetectorModel,
iotevents:ListTagsForResource,
iotevents:UntagResource,
iotevents:TagResource,
iam:PassRole
```

### Delete
```json
iotevents:DeleteDetectorModel,
iotevents:DescribeDetectorModel
```

### List
```json
iotevents:ListDetectorModels
```

