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


Used to retrieve a list of <code>detector_models</code> in a region or to create or delete a <code>detector_models</code> resource, use <code>detector_model</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detector_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::DetectorModel resource creates a detector model. You create a *detector model* (a model of your equipment or process) using *states*. For each state, you define conditional (Boolean) logic that evaluates the incoming inputs to detect significant events. When an event is detected, it can change the state or trigger custom-built or predefined actions using other AWS services. You can define additional events that trigger actions when entering or exiting a state and, optionally, when a condition is met. For more information, see &#91;How to Use AWS IoT Events&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;iotevents&#x2F;latest&#x2F;developerguide&#x2F;how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.detector_models" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="detector_model_name" /></td><td><code>string</code></td><td>The name of the detector model.</td></tr>
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
detector_model_name
FROM aws.iotevents.detector_models
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
 "DetectorModelDefinition": {
  "InitialStateName": "{{ InitialStateName }}",
  "States": [
   {
    "OnEnter": {
     "Events": [
      {
       "Actions": [
        {
         "ClearTimer": {
          "TimerName": "{{ TimerName }}"
         },
         "DynamoDB": {
          "HashKeyField": "{{ HashKeyField }}",
          "HashKeyType": "{{ HashKeyType }}",
          "HashKeyValue": "{{ HashKeyValue }}",
          "Operation": "{{ Operation }}",
          "Payload": {
           "ContentExpression": "{{ ContentExpression }}",
           "Type": "{{ Type }}"
          },
          "PayloadField": "{{ PayloadField }}",
          "RangeKeyField": "{{ RangeKeyField }}",
          "RangeKeyType": "{{ RangeKeyType }}",
          "RangeKeyValue": "{{ RangeKeyValue }}",
          "TableName": "{{ TableName }}"
         },
         "DynamoDBv2": {
          "Payload": null,
          "TableName": "{{ TableName }}"
         },
         "Firehose": {
          "DeliveryStreamName": "{{ DeliveryStreamName }}",
          "Payload": null,
          "Separator": "{{ Separator }}"
         },
         "IotEvents": {
          "InputName": "{{ InputName }}",
          "Payload": null
         },
         "IotSiteWise": {
          "AssetId": "{{ AssetId }}",
          "EntryId": "{{ EntryId }}",
          "PropertyAlias": "{{ PropertyAlias }}",
          "PropertyId": "{{ PropertyId }}",
          "PropertyValue": {
           "Quality": "{{ Quality }}",
           "Timestamp": {
            "OffsetInNanos": "{{ OffsetInNanos }}",
            "TimeInSeconds": "{{ TimeInSeconds }}"
           },
           "Value": {
            "BooleanValue": "{{ BooleanValue }}",
            "DoubleValue": "{{ DoubleValue }}",
            "IntegerValue": "{{ IntegerValue }}",
            "StringValue": "{{ StringValue }}"
           }
          }
         },
         "IotTopicPublish": {
          "MqttTopic": "{{ MqttTopic }}",
          "Payload": null
         },
         "Lambda": {
          "FunctionArn": "{{ FunctionArn }}",
          "Payload": null
         },
         "ResetTimer": {
          "TimerName": "{{ TimerName }}"
         },
         "SetTimer": {
          "DurationExpression": "{{ DurationExpression }}",
          "Seconds": "{{ Seconds }}",
          "TimerName": "{{ TimerName }}"
         },
         "SetVariable": {
          "Value": "{{ Value }}",
          "VariableName": "{{ VariableName }}"
         },
         "Sns": {
          "Payload": null,
          "TargetArn": "{{ TargetArn }}"
         },
         "Sqs": {
          "Payload": null,
          "QueueUrl": "{{ QueueUrl }}",
          "UseBase64": "{{ UseBase64 }}"
         }
        }
       ],
       "Condition": "{{ Condition }}",
       "EventName": "{{ EventName }}"
      }
     ]
    },
    "OnExit": {
     "Events": [
      null
     ]
    },
    "OnInput": {
     "Events": [
      null
     ],
     "TransitionEvents": [
      {
       "Actions": [
        null
       ],
       "Condition": "{{ Condition }}",
       "EventName": "{{ EventName }}",
       "NextState": "{{ NextState }}"
      }
     ]
    },
    "StateName": "{{ StateName }}"
   }
  ]
 },
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.iotevents.detector_models (
 DetectorModelDefinition,
 RoleArn,
 region
)
SELECT 
{{ DetectorModelDefinition }},
 {{ RoleArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DetectorModelDefinition": {
  "InitialStateName": "{{ InitialStateName }}",
  "States": [
   {
    "OnEnter": {
     "Events": [
      {
       "Actions": [
        {
         "ClearTimer": {
          "TimerName": "{{ TimerName }}"
         },
         "DynamoDB": {
          "HashKeyField": "{{ HashKeyField }}",
          "HashKeyType": "{{ HashKeyType }}",
          "HashKeyValue": "{{ HashKeyValue }}",
          "Operation": "{{ Operation }}",
          "Payload": {
           "ContentExpression": "{{ ContentExpression }}",
           "Type": "{{ Type }}"
          },
          "PayloadField": "{{ PayloadField }}",
          "RangeKeyField": "{{ RangeKeyField }}",
          "RangeKeyType": "{{ RangeKeyType }}",
          "RangeKeyValue": "{{ RangeKeyValue }}",
          "TableName": "{{ TableName }}"
         },
         "DynamoDBv2": {
          "Payload": null,
          "TableName": "{{ TableName }}"
         },
         "Firehose": {
          "DeliveryStreamName": "{{ DeliveryStreamName }}",
          "Payload": null,
          "Separator": "{{ Separator }}"
         },
         "IotEvents": {
          "InputName": "{{ InputName }}",
          "Payload": null
         },
         "IotSiteWise": {
          "AssetId": "{{ AssetId }}",
          "EntryId": "{{ EntryId }}",
          "PropertyAlias": "{{ PropertyAlias }}",
          "PropertyId": "{{ PropertyId }}",
          "PropertyValue": {
           "Quality": "{{ Quality }}",
           "Timestamp": {
            "OffsetInNanos": "{{ OffsetInNanos }}",
            "TimeInSeconds": "{{ TimeInSeconds }}"
           },
           "Value": {
            "BooleanValue": "{{ BooleanValue }}",
            "DoubleValue": "{{ DoubleValue }}",
            "IntegerValue": "{{ IntegerValue }}",
            "StringValue": "{{ StringValue }}"
           }
          }
         },
         "IotTopicPublish": {
          "MqttTopic": "{{ MqttTopic }}",
          "Payload": null
         },
         "Lambda": {
          "FunctionArn": "{{ FunctionArn }}",
          "Payload": null
         },
         "ResetTimer": {
          "TimerName": "{{ TimerName }}"
         },
         "SetTimer": {
          "DurationExpression": "{{ DurationExpression }}",
          "Seconds": "{{ Seconds }}",
          "TimerName": "{{ TimerName }}"
         },
         "SetVariable": {
          "Value": "{{ Value }}",
          "VariableName": "{{ VariableName }}"
         },
         "Sns": {
          "Payload": null,
          "TargetArn": "{{ TargetArn }}"
         },
         "Sqs": {
          "Payload": null,
          "QueueUrl": "{{ QueueUrl }}",
          "UseBase64": "{{ UseBase64 }}"
         }
        }
       ],
       "Condition": "{{ Condition }}",
       "EventName": "{{ EventName }}"
      }
     ]
    },
    "OnExit": {
     "Events": [
      null
     ]
    },
    "OnInput": {
     "Events": [
      null
     ],
     "TransitionEvents": [
      {
       "Actions": [
        null
       ],
       "Condition": "{{ Condition }}",
       "EventName": "{{ EventName }}",
       "NextState": "{{ NextState }}"
      }
     ]
    },
    "StateName": "{{ StateName }}"
   }
  ]
 },
 "DetectorModelDescription": "{{ DetectorModelDescription }}",
 "DetectorModelName": "{{ DetectorModelName }}",
 "EvaluationMethod": "{{ EvaluationMethod }}",
 "Key": "{{ Key }}",
 "RoleArn": "{{ RoleArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ DetectorModelDefinition }},
 {{ DetectorModelDescription }},
 {{ DetectorModelName }},
 {{ EvaluationMethod }},
 {{ Key }},
 {{ RoleArn }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
iotevents:DeleteDetectorModel,
iotevents:DescribeDetectorModel
```

### List
```json
iotevents:ListDetectorModels
```

