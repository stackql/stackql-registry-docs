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


Used to retrieve a list of <code>state_machine_aliases</code> in a region or to create or delete a <code>state_machine_aliases</code> resource, use <code>state_machine_alias</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_machine_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for StateMachineAlias</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.stepfunctions.state_machine_aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the alias.</td></tr>
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
FROM aws.stepfunctions.state_machine_aliases
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
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "RoutingConfiguration": [
  {
   "StateMachineVersionArn": "{{ StateMachineVersionArn }}",
   "Weight": "{{ Weight }}"
  }
 ],
 "DeploymentPreference": {
  "StateMachineVersionArn": "{{ StateMachineVersionArn }}",
  "Type": "{{ Type }}",
  "Percentage": "{{ Percentage }}",
  "Interval": "{{ Interval }}",
  "Alarms": [
   "{{ Alarms[0] }}"
  ]
 }
}
>>>
--required properties only
INSERT INTO aws.stepfunctions.state_machine_aliases (
 Name,
 Description,
 RoutingConfiguration,
 DeploymentPreference,
 region
)
SELECT 
{{ Name }},
 {{ Description }},
 {{ RoutingConfiguration }},
 {{ DeploymentPreference }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "RoutingConfiguration": [
  {
   "StateMachineVersionArn": "{{ StateMachineVersionArn }}",
   "Weight": "{{ Weight }}"
  }
 ],
 "DeploymentPreference": {
  "StateMachineVersionArn": "{{ StateMachineVersionArn }}",
  "Type": "{{ Type }}",
  "Percentage": "{{ Percentage }}",
  "Interval": "{{ Interval }}",
  "Alarms": [
   "{{ Alarms[0] }}"
  ]
 }
}
>>>
--all properties
INSERT INTO aws.stepfunctions.state_machine_aliases (
 Name,
 Description,
 RoutingConfiguration,
 DeploymentPreference,
 region
)
SELECT 
 {{ Name }},
 {{ Description }},
 {{ RoutingConfiguration }},
 {{ DeploymentPreference }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
states:DescribeStateMachineAlias,
states:DeleteStateMachineAlias
```

### List
```json
states:ListStateMachineAliases
```

