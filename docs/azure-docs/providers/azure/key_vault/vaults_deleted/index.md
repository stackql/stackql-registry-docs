---
title: vaults_deleted
hide_title: false
hide_table_of_contents: false
keywords:
  - vaults_deleted
  - key_vault
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

Creates, updates, deletes, gets or lists a <code>vaults_deleted</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vaults_deleted</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.vaults_deleted" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vaults_deleted', value: 'view', },
        { label: 'vaults_deleted', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource ID for the deleted key vault. |
| <CopyableCode code="name" /> | `text` | The name of the key vault. |
| <CopyableCode code="deletion_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="purge_protection_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_purge_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type of the key vault. |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vault_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID for the deleted key vault. |
| <CopyableCode code="name" /> | `string` | The name of the key vault. |
| <CopyableCode code="properties" /> | `object` | Properties of the deleted vault. |
| <CopyableCode code="type" /> | `string` | The resource type of the key vault. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId, vaultName" /> | Gets the deleted Azure key vault. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets information about the deleted vaults in a subscription. |

## `SELECT` examples

Gets information about the deleted vaults in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vaults_deleted', value: 'view', },
        { label: 'vaults_deleted', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
deletion_date,
location,
purge_protection_enabled,
scheduled_purge_date,
subscriptionId,
tags,
type,
vaultName,
vault_id
FROM azure.key_vault.vw_vaults_deleted
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.key_vault.vaults_deleted
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

