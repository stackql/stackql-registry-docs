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

Creates, updates, deletes or gets a <code>launch</code> resource or lists <code>launches</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Evidently::Launch.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.evidently.launches" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="project" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="randomization_salt" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="scheduled_splits_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="groups" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="metric_monitors" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="execution_status" /></td><td><code>object</code></td><td>Start or Stop Launch Launch. Default is not started.</td></tr>
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
    <td><CopyableCode code="Name, Project, Groups, ScheduledSplitsConfig, region" /></td>
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

Gets all properties from a <code>launch</code>.
```sql
SELECT
region,
arn,
name,
project,
description,
randomization_salt,
scheduled_splits_config,
groups,
metric_monitors,
tags,
execution_status
FROM aws.evidently.launches
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>launch</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.evidently.launches (
 Name,
 Project,
 ScheduledSplitsConfig,
 Groups,
 region
)
SELECT 
'{{ Name }}',
 '{{ Project }}',
 '{{ ScheduledSplitsConfig }}',
 '{{ Groups }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ Name }}',
 '{{ Project }}',
 '{{ Description }}',
 '{{ RandomizationSalt }}',
 '{{ ScheduledSplitsConfig }}',
 '{{ Groups }}',
 '{{ MetricMonitors }}',
 '{{ Tags }}',
 '{{ ExecutionStatus }}',
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
  - name: launch
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Project
        value: '{{ Project }}'
      - name: Description
        value: '{{ Description }}'
      - name: RandomizationSalt
        value: '{{ RandomizationSalt }}'
      - name: ScheduledSplitsConfig
        value:
          - StartTime: '{{ StartTime }}'
            GroupWeights:
              - GroupName: '{{ GroupName }}'
                SplitWeight: '{{ SplitWeight }}'
            SegmentOverrides:
              - Segment: '{{ Segment }}'
                EvaluationOrder: '{{ EvaluationOrder }}'
                Weights:
                  - null
      - name: Groups
        value:
          - GroupName: '{{ GroupName }}'
            Description: '{{ Description }}'
            Feature: '{{ Feature }}'
            Variation: '{{ Variation }}'
      - name: MetricMonitors
        value:
          - MetricName: '{{ MetricName }}'
            EntityIdKey: '{{ EntityIdKey }}'
            ValueKey: '{{ ValueKey }}'
            EventPattern: '{{ EventPattern }}'
            UnitLabel: '{{ UnitLabel }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: ExecutionStatus
        value:
          Status: '{{ Status }}'
          DesiredState: '{{ DesiredState }}'
          Reason: '{{ Reason }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
evidently:GetLaunch,
evidently:ListTagsForResource
```

### Update
```json
evidently:UpdateLaunch,
evidently:ListTagsForResource,
evidently:TagResource,
evidently:UntagResource,
evidently:GetLaunch,
evidently:StartLaunch,
evidently:StopLaunch
```

### Delete
```json
evidently:DeleteLaunch,
evidently:UntagResource,
evidently:GetLaunch
```

