---
title: parameters
hide_title: false
hide_table_of_contents: false
keywords:
  - parameters
  - ssm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>parameters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>parameters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::SSM::Parameter`` resource creates an SSM parameter in SYSlong Parameter Store.&lt;br&#x2F;&gt;  To create an SSM parameter, you must have the IAMlong (IAM) permissions ``ssm:PutParameter`` and ``ssm:AddTagsToResource``. On stack creation, CFNlong adds the following three tags to the parameter: ``aws:cloudformation:stack-name``, ``aws:cloudformation:logical-id``, and ``aws:cloudformation:stack-id``, in addition to any custom tags you specify.&lt;br&#x2F;&gt; To add, update, or remove tags during stack update, you must have IAM permissions for both ``ssm:AddTagsToResource`` and ``ssm:RemoveTagsFromResource``. For more information, see &#91;Managing Access Using Policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;systems-manager&#x2F;latest&#x2F;userguide&#x2F;security-iam.html#security_iam_access-manage) in the *User Guide*.&lt;br&#x2F;&gt;  For information about valid values for parameters, see &#91;About requirements and constraints for parameter names&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;systems-manager&#x2F;latest&#x2F;userguide&#x2F;sysman-paramstore-su-create.html#sysman-parameter-name-constraints) in the *User Guide* and &#91;PutParameter&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;systems-manager&#x2F;latest&#x2F;APIReference&#x2F;API_PutParameter.html) in the *API Reference*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssm.parameters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the parameter.&lt;br&#x2F;&gt;  The maximum length constraint listed below includes capacity for additional system attributes that aren't part of the name. The maximum length for a parameter name, including the full length of the parameter Amazon Resource Name (ARN), is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters: ``arn:aws:ssm:us-east-2:111222333444:parameter&#x2F;ExampleParameterName``</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name
FROM aws.ssm.parameters
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>parameters</code> resource, the following permissions are required:

### Create
```json
ssm:PutParameter,
ssm:AddTagsToResource,
ssm:GetParameters
```

### List
```json
ssm:DescribeParameters
```

