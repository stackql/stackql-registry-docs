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

Creates, updates, deletes or gets a <code>state_machine</code> resource or lists <code>state_machines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for StateMachine</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.stepfunctions.state_machines" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="definition_substitutions" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="definition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state_machine_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tracing_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="definition_string" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="logging_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="state_machine_revision_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="definition_s3_location" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state_machine_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
Gets all <code>state_machines</code> in a region.
```sql
SELECT
region,
definition_substitutions,
definition,
role_arn,
name,
state_machine_type,
tracing_configuration,
definition_string,
logging_configuration,
state_machine_revision_id,
definition_s3_location,
arn,
state_machine_name,
tags
FROM aws.stepfunctions.state_machines
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>state_machine</code>.
```sql
SELECT
region,
definition_substitutions,
definition,
role_arn,
name,
state_machine_type,
tracing_configuration,
definition_string,
logging_configuration,
state_machine_revision_id,
definition_s3_location,
arn,
state_machine_name,
tags
FROM aws.stepfunctions.state_machines
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

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

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.stepfunctions.state_machines
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>state_machines</code> resource, the following permissions are required:

### Read
```json
states:DescribeStateMachine,
states:ListTagsForResource
```

### Create
```json
states:CreateStateMachine,
states:DescribeStateMachine,
states:TagResource,
iam:PassRole,
s3:GetObject
```

### Update
```json
states:UpdateStateMachine,
states:TagResource,
states:UntagResource,
states:ListTagsForResource,
iam:PassRole
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

