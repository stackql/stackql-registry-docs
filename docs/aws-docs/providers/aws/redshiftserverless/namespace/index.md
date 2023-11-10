---
title: namespace
hide_title: false
hide_table_of_contents: false
keywords:
  - namespace
  - redshiftserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>namespace</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>namespace</td></tr>
<tr><td><b>Id</b></td><td><code>aws.redshiftserverless.namespace</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>admin_user_password</code></td><td><code>string</code></td><td>The password associated with the admin user for the namespace that is being created. Password must be at least 8 characters in length, should be any printable ASCII character. Must contain at least one lowercase letter, one uppercase letter and one decimal digit.</td></tr>
<tr><td><code>admin_username</code></td><td><code>string</code></td><td>The user name associated with the admin user for the namespace that is being created. Only alphanumeric characters and underscores are allowed. It should start with an alphabet.</td></tr>
<tr><td><code>db_name</code></td><td><code>string</code></td><td>The database name associated for the namespace that is being created. Only alphanumeric characters and underscores are allowed. It should start with an alphabet.</td></tr>
<tr><td><code>default_iam_role_arn</code></td><td><code>string</code></td><td>The default IAM role ARN for the namespace that is being created.</td></tr>
<tr><td><code>iam_roles</code></td><td><code>array</code></td><td>A list of AWS Identity and Access Management (IAM) roles that can be used by the namespace to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. The Default role limit for each request is 10.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the namespace.</td></tr>
<tr><td><code>log_exports</code></td><td><code>array</code></td><td>The collection of log types to be exported provided by the customer. Should only be one of the three supported log types: userlog, useractivitylog and connectionlog</td></tr>
<tr><td><code>namespace</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>namespace_name</code></td><td><code>string</code></td><td>A unique identifier for the namespace. You use this identifier to refer to the namespace for any subsequent namespace operations such as deleting or modifying. All alphabetical characters must be lower case. Namespace name should be unique for all namespaces within an AWS account.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The list of tags for the namespace.</td></tr>
<tr><td><code>final_snapshot_name</code></td><td><code>string</code></td><td>The name of the namespace the source snapshot was created from. Please specify the name if needed before deleting namespace</td></tr>
<tr><td><code>final_snapshot_retention_period</code></td><td><code>integer</code></td><td>The number of days to retain automated snapshot in the destination region after they are copied from the source region. If the value is -1, the manual snapshot is retained indefinitely. The value must be either -1 or an integer between 1 and 3,653.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
admin_user_password,
admin_username,
db_name,
default_iam_role_arn,
iam_roles,
kms_key_id,
log_exports,
namespace,
namespace_name,
tags,
final_snapshot_name,
final_snapshot_retention_period
FROM aws.redshiftserverless.namespace
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;NamespaceName&gt;'
```
