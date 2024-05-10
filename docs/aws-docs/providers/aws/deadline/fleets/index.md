---
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
  - deadline
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


Used to retrieve a list of <code>fleets</code> in a region or to create or delete a <code>fleets</code> resource, use <code>fleet</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::Fleet Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.fleets" /></td></tr>
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
FROM aws.deadline.fleets
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- fleet.iql (required properties only)
INSERT INTO aws.deadline.fleets (
 Configuration,
 DisplayName,
 MaxWorkerCount,
 RoleArn,
 region
)
SELECT 
'{{ Configuration }}',
 '{{ DisplayName }}',
 '{{ MaxWorkerCount }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- fleet.iql (all properties)
INSERT INTO aws.deadline.fleets (
 Configuration,
 Description,
 DisplayName,
 FarmId,
 MaxWorkerCount,
 MinWorkerCount,
 RoleArn,
 region
)
SELECT 
 '{{ Configuration }}',
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ FarmId }}',
 '{{ MaxWorkerCount }}',
 '{{ MinWorkerCount }}',
 '{{ RoleArn }}',
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
      - name: Configuration
        value: null
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: FarmId
        value: '{{ FarmId }}'
      - name: MaxWorkerCount
        value: '{{ MaxWorkerCount }}'
      - name: MinWorkerCount
        value: '{{ MinWorkerCount }}'
      - name: RoleArn
        value: '{{ RoleArn }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.deadline.fleets
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>fleets</code> resource, the following permissions are required:

### Create
```json
deadline:CreateFleet,
deadline:GetFleet,
iam:PassRole,
identitystore:ListGroupMembershipsForMember,
logs:CreateLogGroup
```

### Delete
```json
deadline:DeleteFleet,
deadline:GetFleet,
identitystore:ListGroupMembershipsForMember
```

### List
```json
deadline:ListFleets,
identitystore:DescribeGroup,
identitystore:DescribeUser,
identitystore:ListGroupMembershipsForMember
```

