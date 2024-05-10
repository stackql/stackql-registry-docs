---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
  - evidently
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


Used to retrieve a list of <code>experiments</code> in a region or to create or delete a <code>experiments</code> resource, use <code>experiment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Evidently::Experiment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.evidently.experiments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
FROM aws.evidently.experiments
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>experiment</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- experiment.iql (required properties only)
INSERT INTO aws.evidently.experiments (
 Name,
 Project,
 Treatments,
 MetricGoals,
 OnlineAbConfig,
 region
)
SELECT 
'{{ Name }}',
 '{{ Project }}',
 '{{ Treatments }}',
 '{{ MetricGoals }}',
 '{{ OnlineAbConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- experiment.iql (all properties)
INSERT INTO aws.evidently.experiments (
 Name,
 Project,
 Description,
 RunningStatus,
 RandomizationSalt,
 Treatments,
 MetricGoals,
 SamplingRate,
 OnlineAbConfig,
 Segment,
 RemoveSegment,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Project }}',
 '{{ Description }}',
 '{{ RunningStatus }}',
 '{{ RandomizationSalt }}',
 '{{ Treatments }}',
 '{{ MetricGoals }}',
 '{{ SamplingRate }}',
 '{{ OnlineAbConfig }}',
 '{{ Segment }}',
 '{{ RemoveSegment }}',
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
  - name: experiment
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Project
        value: '{{ Project }}'
      - name: Description
        value: '{{ Description }}'
      - name: RunningStatus
        value:
          Status: '{{ Status }}'
          AnalysisCompleteTime: '{{ AnalysisCompleteTime }}'
          Reason: '{{ Reason }}'
          DesiredState: '{{ DesiredState }}'
      - name: RandomizationSalt
        value: '{{ RandomizationSalt }}'
      - name: Treatments
        value:
          - TreatmentName: '{{ TreatmentName }}'
            Description: '{{ Description }}'
            Feature: '{{ Feature }}'
            Variation: '{{ Variation }}'
      - name: MetricGoals
        value:
          - MetricName: '{{ MetricName }}'
            EntityIdKey: '{{ EntityIdKey }}'
            ValueKey: '{{ ValueKey }}'
            EventPattern: '{{ EventPattern }}'
            UnitLabel: '{{ UnitLabel }}'
            DesiredChange: '{{ DesiredChange }}'
      - name: SamplingRate
        value: '{{ SamplingRate }}'
      - name: OnlineAbConfig
        value:
          ControlTreatmentName: '{{ ControlTreatmentName }}'
          TreatmentWeights:
            - Treatment: '{{ Treatment }}'
              SplitWeight: '{{ SplitWeight }}'
      - name: Segment
        value: '{{ Segment }}'
      - name: RemoveSegment
        value: '{{ RemoveSegment }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.evidently.experiments
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>experiments</code> resource, the following permissions are required:

### Create
```json
evidently:CreateExperiment,
evidently:TagResource,
evidently:GetExperiment,
evidently:StartExperiment
```

### Delete
```json
evidently:DeleteExperiment,
evidently:UntagResource,
evidently:GetExperiment
```

