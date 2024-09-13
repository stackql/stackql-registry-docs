---
title: bare_metal_admin_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - bare_metal_admin_clusters
  - gkeonprem
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

Creates, updates, deletes or gets an <code>bare_metal_admin_cluster</code> resource or lists <code>bare_metal_admin_clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bare_metal_admin_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkeonprem.bare_metal_admin_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The bare metal admin cluster resource name. |
| <CopyableCode code="description" /> | `string` | A human readable description of this bare metal admin cluster. |
| <CopyableCode code="annotations" /> | `object` | Annotations on the bare metal admin cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| <CopyableCode code="bareMetalVersion" /> | `string` | The Anthos clusters on bare metal version for the bare metal admin cluster. |
| <CopyableCode code="binaryAuthorization" /> | `object` | Configuration for Binary Authorization. |
| <CopyableCode code="clusterOperations" /> | `object` | BareMetalAdminClusterOperationsConfig specifies the admin cluster's observability infrastructure. |
| <CopyableCode code="controlPlane" /> | `object` | BareMetalAdminControlPlaneConfig specifies the control plane configuration. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this bare metal admin cluster was created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The time at which this bare metal admin cluster was deleted. If the resource is not deleted, this must be empty |
| <CopyableCode code="endpoint" /> | `string` | Output only. The IP address name of bare metal admin cluster's API server. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |
| <CopyableCode code="fleet" /> | `object` | Fleet related configuration. Fleets are a Google Cloud concept for logically organizing clusters, letting you use and manage multi-cluster capabilities and apply consistent policies across your systems. See [Anthos Fleets](`https://cloud.google.com/anthos/multicluster-management/fleets`) for more details on Anthos multi-cluster capabilities using Fleets. ## |
| <CopyableCode code="loadBalancer" /> | `object` | BareMetalAdminLoadBalancerConfig specifies the load balancer configuration. |
| <CopyableCode code="localName" /> | `string` | Output only. The object name of the bare metal cluster custom resource. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the ID in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable. All users should use this name to access their cluster using gkectl or kubectl and should expect to see the local name when viewing admin cluster controller logs. |
| <CopyableCode code="maintenanceConfig" /> | `object` | BareMetalAdminMaintenanceConfig specifies configurations to put bare metal Admin cluster CRs nodes in and out of maintenance. |
| <CopyableCode code="maintenanceStatus" /> | `object` | BareMetalAdminMaintenanceStatus represents the maintenance status for bare metal Admin cluster CR's nodes. |
| <CopyableCode code="networkConfig" /> | `object` | BareMetalAdminNetworkConfig specifies the cluster network configuration. |
| <CopyableCode code="nodeAccessConfig" /> | `object` | Specifies the node access related settings for the bare metal admin cluster. |
| <CopyableCode code="nodeConfig" /> | `object` | BareMetalAdminWorkloadNodeConfig specifies the workload node configurations. |
| <CopyableCode code="osEnvironmentConfig" /> | `object` | Specifies operating system operation settings for cluster provisioning. |
| <CopyableCode code="proxy" /> | `object` | BareMetalAdminProxyConfig specifies the cluster proxy configuration. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. If set, there are currently changes in flight to the bare metal Admin Cluster. |
| <CopyableCode code="securityConfig" /> | `object` | Specifies the security related settings for the bare metal admin cluster. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the bare metal admin cluster. |
| <CopyableCode code="status" /> | `object` | ResourceStatus describes why a cluster or node pool has a certain status. (e.g., ERROR or DEGRADED). |
| <CopyableCode code="storage" /> | `object` | BareMetalAdminStorageConfig specifies the cluster storage configuration. |
| <CopyableCode code="uid" /> | `string` | Output only. The unique identifier of the bare metal admin cluster. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which this bare metal admin cluster was last updated. |
| <CopyableCode code="validationCheck" /> | `object` | ValidationCheck represents the result of preflight check. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_bare_metal_admin_clusters_get" /> | `SELECT` | <CopyableCode code="bareMetalAdminClustersId, locationsId, projectsId" /> | Gets details of a single bare metal admin cluster. |
| <CopyableCode code="projects_locations_bare_metal_admin_clusters_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists bare metal admin clusters in a given project and location. |
| <CopyableCode code="projects_locations_bare_metal_admin_clusters_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new bare metal admin cluster in a given project and location. The API needs to be combined with creating a bootstrap cluster to work. See: https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/creating-clusters/create-admin-cluster-api#prepare_bootstrap_environment |
| <CopyableCode code="projects_locations_bare_metal_admin_clusters_patch" /> | `UPDATE` | <CopyableCode code="bareMetalAdminClustersId, locationsId, projectsId" /> | Updates the parameters of a single bare metal admin cluster. |
| <CopyableCode code="projects_locations_bare_metal_admin_clusters_enroll" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Enrolls an existing bare metal admin cluster to the Anthos On-Prem API within a given project and location. Through enrollment, an existing admin cluster will become Anthos On-Prem API managed. The corresponding GCP resources will be created and all future modifications to the cluster will be expected to be performed through the API. |
| <CopyableCode code="projects_locations_bare_metal_admin_clusters_query_version_config" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Queries the bare metal admin cluster version config. |
| <CopyableCode code="projects_locations_bare_metal_admin_clusters_unenroll" /> | `EXEC` | <CopyableCode code="bareMetalAdminClustersId, locationsId, projectsId" /> | Unenrolls an existing bare metal admin cluster from the Anthos On-Prem API within a given project and location. Unenrollment removes the Cloud reference to the cluster without modifying the underlying OnPrem Resources. Clusters will continue to run; however, they will no longer be accessible through the Anthos On-Prem API or its clients. |

