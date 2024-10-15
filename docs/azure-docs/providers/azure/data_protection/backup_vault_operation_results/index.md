---
title: backup_vault_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vault_operation_results
  - data_protection
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

Creates, updates, deletes, gets or lists a <code>backup_vault_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_vault_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.backup_vault_operation_results" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_vault_operation_results', value: 'view', },
        { label: 'backup_vault_operation_results', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="bcdr_security_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="feature_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity details |
| <CopyableCode code="is_vault_protected_by_resource_guard" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitoring_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="replicated_regions" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guard_operation_requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_move_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_move_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="secure_score" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity details |
| <CopyableCode code="properties" /> | `object` | Backup Vault |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, resourceGroupName, subscriptionId, vaultName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_vault_operation_results', value: 'view', },
        { label: 'backup_vault_operation_results', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
bcdr_security_level,
feature_settings,
identity,
is_vault_protected_by_resource_guard,
monitoring_settings,
operationId,
provisioning_state,
replicated_regions,
resourceGroupName,
resource_guard_operation_requests,
resource_move_details,
resource_move_state,
secure_score,
security_settings,
storage_settings,
subscriptionId,
vaultName
FROM azure.data_protection.vw_backup_vault_operation_results
WHERE operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
properties
FROM azure.data_protection.backup_vault_operation_results
WHERE operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>

