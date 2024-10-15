---
title: managed_hsms_deleted
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_hsms_deleted
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

Creates, updates, deletes, gets or lists a <code>managed_hsms_deleted</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_hsms_deleted</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.managed_hsms_deleted" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_hsms_deleted', value: 'view', },
        { label: 'managed_hsms_deleted', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The Azure Resource Manager resource ID for the deleted managed HSM Pool. |
| <CopyableCode code="name" /> | `text` | The name of the managed HSM Pool. |
| <CopyableCode code="deletion_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="mhsm_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="purge_protection_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_purge_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type of the managed HSM Pool. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Azure Resource Manager resource ID for the deleted managed HSM Pool. |
| <CopyableCode code="name" /> | `string` | The name of the managed HSM Pool. |
| <CopyableCode code="properties" /> | `object` | Properties of the deleted managed HSM. |
| <CopyableCode code="type" /> | `string` | The resource type of the managed HSM Pool. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, name, subscriptionId" /> | Gets the specified deleted managed HSM. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The List operation gets information about the deleted managed HSMs associated with the subscription. |

## `SELECT` examples

The List operation gets information about the deleted managed HSMs associated with the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_hsms_deleted', value: 'view', },
        { label: 'managed_hsms_deleted', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
deletion_date,
location,
mhsm_id,
purge_protection_enabled,
scheduled_purge_date,
subscriptionId,
tags,
type
FROM azure.key_vault.vw_managed_hsms_deleted
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
FROM azure.key_vault.managed_hsms_deleted
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

