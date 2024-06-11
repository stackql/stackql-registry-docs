---
title: portals
hide_title: false
hide_table_of_contents: false
keywords:
  - portals
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>portal</code> resource or lists <code>portals</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>portals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::Portal Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.portals" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="additional_encryption_context" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="authentication_type" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="browser_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="browser_type" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_managed_key" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="ip_access_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="max_concurrent_sessions" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="network_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="portal_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="portal_endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="portal_status" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="renderer_type" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>portals</code> in a region.
```sql
SELECT
region,
portal_arn
FROM aws.workspacesweb.portals
WHERE region = 'us-east-1';
```
Gets all properties from a <code>portal</code>.
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
instance_type,
ip_access_settings_arn,
max_concurrent_sessions,
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
FROM aws.workspacesweb.portals
WHERE region = 'us-east-1' AND data__Identifier = '<PortalArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>portal</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.workspacesweb.portals (
 AdditionalEncryptionContext,
 AuthenticationType,
 BrowserSettingsArn,
 CustomerManagedKey,
 DisplayName,
 InstanceType,
 IpAccessSettingsArn,
 MaxConcurrentSessions,
 NetworkSettingsArn,
 Tags,
 TrustStoreArn,
 UserAccessLoggingSettingsArn,
 UserSettingsArn,
 region
)
SELECT 
'{{ AdditionalEncryptionContext }}',
 '{{ AuthenticationType }}',
 '{{ BrowserSettingsArn }}',
 '{{ CustomerManagedKey }}',
 '{{ DisplayName }}',
 '{{ InstanceType }}',
 '{{ IpAccessSettingsArn }}',
 '{{ MaxConcurrentSessions }}',
 '{{ NetworkSettingsArn }}',
 '{{ Tags }}',
 '{{ TrustStoreArn }}',
 '{{ UserAccessLoggingSettingsArn }}',
 '{{ UserSettingsArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.workspacesweb.portals (
 AdditionalEncryptionContext,
 AuthenticationType,
 BrowserSettingsArn,
 CustomerManagedKey,
 DisplayName,
 InstanceType,
 IpAccessSettingsArn,
 MaxConcurrentSessions,
 NetworkSettingsArn,
 Tags,
 TrustStoreArn,
 UserAccessLoggingSettingsArn,
 UserSettingsArn,
 region
)
SELECT 
 '{{ AdditionalEncryptionContext }}',
 '{{ AuthenticationType }}',
 '{{ BrowserSettingsArn }}',
 '{{ CustomerManagedKey }}',
 '{{ DisplayName }}',
 '{{ InstanceType }}',
 '{{ IpAccessSettingsArn }}',
 '{{ MaxConcurrentSessions }}',
 '{{ NetworkSettingsArn }}',
 '{{ Tags }}',
 '{{ TrustStoreArn }}',
 '{{ UserAccessLoggingSettingsArn }}',
 '{{ UserSettingsArn }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: portal
    props:
      - name: AdditionalEncryptionContext
        value: {}
      - name: AuthenticationType
        value: '{{ AuthenticationType }}'
      - name: BrowserSettingsArn
        value: '{{ BrowserSettingsArn }}'
      - name: CustomerManagedKey
        value: '{{ CustomerManagedKey }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: InstanceType
        value: '{{ InstanceType }}'
      - name: IpAccessSettingsArn
        value: '{{ IpAccessSettingsArn }}'
      - name: MaxConcurrentSessions
        value: null
      - name: NetworkSettingsArn
        value: '{{ NetworkSettingsArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TrustStoreArn
        value: '{{ TrustStoreArn }}'
      - name: UserAccessLoggingSettingsArn
        value: '{{ UserAccessLoggingSettingsArn }}'
      - name: UserSettingsArn
        value: '{{ UserSettingsArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.workspacesweb.portals
WHERE data__Identifier = '<PortalArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>portals</code> resource, the following permissions are required:

### Create
```json
workspaces-web:CreatePortal,
workspaces-web:GetPortal,
workspaces-web:GetPortalServiceProviderMetadata,
workspaces-web:AssociateBrowserSettings,
workspaces-web:AssociateIpAccessSettings,
workspaces-web:AssociateNetworkSettings,
workspaces-web:AssociateTrustStore,
workspaces-web:AssociateUserAccessLoggingSettings,
workspaces-web:AssociateUserSettings,
workspaces-web:ListTagsForResource,
workspaces-web:TagResource,
kms:CreateGrant,
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
sso:DescribeRegisteredRegions
```

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

### List
```json
workspaces-web:ListPortals,
kms:Decrypt
```

