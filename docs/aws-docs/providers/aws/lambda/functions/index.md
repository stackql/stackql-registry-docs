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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>functions</code> in a region or to create or delete a <code>functions</code> resource, use <code>function</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::Lambda::Function`` resource creates a Lambda function. To create a function, you need a &#91;deployment package&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;gettingstarted-package.html) and an &#91;execution role&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;lambda-intro-execution-role.html). The deployment package is a .zip file archive or container image that contains your function code. The execution role grants the function permission to use AWS services, such as Amazon CloudWatch Logs for log streaming and AWS X-Ray for request tracing.&lt;br&#x2F;&gt; You set the package type to ``Image`` if the deployment package is a &#91;container image&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;lambda-images.html). For a container image, the code property must include the URI of a container image in the Amazon ECR registry. You do not need to specify the handler and runtime properties. &lt;br&#x2F;&gt; You set the package type to ``Zip`` if the deployment package is a &#91;.zip file archive&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;gettingstarted-package.html#gettingstarted-package-zip). For a .zip file archive, the code property specifies the location of the .zip file. You must also specify the handler and runtime properties. For a Python example, see &#91;Deploy Python Lambda functions with .zip file archives&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;python-package.html).&lt;br&#x2F;&gt; You can use &#91;code signing&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;configuration-codesigning.html) if your deployment package is a .zip file archive. To enable code signing for this function, specify the ARN of a code-signing configuration. When a user attempts to deploy a code package with ``UpdateFunctionCode``, Lambda checks that the code package has a valid signature from a trusted publisher. The code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.&lt;br&#x2F;&gt; Note that you configure &#91;provisioned concurrency&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;provisioned-concurrency.html) on a ``AWS::Lambda::Version`` or a ``AWS::Lambda::Alias``.&lt;br&#x2F;&gt; For a complete introduction to Lambda functions, see &#91;What is Lambda?&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;lambda-welcome.html) in the *Lambda developer guide.*</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.functions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="function_name" /></td><td><code>string</code></td><td>The name of the Lambda function, up to 64 characters in length. If you don't specify a name, CFN generates one.&lt;br&#x2F;&gt; If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
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
function_name
FROM aws.lambda.functions
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
 "Code": {
  "S3ObjectVersion": "{{ S3ObjectVersion }}",
  "S3Bucket": "{{ S3Bucket }}",
  "ZipFile": "{{ ZipFile }}",
  "S3Key": "{{ S3Key }}",
  "ImageUri": "{{ ImageUri }}"
 },
 "Role": "{{ Role }}"
}
>>>
--required properties only
INSERT INTO aws.lambda.functions (
 Code,
 Role,
 region
)
SELECT 
{{ .Code }},
 {{ .Role }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "TracingConfig": {
  "Mode": "{{ Mode }}"
 },
 "VpcConfig": {
  "Ipv6AllowedForDualStack": "{{ Ipv6AllowedForDualStack }}",
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ],
  "SubnetIds": [
   "{{ SubnetIds[0] }}"
  ]
 },
 "RuntimeManagementConfig": {
  "UpdateRuntimeOn": "{{ UpdateRuntimeOn }}",
  "RuntimeVersionArn": "{{ RuntimeVersionArn }}"
 },
 "ReservedConcurrentExecutions": "{{ ReservedConcurrentExecutions }}",
 "SnapStart": {
  "ApplyOn": "{{ ApplyOn }}"
 },
 "FileSystemConfigs": [
  {
   "Arn": "{{ Arn }}",
   "LocalMountPath": "{{ LocalMountPath }}"
  }
 ],
 "FunctionName": "{{ FunctionName }}",
 "Runtime": "{{ Runtime }}",
 "KmsKeyArn": "{{ KmsKeyArn }}",
 "PackageType": "{{ PackageType }}",
 "CodeSigningConfigArn": "{{ CodeSigningConfigArn }}",
 "Layers": [
  "{{ Layers[0] }}"
 ],
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "ImageConfig": {
  "WorkingDirectory": "{{ WorkingDirectory }}",
  "Command": [
   "{{ Command[0] }}"
  ],
  "EntryPoint": [
   "{{ EntryPoint[0] }}"
  ]
 },
 "MemorySize": "{{ MemorySize }}",
 "DeadLetterConfig": {
  "TargetArn": "{{ TargetArn }}"
 },
 "Timeout": "{{ Timeout }}",
 "Handler": "{{ Handler }}",
 "Code": {
  "S3ObjectVersion": "{{ S3ObjectVersion }}",
  "S3Bucket": "{{ S3Bucket }}",
  "ZipFile": "{{ ZipFile }}",
  "S3Key": "{{ S3Key }}",
  "ImageUri": "{{ ImageUri }}"
 },
 "Role": "{{ Role }}",
 "LoggingConfig": {
  "LogFormat": "{{ LogFormat }}",
  "ApplicationLogLevel": "{{ ApplicationLogLevel }}",
  "LogGroup": "{{ LogGroup }}",
  "SystemLogLevel": "{{ SystemLogLevel }}"
 },
 "Environment": {
  "Variables": {}
 },
 "EphemeralStorage": {
  "Size": "{{ Size }}"
 },
 "Architectures": [
  "{{ Architectures[0] }}"
 ]
}
>>>
--all properties
INSERT INTO aws.lambda.functions (
 Description,
 TracingConfig,
 VpcConfig,
 RuntimeManagementConfig,
 ReservedConcurrentExecutions,
 SnapStart,
 FileSystemConfigs,
 FunctionName,
 Runtime,
 KmsKeyArn,
 PackageType,
 CodeSigningConfigArn,
 Layers,
 Tags,
 ImageConfig,
 MemorySize,
 DeadLetterConfig,
 Timeout,
 Handler,
 Code,
 Role,
 LoggingConfig,
 Environment,
 EphemeralStorage,
 Architectures,
 region
)
SELECT 
 {{ .Description }},
 {{ .TracingConfig }},
 {{ .VpcConfig }},
 {{ .RuntimeManagementConfig }},
 {{ .ReservedConcurrentExecutions }},
 {{ .SnapStart }},
 {{ .FileSystemConfigs }},
 {{ .FunctionName }},
 {{ .Runtime }},
 {{ .KmsKeyArn }},
 {{ .PackageType }},
 {{ .CodeSigningConfigArn }},
 {{ .Layers }},
 {{ .Tags }},
 {{ .ImageConfig }},
 {{ .MemorySize }},
 {{ .DeadLetterConfig }},
 {{ .Timeout }},
 {{ .Handler }},
 {{ .Code }},
 {{ .Role }},
 {{ .LoggingConfig }},
 {{ .Environment }},
 {{ .EphemeralStorage }},
 {{ .Architectures }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lambda.functions
WHERE data__Identifier = '<FunctionName>'
AND region = 'us-east-1';
```

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

### Delete
```json
lambda:DeleteFunction,
lambda:GetFunction,
ec2:DescribeNetworkInterfaces
```

