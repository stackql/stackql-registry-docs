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
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: exadataInfrastructure
      value: string
    - name: displayName
      value: string
    - name: gcpOracleZone
      value: string
    - name: properties
      value:
        - name: ocid
          value: string
        - name: licenseType
          value: string
        - name: giVersion
          value: string
        - name: timeZone
          value:
            - name: id
              value: string
            - name: version
              value: string
        - name: sshPublicKeys
          value:
            - string
        - name: nodeCount
          value: integer
        - name: shape
          value: string
        - name: ocpuCount
          value: number
        - name: memorySizeGb
          value: integer
        - name: dbNodeStorageSizeGb
          value: integer
        - name: storageSizeGb
          value: integer
        - name: dataStorageSizeTb
          value: number
        - name: diskRedundancy
          value: string
        - name: sparseDiskgroupEnabled
          value: boolean
        - name: localBackupEnabled
          value: boolean
        - name: hostnamePrefix
          value: string
        - name: diagnosticsDataCollectionOptions
          value:
            - name: diagnosticsEventsEnabled
              value: boolean
            - name: healthMonitoringEnabled
              value: boolean
            - name: incidentLogsEnabled
              value: boolean
        - name: state
          value: string
        - name: scanListenerPortTcp
          value: integer
        - name: scanListenerPortTcpSsl
          value: integer
        - name: domain
          value: string
        - name: scanDns
          value: string
        - name: hostname
          value: string
        - name: cpuCoreCount
          value: integer
        - name: systemVersion
          value: string
        - name: scanIpIds
          value:
            - string
        - name: scanDnsRecordId
          value: string
        - name: ociUrl
          value: string
        - name: dbServerOcids
          value:
            - string
        - name: compartmentId
          value: string
        - name: dnsListenerIp
          value: string
        - name: clusterName
          value: string
    - name: labels
      value: object
    - name: createTime
      value: string
    - name: cidr
      value: string
    - name: backupSubnetCidr
      value: string
    - name: network
      value: string

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
