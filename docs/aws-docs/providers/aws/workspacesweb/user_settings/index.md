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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>user_settings</code> resource, use <code>user_settings</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::UserSettings Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.user_settings" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="additional_encryption_context" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="associated_portal_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="cookie_synchronization_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="copy_allowed" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_managed_key" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="disconnect_timeout_in_minutes" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="download_allowed" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="idle_disconnect_timeout_in_minutes" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="paste_allowed" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="print_allowed" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="upload_allowed" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_settings_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.workspacesweb.user_settings
WHERE data__Identifier = '<UserSettingsArn>';
```

## Permissions

To operate on the <code>user_settings</code> resource, the following permissions are required:

### Read
```json
workspaces-web:GetUserSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Update
```json
workspaces-web:UpdateUserSettings,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:GetUserSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
workspaces-web:GetUserSettings,
workspaces-web:DeleteUserSettings,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

