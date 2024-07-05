---
title: stack_set_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - stack_set_tags
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

Expands all tag keys and values for <code>stack_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stack_set_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>StackSet as a resource provides one-click experience for provisioning a StackSet and StackInstances</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.stack_set_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="stack_set_name" /></td><td><code>string</code></td><td>The name to associate with the stack set. The name must be unique in the Region where you create your stack set.</td></tr>
<tr><td><CopyableCode code="stack_set_id" /></td><td><code>string</code></td><td>The ID of the stack set that you're creating.</td></tr>
<tr><td><CopyableCode code="administration_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account.</td></tr>
<tr><td><CopyableCode code="auto_deployment" /></td><td><code>object</code></td><td>Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if PermissionModel is SERVICE_MANAGED.</td></tr>
<tr><td><CopyableCode code="capabilities" /></td><td><code>array</code></td><td>In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for AWS CloudFormation to create the stack set and related stack instances.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the stack set. You can use the description to identify the stack set's purpose or other important information.</td></tr>
<tr><td><CopyableCode code="execution_role_name" /></td><td><code>string</code></td><td>The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.</td></tr>
<tr><td><CopyableCode code="operation_preferences" /></td><td><code>object</code></td><td>The user-specified preferences for how AWS CloudFormation performs a stack set operation.</td></tr>
<tr><td><CopyableCode code="stack_instances_group" /></td><td><code>array</code></td><td>A group of stack instances with parameters in some specific accounts and regions.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>array</code></td><td>The input parameters for the stack set template.</td></tr>
<tr><td><CopyableCode code="permission_model" /></td><td><code>string</code></td><td>Describes how the IAM roles required for stack set operations are created. By default, SELF-MANAGED is specified.</td></tr>
<tr><td><CopyableCode code="template_body" /></td><td><code>string</code></td><td>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.</td></tr>
<tr><td><CopyableCode code="template_url" /></td><td><code>string</code></td><td>Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.</td></tr>
<tr><td><CopyableCode code="call_as" /></td><td><code>string</code></td><td>Specifies the AWS account that you are acting from. By default, SELF is specified. For self-managed permissions, specify SELF; for service-managed permissions, if you are signed in to the organization's management account, specify SELF. If you are signed in to a delegated administrator account, specify DELEGATED_ADMIN.</td></tr>
<tr><td><CopyableCode code="managed_execution" /></td><td><code>object</code></td><td>Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>stack_sets</code> in a region.
```sql
SELECT
region,
stack_set_name,
stack_set_id,
administration_role_arn,
auto_deployment,
capabilities,
description,
execution_role_name,
operation_preferences,
stack_instances_group,
parameters,
permission_model,
template_body,
template_url,
call_as,
managed_execution,
tag_key,
tag_value
FROM aws.cloudformation.stack_set_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>stack_set_tags</code> resource, see <a href="/providers/aws/cloudformation/stack_sets/#permissions"><code>stack_sets</code></a>


