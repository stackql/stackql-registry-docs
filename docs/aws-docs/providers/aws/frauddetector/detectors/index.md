---
title: detectors
hide_title: false
hide_table_of_contents: false
keywords:
  - detectors
  - frauddetector
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


Used to retrieve a list of <code>detectors</code> in a region or to create or delete a <code>detectors</code> resource, use <code>detector</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema for a Detector in Amazon Fraud Detector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.frauddetector.detectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the detector.</td></tr>
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
    <td><CopyableCode code="DetectorId, EventType, Rules, region" /></td>
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
FROM aws.frauddetector.detectors
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>detector</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.frauddetector.detectors (
 DetectorId,
 Rules,
 EventType,
 region
)
SELECT 
'{{ DetectorId }}',
 '{{ Rules }}',
 '{{ EventType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.frauddetector.detectors (
 DetectorId,
 DetectorVersionStatus,
 RuleExecutionMode,
 Tags,
 Description,
 Rules,
 EventType,
 AssociatedModels,
 region
)
SELECT 
 '{{ DetectorId }}',
 '{{ DetectorVersionStatus }}',
 '{{ RuleExecutionMode }}',
 '{{ Tags }}',
 '{{ Description }}',
 '{{ Rules }}',
 '{{ EventType }}',
 '{{ AssociatedModels }}',
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
  - name: detector
    props:
      - name: DetectorId
        value: '{{ DetectorId }}'
      - name: DetectorVersionStatus
        value: '{{ DetectorVersionStatus }}'
      - name: RuleExecutionMode
        value: '{{ RuleExecutionMode }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Description
        value: '{{ Description }}'
      - name: Rules
        value:
          - RuleId: '{{ RuleId }}'
            RuleVersion: '{{ RuleVersion }}'
            DetectorId: '{{ DetectorId }}'
            Expression: '{{ Expression }}'
            Language: '{{ Language }}'
            Outcomes:
              - Name: '{{ Name }}'
                Tags:
                  - null
                Description: '{{ Description }}'
            Arn: '{{ Arn }}'
            Description: '{{ Description }}'
            Tags:
              - null
            CreatedTime: '{{ CreatedTime }}'
            LastUpdatedTime: '{{ LastUpdatedTime }}'
      - name: EventType
        value:
          Name: '{{ Name }}'
          Tags:
            - null
          Description: '{{ Description }}'
          EventVariables:
            - Arn: '{{ Arn }}'
              Inline: '{{ Inline }}'
              Name: '{{ Name }}'
              DataSource: '{{ DataSource }}'
              DataType: '{{ DataType }}'
              DefaultValue: '{{ DefaultValue }}'
              VariableType: '{{ VariableType }}'
              Description: '{{ Description }}'
              Tags:
                - null
              CreatedTime: '{{ CreatedTime }}'
              LastUpdatedTime: '{{ LastUpdatedTime }}'
          Labels:
            - Name: '{{ Name }}'
              Tags:
                - null
              Description: '{{ Description }}'
          EntityTypes:
            - Arn: '{{ Arn }}'
              Inline: '{{ Inline }}'
              Name: '{{ Name }}'
              Description: '{{ Description }}'
              Tags:
                - null
              CreatedTime: '{{ CreatedTime }}'
              LastUpdatedTime: '{{ LastUpdatedTime }}'
      - name: AssociatedModels
        value:
          - Arn: '{{ Arn }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.frauddetector.detectors
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>detectors</code> resource, the following permissions are required:

### Create
```json
frauddetector:PutDetector,
frauddetector:CreateDetectorVersion,
frauddetector:UpdateDetectorVersionStatus,
frauddetector:CreateRule,
frauddetector:CreateVariable,
frauddetector:PutLabel,
frauddetector:PutOutcome,
frauddetector:PutEntityType,
frauddetector:PutEventType,
frauddetector:DescribeDetector,
frauddetector:GetDetectors,
frauddetector:GetDetectorVersion,
frauddetector:GetRules,
frauddetector:GetVariables,
frauddetector:GetEventTypes,
frauddetector:GetExternalModels,
frauddetector:GetModelVersion,
frauddetector:GetLabels,
frauddetector:GetOutcomes,
frauddetector:GetEntityTypes,
frauddetector:ListTagsForResource
```

### Delete
```json
frauddetector:GetDetectors,
frauddetector:GetDetectorVersion,
frauddetector:DescribeDetector,
frauddetector:GetRules,
frauddetector:GetVariables,
frauddetector:GetEventTypes,
frauddetector:GetLabels,
frauddetector:GetOutcomes,
frauddetector:GetEntityTypes,
frauddetector:DeleteDetector,
frauddetector:DeleteDetectorVersion,
frauddetector:DeleteRule,
frauddetector:DeleteEventType,
frauddetector:DeleteVariable,
frauddetector:DeleteLabel,
frauddetector:DeleteOutcome,
frauddetector:DeleteEntityType,
frauddetector:ListTagsForResource
```

### List
```json
frauddetector:GetDetectors,
frauddetector:GetDetectorVersion,
frauddetector:DescribeDetector,
frauddetector:GetRules,
frauddetector:GetVariables,
frauddetector:GetEventTypes,
frauddetector:GetExternalModels,
frauddetector:GetModelVersion,
frauddetector:GetLabels,
frauddetector:GetOutcomes,
frauddetector:GetEntityTypes,
frauddetector:ListTagsForResource
```

