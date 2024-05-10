---
title: stacks
hide_title: false
hide_table_of_contents: false
keywords:
  - stacks
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


Used to retrieve a list of <code>stacks</code> in a region or to create or delete a <code>stacks</code> resource, use <code>stack</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CloudFormation::Stack resource nests a stack as a resource in a top-level template.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.stacks" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="stack_id" /></td><td><code>string</code></td><td></td></tr>
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
stack_id
FROM aws.cloudformation.stacks
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>stack</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- stack.iql (required properties only)
INSERT INTO aws.cloudformation.stacks (
 StackName,
 region
)
SELECT 
'{{ StackName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- stack.iql (all properties)
INSERT INTO aws.cloudformation.stacks (
 Capabilities,
 RoleARN,
 Description,
 DisableRollback,
 EnableTerminationProtection,
 NotificationARNs,
 Parameters,
 StackName,
 StackPolicyBody,
 StackPolicyURL,
 StackStatusReason,
 Tags,
 TemplateBody,
 TemplateURL,
 TimeoutInMinutes,
 region
)
SELECT 
 '{{ Capabilities }}',
 '{{ RoleARN }}',
 '{{ Description }}',
 '{{ DisableRollback }}',
 '{{ EnableTerminationProtection }}',
 '{{ NotificationARNs }}',
 '{{ Parameters }}',
 '{{ StackName }}',
 '{{ StackPolicyBody }}',
 '{{ StackPolicyURL }}',
 '{{ StackStatusReason }}',
 '{{ Tags }}',
 '{{ TemplateBody }}',
 '{{ TemplateURL }}',
 '{{ TimeoutInMinutes }}',
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
  - name: stack
    props:
      - name: Capabilities
        value:
          - '{{ Capabilities[0] }}'
      - name: RoleARN
        value: '{{ RoleARN }}'
      - name: Description
        value: '{{ Description }}'
      - name: DisableRollback
        value: '{{ DisableRollback }}'
      - name: EnableTerminationProtection
        value: '{{ EnableTerminationProtection }}'
      - name: NotificationARNs
        value:
          - '{{ NotificationARNs[0] }}'
      - name: Parameters
        value: {}
      - name: StackName
        value: '{{ StackName }}'
      - name: StackPolicyBody
        value: {}
      - name: StackPolicyURL
        value: '{{ StackPolicyURL }}'
      - name: StackStatusReason
        value: '{{ StackStatusReason }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TemplateBody
        value: {}
      - name: TemplateURL
        value: '{{ TemplateURL }}'
      - name: TimeoutInMinutes
        value: '{{ TimeoutInMinutes }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cloudformation.stacks
WHERE data__Identifier = '<StackId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>stacks</code> resource, the following permissions are required:

### Create
```json
cloudformation:DescribeStacks,
cloudformation:CreateStack,
iam:PassRole
```

### Delete
```json
cloudformation:DescribeStacks,
cloudformation:DeleteStack
```

### List
```json
cloudformation:ListStacks
```

