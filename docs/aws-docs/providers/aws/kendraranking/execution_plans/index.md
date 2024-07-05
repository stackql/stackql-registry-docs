---
title: execution_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - execution_plans
  - kendraranking
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

Creates, updates, deletes or gets an <code>execution_plan</code> resource or lists <code>execution_plans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>execution_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A KendraRanking Rescore execution plan</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kendraranking.execution_plans" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Unique ID of rescore execution plan</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the execution plan</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags for labeling the execution plan</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of kendra ranking rescore execution plan</td></tr>
<tr><td><CopyableCode code="capacity_units" /></td><td><code>object</code></td><td>Capacity units</td></tr>
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
    <td><CopyableCode code="Name, region" /></td>
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
Gets all <code>execution_plans</code> in a region.
```sql
SELECT
region,
id,
arn,
description,
tags,
name,
capacity_units
FROM aws.kendraranking.execution_plans
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>execution_plan</code>.
```sql
SELECT
region,
id,
arn,
description,
tags,
name,
capacity_units
FROM aws.kendraranking.execution_plans
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>execution_plan</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.kendraranking.execution_plans (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.kendraranking.execution_plans (
 Description,
 Tags,
 Name,
 CapacityUnits,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Tags }}',
 '{{ Name }}',
 '{{ CapacityUnits }}',
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
  - name: execution_plan
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Name
        value: '{{ Name }}'
      - name: CapacityUnits
        value:
          RescoreCapacityUnits: '{{ RescoreCapacityUnits }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.kendraranking.execution_plans
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>execution_plans</code> resource, the following permissions are required:

### Create
```json
kendra-ranking:CreateRescoreExecutionPlan,
kendra-ranking:DescribeRescoreExecutionPlan,
kendra-ranking:UpdateRescoreExecutionPlan,
kendra-ranking:ListTagsForResource,
kendra-ranking:TagResource
```

### Read
```json
kendra-ranking:DescribeRescoreExecutionPlan,
kendra-ranking:ListTagsForResource
```

### Update
```json
kendra-ranking:DescribeRescoreExecutionPlan,
kendra-ranking:UpdateRescoreExecutionPlan,
kendra-ranking:ListTagsForResource,
kendra-ranking:TagResource,
kendra-ranking:UntagResource
```

### Delete
```json
kendra-ranking:DescribeRescoreExecutionPlan,
kendra-ranking:DeleteRescoreExecutionPlan
```

### List
```json
kendra-ranking:ListRescoreExecutionPlans
```

