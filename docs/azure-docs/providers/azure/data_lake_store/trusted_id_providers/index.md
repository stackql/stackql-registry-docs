---
title: trusted_id_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - trusted_id_providers
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

Creates, updates, deletes, gets or lists a <code>trusted_id_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trusted_id_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_lake_store.trusted_id_providers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_trusted_id_providers', value: 'view', },
        { label: 'trusted_id_providers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="id_provider" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="trustedIdProviderName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | The trusted identity provider properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, trustedIdProviderName" /> | Gets the specified Data Lake Store trusted identity provider. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the Data Lake Store trusted identity providers within the specified Data Lake Store account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, trustedIdProviderName, data__properties" /> | Creates or updates the specified trusted identity provider. During update, the trusted identity provider with the specified name will be replaced with this new provider |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, trustedIdProviderName" /> | Deletes the specified trusted identity provider from the specified Data Lake Store account |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, trustedIdProviderName" /> | Updates the specified trusted identity provider. |

## `SELECT` examples

Lists the Data Lake Store trusted identity providers within the specified Data Lake Store account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_trusted_id_providers', value: 'view', },
        { label: 'trusted_id_providers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
id_provider,
resourceGroupName,
subscriptionId,
trustedIdProviderName,
type
FROM azure.data_lake_store.vw_trusted_id_providers
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
type
FROM azure.data_lake_store.trusted_id_providers
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>trusted_id_providers</code> resource.

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
INSERT INTO azure.data_lake_store.trusted_id_providers (
accountName,
resourceGroupName,
subscriptionId,
trustedIdProviderName,
data__properties,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ trustedIdProviderName }}',
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
        - name: idProvider
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>trusted_id_providers</code> resource.

```sql
/*+ update */
UPDATE azure.data_lake_store.trusted_id_providers
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trustedIdProviderName = '{{ trustedIdProviderName }}';
```

## `DELETE` example

Deletes the specified <code>trusted_id_providers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_lake_store.trusted_id_providers
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trustedIdProviderName = '{{ trustedIdProviderName }}';
```
