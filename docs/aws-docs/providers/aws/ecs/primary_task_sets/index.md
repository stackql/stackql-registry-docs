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


Used to retrieve a list of <code>primary_task_sets</code> in a region or to create or delete a <code>primary_task_sets</code> resource, use <code>primary_task_set</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>primary_task_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A pseudo-resource that manages which of your ECS task sets is primary.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.primary_task_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.</td></tr>
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
cluster,
service
FROM aws.ecs.primary_task_sets
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
 "Cluster": "{{ Cluster }}",
 "TaskSetId": "{{ TaskSetId }}",
 "Service": "{{ Service }}"
}
>>>
--required properties only
INSERT INTO aws.ecs.primary_task_sets (
 Cluster,
 TaskSetId,
 Service,
 region
)
SELECT 
{{ Cluster }},
 {{ TaskSetId }},
 {{ Service }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Cluster": "{{ Cluster }}",
 "TaskSetId": "{{ TaskSetId }}",
 "Service": "{{ Service }}"
}
>>>
--all properties
INSERT INTO aws.ecs.primary_task_sets (
 Cluster,
 TaskSetId,
 Service,
 region
)
SELECT 
 {{ Cluster }},
 {{ TaskSetId }},
 {{ Service }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ecs.primary_task_sets
WHERE data__Identifier = '<Cluster|Service>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>primary_task_sets</code> resource, the following permissions are required:

### Create
```json
ecs:DescribeTaskSets,
ecs:UpdateServicePrimaryTaskSet
```

