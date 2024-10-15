---
title: remote_rendering_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - remote_rendering_accounts
  - mixed_reality
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

Creates, updates, deletes, gets or lists a <code>remote_rendering_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>remote_rendering_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mixed_reality.remote_rendering_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_remote_rendering_accounts', value: 'view', },
        { label: 'remote_rendering_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_domain" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="kind" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="plan" /> | `text` | Identity for the resource. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="storage_account_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="plan" /> | `object` | Identity for the resource. |
| <CopyableCode code="properties" /> | `object` | Common Properties shared by Mixed Reality Accounts |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieve a Remote Rendering Account. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List Resources by Resource Group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Remote Rendering Accounts by Subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Creating or Updating a Remote Rendering Account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Delete a Remote Rendering Account. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Updating a Remote Rendering Account |
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Regenerate specified Key of a Remote Rendering Account |

## `SELECT` examples

List Remote Rendering Accounts by Subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_remote_rendering_accounts', value: 'view', },
        { label: 'remote_rendering_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
account_domain,
account_id,
identity,
kind,
location,
plan,
resourceGroupName,
sku,
storage_account_name,
subscriptionId,
system_data,
tags
FROM azure.mixed_reality.vw_remote_rendering_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
kind,
location,
plan,
properties,
sku,
systemData,
tags
FROM azure.mixed_reality.remote_rendering_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>remote_rendering_accounts</code> resource.

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
INSERT INTO azure.mixed_reality.remote_rendering_accounts (
accountName,
resourceGroupName,
subscriptionId,
tags,
location,
properties,
identity,
plan,
sku,
kind,
systemData
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ identity }}',
'{{ plan }}',
'{{ sku }}',
'{{ kind }}',
'{{ systemData }}'
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
    - name: properties
      value:
        - name: storageAccountName
          value: string
        - name: accountId
          value: string
        - name: accountDomain
          value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>remote_rendering_accounts</code> resource.

```sql
/*+ update */
UPDATE azure.mixed_reality.remote_rendering_accounts
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
plan = '{{ plan }}',
sku = '{{ sku }}',
kind = '{{ kind }}',
systemData = '{{ systemData }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>remote_rendering_accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mixed_reality.remote_rendering_accounts
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
