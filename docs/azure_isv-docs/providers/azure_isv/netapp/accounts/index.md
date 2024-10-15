---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - netapp
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

Creates, updates, deletes, gets or lists a <code>accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_accounts', value: 'view', },
        { label: 'accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="active_directories" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_showmount" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | NetApp account properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Get the NetApp account |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List and describe all NetApp accounts in the resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List and describe all NetApp accounts in the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__location" /> | Create or update the specified NetApp account within the resource group |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Delete the specified NetApp account |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Patch the specified NetApp account |
| <CopyableCode code="renew_credentials" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Renew identity credentials that are used to authenticate to key vault, for customer-managed key encryption. If encryption.identity.principalId does not match identity.principalId, running this operation will fix it. |

## `SELECT` examples

List and describe all NetApp accounts in the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_accounts', value: 'view', },
        { label: 'accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
active_directories,
disable_showmount,
encryption,
etag,
identity,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure_isv.netapp.vw_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
identity,
location,
properties,
tags
FROM azure_isv.netapp.accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>accounts</code> resource.

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
INSERT INTO azure_isv.netapp.accounts (
accountName,
resourceGroupName,
subscriptionId,
data__location,
tags,
location,
properties,
identity
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: etag
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: activeDirectories
          value:
            - - name: activeDirectoryId
                value: string
              - name: username
                value: string
              - name: password
                value: string
              - name: domain
                value: string
              - name: dns
                value: string
              - name: status
                value: string
              - name: statusDetails
                value: string
              - name: smbServerName
                value: string
              - name: organizationalUnit
                value: string
              - name: site
                value: string
              - name: backupOperators
                value:
                  - string
              - name: administrators
                value:
                  - string
              - name: kdcIP
                value: string
              - name: adName
                value: string
              - name: serverRootCACertificate
                value: string
              - name: aesEncryption
                value: boolean
              - name: ldapSigning
                value: boolean
              - name: securityOperators
                value:
                  - string
              - name: ldapOverTLS
                value: boolean
              - name: allowLocalNfsUsersWithLdap
                value: boolean
              - name: encryptDCConnections
                value: boolean
              - name: ldapSearchScope
                value:
                  - name: userDN
                    value: string
                  - name: groupDN
                    value: string
                  - name: groupMembershipFilter
                    value: string
              - name: preferredServersForLdapClient
                value: string
        - name: encryption
          value:
            - name: keySource
              value: string
            - name: keyVaultProperties
              value:
                - name: keyVaultId
                  value: string
                - name: keyVaultUri
                  value: string
                - name: keyName
                  value: string
                - name: keyVaultResourceId
                  value: string
                - name: status
                  value: string
            - name: identity
              value:
                - name: principalId
                  value: string
                - name: userAssignedIdentity
                  value: string
        - name: disableShowmount
          value: boolean
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>accounts</code> resource.

```sql
/*+ update */
UPDATE azure_isv.netapp.accounts
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.netapp.accounts
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
