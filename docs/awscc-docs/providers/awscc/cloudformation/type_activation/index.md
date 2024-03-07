---
title: type_activation
hide_title: false
hide_table_of_contents: false
keywords:
  - type_activation
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
Gets an individual <code>type_activation</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>type_activation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>type_activation</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudformation.type_activation</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the extension.</td></tr>
<tr><td><code>execution_role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.</td></tr>
<tr><td><code>publisher_id</code></td><td><code>string</code></td><td>The publisher id assigned by CloudFormation for publishing in this region.</td></tr>
<tr><td><code>logging_config</code></td><td><code>object</code></td><td>Specifies logging configuration information for a type.</td></tr>
<tr><td><code>public_type_arn</code></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) assigned to the public extension upon publication</td></tr>
<tr><td><code>auto_update</code></td><td><code>boolean</code></td><td>Whether to automatically update the extension in this account and region when a new minor version is published by the extension publisher. Major versions released by the publisher must be manually updated.</td></tr>
<tr><td><code>type_name_alias</code></td><td><code>string</code></td><td>An alias to assign to the public extension in this account and region. If you specify an alias for the extension, you must then use the alias to refer to the extension in your templates.</td></tr>
<tr><td><code>version_bump</code></td><td><code>string</code></td><td>Manually updates a previously-enabled type to a new major or minor version, if available. You can also use this parameter to update the value of AutoUpdateEnabled</td></tr>
<tr><td><code>major_version</code></td><td><code>string</code></td><td>The Major Version of the type you want to enable</td></tr>
<tr><td><code>type_name</code></td><td><code>string</code></td><td>The name of the type being registered.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The kind of extension</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
execution_role_arn,
publisher_id,
logging_config,
public_type_arn,
auto_update,
type_name_alias,
version_bump,
major_version,
type_name,
type
FROM awscc.cloudformation.type_activation
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>type_activation</code> resource, the following permissions are required:

### Update
```json
cloudformation:ActivateType,
cloudformation:DescribeType,
iam:PassRole
```

### Read
```json
cloudformation:DescribeType
```

### Delete
```json
cloudformation:DeactivateType,
cloudformation:DescribeType
```

