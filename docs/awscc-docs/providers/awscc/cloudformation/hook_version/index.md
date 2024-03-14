---
title: hook_version
hide_title: false
hide_table_of_contents: false
keywords:
  - hook_version
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
Gets an individual <code>hook_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hook_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>hook_version</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudformation.hook_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type, here the HookVersion. This is used to uniquely identify a HookVersion resource</td></tr>
<tr><td><code>type_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type without the versionID.</td></tr>
<tr><td><code>execution_role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.</td></tr>
<tr><td><code>is_default_version</code></td><td><code>boolean</code></td><td>Indicates if this type version is the current default version</td></tr>
<tr><td><code>logging_config</code></td><td><code>object</code></td><td>Specifies logging configuration information for a type.</td></tr>
<tr><td><code>schema_handler_package</code></td><td><code>string</code></td><td>A url to the S3 bucket containing the schema handler package that contains the schema, event handlers, and associated files for the type you want to register.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;For information on generating a schema handler package for the type you want to register, see submit in the CloudFormation CLI User Guide.</td></tr>
<tr><td><code>type_name</code></td><td><code>string</code></td><td>The name of the type being registered.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><code>version_id</code></td><td><code>string</code></td><td>The ID of the version of the type represented by this hook instance.</td></tr>
<tr><td><code>visibility</code></td><td><code>string</code></td><td>The scope at which the type is visible and usable in CloudFormation operations.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Valid values include:&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;PRIVATE: The type is only visible and usable within the account in which it is registered. Currently, AWS CloudFormation marks any types you register as PRIVATE.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;PUBLIC: The type is publically visible and usable within any Amazon account.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
type_arn,
execution_role_arn,
is_default_version,
logging_config,
schema_handler_package,
type_name,
version_id,
visibility
FROM awscc.cloudformation.hook_version
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>hook_version</code> resource, the following permissions are required:

### Read
```json
cloudformation:DescribeType
```

### Delete
```json
cloudformation:DeregisterType,
cloudformation:DescribeType
```

