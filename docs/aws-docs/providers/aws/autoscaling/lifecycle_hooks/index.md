---
title: lifecycle_hooks
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_hooks
  - autoscaling
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


Used to retrieve a list of <code>lifecycle_hooks</code> in a region or to create or delete a <code>lifecycle_hooks</code> resource, use <code>lifecycle_hook</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lifecycle_hooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AutoScaling::LifecycleHook</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.lifecycle_hooks" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="auto_scaling_group_name" /></td><td><code>string</code></td><td>The name of the Auto Scaling group for the lifecycle hook.</td></tr>
<tr><td><CopyableCode code="lifecycle_hook_name" /></td><td><code>string</code></td><td>The name of the lifecycle hook.</td></tr>
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
auto_scaling_group_name,
lifecycle_hook_name
FROM aws.autoscaling.lifecycle_hooks
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>lifecycle_hook</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- lifecycle_hook.iql (required properties only)
INSERT INTO aws.autoscaling.lifecycle_hooks (
 AutoScalingGroupName,
 LifecycleTransition,
 region
)
SELECT 
'{{ AutoScalingGroupName }}',
 '{{ LifecycleTransition }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- lifecycle_hook.iql (all properties)
INSERT INTO aws.autoscaling.lifecycle_hooks (
 AutoScalingGroupName,
 DefaultResult,
 HeartbeatTimeout,
 LifecycleHookName,
 LifecycleTransition,
 NotificationMetadata,
 NotificationTargetARN,
 RoleARN,
 region
)
SELECT 
 '{{ AutoScalingGroupName }}',
 '{{ DefaultResult }}',
 '{{ HeartbeatTimeout }}',
 '{{ LifecycleHookName }}',
 '{{ LifecycleTransition }}',
 '{{ NotificationMetadata }}',
 '{{ NotificationTargetARN }}',
 '{{ RoleARN }}',
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
  - name: lifecycle_hook
    props:
      - name: AutoScalingGroupName
        value: '{{ AutoScalingGroupName }}'
      - name: DefaultResult
        value: '{{ DefaultResult }}'
      - name: HeartbeatTimeout
        value: '{{ HeartbeatTimeout }}'
      - name: LifecycleHookName
        value: '{{ LifecycleHookName }}'
      - name: LifecycleTransition
        value: '{{ LifecycleTransition }}'
      - name: NotificationMetadata
        value: '{{ NotificationMetadata }}'
      - name: NotificationTargetARN
        value: '{{ NotificationTargetARN }}'
      - name: RoleARN
        value: '{{ RoleARN }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.autoscaling.lifecycle_hooks
WHERE data__Identifier = '<AutoScalingGroupName|LifecycleHookName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>lifecycle_hooks</code> resource, the following permissions are required:

### Create
```json
autoscaling:PutLifecycleHook,
autoscaling:DescribeLifecycleHooks,
iam:PassRole
```

### Delete
```json
autoscaling:DeleteLifecycleHook,
autoscaling:DescribeLifecycleHooks
```

### List
```json
autoscaling:DescribeLifecycleHooks
```

