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

Creates, updates, deletes or gets a <code>profiling_group</code> resource or lists <code>profiling_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiling_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This resource schema represents the Profiling Group resource in the Amazon CodeGuru Profiler service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codeguruprofiler.profiling_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="profiling_group_name" /></td><td><code>string</code></td><td>The name of the profiling group.</td></tr>
<tr><td><CopyableCode code="compute_platform" /></td><td><code>string</code></td><td>The compute platform of the profiling group.</td></tr>
<tr><td><CopyableCode code="agent_permissions" /></td><td><code>object</code></td><td>The agent permissions attached to this profiling group.</td></tr>
<tr><td><CopyableCode code="anomaly_detection_notification_configuration" /></td><td><code>array</code></td><td>Configuration for Notification Channels for Anomaly Detection feature in CodeGuru Profiler which enables customers to detect anomalies in the application profile for those methods that represent the highest proportion of CPU time or latency</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified profiling group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags associated with a profiling group.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html"><code>AWS::CodeGuruProfiler::ProfilingGroup</code></a>.

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
    <td><CopyableCode code="ProfilingGroupName, region" /></td>
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
Gets all <code>profiling_groups</code> in a region.
```sql
SELECT
region,
profiling_group_name,
compute_platform,
agent_permissions,
anomaly_detection_notification_configuration,
arn,
tags
FROM aws.codeguruprofiler.profiling_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>profiling_group</code>.
```sql
SELECT
region,
profiling_group_name,
compute_platform,
agent_permissions,
anomaly_detection_notification_configuration,
arn,
tags
FROM aws.codeguruprofiler.profiling_groups
WHERE region = 'us-east-1' AND data__Identifier = '<ProfilingGroupName>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
codeguru-profiler:DescribeProfilingGroup,
codeguru-profiler:ListTagsForResource,
codeguru-profiler:GetNotificationConfiguration,
codeguru-profiler:GetPolicy
```

### Update
```json
sns:Publish,
codeguru-profiler:DescribeProfilingGroup,
codeguru-profiler:AddNotificationChannels,
codeguru-profiler:GetNotificationConfiguration,
codeguru-profiler:RemoveNotificationChannel,
codeguru-profiler:PutPermission,
codeguru-profiler:RemovePermission,
codeguru-profiler:GetPolicy,
codeguru-profiler:TagResource,
codeguru-profiler:UntagResource,
codeguru-profiler:ListTagsForResource
```

### Delete
```json
codeguru-profiler:DeleteProfilingGroup
```

### List
```json
codeguru-profiler:ListProfilingGroups,
codeguru-profiler:ListTagsForResource,
codeguru-profiler:GetNotificationConfiguration,
codeguru-profiler:GetPolicy
```
