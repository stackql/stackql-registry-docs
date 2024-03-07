---
title: user_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - user_settings
  - workspacesweb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>user_settings</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_settings</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.workspacesweb.user_settings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>additional_encryption_context</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>associated_portal_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>cookie_synchronization_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>copy_allowed</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>customer_managed_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>disconnect_timeout_in_minutes</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>download_allowed</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>idle_disconnect_timeout_in_minutes</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>paste_allowed</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>print_allowed</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>upload_allowed</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_settings_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>user_settings</code> resource, the following permissions are required:

### Read
<pre>
workspaces-web:GetUserSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt</pre>

### Update
<pre>
workspaces-web:UpdateUserSettings,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:GetUserSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt</pre>

### Delete
<pre>
workspaces-web:GetUserSettings,
workspaces-web:DeleteUserSettings,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt</pre>


## Example
```sql
SELECT
region,
additional_encryption_context,
associated_portal_arns,
cookie_synchronization_configuration,
copy_allowed,
customer_managed_key,
disconnect_timeout_in_minutes,
download_allowed,
idle_disconnect_timeout_in_minutes,
paste_allowed,
print_allowed,
tags,
upload_allowed,
user_settings_arn
FROM awscc.workspacesweb.user_settings
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;UserSettingsArn&gt;'
```
