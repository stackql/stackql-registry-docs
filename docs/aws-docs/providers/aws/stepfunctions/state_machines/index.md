---
title: state_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - state_machines
  - stepfunctions
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


Used to retrieve a list of <code>state_machines</code> in a region or to create or delete a <code>state_machines</code> resource, use <code>state_machine</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for StateMachine</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.stepfunctions.state_machines" /></td></tr>
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
    <td><CopyableCode code="RoleArn, region" /></td>
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
FROM aws.stepfunctions.state_machines
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>state_machine</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.stepfunctions.state_machines (
 RoleArn,
 region
)
SELECT 
'{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.stepfunctions.state_machines (
 DefinitionSubstitutions,
 Definition,
 RoleArn,
 StateMachineType,
 TracingConfiguration,
 DefinitionString,
 LoggingConfiguration,
 DefinitionS3Location,
 StateMachineName,
 Tags,
 region
)
SELECT 
 '{{ DefinitionSubstitutions }}',
 '{{ Definition }}',
 '{{ RoleArn }}',
 '{{ StateMachineType }}',
 '{{ TracingConfiguration }}',
 '{{ DefinitionString }}',
 '{{ LoggingConfiguration }}',
 '{{ DefinitionS3Location }}',
 '{{ StateMachineName }}',
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
  - name: state_machine
    props:
      - name: DefinitionSubstitutions
        value: {}
      - name: Definition
        value: {}
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: StateMachineType
        value: '{{ StateMachineType }}'
      - name: TracingConfiguration
        value:
          Enabled: '{{ Enabled }}'
      - name: DefinitionString
        value: '{{ DefinitionString }}'
      - name: LoggingConfiguration
        value:
          IncludeExecutionData: '{{ IncludeExecutionData }}'
          Destinations:
            - CloudWatchLogsLogGroup:
                LogGroupArn: '{{ LogGroupArn }}'
          Level: '{{ Level }}'
      - name: DefinitionS3Location
        value:
          Bucket: '{{ Bucket }}'
          Version: '{{ Version }}'
          Key: '{{ Key }}'
      - name: StateMachineName
        value: '{{ StateMachineName }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.stepfunctions.state_machines
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>state_machines</code> resource, the following permissions are required:

### Create
```json
states:CreateStateMachine,
states:DescribeStateMachine,
states:TagResource,
iam:PassRole,
s3:GetObject
```

### List
```json
states:ListStateMachines
```

### Delete
```json
states:DeleteStateMachine,
states:DescribeStateMachine
```

