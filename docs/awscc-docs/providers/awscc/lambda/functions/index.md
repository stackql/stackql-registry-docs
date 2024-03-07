---
title: functions
hide_title: false
hide_table_of_contents: false
keywords:
  - functions
  - lambda
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>functions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>functions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lambda.functions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>function_name</code></td><td><code>string</code></td><td>The name of the Lambda function, up to 64 characters in length. If you don't specify a name, CFN generates one.&lt;br&#x2F;&gt; If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>functions</code> resource, the following permissions are required:

### Create
```json
lambda:CreateFunction,
lambda:GetFunction,
lambda:PutFunctionConcurrency,
iam:PassRole,
s3:GetObject,
s3:GetObjectVersion,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
elasticfilesystem:DescribeMountTargets,
kms:CreateGrant,
kms:Decrypt,
kms:Encrypt,
kms:GenerateDataKey,
lambda:GetCodeSigningConfig,
lambda:GetFunctionCodeSigningConfig,
lambda:GetLayerVersion,
lambda:GetRuntimeManagementConfig,
lambda:PutRuntimeManagementConfig,
lambda:TagResource,
lambda:GetPolicy,
lambda:AddPermission,
lambda:RemovePermission,
lambda:GetResourcePolicy,
lambda:PutResourcePolicy
```

### List
```json
lambda:ListFunctions
```


## Example
```sql
SELECT
region,
function_name
FROM awscc.lambda.functions
WHERE region = 'us-east-1'
```
