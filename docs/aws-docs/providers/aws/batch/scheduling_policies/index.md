---
title: scheduling_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduling_policies
  - batch
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


Used to retrieve a list of <code>scheduling_policies</code> in a region or to create or delete a <code>scheduling_policies</code> resource, use <code>scheduling_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduling_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type schema for AWS::Batch::SchedulingPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.batch.scheduling_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td></td></tr>
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
FROM aws.batch.scheduling_policies
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>scheduling_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- scheduling_policy.iql (required properties only)
INSERT INTO aws.batch.scheduling_policies (
 Name,
 FairsharePolicy,
 Tags,
 region
)
SELECT 
'{{ Name }}',
 '{{ FairsharePolicy }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- scheduling_policy.iql (all properties)
INSERT INTO aws.batch.scheduling_policies (
 Name,
 FairsharePolicy,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ FairsharePolicy }}',
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
  - name: scheduling_policy
    props:
      - name: Name
        value: '{{ Name }}'
      - name: FairsharePolicy
        value:
          ShareDecaySeconds: null
          ComputeReservation: null
          ShareDistribution:
            - ShareIdentifier: '{{ ShareIdentifier }}'
              WeightFactor: null
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.batch.scheduling_policies
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>scheduling_policies</code> resource, the following permissions are required:

### Create
```json
Batch:CreateSchedulingPolicy,
Batch:TagResource
```

### Delete
```json
Batch:DescribeSchedulingPolicies,
Batch:DeleteSchedulingPolicy
```

### List
```json
Batch:ListSchedulingPolicies,
Batch:DescribeSchedulingPolicies
```

