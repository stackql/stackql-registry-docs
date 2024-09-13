
---
title: workstation_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - workstation_clusters
  - workstations
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

Creates, updates, deletes or gets an <code>workstation_cluster</code> resource or lists <code>workstation_clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workstation_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workstations.workstation_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Full name of this workstation cluster. |
| <CopyableCode code="annotations" /> | `object` | Optional. Client-specified annotations. |
| <CopyableCode code="conditions" /> | `array` | Output only. Status conditions describing the workstation cluster's current state. |
| <CopyableCode code="controlPlaneIp" /> | `string` | Output only. The private IP address of the control plane for this workstation cluster. Workstation VMs need access to this IP address to work with the service, so make sure that your firewall rules allow egress from the workstation VMs to this address. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when this workstation cluster was created. |
| <CopyableCode code="degraded" /> | `boolean` | Output only. Whether this workstation cluster is in degraded mode, in which case it may require user action to restore full functionality. Details can be found in conditions. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. Time when this workstation cluster was soft-deleted. |
| <CopyableCode code="displayName" /> | `string` | Optional. Human-readable name for this workstation cluster. |
| <CopyableCode code="domainConfig" /> | `object` | Configuration options for a custom domain. |
| <CopyableCode code="etag" /> | `string` | Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation cluster and that are also propagated to the underlying Compute Engine resources. |
| <CopyableCode code="network" /> | `string` | Immutable. Name of the Compute Engine network in which instances associated with this workstation cluster will be created. |
| <CopyableCode code="privateClusterConfig" /> | `object` | Configuration options for private workstation clusters. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Indicates whether this workstation cluster is currently being updated to match its intended state. |
| <CopyableCode code="subnetwork" /> | `string` | Immutable. Name of the Compute Engine subnetwork in which instances associated with this workstation cluster will be created. Must be part of the subnetwork specified for this workstation cluster. |
| <CopyableCode code="uid" /> | `string` | Output only. A system-assigned unique identifier for this workstation cluster. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when this workstation cluster was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, workstationClustersId" /> | Returns the requested workstation cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns all workstation clusters in the specified location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new workstation cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, workstationClustersId" /> | Deletes the specified workstation cluster. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, workstationClustersId" /> | Updates an existing workstation cluster. |

## `SELECT` examples

Returns all workstation clusters in the specified location.

```sql
SELECT
name,
annotations,
conditions,
controlPlaneIp,
createTime,
degraded,
deleteTime,
displayName,
domainConfig,
etag,
labels,
network,
privateClusterConfig,
reconciling,
subnetwork,
uid,
updateTime
FROM google.workstations.workstation_clusters
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workstation_clusters</code> resource.

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
INSERT INTO google.workstations.workstation_clusters (
locationsId,
projectsId,
name,
displayName,
uid,
reconciling,
annotations,
labels,
createTime,
updateTime,
deleteTime,
etag,
network,
subnetwork,
controlPlaneIp,
privateClusterConfig,
domainConfig,
degraded,
conditions
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ uid }}',
true|false,
'{{ annotations }}',
'{{ labels }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ deleteTime }}',
'{{ etag }}',
'{{ network }}',
'{{ subnetwork }}',
'{{ controlPlaneIp }}',
'{{ privateClusterConfig }}',
'{{ domainConfig }}',
true|false,
'{{ conditions }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: uid
        value: '{{ uid }}'
      - name: reconciling
        value: '{{ reconciling }}'
      - name: annotations
        value: '{{ annotations }}'
      - name: labels
        value: '{{ labels }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: deleteTime
        value: '{{ deleteTime }}'
      - name: etag
        value: '{{ etag }}'
      - name: network
        value: '{{ network }}'
      - name: subnetwork
        value: '{{ subnetwork }}'
      - name: controlPlaneIp
        value: '{{ controlPlaneIp }}'
      - name: privateClusterConfig
        value: '{{ privateClusterConfig }}'
      - name: domainConfig
        value: '{{ domainConfig }}'
      - name: degraded
        value: '{{ degraded }}'
      - name: conditions
        value: '{{ conditions }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a workstation_cluster only if the necessary resources are available.

```sql
UPDATE google.workstations.workstation_clusters
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
uid = '{{ uid }}',
reconciling = true|false,
annotations = '{{ annotations }}',
labels = '{{ labels }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
deleteTime = '{{ deleteTime }}',
etag = '{{ etag }}',
network = '{{ network }}',
subnetwork = '{{ subnetwork }}',
controlPlaneIp = '{{ controlPlaneIp }}',
privateClusterConfig = '{{ privateClusterConfig }}',
domainConfig = '{{ domainConfig }}',
degraded = true|false,
conditions = '{{ conditions }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workstationClustersId = '{{ workstationClustersId }}';
```

## `DELETE` example

Deletes the specified workstation_cluster resource.

```sql
DELETE FROM google.workstations.workstation_clusters
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workstationClustersId = '{{ workstationClustersId }}';
```
