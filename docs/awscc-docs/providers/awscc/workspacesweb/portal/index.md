---
title: portal
hide_title: false
hide_table_of_contents: false
keywords:
  - portal
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
Gets an individual <code>portal</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>portal</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>portal</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.workspacesweb.portal</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>additional_encryption_context</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>authentication_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>browser_settings_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>browser_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>customer_managed_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ip_access_settings_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_settings_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>portal_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>portal_endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>portal_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>renderer_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_provider_saml_metadata</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status_reason</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>trust_store_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_access_logging_settings_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_settings_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
additional_encryption_context,
authentication_type,
browser_settings_arn,
browser_type,
creation_date,
customer_managed_key,
display_name,
ip_access_settings_arn,
network_settings_arn,
portal_arn,
portal_endpoint,
portal_status,
renderer_type,
service_provider_saml_metadata,
status_reason,
tags,
trust_store_arn,
user_access_logging_settings_arn,
user_settings_arn
FROM awscc.workspacesweb.portal
WHERE data__Identifier = '<PortalArn>';
```

## Permissions

To operate on the <code>portal</code> resource, the following permissions are required:

### Read
```json
workspaces-web:GetPortal,
workspaces-web:GetPortalServiceProviderMetadata,
workspaces-web:ListTagsForResource,
kms:Decrypt
```

### Update
```json
workspaces-web:GetPortal,
workspaces-web:GetPortalServiceProviderMetadata,
workspaces-web:UpdatePortal,
workspaces-web:AssociateBrowserSettings,
workspaces-web:AssociateIpAccessSettings,
workspaces-web:AssociateNetworkSettings,
workspaces-web:AssociateTrustStore,
workspaces-web:AssociateUserAccessLoggingSettings,
workspaces-web:AssociateUserSettings,
workspaces-web:DisassociateBrowserSettings,
workspaces-web:DisassociateIpAccessSettings,
workspaces-web:DisassociateNetworkSettings,
workspaces-web:DisassociateTrustStore,
workspaces-web:DisassociateUserAccessLoggingSettings,
workspaces-web:DisassociateUserSettings,
workspaces-web:ListTagsForResource,
workspaces-web:TagResource,
workspaces-web:UntagResource,
kms:CreateGrant,
kms:Encrypt,
kms:GenerateDataKey,
kms:Decrypt,
ec2:CreateNetworkInterface,
ec2:CreateNetworkInterfacePermission,
ec2:DeleteNetworkInterface,
ec2:DeleteNetworkInterfacePermission,
ec2:ModifyNetworkInterfaceAttribute,
kinesis:PutRecord,
kinesis:PutRecords,
kinesis:DescribeStreamSummary,
sso:CreateManagedApplicationInstance,
sso:DeleteManagedApplicationInstance,
sso:DescribeRegisteredRegions,
sso:GetApplicationInstance,
sso:ListApplicationInstances
```

### Delete
```json
workspaces-web:GetPortal,
workspaces-web:DeletePortal,
workspaces-web:DisassociateBrowserSettings,
workspaces-web:DisassociateIpAccessSettings,
workspaces-web:DisassociateNetworkSettings,
workspaces-web:DisassociateTrustStore,
workspaces-web:DisassociateUserAccessLoggingSettings,
workspaces-web:DisassociateUserSettings,
kms:Decrypt,
sso:DeleteManagedApplicationInstance
```

