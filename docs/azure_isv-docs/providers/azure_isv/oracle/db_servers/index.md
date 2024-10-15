---
title: db_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - db_servers
  - oracle
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

Creates, updates, deletes, gets or lists a <code>db_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.db_servers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_db_servers', value: 'view', },
        { label: 'db_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="autonomous_virtual_machine_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="autonomous_vm_cluster_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloudexadatainfrastructurename" /> | `text` | field from the `properties` object |
| <CopyableCode code="compartment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cpu_core_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="db_node_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="db_node_storage_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="db_server_patching_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="dbserverocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="exadata_infrastructure_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_cpu_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_db_node_storage_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_memory_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="memory_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="ocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shape" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_cluster_ids" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | DbServer resource properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudexadatainfrastructurename, dbserverocid, resourceGroupName, subscriptionId" /> | Get a DbServer |

## `SELECT` examples

Get a DbServer

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_db_servers', value: 'view', },
        { label: 'db_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
autonomous_virtual_machine_ids,
autonomous_vm_cluster_ids,
cloudexadatainfrastructurename,
compartment_id,
cpu_core_count,
db_node_ids,
db_node_storage_size_in_gbs,
db_server_patching_details,
dbserverocid,
display_name,
exadata_infrastructure_id,
lifecycle_details,
lifecycle_state,
max_cpu_count,
max_db_node_storage_in_gbs,
max_memory_in_gbs,
memory_size_in_gbs,
ocid,
provisioning_state,
resourceGroupName,
shape,
subscriptionId,
time_created,
vm_cluster_ids
FROM azure_isv.oracle.vw_db_servers
WHERE cloudexadatainfrastructurename = '{{ cloudexadatainfrastructurename }}'
AND dbserverocid = '{{ dbserverocid }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.oracle.db_servers
WHERE cloudexadatainfrastructurename = '{{ cloudexadatainfrastructurename }}'
AND dbserverocid = '{{ dbserverocid }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