## `SELECT` examples

Lists bare metal admin clusters in a given project and location.

```sql
SELECT
name,
description,
annotations,
bareMetalVersion,
binaryAuthorization,
clusterOperations,
controlPlane,
createTime,
deleteTime,
endpoint,
etag,
fleet,
loadBalancer,
localName,
maintenanceConfig,
maintenanceStatus,
networkConfig,
nodeAccessConfig,
nodeConfig,
osEnvironmentConfig,
proxy,
reconciling,
securityConfig,
state,
status,
storage,
uid,
updateTime,
validationCheck
FROM google.gkeonprem.bare_metal_admin_clusters
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bare_metal_admin_clusters</code> resource.

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
INSERT INTO google.gkeonprem.bare_metal_admin_clusters (
locationsId,
projectsId,
name,
description,
uid,
bareMetalVersion,
state,
endpoint,
reconciling,
createTime,
updateTime,
deleteTime,
localName,
etag,
annotations,
networkConfig,
controlPlane,
loadBalancer,
storage,
fleet,
clusterOperations,
status,
maintenanceConfig,
maintenanceStatus,
validationCheck,
nodeConfig,
proxy,
securityConfig,
nodeAccessConfig,
osEnvironmentConfig,
binaryAuthorization
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ uid }}',
'{{ bareMetalVersion }}',
'{{ state }}',
'{{ endpoint }}',
true|false,
'{{ createTime }}',
'{{ updateTime }}',
'{{ deleteTime }}',
'{{ localName }}',
'{{ etag }}',
'{{ annotations }}',
'{{ networkConfig }}',
'{{ controlPlane }}',
'{{ loadBalancer }}',
'{{ storage }}',
'{{ fleet }}',
'{{ clusterOperations }}',
'{{ status }}',
'{{ maintenanceConfig }}',
'{{ maintenanceStatus }}',
'{{ validationCheck }}',
'{{ nodeConfig }}',
'{{ proxy }}',
'{{ securityConfig }}',
'{{ nodeAccessConfig }}',
'{{ osEnvironmentConfig }}',
'{{ binaryAuthorization }}'
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
      - name: description
        value: '{{ description }}'
      - name: uid
        value: '{{ uid }}'
      - name: bareMetalVersion
        value: '{{ bareMetalVersion }}'
      - name: state
        value: '{{ state }}'
      - name: endpoint
        value: '{{ endpoint }}'
      - name: reconciling
        value: '{{ reconciling }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: deleteTime
        value: '{{ deleteTime }}'
      - name: localName
        value: '{{ localName }}'
      - name: etag
        value: '{{ etag }}'
      - name: annotations
        value: '{{ annotations }}'
      - name: networkConfig
        value: '{{ networkConfig }}'
      - name: controlPlane
        value: '{{ controlPlane }}'
      - name: loadBalancer
        value: '{{ loadBalancer }}'
      - name: storage
        value: '{{ storage }}'
      - name: fleet
        value: '{{ fleet }}'
      - name: clusterOperations
        value: '{{ clusterOperations }}'
      - name: status
        value: '{{ status }}'
      - name: maintenanceConfig
        value: '{{ maintenanceConfig }}'
      - name: maintenanceStatus
        value: '{{ maintenanceStatus }}'
      - name: validationCheck
        value: '{{ validationCheck }}'
      - name: nodeConfig
        value: '{{ nodeConfig }}'
      - name: proxy
        value: '{{ proxy }}'
      - name: securityConfig
        value: '{{ securityConfig }}'
      - name: nodeAccessConfig
        value: '{{ nodeAccessConfig }}'
      - name: osEnvironmentConfig
        value: '{{ osEnvironmentConfig }}'
      - name: binaryAuthorization
        value: '{{ binaryAuthorization }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a bare_metal_admin_cluster only if the necessary resources are available.

```sql
UPDATE google.gkeonprem.bare_metal_admin_clusters
SET 
name = '{{ name }}',
description = '{{ description }}',
uid = '{{ uid }}',
bareMetalVersion = '{{ bareMetalVersion }}',
state = '{{ state }}',
endpoint = '{{ endpoint }}',
reconciling = true|false,
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
deleteTime = '{{ deleteTime }}',
localName = '{{ localName }}',
etag = '{{ etag }}',
annotations = '{{ annotations }}',
networkConfig = '{{ networkConfig }}',
controlPlane = '{{ controlPlane }}',
loadBalancer = '{{ loadBalancer }}',
storage = '{{ storage }}',
fleet = '{{ fleet }}',
clusterOperations = '{{ clusterOperations }}',
status = '{{ status }}',
maintenanceConfig = '{{ maintenanceConfig }}',
maintenanceStatus = '{{ maintenanceStatus }}',
validationCheck = '{{ validationCheck }}',
nodeConfig = '{{ nodeConfig }}',
proxy = '{{ proxy }}',
securityConfig = '{{ securityConfig }}',
nodeAccessConfig = '{{ nodeAccessConfig }}',
osEnvironmentConfig = '{{ osEnvironmentConfig }}',
binaryAuthorization = '{{ binaryAuthorization }}'
WHERE 
bareMetalAdminClustersId = '{{ bareMetalAdminClustersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
