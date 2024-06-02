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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workstation_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="workstations.workstation_clusters" /></td></tr>
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
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Returns all workstation clusters in the specified location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, workstationClustersId" /> | Updates an existing workstation cluster. |
