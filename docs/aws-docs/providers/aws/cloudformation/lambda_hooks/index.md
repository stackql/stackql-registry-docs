---
title: lambda_hooks
hide_title: false
hide_table_of_contents: false
keywords:
  - lambda_hooks
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

Creates, updates, deletes or gets a <code>lambda_hook</code> resource or lists <code>lambda_hooks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lambda_hooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This is a CloudFormation resource for the first-party AWS::Hooks::LambdaHook.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.lambda_hooks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="lambda_function" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN), Partial ARN, name, version, or alias of the Lambda function to invoke with this hook.</td></tr>
<tr><td><CopyableCode code="hook_status" /></td><td><code>string</code></td><td>Attribute to specify which stacks this hook applies to or should get invoked for</td></tr>
<tr><td><CopyableCode code="target_operations" /></td><td><code>array</code></td><td>Which operations should this Hook run against? Resource changes, stacks or change sets.</td></tr>
<tr><td><CopyableCode code="failure_mode" /></td><td><code>string</code></td><td>Attribute to specify CloudFormation behavior on hook failure.</td></tr>
<tr><td><CopyableCode code="target_filters" /></td><td><code>object</code></td><td>Attribute to specify which targets should invoke the hook</td></tr>
<tr><td><CopyableCode code="stack_filters" /></td><td><code>object</code></td><td>Filters to allow hooks to target specific stack attributes</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>The typename alias for the hook.</td></tr>
<tr><td><CopyableCode code="hook_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the activated hook</td></tr>
<tr><td><CopyableCode code="execution_role" /></td><td><code>string</code></td><td>The execution role ARN assumed by Hooks to invoke Lambda.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-lambdahook.html"><code>AWS::CloudFormation::LambdaHook</code></a>.

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
    <td><CopyableCode code="LambdaFunction, FailureMode, Alias, ExecutionRole, TargetOperations, HookStatus, region" /></td>
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
Gets all <code>lambda_hooks</code> in a region.
```sql
SELECT
region,
lambda_function,
hook_status,
target_operations,
failure_mode,
target_filters,
stack_filters,
alias,
hook_arn,
execution_role
FROM aws.cloudformation.lambda_hooks
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>lambda_hook</code>.
```sql
SELECT
region,
lambda_function,
hook_status,
target_operations,
failure_mode,
target_filters,
stack_filters,
alias,
hook_arn,
execution_role
FROM aws.cloudformation.lambda_hooks
WHERE region = 'us-east-1' AND data__Identifier = '<HookArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>lambda_hook</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudformation.lambda_hooks (
 LambdaFunction,
 HookStatus,
 TargetOperations,
 FailureMode,
 Alias,
 ExecutionRole,
 region
)
SELECT 
'{{ LambdaFunction }}',
 '{{ HookStatus }}',
 '{{ TargetOperations }}',
 '{{ FailureMode }}',
 '{{ Alias }}',
 '{{ ExecutionRole }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudformation.lambda_hooks (
 LambdaFunction,
 HookStatus,
 TargetOperations,
 FailureMode,
 TargetFilters,
 StackFilters,
 Alias,
 ExecutionRole,
 region
)
SELECT 
 '{{ LambdaFunction }}',
 '{{ HookStatus }}',
 '{{ TargetOperations }}',
 '{{ FailureMode }}',
 '{{ TargetFilters }}',
 '{{ StackFilters }}',
 '{{ Alias }}',
 '{{ ExecutionRole }}',
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
  - name: lambda_hook
    props:
      - name: LambdaFunction
        value: '{{ LambdaFunction }}'
      - name: HookStatus
        value: '{{ HookStatus }}'
      - name: TargetOperations
        value:
          - '{{ TargetOperations[0] }}'
      - name: FailureMode
        value: '{{ FailureMode }}'
      - name: TargetFilters
        value: {}
      - name: StackFilters
        value:
          FilteringCriteria: '{{ FilteringCriteria }}'
          StackNames:
            Include:
              - '{{ Include[0] }}'
            Exclude:
              - null
          StackRoles:
            Include:
              - '{{ Include[0] }}'
            Exclude:
              - null
      - name: Alias
        value: '{{ Alias }}'
      - name: ExecutionRole
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cloudformation.lambda_hooks
WHERE data__Identifier = '<HookArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>lambda_hooks</code> resource, the following permissions are required:

### Create
```json
cloudformation:ListTypes,
cloudformation:ActivateType,
cloudformation:BatchDescribeTypeConfigurations,
cloudformation:DescribeType,
cloudformation:SetTypeConfiguration,
iam:PassRole
```

### Read
```json
cloudformation:BatchDescribeTypeConfigurations,
cloudformation:DescribeType
```

### Update
```json
cloudformation:BatchDescribeTypeConfigurations,
cloudformation:DescribeType,
cloudformation:SetTypeConfiguration,
iam:PassRole
```

### Delete
```json
cloudformation:BatchDescribeTypeConfigurations,
cloudformation:DeactivateType,
cloudformation:DescribeType,
cloudformation:SetTypeConfiguration
```

### List
```json
cloudformation:ListTypes,
cloudformation:BatchDescribeTypeConfigurations,
cloudformation:DescribeType
```
