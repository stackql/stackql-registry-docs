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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>portal</code> resource, use <code>portals</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>portal</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::Portal Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.portal" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="additional_encryption_context" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="authentication_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="browser_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="browser_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_managed_key" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ip_access_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="portal_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="portal_endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="portal_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="renderer_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_provider_saml_metadata" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_reason" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="trust_store_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_access_logging_settings_arn" /></td><td><code>string</code></td><td></td></tr>
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
FROM aws.workspacesweb.portal
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

