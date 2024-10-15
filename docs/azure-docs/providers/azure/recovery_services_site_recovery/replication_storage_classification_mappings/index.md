---
title: replication_storage_classification_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_storage_classification_mappings
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

Creates, updates, deletes, gets or lists a <code>replication_storage_classification_mappings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_storage_classification_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_storage_classification_mappings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_storage_classification_mappings', value: 'view', },
        { label: 'replication_storage_classification_mappings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageClassificationMappingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageClassificationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_storage_classification_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Storage mapping properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, resourceGroupName, resourceName, storageClassificationMappingName, storageClassificationName, subscriptionId" /> | Gets the details of the specified storage classification mapping. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Lists the storage classification mappings in the vault. |
| <CopyableCode code="list_by_replication_storage_classifications" /> | `SELECT` | <CopyableCode code="fabricName, resourceGroupName, resourceName, storageClassificationName, subscriptionId" /> | Lists the storage classification mappings for the fabric. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fabricName, resourceGroupName, resourceName, storageClassificationMappingName, storageClassificationName, subscriptionId" /> | The operation to create a storage classification mapping. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fabricName, resourceGroupName, resourceName, storageClassificationMappingName, storageClassificationName, subscriptionId" /> | The operation to delete a storage classification mapping. |

## `SELECT` examples

Lists the storage classification mappings in the vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_storage_classification_mappings', value: 'view', },
        { label: 'replication_storage_classification_mappings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
fabricName,
location,
resourceGroupName,
resourceName,
storageClassificationMappingName,
storageClassificationName,
subscriptionId,
target_storage_classification_id,
type
FROM azure.recovery_services_site_recovery.vw_replication_storage_classification_mappings
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
FROM azure.recovery_services_site_recovery.replication_storage_classification_mappings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_storage_classification_mappings</code> resource.

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
INSERT INTO azure.recovery_services_site_recovery.replication_storage_classification_mappings (
fabricName,
resourceGroupName,
resourceName,
storageClassificationMappingName,
storageClassificationName,
subscriptionId,
properties
)
SELECT 
'{{ fabricName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ storageClassificationMappingName }}',
'{{ storageClassificationName }}',
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
        - name: targetStorageClassificationId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>replication_storage_classification_mappings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_site_recovery.replication_storage_classification_mappings
WHERE fabricName = '{{ fabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND storageClassificationMappingName = '{{ storageClassificationMappingName }}'
AND storageClassificationName = '{{ storageClassificationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
