---
title: local_users
hide_title: false
hide_table_of_contents: false
keywords:
  - local_users
  - storage
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>local_users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.local_users" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_local_users', value: 'view', },
        { label: 'local_users', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_acl_authorization" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="has_shared_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="has_ssh_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="has_ssh_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="home_directory" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_nf_sv3_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="permission_scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sid" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssh_authorized_keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="user_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="username" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The Storage Account Local User properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, username" /> | Get the local user of the storage account by username. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List the local users associated with the storage account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, username" /> | Create or update the properties of a local user associated with the storage account. Properties for NFSv3 enablement and extended groups cannot be set with other properties. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, username" /> | Deletes the local user associated with the specified storage account. |
| <CopyableCode code="regenerate_password" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, username" /> | Regenerate the local user SSH password. |

## `SELECT` examples

List the local users associated with the storage account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_local_users', value: 'view', },
        { label: 'local_users', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
allow_acl_authorization,
extended_groups,
group_id,
has_shared_key,
has_ssh_key,
has_ssh_password,
home_directory,
is_nf_sv3_enabled,
permission_scopes,
resourceGroupName,
sid,
ssh_authorized_keys,
subscriptionId,
system_data,
type,
user_id,
username
FROM azure.storage.vw_local_users
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.storage.local_users
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>local_users</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.storage.local_users (
accountName,
resourceGroupName,
subscriptionId,
username,
properties,
systemData
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ username }}',
'{{ properties }}',
'{{ systemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: permissionScopes
          value:
            - - name: permissions
                value: string
              - name: service
                value: string
              - name: resourceName
                value: string
        - name: homeDirectory
          value: string
        - name: sshAuthorizedKeys
          value: []
        - name: sid
          value: string
        - name: hasSharedKey
          value: boolean
        - name: hasSshKey
          value: boolean
        - name: hasSshPassword
          value: boolean
        - name: userId
          value: integer
        - name: groupId
          value: integer
        - name: allowAclAuthorization
          value: boolean
        - name: extendedGroups
          value:
            - integer
        - name: isNFSv3Enabled
          value: boolean
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>local_users</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage.local_users
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND username = '{{ username }}';
```
