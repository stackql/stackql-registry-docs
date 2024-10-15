---
title: replication_protection_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_containers
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

Creates, updates, deletes, gets or lists a <code>replication_protection_containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_protection_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protection_containers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protection_containers', value: 'view', },
        { label: 'replication_protection_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_specific_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="pairing_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="protected_item_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="protectionContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Protection profile custom data details. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of a protection container. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Lists the protection containers in a vault. |
| <CopyableCode code="list_by_replication_fabrics" /> | `SELECT` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId" /> | Lists the protection containers in the specified fabric. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Operation to create a protection container. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Operation to remove a protection container. |
| <CopyableCode code="discover_protectable_item" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to a add a protectable item to a protection container(Add physical server). |
| <CopyableCode code="switch_cluster_protection" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Operation to switch protection from one container to another. |
| <CopyableCode code="switch_protection" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Operation to switch protection from one container to another or one replication provider to another. |

## `SELECT` examples

Lists the protection containers in a vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protection_containers', value: 'view', },
        { label: 'replication_protection_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
fabricName,
fabric_friendly_name,
fabric_specific_details,
fabric_type,
friendly_name,
location,
pairing_status,
protected_item_count,
protectionContainerName,
resourceGroupName,
resourceName,
role,
subscriptionId,
type
FROM azure.recovery_services_site_recovery.vw_replication_protection_containers
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
FROM azure.recovery_services_site_recovery.replication_protection_containers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_protection_containers</code> resource.

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
INSERT INTO azure.recovery_services_site_recovery.replication_protection_containers (
fabricName,
protectionContainerName,
resourceGroupName,
resourceName,
subscriptionId,
properties
)
SELECT 
'{{ fabricName }}',
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
        - name: providerSpecificInput
          value:
            - - name: instanceType
                value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>replication_protection_containers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_site_recovery.replication_protection_containers
WHERE fabricName = '{{ fabricName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
