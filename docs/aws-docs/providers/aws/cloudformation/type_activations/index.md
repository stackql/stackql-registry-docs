---
title: type_activations
hide_title: false
hide_table_of_contents: false
keywords:
  - type_activations
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
Retrieves a list of <code>type_activations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>type_activations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>type_activations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudformation.type_activations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the extension.</td></tr>
<tr><td><code>ExecutionRoleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.</td></tr>
<tr><td><code>PublisherId</code></td><td><code>string</code></td><td>The publisher id assigned by CloudFormation for publishing in this region.</td></tr>
<tr><td><code>LoggingConfig</code></td><td><code>undefined</code></td><td>Specifies logging configuration information for a type.</td></tr>
<tr><td><code>PublicTypeArn</code></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) assigned to the public extension upon publication</td></tr>
<tr><td><code>AutoUpdate</code></td><td><code>boolean</code></td><td>Whether to automatically update the extension in this account and region when a new minor version is published by the extension publisher. Major versions released by the publisher must be manually updated.</td></tr>
<tr><td><code>TypeNameAlias</code></td><td><code>string</code></td><td>An alias to assign to the public extension in this account and region. If you specify an alias for the extension, you must then use the alias to refer to the extension in your templates.</td></tr>
<tr><td><code>VersionBump</code></td><td><code>string</code></td><td>Manually updates a previously-enabled type to a new major or minor version, if available. You can also use this parameter to update the value of AutoUpdateEnabled</td></tr>
<tr><td><code>MajorVersion</code></td><td><code>string</code></td><td>The Major Version of the type you want to enable</td></tr>
<tr><td><code>TypeName</code></td><td><code>string</code></td><td>The name of the type being registered.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td>The kind of extension</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.cloudformation.type_activations<br/>WHERE region = 'us-east-1'
</pre>
