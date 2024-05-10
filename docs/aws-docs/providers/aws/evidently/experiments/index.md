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
 "Name": "{{ Name }}",
 "Project": "{{ Project }}",
 "Treatments": [
  {
   "TreatmentName": "{{ TreatmentName }}",
   "Description": "{{ Description }}",
   "Feature": "{{ Feature }}",
   "Variation": "{{ Variation }}"
  }
 ],
 "MetricGoals": [
  {
   "MetricName": "{{ MetricName }}",
   "EntityIdKey": "{{ EntityIdKey }}",
   "ValueKey": "{{ ValueKey }}",
   "EventPattern": "{{ EventPattern }}",
   "UnitLabel": "{{ UnitLabel }}",
   "DesiredChange": "{{ DesiredChange }}"
  }
 ],
 "OnlineAbConfig": {
  "ControlTreatmentName": "{{ ControlTreatmentName }}",
  "TreatmentWeights": [
   {
    "Treatment": "{{ Treatment }}",
    "SplitWeight": "{{ SplitWeight }}"
   }
  ]
 }
}
>>>
--required properties only
INSERT INTO aws.evidently.experiments (
 Name,
 Project,
 Treatments,
 MetricGoals,
 OnlineAbConfig,
 region
)
SELECT 
{{ .Name }},
 {{ .Project }},
 {{ .Treatments }},
 {{ .MetricGoals }},
 {{ .OnlineAbConfig }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Project": "{{ Project }}",
 "Description": "{{ Description }}",
 "RunningStatus": {
  "Status": "{{ Status }}",
  "AnalysisCompleteTime": "{{ AnalysisCompleteTime }}",
  "Reason": "{{ Reason }}",
  "DesiredState": "{{ DesiredState }}"
 },
 "RandomizationSalt": "{{ RandomizationSalt }}",
 "Treatments": [
  {
   "TreatmentName": "{{ TreatmentName }}",
   "Description": "{{ Description }}",
   "Feature": "{{ Feature }}",
   "Variation": "{{ Variation }}"
  }
 ],
 "MetricGoals": [
  {
   "MetricName": "{{ MetricName }}",
   "EntityIdKey": "{{ EntityIdKey }}",
   "ValueKey": "{{ ValueKey }}",
   "EventPattern": "{{ EventPattern }}",
   "UnitLabel": "{{ UnitLabel }}",
   "DesiredChange": "{{ DesiredChange }}"
  }
 ],
 "SamplingRate": "{{ SamplingRate }}",
 "OnlineAbConfig": {
  "ControlTreatmentName": "{{ ControlTreatmentName }}",
  "TreatmentWeights": [
   {
    "Treatment": "{{ Treatment }}",
    "SplitWeight": "{{ SplitWeight }}"
   }
  ]
 },
 "Segment": "{{ Segment }}",
 "RemoveSegment": "{{ RemoveSegment }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ .Name }},
 {{ .Project }},
 {{ .Description }},
 {{ .RunningStatus }},
 {{ .RandomizationSalt }},
 {{ .Treatments }},
 {{ .MetricGoals }},
 {{ .SamplingRate }},
 {{ .OnlineAbConfig }},
 {{ .Segment }},
 {{ .RemoveSegment }},
 {{ .Tags }},
 'us-east-1';
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

