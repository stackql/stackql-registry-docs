---
title: profiling_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - profiling_groups
  - codeguruprofiler
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


Used to retrieve a list of <code>profiling_groups</code> in a region or to create or delete a <code>profiling_groups</code> resource, use <code>profiling_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiling_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This resource schema represents the Profiling Group resource in the Amazon CodeGuru Profiler service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codeguruprofiler.profiling_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="profiling_group_name" /></td><td><code>string</code></td><td>The name of the profiling group.</td></tr>
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
profiling_group_name
FROM aws.codeguruprofiler.profiling_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>profiling_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- profiling_group.iql (required properties only)
INSERT INTO aws.codeguruprofiler.profiling_groups (
 ProfilingGroupName,
 region
)
SELECT 
'{{ ProfilingGroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- profiling_group.iql (all properties)
INSERT INTO aws.codeguruprofiler.profiling_groups (
 ProfilingGroupName,
 ComputePlatform,
 AgentPermissions,
 AnomalyDetectionNotificationConfiguration,
 Tags,
 region
)
SELECT 
 '{{ ProfilingGroupName }}',
 '{{ ComputePlatform }}',
 '{{ AgentPermissions }}',
 '{{ AnomalyDetectionNotificationConfiguration }}',
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
  - name: profiling_group
    props:
      - name: ProfilingGroupName
        value: '{{ ProfilingGroupName }}'
      - name: ComputePlatform
        value: '{{ ComputePlatform }}'
      - name: AgentPermissions
        value:
          Principals:
            - '{{ Principals[0] }}'
      - name: AnomalyDetectionNotificationConfiguration
        value:
          - channelId: '{{ channelId }}'
            channelUri: '{{ channelUri }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.codeguruprofiler.profiling_groups
WHERE data__Identifier = '<ProfilingGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>profiling_groups</code> resource, the following permissions are required:

### Create
```json
sns:Publish,
codeguru-profiler:AddNotificationChannels,
codeguru-profiler:CreateProfilingGroup,
codeguru-profiler:PutPermission,
codeguru-profiler:TagResource
```

### Delete
```json
codeguru-profiler:DeleteProfilingGroup
```

### List
```json
codeguru-profiler:ListProfilingGroups,
codeguru-profiler:ListTagsForResource
```

