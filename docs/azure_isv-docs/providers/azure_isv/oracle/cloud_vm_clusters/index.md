---
title: cloud_vm_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_vm_clusters
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

Creates, updates, deletes, gets or lists a <code>cloud_vm_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_vm_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.cloud_vm_clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_vm_clusters', value: 'view', },
        { label: 'cloud_vm_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="backup_subnet_cidr" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_exadata_infrastructure_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloudvmclustername" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="compartment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_nodes" /> | `text` | field from the `properties` object |
| <CopyableCode code="cpu_core_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_collection_options" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_storage_percentage" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_storage_size_in_tbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="db_node_storage_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="db_servers" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_redundancy" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain" /> | `text` | field from the `properties` object |
| <CopyableCode code="gi_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostname" /> | `text` | field from the `properties` object |
| <CopyableCode code="iorm_config_cache" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_local_backup_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_sparse_diskgroup_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_update_history_entry_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="license_model" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="listener_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="memory_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="nsg_cidrs" /> | `text` | field from the `properties` object |
| <CopyableCode code="nsg_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="oci_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="ocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="ocpu_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scan_dns_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="scan_dns_record_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="scan_ip_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="scan_listener_port_tcp" /> | `text` | field from the `properties` object |
| <CopyableCode code="scan_listener_port_tcp_ssl" /> | `text` | field from the `properties` object |
| <CopyableCode code="shape" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssh_public_keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet_ocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="vip_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="zone_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | CloudVmCluster resource model |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId" /> | Get a CloudVmCluster |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List CloudVmCluster resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List CloudVmCluster resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId" /> | Create a CloudVmCluster |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId" /> | Delete a CloudVmCluster |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId" /> | Update a CloudVmCluster |
| <CopyableCode code="add_vms" /> | `EXEC` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId, data__dbServers" /> | Add VMs to the VM Cluster |
| <CopyableCode code="remove_vms" /> | `EXEC` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId, data__dbServers" /> | Remove VMs from the VM Cluster |

## `SELECT` examples

List CloudVmCluster resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_vm_clusters', value: 'view', },
        { label: 'cloud_vm_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
backup_subnet_cidr,
cloud_exadata_infrastructure_id,
cloudvmclustername,
cluster_name,
compartment_id,
compute_nodes,
cpu_core_count,
data_collection_options,
data_storage_percentage,
data_storage_size_in_tbs,
db_node_storage_size_in_gbs,
db_servers,
disk_redundancy,
display_name,
domain,
gi_version,
hostname,
iorm_config_cache,
is_local_backup_enabled,
is_sparse_diskgroup_enabled,
last_update_history_entry_id,
license_model,
lifecycle_details,
lifecycle_state,
listener_port,
location,
memory_size_in_gbs,
node_count,
nsg_cidrs,
nsg_url,
oci_url,
ocid,
ocpu_count,
provisioning_state,
resourceGroupName,
scan_dns_name,
scan_dns_record_id,
scan_ip_ids,
scan_listener_port_tcp,
scan_listener_port_tcp_ssl,
shape,
ssh_public_keys,
storage_size_in_gbs,
subnet_id,
subnet_ocid,
subscriptionId,
system_version,
tags,
time_created,
time_zone,
vip_ids,
vnet_id,
zone_id
FROM azure_isv.oracle.vw_cloud_vm_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_isv.oracle.cloud_vm_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cloud_vm_clusters</code> resource.

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
INSERT INTO azure_isv.oracle.cloud_vm_clusters (
cloudvmclustername,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ cloudvmclustername }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: ocid
          value: []
        - name: listenerPort
          value: integer
        - name: nodeCount
          value: integer
        - name: storageSizeInGbs
          value: integer
        - name: dataStorageSizeInTbs
          value: number
        - name: dbNodeStorageSizeInGbs
          value: integer
        - name: memorySizeInGbs
          value: integer
        - name: timeCreated
          value: string
        - name: lifecycleDetails
          value: string
        - name: timeZone
          value: string
        - name: hostname
          value: string
        - name: domain
          value: string
        - name: cpuCoreCount
          value: integer
        - name: ocpuCount
          value: number
        - name: clusterName
          value: string
        - name: dataStoragePercentage
          value: integer
        - name: isLocalBackupEnabled
          value: boolean
        - name: cloudExadataInfrastructureId
          value: []
        - name: isSparseDiskgroupEnabled
          value: boolean
        - name: systemVersion
          value: string
        - name: sshPublicKeys
          value:
            - string
        - name: licenseModel
          value: []
        - name: diskRedundancy
          value: []
        - name: scanIpIds
          value:
            - string
        - name: vipIds
          value:
            - string
        - name: scanDnsName
          value: string
        - name: scanListenerPortTcp
          value: integer
        - name: scanListenerPortTcpSsl
          value: integer
        - name: shape
          value: string
        - name: provisioningState
          value: []
        - name: lifecycleState
          value: []
        - name: vnetId
          value: []
        - name: giVersion
          value: string
        - name: ociUrl
          value: string
        - name: nsgUrl
          value: string
        - name: subnetId
          value: []
        - name: backupSubnetCidr
          value: string
        - name: nsgCidrs
          value:
            - - name: source
                value: string
              - name: destinationPortRange
                value:
                  - name: min
                    value: integer
                  - name: max
                    value: integer
        - name: dataCollectionOptions
          value:
            - name: isDiagnosticsEventsEnabled
              value: boolean
            - name: isHealthMonitoringEnabled
              value: boolean
            - name: isIncidentLogsEnabled
              value: boolean
        - name: displayName
          value: string
        - name: computeNodes
          value:
            - []
        - name: iormConfigCache
          value:
            - name: dbPlans
              value:
                - - name: dbName
                    value: string
                  - name: flashCacheLimit
                    value: string
                  - name: share
                    value: integer
            - name: lifecycleDetails
              value: string
            - name: lifecycleState
              value: []
            - name: objective
              value: []
        - name: dbServers
          value:
            - []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>cloud_vm_clusters</code> resource.

```sql
/*+ update */
UPDATE azure_isv.oracle.cloud_vm_clusters
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
cloudvmclustername = '{{ cloudvmclustername }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>cloud_vm_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.oracle.cloud_vm_clusters
WHERE cloudvmclustername = '{{ cloudvmclustername }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
