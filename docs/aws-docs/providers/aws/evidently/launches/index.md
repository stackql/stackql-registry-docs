---
title: launches
hide_title: false
hide_table_of_contents: false
keywords:
  - launches
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


Used to retrieve a list of <code>launches</code> in a region or to create or delete a <code>launches</code> resource, use <code>launch</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Evidently::Launch.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.evidently.launches" /></td></tr>
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
FROM aws.evidently.launches
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
 "ScheduledSplitsConfig": [
  {
   "StartTime": "{{ StartTime }}",
   "GroupWeights": [
    {
     "GroupName": "{{ GroupName }}",
     "SplitWeight": "{{ SplitWeight }}"
    }
   ],
   "SegmentOverrides": [
    {
     "Segment": "{{ Segment }}",
     "EvaluationOrder": "{{ EvaluationOrder }}",
     "Weights": [
      null
     ]
    }
   ]
  }
 ],
 "Groups": [
  {
   "GroupName": "{{ GroupName }}",
   "Description": "{{ Description }}",
   "Feature": "{{ Feature }}",
   "Variation": "{{ Variation }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.evidently.launches (
 Name,
 Project,
 ScheduledSplitsConfig,
 Groups,
 region
)
SELECT 
{{ Name }},
 {{ Project }},
 {{ ScheduledSplitsConfig }},
 {{ Groups }},
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
 "RandomizationSalt": "{{ RandomizationSalt }}",
 "ScheduledSplitsConfig": [
  {
   "StartTime": "{{ StartTime }}",
   "GroupWeights": [
    {
     "GroupName": "{{ GroupName }}",
     "SplitWeight": "{{ SplitWeight }}"
    }
   ],
   "SegmentOverrides": [
    {
     "Segment": "{{ Segment }}",
     "EvaluationOrder": "{{ EvaluationOrder }}",
     "Weights": [
      null
     ]
    }
   ]
  }
 ],
 "Groups": [
  {
   "GroupName": "{{ GroupName }}",
   "Description": "{{ Description }}",
   "Feature": "{{ Feature }}",
   "Variation": "{{ Variation }}"
  }
 ],
 "MetricMonitors": [
  {
   "MetricName": "{{ MetricName }}",
   "EntityIdKey": "{{ EntityIdKey }}",
   "ValueKey": "{{ ValueKey }}",
   "EventPattern": "{{ EventPattern }}",
   "UnitLabel": "{{ UnitLabel }}"
  }
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "ExecutionStatus": {
  "Status": "{{ Status }}",
  "DesiredState": "{{ DesiredState }}",
  "Reason": "{{ Reason }}"
 }
}
>>>
--all properties
INSERT INTO aws.evidently.launches (
 Name,
 Project,
 Description,
 RandomizationSalt,
 ScheduledSplitsConfig,
 Groups,
 MetricMonitors,
 Tags,
 ExecutionStatus,
 region
)
SELECT 
 {{ Name }},
 {{ Project }},
 {{ Description }},
 {{ RandomizationSalt }},
 {{ ScheduledSplitsConfig }},
 {{ Groups }},
 {{ MetricMonitors }},
 {{ Tags }},
 {{ ExecutionStatus }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.evidently.launches
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>launches</code> resource, the following permissions are required:

### Create
```json
evidently:CreateLaunch,
evidently:TagResource,
evidently:GetLaunch,
evidently:StartLaunch
```

### Delete
```json
evidently:DeleteLaunch,
evidently:UntagResource,
evidently:GetLaunch
```

