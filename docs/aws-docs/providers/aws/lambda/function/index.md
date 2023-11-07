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
<tr><td><b>Id</b></td><td><code>aws.lambda.function</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>A description of the function.</td></tr>
<tr><td><code>TracingConfig</code></td><td><code>object</code></td><td>Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.</td></tr>
<tr><td><code>VpcConfig</code></td><td><code>object</code></td><td>For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC.</td></tr>
<tr><td><code>RuntimeManagementConfig</code></td><td><code>object</code></td><td>RuntimeManagementConfig</td></tr>
<tr><td><code>ReservedConcurrentExecutions</code></td><td><code>integer</code></td><td>The number of simultaneous executions to reserve for the function.</td></tr>
<tr><td><code>SnapStart</code></td><td><code>object</code></td><td>The SnapStart setting of your function</td></tr>
<tr><td><code>FileSystemConfigs</code></td><td><code>array</code></td><td>Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an AWS::EFS::MountTarget resource, you must also specify a DependsOn attribute to ensure that the mount target is created or updated before the function.</td></tr>
<tr><td><code>FunctionName</code></td><td><code>string</code></td><td>The name of the Lambda function, up to 64 characters in length. If you don't specify a name, AWS CloudFormation generates one.</td></tr>
<tr><td><code>Runtime</code></td><td><code>string</code></td><td>The identifier of the function's runtime.</td></tr>
<tr><td><code>KmsKeyArn</code></td><td><code>string</code></td><td>The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.</td></tr>
<tr><td><code>PackageType</code></td><td><code>string</code></td><td>PackageType.</td></tr>
<tr><td><code>CodeSigningConfigArn</code></td><td><code>string</code></td><td>A unique Arn for CodeSigningConfig resource</td></tr>
<tr><td><code>Layers</code></td><td><code>array</code></td><td>A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of tags to apply to the function.</td></tr>
<tr><td><code>ImageConfig</code></td><td><code>object</code></td><td>ImageConfig</td></tr>
<tr><td><code>MemorySize</code></td><td><code>integer</code></td><td>The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.</td></tr>
<tr><td><code>DeadLetterConfig</code></td><td><code>object</code></td><td>A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing.</td></tr>
<tr><td><code>Timeout</code></td><td><code>integer</code></td><td>The amount of time that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds.</td></tr>
<tr><td><code>Handler</code></td><td><code>string</code></td><td>The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime</td></tr>
<tr><td><code>SnapStartResponse</code></td><td><code>object</code></td><td>The SnapStart response of your function</td></tr>
<tr><td><code>Code</code></td><td><code>object</code></td><td>The code for the function.</td></tr>
<tr><td><code>Role</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the function's execution role.</td></tr>
<tr><td><code>Environment</code></td><td><code>object</code></td><td>Environment variables that are accessible from function code during execution.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Unique identifier for function resources</td></tr>
<tr><td><code>EphemeralStorage</code></td><td><code>object</code></td><td>A function's ephemeral storage settings.</td></tr>
<tr><td><code>Architectures</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.lambda.function<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;FunctionName&gt;'
</pre>
