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
FROM aws.stepfunctions.state_machines
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
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.stepfunctions.state_machines (
 RoleArn,
 region
)
SELECT 
{{ RoleArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DefinitionSubstitutions": {},
 "Definition": {},
 "RoleArn": "{{ RoleArn }}",
 "StateMachineType": "{{ StateMachineType }}",
 "TracingConfiguration": {
  "Enabled": "{{ Enabled }}"
 },
 "DefinitionString": "{{ DefinitionString }}",
 "LoggingConfiguration": {
  "IncludeExecutionData": "{{ IncludeExecutionData }}",
  "Destinations": [
   {
    "CloudWatchLogsLogGroup": {
     "LogGroupArn": "{{ LogGroupArn }}"
    }
   }
  ],
  "Level": "{{ Level }}"
 },
 "DefinitionS3Location": {
  "Bucket": "{{ Bucket }}",
  "Version": "{{ Version }}",
  "Key": "{{ Key }}"
 },
 "StateMachineName": "{{ StateMachineName }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--all properties
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
 {{ DefinitionSubstitutions }},
 {{ Definition }},
 {{ RoleArn }},
 {{ StateMachineType }},
 {{ TracingConfiguration }},
 {{ DefinitionString }},
 {{ LoggingConfiguration }},
 {{ DefinitionS3Location }},
 {{ StateMachineName }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

