---
title: state_machine_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - state_machine_aliases
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

Creates, updates, deletes or gets a <code>state_machine_alias</code> resource or lists <code>state_machine_aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_machine_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for StateMachineAlias</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.stepfunctions.state_machine_aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the alias.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The alias name.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>An optional description of the alias.</td></tr>
<tr><td><CopyableCode code="routing_configuration" /></td><td><code>array</code></td><td>The routing configuration of the alias. One or two versions can be mapped to an alias to split StartExecution requests of the same state machine.</td></tr>
<tr><td><CopyableCode code="deployment_preference" /></td><td><code>object</code></td><td>The settings to enable gradual state machine deployments.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachinealias.html"><code>AWS::StepFunctions::StateMachineAlias</code></a>.

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
Gets all <code>state_machine_aliases</code> in a region.
```sql
SELECT
region,
arn,
name,
description,
routing_configuration,
deployment_preference
FROM aws.stepfunctions.state_machine_aliases
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>state_machine_alias</code>.
```sql
SELECT
region,
arn,
name,
description,
routing_configuration,
deployment_preference
FROM aws.stepfunctions.state_machine_aliases
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>state_machine_alias</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.stepfunctions.state_machine_aliases (
 Name,
 Description,
 RoutingConfiguration,
 DeploymentPreference,
 region
)
SELECT 
'{{ Name }}',
 '{{ Description }}',
 '{{ RoutingConfiguration }}',
 '{{ DeploymentPreference }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.stepfunctions.state_machine_aliases (
 Name,
 Description,
 RoutingConfiguration,
 DeploymentPreference,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ RoutingConfiguration }}',
 '{{ DeploymentPreference }}',
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
  - name: state_machine_alias
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: RoutingConfiguration
        value:
          - StateMachineVersionArn: '{{ StateMachineVersionArn }}'
            Weight: '{{ Weight }}'
      - name: DeploymentPreference
        value:
          StateMachineVersionArn: '{{ StateMachineVersionArn }}'
          Type: '{{ Type }}'
          Percentage: '{{ Percentage }}'
          Interval: '{{ Interval }}'
          Alarms:
            - '{{ Alarms[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.stepfunctions.state_machine_aliases
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>state_machine_aliases</code> resource, the following permissions are required:

### Create
```json
states:CreateStateMachineAlias,
states:DescribeStateMachineAlias
```

### Read
```json
states:DescribeStateMachineAlias
```

### Update
```json
cloudwatch:DescribeAlarms,
states:UpdateStateMachineAlias,
states:DescribeStateMachineAlias
```

### Delete
```json
states:DescribeStateMachineAlias,
states:DeleteStateMachineAlias
```

### List
```json
states:ListStateMachineAliases
```
