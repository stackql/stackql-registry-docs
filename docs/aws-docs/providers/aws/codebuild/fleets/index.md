---
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
  - codebuild
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

Creates, updates, deletes or gets a <code>fleet</code> resource or lists <code>fleets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CodeBuild::Fleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codebuild.fleets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="base_capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="compute_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="overflow_behavior" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="fleet_service_role" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="fleet_vpc_config" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>fleets</code> in a region.
```sql
SELECT
region,
arn
FROM aws.codebuild.fleets
WHERE region = 'us-east-1';
```
Gets all properties from a <code>fleet</code>.
```sql
SELECT
region,
name,
base_capacity,
environment_type,
compute_type,
overflow_behavior,
fleet_service_role,
fleet_vpc_config,
tags,
arn
FROM aws.codebuild.fleets
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>fleet</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.codebuild.fleets (
 Name,
 BaseCapacity,
 EnvironmentType,
 ComputeType,
 OverflowBehavior,
 FleetServiceRole,
 FleetVpcConfig,
 Tags,
 region
)
SELECT 
'{{ Name }}',
 '{{ BaseCapacity }}',
 '{{ EnvironmentType }}',
 '{{ ComputeType }}',
 '{{ OverflowBehavior }}',
 '{{ FleetServiceRole }}',
 '{{ FleetVpcConfig }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.codebuild.fleets (
 Name,
 BaseCapacity,
 EnvironmentType,
 ComputeType,
 OverflowBehavior,
 FleetServiceRole,
 FleetVpcConfig,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ BaseCapacity }}',
 '{{ EnvironmentType }}',
 '{{ ComputeType }}',
 '{{ OverflowBehavior }}',
 '{{ FleetServiceRole }}',
 '{{ FleetVpcConfig }}',
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
  - name: fleet
    props:
      - name: Name
        value: '{{ Name }}'
      - name: BaseCapacity
        value: '{{ BaseCapacity }}'
      - name: EnvironmentType
        value: '{{ EnvironmentType }}'
      - name: ComputeType
        value: '{{ ComputeType }}'
      - name: OverflowBehavior
        value: '{{ OverflowBehavior }}'
      - name: FleetServiceRole
        value: '{{ FleetServiceRole }}'
      - name: FleetVpcConfig
        value:
          VpcId: '{{ VpcId }}'
          Subnets:
            - '{{ Subnets[0] }}'
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
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
DELETE FROM aws.codebuild.fleets
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>fleets</code> resource, the following permissions are required:

### Create
```json
codebuild:BatchGetFleets,
codebuild:CreateFleet,
iam:PassRole
```

### Delete
```json
codebuild:BatchGetFleets,
codebuild:DeleteFleet
```

### Read
```json
codebuild:BatchGetFleets
```

### List
```json
codebuild:ListFleets
```

### Update
```json
codebuild:BatchGetFleets,
codebuild:UpdateFleet,
iam:PassRole
```

