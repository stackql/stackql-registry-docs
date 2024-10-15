---
title: replication_protection_container_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_container_mappings
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

Creates, updates, deletes, gets or lists a <code>replication_protection_container_mappings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_protection_container_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protection_container_mappings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protection_container_mappings', value: 'view', },
        { label: 'replication_protection_container_mappings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="health" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_error_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="mappingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="protectionContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_specific_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_fabric_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_protection_container_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_fabric_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_protection_container_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_protection_container_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Protection container mapping properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of a protection container mapping. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Lists the protection container mappings in the vault. |
| <CopyableCode code="list_by_replication_protection_containers" /> | `SELECT` | <CopyableCode code="fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Lists the protection container mappings for a protection container. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to create a protection container mapping. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to delete or remove a protection container mapping. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to update protection container mapping. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to purge(force delete) a protection container mapping. |

## `SELECT` examples

Lists the protection container mappings in the vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protection_container_mappings', value: 'view', },
        { label: 'replication_protection_container_mappings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
fabricName,
health,
health_error_details,
location,
mappingName,
policy_friendly_name,
policy_id,
protectionContainerName,
provider_specific_details,
resourceGroupName,
resourceName,
source_fabric_friendly_name,
source_protection_container_friendly_name,
state,
subscriptionId,
target_fabric_friendly_name,
target_protection_container_friendly_name,
target_protection_container_id,
type
FROM azure.recovery_services_site_recovery.vw_replication_protection_container_mappings
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
FROM azure.recovery_services_site_recovery.replication_protection_container_mappings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_protection_container_mappings</code> resource.

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
INSERT INTO azure.recovery_services_site_recovery.replication_protection_container_mappings (
fabricName,
mappingName,
protectionContainerName,
resourceGroupName,
resourceName,
subscriptionId,
properties
)
SELECT 
'{{ fabricName }}',
'{{ mappingName }}',
'{{ protectionContainerName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
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
        - name: targetProtectionContainerId
          value: string
        - name: policyId
          value: string
        - name: providerSpecificInput
          value:
            - name: instanceType
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>replication_protection_container_mappings</code> resource.

```sql
/*+ update */
UPDATE azure.recovery_services_site_recovery.replication_protection_container_mappings
SET 
properties = '{{ properties }}'
WHERE 
fabricName = '{{ fabricName }}'
AND mappingName = '{{ mappingName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>replication_protection_container_mappings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_site_recovery.replication_protection_container_mappings
WHERE fabricName = '{{ fabricName }}'
AND mappingName = '{{ mappingName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
