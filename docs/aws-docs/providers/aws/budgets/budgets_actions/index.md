---
title: budgets_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - budgets_actions
  - budgets
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


Used to retrieve a list of <code>budgets_actions</code> in a region or to create or delete a <code>budgets_actions</code> resource, use <code>budgets_action</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>budgets_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.budgets.budgets_actions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="action_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="budget_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="BudgetName, NotificationType, ActionType, ActionThreshold, ExecutionRoleArn, Definition, Subscribers, region" /></td>
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
action_id,
budget_name
FROM aws.budgets.budgets_actions
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>budgets_action</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.budgets.budgets_actions (
 BudgetName,
 NotificationType,
 ActionType,
 ActionThreshold,
 ExecutionRoleArn,
 Subscribers,
 Definition,
 region
)
SELECT 
'{{ BudgetName }}',
 '{{ NotificationType }}',
 '{{ ActionType }}',
 '{{ ActionThreshold }}',
 '{{ ExecutionRoleArn }}',
 '{{ Subscribers }}',
 '{{ Definition }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.budgets.budgets_actions (
 BudgetName,
 NotificationType,
 ActionType,
 ActionThreshold,
 ExecutionRoleArn,
 ApprovalModel,
 Subscribers,
 Definition,
 region
)
SELECT 
 '{{ BudgetName }}',
 '{{ NotificationType }}',
 '{{ ActionType }}',
 '{{ ActionThreshold }}',
 '{{ ExecutionRoleArn }}',
 '{{ ApprovalModel }}',
 '{{ Subscribers }}',
 '{{ Definition }}',
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
  - name: budgets_action
    props:
      - name: BudgetName
        value: '{{ BudgetName }}'
      - name: NotificationType
        value: '{{ NotificationType }}'
      - name: ActionType
        value: '{{ ActionType }}'
      - name: ActionThreshold
        value:
          Value: null
          Type: '{{ Type }}'
      - name: ExecutionRoleArn
        value: '{{ ExecutionRoleArn }}'
      - name: ApprovalModel
        value: '{{ ApprovalModel }}'
      - name: Subscribers
        value:
          - Type: '{{ Type }}'
            Address: '{{ Address }}'
      - name: Definition
        value:
          IamActionDefinition:
            PolicyArn: '{{ PolicyArn }}'
            Roles:
              - '{{ Roles[0] }}'
            Groups:
              - '{{ Groups[0] }}'
            Users:
              - '{{ Users[0] }}'
          ScpActionDefinition:
            PolicyId: '{{ PolicyId }}'
            TargetIds:
              - '{{ TargetIds[0] }}'
          SsmActionDefinition:
            Subtype: '{{ Subtype }}'
            Region: '{{ Region }}'
            InstanceIds:
              - '{{ InstanceIds[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.budgets.budgets_actions
WHERE data__Identifier = '<ActionId|BudgetName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>budgets_actions</code> resource, the following permissions are required:

### Create
```json
budgets:CreateBudgetAction,
iam:PassRole
```

### Delete
```json
budgets:DeleteBudgetAction
```

### List
```json
budgets:DescribeBudgetActionsForAccount,
budgets:DescribeBudgetActionsForBudget
```

