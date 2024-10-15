---
title: sql_server_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_server_instances
  - azure_arc_data
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

Creates, updates, deletes, gets or lists a <code>sql_server_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_server_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.sql_server_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_server_instances', value: 'view', },
        { label: 'sql_server_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="always_on_role" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_defender_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_defender_status_last_updated" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="collation" /> | `text` | field from the `properties` object |
| <CopyableCode code="container_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cores" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="edition" /> | `text` | field from the `properties` object |
| <CopyableCode code="failover_cluster" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_inventory_upload_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_usage_upload_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="license_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="monitoring" /> | `text` | field from the `properties` object |
| <CopyableCode code="patch_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlServerInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tcp_dynamic_ports" /> | `text` | field from the `properties` object |
| <CopyableCode code="tcp_static_ports" /> | `text` | field from the `properties` object |
| <CopyableCode code="upgrade_locked_until" /> | `text` | field from the `properties` object |
| <CopyableCode code="v_core" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of SqlServerInstance. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Retrieves a SQL Server Instance resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all sqlServerInstances in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Creates or replaces a SQL Server Instance resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Deletes a SQL Server Instance resource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Updates a SQL Server Instance resource |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_server_instances', value: 'view', },
        { label: 'sql_server_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
always_on_role,
azure_defender_status,
azure_defender_status_last_updated,
backup_policy,
collation,
container_resource_id,
cores,
create_time,
current_version,
edition,
failover_cluster,
host_type,
instance_name,
last_inventory_upload_time,
last_usage_upload_time,
license_type,
location,
monitoring,
patch_level,
product_id,
provisioning_state,
resourceGroupName,
sqlServerInstanceName,
status,
subscriptionId,
tags,
tcp_dynamic_ports,
tcp_static_ports,
upgrade_locked_until,
v_core,
version
FROM azure.azure_arc_data.vw_sql_server_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.azure_arc_data.sql_server_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_server_instances</code> resource.

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
INSERT INTO azure.azure_arc_data.sql_server_instances (
resourceGroupName,
sqlServerInstanceName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sqlServerInstanceName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
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
        - name: version
          value: string
        - name: edition
          value: string
        - name: containerResourceId
          value: string
        - name: createTime
          value: string
        - name: vCore
          value: string
        - name: cores
          value: string
        - name: status
          value: string
        - name: patchLevel
          value: string
        - name: collation
          value: string
        - name: currentVersion
          value: string
        - name: instanceName
          value: string
        - name: tcpDynamicPorts
          value: string
        - name: tcpStaticPorts
          value: string
        - name: productId
          value: string
        - name: licenseType
          value: string
        - name: azureDefenderStatusLastUpdated
          value: string
        - name: azureDefenderStatus
          value: string
        - name: provisioningState
          value: string
        - name: lastInventoryUploadTime
          value: string
        - name: lastUsageUploadTime
          value: string
        - name: hostType
          value: string
        - name: alwaysOnRole
          value: string
        - name: failoverCluster
          value:
            - name: id
              value: string
            - name: networkName
              value: string
            - name: sqlInstanceIds
              value:
                - string
            - name: hostNames
              value:
                - string
        - name: backupPolicy
          value:
            - name: retentionPeriodDays
              value: integer
            - name: fullBackupDays
              value: integer
            - name: differentialBackupHours
              value: integer
            - name: transactionLogBackupMinutes
              value: integer
        - name: upgradeLockedUntil
          value: string
        - name: monitoring
          value:
            - name: enabled
              value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sql_server_instances</code> resource.

```sql
/*+ update */
UPDATE azure.azure_arc_data.sql_server_instances
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerInstanceName = '{{ sqlServerInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sql_server_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.azure_arc_data.sql_server_instances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerInstanceName = '{{ sqlServerInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
