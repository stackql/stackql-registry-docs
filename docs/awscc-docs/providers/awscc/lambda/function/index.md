---
title: function
hide_title: false
hide_table_of_contents: false
keywords:
  - function
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
Gets an individual <code>function</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>function</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>function</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lambda.function</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the function.</td></tr>
<tr><td><code>tracing_config</code></td><td><code>object</code></td><td>Set ``Mode`` to ``Active`` to sample and trace a subset of incoming requests with &#91;X-Ray&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;services-xray.html).</td></tr>
<tr><td><code>vpc_config</code></td><td><code>object</code></td><td>For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see &#91;Configuring a Lambda function to access resources in a VPC&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;configuration-vpc.html).</td></tr>
<tr><td><code>runtime_management_config</code></td><td><code>object</code></td><td>Sets the runtime management configuration for a function's version. For more information, see &#91;Runtime updates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;runtimes-update.html).</td></tr>
<tr><td><code>reserved_concurrent_executions</code></td><td><code>integer</code></td><td>The number of simultaneous executions to reserve for the function.</td></tr>
<tr><td><code>snap_start</code></td><td><code>object</code></td><td>The function's &#91;SnapStart&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;snapstart.html) setting.</td></tr>
<tr><td><code>file_system_configs</code></td><td><code>array</code></td><td>Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an &#91;AWS::EFS::MountTarget&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-efs-mounttarget.html) resource, you must also specify a ``DependsOn`` attribute to ensure that the mount target is created or updated before the function.&lt;br&#x2F;&gt; For more information about using the ``DependsOn`` attribute, see &#91;DependsOn Attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-dependson.html).</td></tr>
<tr><td><code>function_name</code></td><td><code>string</code></td><td>The name of the Lambda function, up to 64 characters in length. If you don't specify a name, CFN generates one.&lt;br&#x2F;&gt; If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><code>runtime</code></td><td><code>string</code></td><td>The identifier of the function's &#91;runtime&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;lambda-runtimes.html). Runtime is required if the deployment package is a .zip file archive.&lt;br&#x2F;&gt; The following list includes deprecated runtimes. For more information, see &#91;Runtime deprecation policy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;lambda-runtimes.html#runtime-support-policy).</td></tr>
<tr><td><code>kms_key_arn</code></td><td><code>string</code></td><td>The ARN of the KMSlong (KMS) customer managed key that's used to encrypt your function's &#91;environment variables&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;configuration-envvars.html#configuration-envvars-encryption). When &#91;Lambda SnapStart&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;snapstart-security.html) is activated, Lambda also uses this key is to encrypt your function's snapshot. If you deploy your function using a container image, Lambda also uses this key to encrypt your function when it's deployed. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). If you don't provide a customer managed key, Lambda uses a default service key.</td></tr>
<tr><td><code>package_type</code></td><td><code>string</code></td><td>The type of deployment package. Set to ``Image`` for container image and set ``Zip`` for .zip file archive.</td></tr>
<tr><td><code>code_signing_config_arn</code></td><td><code>string</code></td><td>To enable code signing for this function, specify the ARN of a code-signing configuration. A code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.</td></tr>
<tr><td><code>layers</code></td><td><code>array</code></td><td>A list of &#91;function layers&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;configuration-layers.html) to add to the function's execution environment. Specify each layer by its ARN, including the version.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of &#91;tags&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;tagging.html) to apply to the function.</td></tr>
<tr><td><code>image_config</code></td><td><code>object</code></td><td>Configuration values that override the container image Dockerfile settings. For more information, see &#91;Container image settings&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;images-create.html#images-parms).</td></tr>
<tr><td><code>memory_size</code></td><td><code>integer</code></td><td>The amount of &#91;memory available to the function&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;configuration-function-common.html#configuration-memory-console) at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB. Note that new AWS accounts have reduced concurrency and memory quotas. AWS raises these quotas automatically based on your usage. You can also request a quota increase.</td></tr>
<tr><td><code>dead_letter_config</code></td><td><code>object</code></td><td>A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see &#91;Dead-letter queues&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;invocation-async.html#invocation-dlq).</td></tr>
<tr><td><code>timeout</code></td><td><code>integer</code></td><td>The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds. For more information, see &#91;Lambda execution environment&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;runtimes-context.html).</td></tr>
<tr><td><code>handler</code></td><td><code>string</code></td><td>The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see &#91;Lambda programming model&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;foundation-progmodel.html).</td></tr>
<tr><td><code>snap_start_response</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>code</code></td><td><code>object</code></td><td>The code for the function.</td></tr>
<tr><td><code>role</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the function's execution role.</td></tr>
<tr><td><code>logging_config</code></td><td><code>object</code></td><td>The function's Amazon CloudWatch Logs configuration settings.</td></tr>
<tr><td><code>environment</code></td><td><code>object</code></td><td>Environment variables that are accessible from function code during execution.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ephemeral_storage</code></td><td><code>object</code></td><td>The size of the function's ``&#x2F;tmp`` directory in MB. The default value is 512, but it can be any whole number between 512 and 10,240 MB.</td></tr>
<tr><td><code>architectures</code></td><td><code>array</code></td><td>The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86_64). The default value is ``x86_64``.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>function</code> resource, the following permissions are required:

### Read
<pre>
lambda:GetFunction,
lambda:GetFunctionCodeSigningConfig</pre>

### Update
<pre>
lambda:DeleteFunctionConcurrency,
lambda:GetFunction,
lambda:PutFunctionConcurrency,
lambda:ListTags,
lambda:TagResource,
lambda:UntagResource,
lambda:UpdateFunctionConfiguration,
lambda:UpdateFunctionCode,
iam:PassRole,
s3:GetObject,
s3:GetObjectVersion,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
elasticfilesystem:DescribeMountTargets,
kms:CreateGrant,
kms:Decrypt,
kms:GenerateDataKey,
lambda:GetRuntimeManagementConfig,
lambda:PutRuntimeManagementConfig,
lambda:PutFunctionCodeSigningConfig,
lambda:DeleteFunctionCodeSigningConfig,
lambda:GetCodeSigningConfig,
lambda:GetFunctionCodeSigningConfig,
lambda:GetPolicy,
lambda:AddPermission,
lambda:RemovePermission,
lambda:GetResourcePolicy,
lambda:PutResourcePolicy,
lambda:DeleteResourcePolicy</pre>

### Delete
<pre>
lambda:DeleteFunction,
lambda:GetFunction,
ec2:DescribeNetworkInterfaces</pre>


## Example
```sql
SELECT
region,
description,
tracing_config,
vpc_config,
runtime_management_config,
reserved_concurrent_executions,
snap_start,
file_system_configs,
function_name,
runtime,
kms_key_arn,
package_type,
code_signing_config_arn,
layers,
tags,
image_config,
memory_size,
dead_letter_config,
timeout,
handler,
snap_start_response,
code,
role,
logging_config,
environment,
arn,
ephemeral_storage,
architectures
FROM awscc.lambda.function
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;FunctionName&gt;'
```
