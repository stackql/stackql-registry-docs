---
title: replicationv_center
hide_title: false
hide_table_of_contents: false
keywords:
  - replicationv_center
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

Creates, updates, deletes, gets or lists a <code>replicationv_center</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replicationv_center</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replicationv_center" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replicationv_center', value: 'view', },
        { label: 'replicationv_center', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="discovery_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_arm_resource_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="infrastructure_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="internal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_heartbeat" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="port" /> | `text` | field from the `properties` object |
| <CopyableCode code="process_server_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_as_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
| <CopyableCode code="vcenterName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | vCenter properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId, vcenterName" /> | Gets the details of a registered vCenter server(Add vCenter server). |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Lists the vCenter servers registered in the vault. |
| <CopyableCode code="list_by_replication_fabrics" /> | `SELECT` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId" /> | Lists the vCenter servers registered in a fabric. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId, vcenterName" /> | The operation to create a vCenter object.. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId, vcenterName" /> | The operation to remove(unregister) a registered vCenter server from the vault. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId, vcenterName" /> | The operation to update a registered vCenter. |

## `SELECT` examples

Lists the vCenter servers registered in the vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replicationv_center', value: 'view', },
        { label: 'replicationv_center', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
discovery_status,
fabricName,
fabric_arm_resource_name,
friendly_name,
health_errors,
infrastructure_id,
internal_id,
ip_address,
last_heartbeat,
location,
port,
process_server_id,
resourceGroupName,
resourceName,
run_as_account_id,
subscriptionId,
type,
vcenterName
FROM azure.recovery_services_site_recovery.vw_replicationv_center
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
FROM azure.recovery_services_site_recovery.replicationv_center
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replicationv_center</code> resource.

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
INSERT INTO azure.recovery_services_site_recovery.replicationv_center (
fabricName,
resourceGroupName,
resourceName,
subscriptionId,
vcenterName,
properties
)
SELECT 
'{{ fabricName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ vcenterName }}',
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
        - name: friendlyName
          value: string
        - name: ipAddress
          value: string
        - name: processServerId
          value: string
        - name: port
          value: string
        - name: runAsAccountId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>replicationv_center</code> resource.

```sql
/*+ update */
UPDATE azure.recovery_services_site_recovery.replicationv_center
SET 
properties = '{{ properties }}'
WHERE 
fabricName = '{{ fabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vcenterName = '{{ vcenterName }}';
```

## `DELETE` example

Deletes the specified <code>replicationv_center</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_site_recovery.replicationv_center
WHERE fabricName = '{{ fabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vcenterName = '{{ vcenterName }}';
```
