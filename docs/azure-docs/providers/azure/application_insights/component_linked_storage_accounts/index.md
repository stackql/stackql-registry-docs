---
title: component_linked_storage_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - component_linked_storage_accounts
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>component_linked_storage_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_linked_storage_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.component_linked_storage_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_component_linked_storage_accounts', value: 'view', },
        { label: 'component_linked_storage_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="linked_storage_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageType" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | An Application Insights component linked storage account |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, storageType, subscriptionId" /> | Returns the current linked storage settings for an Application Insights component. |
| <CopyableCode code="create_and_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, storageType, subscriptionId" /> | Replace current linked storage account for an Application Insights component. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, storageType, subscriptionId" /> | Delete linked storage accounts for an Application Insights component. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, storageType, subscriptionId" /> | Update linked storage accounts for an Application Insights component. |

## `SELECT` examples

Returns the current linked storage settings for an Application Insights component.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_component_linked_storage_accounts', value: 'view', },
        { label: 'component_linked_storage_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
linked_storage_account,
resourceGroupName,
resourceName,
storageType,
subscriptionId
FROM azure.application_insights.vw_component_linked_storage_accounts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND storageType = '{{ storageType }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.application_insights.component_linked_storage_accounts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND storageType = '{{ storageType }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>component_linked_storage_accounts</code> resource.

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
INSERT INTO azure.application_insights.component_linked_storage_accounts (
resourceGroupName,
resourceName,
storageType,
subscriptionId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ storageType }}',
'{{ subscriptionId }}',
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
        - name: linkedStorageAccount
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>component_linked_storage_accounts</code> resource.

```sql
/*+ update */
UPDATE azure.application_insights.component_linked_storage_accounts
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND storageType = '{{ storageType }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>component_linked_storage_accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.application_insights.component_linked_storage_accounts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND storageType = '{{ storageType }}'
AND subscriptionId = '{{ subscriptionId }}';
```
