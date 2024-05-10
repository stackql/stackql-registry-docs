---
title: stack_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - stack_sets
  - cloudformation
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


Used to retrieve a list of <code>stack_sets</code> in a region or to create or delete a <code>stack_sets</code> resource, use <code>stack_set</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stack_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>StackSet as a resource provides one-click experience for provisioning a StackSet and StackInstances</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.stack_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="stack_set_id" /></td><td><code>string</code></td><td>The ID of the stack set that you're creating.</td></tr>
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
stack_set_id
FROM aws.cloudformation.stack_sets
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
 "StackSetName": "{{ StackSetName }}",
 "PermissionModel": "{{ PermissionModel }}"
}
>>>
--required properties only
INSERT INTO aws.cloudformation.stack_sets (
 StackSetName,
 PermissionModel,
 region
)
SELECT 
{{ StackSetName }},
 {{ PermissionModel }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "StackSetName": "{{ StackSetName }}",
 "AdministrationRoleARN": "{{ AdministrationRoleARN }}",
 "AutoDeployment": {
  "Enabled": "{{ Enabled }}",
  "RetainStacksOnAccountRemoval": "{{ RetainStacksOnAccountRemoval }}"
 },
 "Capabilities": [
  "{{ Capabilities[0] }}"
 ],
 "Description": "{{ Description }}",
 "ExecutionRoleName": "{{ ExecutionRoleName }}",
 "OperationPreferences": {
  "FailureToleranceCount": "{{ FailureToleranceCount }}",
  "FailureTolerancePercentage": "{{ FailureTolerancePercentage }}",
  "MaxConcurrentCount": "{{ MaxConcurrentCount }}",
  "MaxConcurrentPercentage": "{{ MaxConcurrentPercentage }}",
  "RegionOrder": [
   "{{ RegionOrder[0] }}"
  ],
  "RegionConcurrencyType": "{{ RegionConcurrencyType }}"
 },
 "StackInstancesGroup": [
  {
   "DeploymentTargets": {
    "Accounts": [
     "{{ Accounts[0] }}"
    ],
    "AccountsUrl": "{{ AccountsUrl }}",
    "OrganizationalUnitIds": [
     "{{ OrganizationalUnitIds[0] }}"
    ],
    "AccountFilterType": "{{ AccountFilterType }}"
   },
   "Regions": [
    null
   ],
   "ParameterOverrides": [
    {
     "ParameterKey": "{{ ParameterKey }}",
     "ParameterValue": "{{ ParameterValue }}"
    }
   ]
  }
 ],
 "Parameters": [
  null
 ],
 "PermissionModel": "{{ PermissionModel }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "TemplateBody": "{{ TemplateBody }}",
 "TemplateURL": "{{ TemplateURL }}",
 "CallAs": "{{ CallAs }}",
 "ManagedExecution": {
  "Active": "{{ Active }}"
 }
}
>>>
--all properties
INSERT INTO aws.cloudformation.stack_sets (
 StackSetName,
 AdministrationRoleARN,
 AutoDeployment,
 Capabilities,
 Description,
 ExecutionRoleName,
 OperationPreferences,
 StackInstancesGroup,
 Parameters,
 PermissionModel,
 Tags,
 TemplateBody,
 TemplateURL,
 CallAs,
 ManagedExecution,
 region
)
SELECT 
 {{ StackSetName }},
 {{ AdministrationRoleARN }},
 {{ AutoDeployment }},
 {{ Capabilities }},
 {{ Description }},
 {{ ExecutionRoleName }},
 {{ OperationPreferences }},
 {{ StackInstancesGroup }},
 {{ Parameters }},
 {{ PermissionModel }},
 {{ Tags }},
 {{ TemplateBody }},
 {{ TemplateURL }},
 {{ CallAs }},
 {{ ManagedExecution }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cloudformation.stack_sets
WHERE data__Identifier = '<StackSetId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>stack_sets</code> resource, the following permissions are required:

### Create
```json
cloudformation:GetTemplateSummary,
cloudformation:CreateStackSet,
cloudformation:CreateStackInstances,
cloudformation:DescribeStackSetOperation,
cloudformation:ListStackSetOperationResults,
cloudformation:TagResource,
iam:PassRole
```

### Delete
```json
cloudformation:DeleteStackSet,
cloudformation:DeleteStackInstances,
cloudformation:DescribeStackSet,
cloudformation:DescribeStackSetOperation,
cloudformation:ListStackSetOperationResults,
cloudformation:UntagResource
```

### List
```json
cloudformation:ListStackSets,
cloudformation:DescribeStackSet,
cloudformation:ListStackInstances,
cloudformation:DescribeStackInstance
```

