---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - data_lake_store
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_lake_store.accounts" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_tier" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewall_allow_azure_ips" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewall_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewall_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `object` | The encryption identity properties. |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="new_tier" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="trusted_id_provider_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="trusted_id_providers" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
| <CopyableCode code="virtual_network_rules" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="identity" /> | `object` | The encryption identity properties. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | Data Lake Store account properties information. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the specified Data Lake Store account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the Data Lake Store accounts within the subscription. The response includes a link to the next page of results, if any. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the Data Lake Store accounts within a specific resource group. The response includes a link to the next page of results, if any. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__location" /> | Creates the specified Data Lake Store account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Deletes the specified Data Lake Store account. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Updates the specified Data Lake Store account information. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__type" /> | Checks whether the specified account name is available or taken. |
| <CopyableCode code="enable_key_vault" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Attempts to enable a user managed Key Vault for encryption of the specified Data Lake Store account. |

## `SELECT` examples

Lists the Data Lake Store accounts within the subscription. The response includes a link to the next page of results, if any.

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
id,
name,
accountName,
account_id,
creation_time,
current_tier,
default_group,
encryption_config,
encryption_provisioning_state,
encryption_state,
endpoint,
firewall_allow_azure_ips,
firewall_rules,
firewall_state,
identity,
last_modified_time,
location,
new_tier,
provisioning_state,
resourceGroupName,
state,
subscriptionId,
tags,
trusted_id_provider_state,
trusted_id_providers,
type,
virtual_network_rules
FROM azure.data_lake_store.vw_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
tags,
type
FROM azure.data_lake_store.accounts
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
INSERT INTO azure.data_lake_store.accounts (
accountName,
resourceGroupName,
subscriptionId,
data__location,
location,
tags,
identity,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ location }}',
'{{ tags }}',
'{{ identity }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: identity
      value:
        - name: type
          value: string
        - name: principalId
          value: string
        - name: tenantId
          value: string
    - name: properties
      value:
        - name: defaultGroup
          value: string
        - name: encryptionConfig
          value:
            - name: type
              value: string
            - name: keyVaultMetaInfo
              value:
                - name: keyVaultResourceId
                  value: string
                - name: encryptionKeyName
                  value: string
                - name: encryptionKeyVersion
                  value: string
        - name: encryptionState
          value: string
        - name: firewallRules
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: startIpAddress
                    value: string
                  - name: endIpAddress
                    value: string
        - name: virtualNetworkRules
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: subnetId
                    value: string
        - name: firewallState
          value: string
        - name: firewallAllowAzureIps
          value: string
        - name: trustedIdProviders
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: idProvider
                    value: string
        - name: trustedIdProviderState
          value: string
        - name: newTier
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>accounts</code> resource.

```sql
/*+ update */
UPDATE azure.data_lake_store.accounts
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_lake_store.accounts
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
