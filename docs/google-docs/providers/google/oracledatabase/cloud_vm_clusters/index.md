---
title: cloud_vm_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_vm_clusters
  - oracledatabase
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.oracledatabase.cloud_vm_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The name of the VM Cluster resource with the format: projects/{project}/locations/{region}/cloudVmClusters/{cloud_vm_cluster} |
| <CopyableCode code="backupSubnetCidr" /> | `string` | Required. CIDR range of the backup subnet. |
| <CopyableCode code="cidr" /> | `string` | Required. Network settings. CIDR to use for cluster IP allocation. |
| <CopyableCode code="createTime" /> | `string` | Output only. The date and time that the VM cluster was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly name for this resource. |
| <CopyableCode code="exadataInfrastructure" /> | `string` | Required. The name of the Exadata Infrastructure resource on which VM cluster resource is created, in the following format: projects/{project}/locations/{region}/cloudExadataInfrastuctures/{cloud_extradata_infrastructure} |
| <CopyableCode code="gcpOracleZone" /> | `string` | Output only. GCP location where Oracle Exadata is hosted. It is same as GCP Oracle zone of Exadata infrastructure. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels or tags associated with the VM Cluster. |
| <CopyableCode code="network" /> | `string` | Required. The name of the VPC network. Format: projects/{project}/global/networks/{network} |
| <CopyableCode code="properties" /> | `object` | Various properties and settings associated with Exadata VM cluster. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudVmClustersId, locationsId, projectsId" /> | Gets details of a single VM Cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the VM Clusters in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new VM Cluster in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudVmClustersId, locationsId, projectsId" /> | Deletes a single VM Cluster. |

## `SELECT` examples

Lists the VM Clusters in a given project and location.

```sql
SELECT
name,
backupSubnetCidr,
cidr,
createTime,
displayName,
exadataInfrastructure,
gcpOracleZone,
labels,
network,
properties
FROM google.oracledatabase.cloud_vm_clusters
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

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
INSERT INTO google.oracledatabase.cloud_vm_clusters (
locationsId,
projectsId,
name,
exadataInfrastructure,
displayName,
properties,
labels,
cidr,
backupSubnetCidr,
network
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ exadataInfrastructure }}',
'{{ displayName }}',
'{{ properties }}',
'{{ labels }}',
'{{ cidr }}',
'{{ backupSubnetCidr }}',
'{{ network }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
exadataInfrastructure: string
displayName: string
gcpOracleZone: string
properties:
  ocid: string
  licenseType: string
  giVersion: string
  timeZone:
    id: string
    version: string
  sshPublicKeys:
    - type: string
  nodeCount: integer
  shape: string
  ocpuCount: number
  memorySizeGb: integer
  dbNodeStorageSizeGb: integer
  storageSizeGb: integer
  dataStorageSizeTb: number
  diskRedundancy: string
  sparseDiskgroupEnabled: boolean
  localBackupEnabled: boolean
  hostnamePrefix: string
  diagnosticsDataCollectionOptions:
    diagnosticsEventsEnabled: boolean
    healthMonitoringEnabled: boolean
    incidentLogsEnabled: boolean
  state: string
  scanListenerPortTcp: integer
  scanListenerPortTcpSsl: integer
  domain: string
  scanDns: string
  hostname: string
  cpuCoreCount: integer
  systemVersion: string
  scanIpIds:
    - type: string
  scanDnsRecordId: string
  ociUrl: string
  dbServerOcids:
    - type: string
  compartmentId: string
  dnsListenerIp: string
  clusterName: string
labels: object
createTime: string
cidr: string
backupSubnetCidr: string
network: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>cloud_vm_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM google.oracledatabase.cloud_vm_clusters
WHERE cloudVmClustersId = '{{ cloudVmClustersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
