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

Creates, updates, deletes or gets a <code>stack</code> resource or lists <code>stacks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CloudFormation::Stack resource nests a stack as a resource in a top-level template.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.stacks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="capabilities" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="outputs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="disable_rollback" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_termination_protection" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="notification_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="parent_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="root_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="change_set_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_policy_body" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_policy_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_status_reason" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="template_body" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="template_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="timeout_in_minutes" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="last_update_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stack.html"><code>AWS::CloudFormation::Stack</code></a>.

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
    <td><CopyableCode code="StackName, region" /></td>
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
Gets all <code>stacks</code> in a region.
```sql
SELECT
region,
capabilities,
role_arn,
outputs,
description,
disable_rollback,
enable_termination_protection,
notification_arns,
parameters,
parent_id,
root_id,
change_set_id,
stack_name,
stack_id,
stack_policy_body,
stack_policy_url,
stack_status,
stack_status_reason,
tags,
template_body,
template_url,
timeout_in_minutes,
last_update_time,
creation_time
FROM aws.cloudformation.stacks
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>stack</code>.
```sql
SELECT
region,
capabilities,
role_arn,
outputs,
description,
disable_rollback,
enable_termination_protection,
notification_arns,
parameters,
parent_id,
root_id,
change_set_id,
stack_name,
stack_id,
stack_policy_body,
stack_policy_url,
stack_status,
stack_status_reason,
tags,
template_body,
template_url,
timeout_in_minutes,
last_update_time,
creation_time
FROM aws.cloudformation.stacks
WHERE region = 'us-east-1' AND data__Identifier = '<StackId>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Update
```json
cloudformation:DescribeStacks,
cloudformation:UpdateStack,
cloudformation:UpdateTerminationProtection,
cloudformation:SetStackPolicy,
iam:PassRole
```

### Delete
```json
cloudformation:DescribeStacks,
cloudformation:DeleteStack
```

### Read
```json
cloudformation:DescribeStacks,
cloudformation:GetStackPolicy,
cloudformation:GetTemplate
```

### List
```json
cloudformation:ListStacks
```
