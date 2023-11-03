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
Retrieves a list of <code>stack_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stack_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudformation.stack_sets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>StackSetName</code></td><td><code>string</code></td><td>The name to associate with the stack set. The name must be unique in the Region where you create your stack set.</td></tr><tr><td><code>StackSetId</code></td><td><code>string</code></td><td>The ID of the stack set that you're creating.</td></tr><tr><td><code>AdministrationRoleARN</code></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account.</td></tr><tr><td><code>AutoDeployment</code></td><td><code>undefined</code></td><td>Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if PermissionModel is SERVICE_MANAGED.</td></tr><tr><td><code>Capabilities</code></td><td><code>array</code></td><td>In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for AWS CloudFormation to create the stack set and related stack instances.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>A description of the stack set. You can use the description to identify the stack set's purpose or other important information.</td></tr><tr><td><code>ExecutionRoleName</code></td><td><code>string</code></td><td>The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.</td></tr><tr><td><code>OperationPreferences</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>StackInstancesGroup</code></td><td><code>array</code></td><td>A group of stack instances with parameters in some specific accounts and regions.</td></tr><tr><td><code>Parameters</code></td><td><code>array</code></td><td>The input parameters for the stack set template.</td></tr><tr><td><code>PermissionModel</code></td><td><code>string</code></td><td>Describes how the IAM roles required for stack set operations are created. By default, SELF-MANAGED is specified.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.</td></tr><tr><td><code>TemplateBody</code></td><td><code>string</code></td><td>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.</td></tr><tr><td><code>TemplateURL</code></td><td><code>string</code></td><td>Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.</td></tr><tr><td><code>CallAs</code></td><td><code>string</code></td><td>Specifies the AWS account that you are acting from. By default, SELF is specified. For self-managed permissions, specify SELF; for service-managed permissions, if you are signed in to the organization's management account, specify SELF. If you are signed in to a delegated administrator account, specify DELEGATED_ADMIN.</td></tr><tr><td><code>ManagedExecution</code></td><td><code>object</code></td><td>Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.cloudformation.stack_sets
WHERE region = 'us-east-1'
```
