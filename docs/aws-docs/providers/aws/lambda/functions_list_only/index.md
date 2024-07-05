---
title: functions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - functions_list_only
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

Lists <code>functions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/functions/"><code>functions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::Lambda::Function</code> resource creates a Lambda function. To create a function, you need a &#91;deployment package&#93;(https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html) and an &#91;execution role&#93;(https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html). The deployment package is a .zip file archive or container image that contains your function code. The execution role grants the function permission to use AWS services, such as Amazon CloudWatch Logs for log streaming and AWS X-Ray for request tracing.<br />You set the package type to <code>Image</code> if the deployment package is a &#91;container image&#93;(https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html). For a container image, the code property must include the URI of a container image in the Amazon ECR registry. You do not need to specify the handler and runtime properties. <br />You set the package type to <code>Zip</code> if the deployment package is a &#91;.zip file archive&#93;(https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html#gettingstarted-package-zip). For a .zip file archive, the code property specifies the location of the .zip file. You must also specify the handler and runtime properties. For a Python example, see &#91;Deploy Python Lambda functions with .zip file archives&#93;(https://docs.aws.amazon.com/lambda/latest/dg/python-package.html).<br />You can use &#91;code signing&#93;(https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html) if your deployment package is a .zip file archive. To enable code signing for this function, specify the ARN of a code-signing configuration. When a user attempts to deploy a code package with <code>UpdateFunctionCode</code>, Lambda checks that the code package has a valid signature from a trusted publisher. The code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.<br />Note that you configure &#91;provisioned concurrency&#93;(https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) on a <code>AWS::Lambda::Version</code> or a <code>AWS::Lambda::Alias</code>.<br />For a complete introduction to Lambda functions, see &#91;What is Lambda?&#93;(https://docs.aws.amazon.com/lambda/latest/dg/lambda-welcome.html) in the *Lambda developer guide.*</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.functions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the function.</td></tr>
<tr><td><CopyableCode code="tracing_config" /></td><td><code>object</code></td><td>Set <code>Mode</code> to <code>Active</code> to sample and trace a subset of incoming requests with &#91;X-Ray&#93;(https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html).</td></tr>
<tr><td><CopyableCode code="vpc_config" /></td><td><code>object</code></td><td>For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see &#91;Configuring a Lambda function to access resources in a VPC&#93;(https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html).</td></tr>
<tr><td><CopyableCode code="runtime_management_config" /></td><td><code>object</code></td><td>Sets the runtime management configuration for a function's version. For more information, see &#91;Runtime updates&#93;(https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html).</td></tr>
<tr><td><CopyableCode code="reserved_concurrent_executions" /></td><td><code>integer</code></td><td>The number of simultaneous executions to reserve for the function.</td></tr>
<tr><td><CopyableCode code="snap_start" /></td><td><code>object</code></td><td>The function's &#91;SnapStart&#93;(https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) setting.</td></tr>
<tr><td><CopyableCode code="file_system_configs" /></td><td><code>array</code></td><td>Connection settings for an Amazon EFS file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an &#91;AWS::EFS::MountTarget&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html) resource, you must also specify a <code>DependsOn</code> attribute to ensure that the mount target is created or updated before the function.<br />For more information about using the <code>DependsOn</code> attribute, see &#91;DependsOn Attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html).</td></tr>
<tr><td><CopyableCode code="function_name" /></td><td><code>string</code></td><td>The name of the Lambda function, up to 64 characters in length. If you don't specify a name, CFN generates one.<br />If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="runtime" /></td><td><code>string</code></td><td>The identifier of the function's &#91;runtime&#93;(https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Runtime is required if the deployment package is a .zip file archive.<br />The following list includes deprecated runtimes. For more information, see &#91;Runtime deprecation policy&#93;(https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy).</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>The ARN of the KMSlong (KMS) customer managed key that's used to encrypt your function's &#91;environment variables&#93;(https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption). When &#91;Lambda SnapStart&#93;(https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html) is activated, Lambda also uses this key is to encrypt your function's snapshot. If you deploy your function using a container image, Lambda also uses this key to encrypt your function when it's deployed. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). If you don't provide a customer managed key, Lambda uses a default service key.</td></tr>
<tr><td><CopyableCode code="package_type" /></td><td><code>string</code></td><td>The type of deployment package. Set to <code>Image</code> for container image and set <code>Zip</code> for .zip file archive.</td></tr>
<tr><td><CopyableCode code="code_signing_config_arn" /></td><td><code>string</code></td><td>To enable code signing for this function, specify the ARN of a code-signing configuration. A code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.</td></tr>
<tr><td><CopyableCode code="layers" /></td><td><code>array</code></td><td>A list of &#91;function layers&#93;(https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) to add to the function's execution environment. Specify each layer by its ARN, including the version.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of &#91;tags&#93;(https://docs.aws.amazon.com/lambda/latest/dg/tagging.html) to apply to the function.</td></tr>
<tr><td><CopyableCode code="image_config" /></td><td><code>object</code></td><td>Configuration values that override the container image Dockerfile settings. For more information, see &#91;Container image settings&#93;(https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms).</td></tr>
<tr><td><CopyableCode code="memory_size" /></td><td><code>integer</code></td><td>The amount of &#91;memory available to the function&#93;(https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-memory-console) at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB. Note that new AWS accounts have reduced concurrency and memory quotas. AWS raises these quotas automatically based on your usage. You can also request a quota increase.</td></tr>
<tr><td><CopyableCode code="dead_letter_config" /></td><td><code>object</code></td><td>A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see &#91;Dead-letter queues&#93;(https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq).</td></tr>
<tr><td><CopyableCode code="timeout" /></td><td><code>integer</code></td><td>The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds. For more information, see &#91;Lambda execution environment&#93;(https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html).</td></tr>
<tr><td><CopyableCode code="handler" /></td><td><code>string</code></td><td>The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see &#91;Lambda programming model&#93;(https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html).</td></tr>
<tr><td><CopyableCode code="snap_start_response" /></td><td><code>object</code></td><td>The function's &#91;SnapStart&#93;(https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) setting.</td></tr>
<tr><td><CopyableCode code="code" /></td><td><code>object</code></td><td>The code for the function.</td></tr>
<tr><td><CopyableCode code="role" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the function's execution role.</td></tr>
<tr><td><CopyableCode code="logging_config" /></td><td><code>object</code></td><td>The function's Amazon CloudWatch Logs configuration settings.</td></tr>
<tr><td><CopyableCode code="environment" /></td><td><code>object</code></td><td>Environment variables that are accessible from function code during execution.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ephemeral_storage" /></td><td><code>object</code></td><td>The size of the function's <code>/tmp</code> directory in MB. The default value is 512, but it can be any whole number between 512 and 10,240 MB.</td></tr>
<tr><td><CopyableCode code="architectures" /></td><td><code>array</code></td><td>The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86_64). The default value is <code>x86_64</code>.</td></tr>
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
Lists all <code>functions</code> in a region.
```sql
SELECT
region,
function_name
FROM aws.lambda.functions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>functions_list_only</code> resource, see <a href="/providers/aws/lambda/functions/#permissions"><code>functions</code></a>


