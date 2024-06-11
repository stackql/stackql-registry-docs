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

Creates, updates, deletes or gets an <code>experiment</code> resource or lists <code>experiments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Evidently::Experiment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.evidently.experiments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="project" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="running_status" /></td><td><code>object</code></td><td>Start Experiment. Default is False</td></tr>
<tr><td><CopyableCode code="randomization_salt" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="treatments" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="metric_goals" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="sampling_rate" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="online_ab_config" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="segment" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="remove_segment" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="Name, Project, Treatments, MetricGoals, OnlineAbConfig, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an <code>experiment</code>.
```sql
SELECT
region,
arn,
name,
project,
description,
running_status,
randomization_salt,
treatments,
metric_goals,
sampling_rate,
online_ab_config,
segment,
remove_segment,
tags
FROM aws.evidently.experiments
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>experiment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
evidently:GetExperiment,
evidently:ListTagsForResource
```

### Update
```json
evidently:UpdateExperiment,
evidently:TagResource,
evidently:UntagResource,
evidently:GetExperiment,
evidently:StartExperiment,
evidently:StopExperiment
```

### Delete
```json
evidently:DeleteExperiment,
evidently:UntagResource,
evidently:GetExperiment
```

