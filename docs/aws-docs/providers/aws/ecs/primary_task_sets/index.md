---
title: primary_task_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - primary_task_sets
  - ecs
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

Creates, updates, deletes or gets a <code>primary_task_set</code> resource or lists <code>primary_task_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>primary_task_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A pseudo-resource that manages which of your ECS task sets is primary.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.primary_task_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.</td></tr>
<tr><td><CopyableCode code="task_set_id" /></td><td><code>string</code></td><td>The ID or full Amazon Resource Name (ARN) of the task set.</td></tr>
<tr><td><CopyableCode code="service" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the service to create the task set in.</td></tr>
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
    <td><CopyableCode code="Cluster, Service, TaskSetId, region" /></td>
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

Gets all properties from an individual <code>primary_task_set</code>.
```sql
SELECT
region,
cluster,
task_set_id,
service
FROM aws.ecs.primary_task_sets
WHERE region = 'us-east-1' AND data__Identifier = '<Cluster>|<Service>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>primary_task_set</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ecs.primary_task_sets (
 Cluster,
 TaskSetId,
 Service,
 region
)
SELECT 
'{{ Cluster }}',
 '{{ TaskSetId }}',
 '{{ Service }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ecs.primary_task_sets (
 Cluster,
 TaskSetId,
 Service,
 region
)
SELECT 
 '{{ Cluster }}',
 '{{ TaskSetId }}',
 '{{ Service }}',
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
  - name: primary_task_set
    props:
      - name: Cluster
        value: '{{ Cluster }}'
      - name: TaskSetId
        value: '{{ TaskSetId }}'
      - name: Service
        value: '{{ Service }}'

```
</TabItem>
</Tabs>

## Permissions

To operate on the <code>primary_task_sets</code> resource, the following permissions are required:

### Create
```json
ecs:DescribeTaskSets,
ecs:UpdateServicePrimaryTaskSet
```

### Update
```json
ecs:DescribeTaskSets,
ecs:UpdateServicePrimaryTaskSet
```

