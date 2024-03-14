---
title: ip_access_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_access_settings
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
Gets an individual <code>ip_access_settings</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_access_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>ip_access_settings</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.workspacesweb.ip_access_settings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>additional_encryption_context</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>associated_portal_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>creation_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>customer_managed_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ip_access_settings_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ip_rules</code></td><td><code>array</code></td><td></td></tr>
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
creation_date,
customer_managed_key,
description,
display_name,
ip_access_settings_arn,
ip_rules,
tags
FROM awscc.workspacesweb.ip_access_settings
WHERE data__Identifier = '<IpAccessSettingsArn>';
```

## Permissions

To operate on the <code>ip_access_settings</code> resource, the following permissions are required:

### Read
```json
workspaces-web:GetIpAccessSettings,
workspaces-web:ListIpAccessSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Update
```json
workspaces-web:UpdateIpAccessSettings,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:GetIpAccessSettings,
workspaces-web:ListIpAccessSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
workspaces-web:GetIpAccessSettings,
workspaces-web:ListIpAccessSettings,
workspaces-web:DeleteIpAccessSettings,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

