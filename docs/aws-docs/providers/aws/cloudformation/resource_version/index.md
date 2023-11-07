---
title: resource_version
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_version
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
Gets an individual <code>resource_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_version</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudformation.resource_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type, here the ResourceVersion. This is used to uniquely identify a ResourceVersion resource</td></tr>
<tr><td><code>TypeArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type without the versionID.</td></tr>
<tr><td><code>ExecutionRoleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.</td></tr>
<tr><td><code>IsDefaultVersion</code></td><td><code>boolean</code></td><td>Indicates if this type version is the current default version</td></tr>
<tr><td><code>LoggingConfig</code></td><td><code>object</code></td><td>Specifies logging configuration information for a type.</td></tr>
<tr><td><code>ProvisioningType</code></td><td><code>string</code></td><td>The provisioning behavior of the type. AWS CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.</td></tr>
<tr><td><code>SchemaHandlerPackage</code></td><td><code>string</code></td><td>A url to the S3 bucket containing the schema handler package that contains the schema, event handlers, and associated files for the type you want to register.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;For information on generating a schema handler package for the type you want to register, see submit in the CloudFormation CLI User Guide.</td></tr>
<tr><td><code>TypeName</code></td><td><code>string</code></td><td>The name of the type being registered.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><code>VersionId</code></td><td><code>string</code></td><td>The ID of the version of the type represented by this resource instance.</td></tr>
<tr><td><code>Visibility</code></td><td><code>string</code></td><td>The scope at which the type is visible and usable in CloudFormation operations.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Valid values include:&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;PRIVATE: The type is only visible and usable within the account in which it is registered. Currently, AWS CloudFormation marks any types you register as PRIVATE.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;PUBLIC: The type is publically visible and usable within any Amazon account.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.cloudformation.resource_version<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Arn&gt;'
</pre>
