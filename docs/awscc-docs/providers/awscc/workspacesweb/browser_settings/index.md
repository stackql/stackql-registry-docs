---
title: browser_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - browser_settings
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
Gets an individual <code>browser_settings</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>browser_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>browser_settings</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.workspacesweb.browser_settings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>additional_encryption_context</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>associated_portal_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>browser_policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>browser_settings_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>customer_managed_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
additional_encryption_context,
associated_portal_arns,
browser_policy,
browser_settings_arn,
customer_managed_key,
tags
FROM awscc.workspacesweb.browser_settings
WHERE region = 'us-east-1'
AND data__Identifier = '{BrowserSettingsArn}';
```

## Permissions

To operate on the <code>browser_settings</code> resource, the following permissions are required:

### Read
```json
workspaces-web:GetBrowserSettings,
workspaces-web:ListBrowserSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Update
```json
workspaces-web:UpdateBrowserSettings,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:GetBrowserSettings,
workspaces-web:ListBrowserSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
workspaces-web:GetBrowserSettings,
workspaces-web:DeleteBrowserSettings,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

