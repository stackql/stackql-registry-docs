---
title: replication_vault_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_vault_settings
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>replication_vault_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_vault_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_vault_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_vault_settings', value: 'view', },
        { label: 'replication_vault_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="migration_solution_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
| <CopyableCode code="vaultSettingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmware_to_azure_provider_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Vault setting properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, vaultSettingName" /> | Gets the vault setting. This includes the Migration Hub connection settings. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets the list of vault setting. This includes the Migration Hub connection settings. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, vaultSettingName, data__properties" /> | The operation to configure vault setting. |

## `SELECT` examples

Gets the list of vault setting. This includes the Migration Hub connection settings.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_vault_settings', value: 'view', },
        { label: 'replication_vault_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
location,
migration_solution_id,
resourceGroupName,
resourceName,
subscriptionId,
type,
vaultSettingName,
vmware_to_azure_provider_type
FROM azure.recovery_services_site_recovery.vw_replication_vault_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure.recovery_services_site_recovery.replication_vault_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_vault_settings</code> resource.

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
INSERT INTO azure.recovery_services_site_recovery.replication_vault_settings (
resourceGroupName,
resourceName,
subscriptionId,
vaultSettingName,
data__properties,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ vaultSettingName }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: migrationSolutionId
          value: string
        - name: vmwareToAzureProviderType
          value: string

```
</TabItem>
</Tabs>
