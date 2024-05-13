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


Used to retrieve a list of <code>portals</code> in a region or to create or delete a <code>portals</code> resource, use <code>portal</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>portals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::Portal Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.portals" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="portal_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
portal_arn
FROM aws.workspacesweb.portals
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
 IpAccessSettingsArn,
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
 '{{ IpAccessSettingsArn }}',
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
 IpAccessSettingsArn,
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
 '{{ IpAccessSettingsArn }}',
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
      - name: IpAccessSettingsArn
        value: '{{ IpAccessSettingsArn }}'
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

## `DELETE` Example

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

