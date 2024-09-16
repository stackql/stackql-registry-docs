---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - dataproc
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataproc.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterName" /> | `string` | Required. The cluster name, which must be unique within a project. The name must start with a lowercase letter, and can contain up to 51 lowercase letters, numbers, and hyphens. It cannot end with a hyphen. The name of a deleted cluster can be reused. |
| <CopyableCode code="clusterUuid" /> | `string` | Output only. A cluster UUID (Unique Universal Identifier). Dataproc generates this value when it creates the cluster. |
| <CopyableCode code="config" /> | `object` | The cluster config. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels to associate with this cluster. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a cluster. |
| <CopyableCode code="metrics" /> | `object` | Contains cluster daemon metrics, such as HDFS and YARN stats.Beta Feature: This report is available for testing purposes only. It may be changed before final release. |
| <CopyableCode code="projectId" /> | `string` | Required. The Google Cloud Platform project ID that the cluster belongs to. |
| <CopyableCode code="status" /> | `object` | The status of a cluster and its instances. |
| <CopyableCode code="statusHistory" /> | `array` | Output only. The previous cluster status. |
| <CopyableCode code="virtualClusterConfig" /> | `object` | The Dataproc cluster config for a cluster that does not directly control the underlying compute resources, such as a Dataproc-on-GKE cluster (https://cloud.google.com/dataproc/docs/guides/dpgke/dataproc-gke-overview). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_regions_clusters_get" /> | `SELECT` | <CopyableCode code="clusterName, projectId, region" /> | Gets the resource representation for a cluster in a project. |
| <CopyableCode code="projects_regions_clusters_list" /> | `SELECT` | <CopyableCode code="projectId, region" /> | Lists all regions/{region}/clusters in a project alphabetically. |
| <CopyableCode code="projects_regions_clusters_create" /> | `INSERT` | <CopyableCode code="projectId, region" /> | Creates a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). |
| <CopyableCode code="projects_regions_clusters_delete" /> | `DELETE` | <CopyableCode code="clusterName, projectId, region" /> | Deletes a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). |
| <CopyableCode code="projects_regions_clusters_patch" /> | `UPDATE` | <CopyableCode code="clusterName, projectId, region" /> | Updates a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). The cluster must be in a RUNNING state or an error is returned. |
| <CopyableCode code="projects_regions_clusters_diagnose" /> | `EXEC` | <CopyableCode code="clusterName, projectId, region" /> | Gets cluster diagnostic information. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). After the operation completes, Operation.response contains DiagnoseClusterResults (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#diagnoseclusterresults). |
| <CopyableCode code="projects_regions_clusters_inject_credentials" /> | `EXEC` | <CopyableCode code="clustersId, projectsId, regionsId" /> | Inject encrypted credentials into all of the VMs in a cluster.The target cluster must be a personal auth cluster assigned to the user who is issuing the RPC. |
| <CopyableCode code="projects_regions_clusters_repair" /> | `EXEC` | <CopyableCode code="clusterName, projectId, region" /> | Repairs a cluster. |
| <CopyableCode code="projects_regions_clusters_start" /> | `EXEC` | <CopyableCode code="clusterName, projectId, region" /> | Starts a cluster in a project. |
| <CopyableCode code="projects_regions_clusters_stop" /> | `EXEC` | <CopyableCode code="clusterName, projectId, region" /> | Stops a cluster in a project. |

## `SELECT` examples

Lists all regions/{region}/clusters in a project alphabetically.

```sql
SELECT
clusterName,
clusterUuid,
config,
labels,
metrics,
projectId,
status,
statusHistory,
virtualClusterConfig
FROM google.dataproc.clusters
WHERE projectId = '{{ projectId }}'
AND region = '{{ region }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters</code> resource.

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
INSERT INTO google.dataproc.clusters (
projectId,
region,
projectId,
clusterName,
config,
virtualClusterConfig,
labels
)
SELECT 
'{{ projectId }}',
'{{ region }}',
'{{ projectId }}',
'{{ clusterName }}',
'{{ config }}',
'{{ virtualClusterConfig }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: projectId
      value: '{{ projectId }}'
    - name: clusterName
      value: '{{ clusterName }}'
    - name: config
      value:
        - name: configBucket
          value: '{{ configBucket }}'
        - name: tempBucket
          value: '{{ tempBucket }}'
        - name: gceClusterConfig
          value:
            - name: zoneUri
              value: '{{ zoneUri }}'
            - name: networkUri
              value: '{{ networkUri }}'
            - name: subnetworkUri
              value: '{{ subnetworkUri }}'
            - name: internalIpOnly
              value: '{{ internalIpOnly }}'
            - name: privateIpv6GoogleAccess
              value: '{{ privateIpv6GoogleAccess }}'
            - name: serviceAccount
              value: '{{ serviceAccount }}'
            - name: serviceAccountScopes
              value:
                - name: type
                  value: '{{ type }}'
            - name: tags
              value:
                - name: type
                  value: '{{ type }}'
            - name: metadata
              value: '{{ metadata }}'
            - name: reservationAffinity
              value:
                - name: consumeReservationType
                  value: '{{ consumeReservationType }}'
                - name: key
                  value: '{{ key }}'
                - name: values
                  value:
                    - name: type
                      value: '{{ type }}'
            - name: nodeGroupAffinity
              value:
                - name: nodeGroupUri
                  value: '{{ nodeGroupUri }}'
            - name: shieldedInstanceConfig
              value:
                - name: enableSecureBoot
                  value: '{{ enableSecureBoot }}'
                - name: enableVtpm
                  value: '{{ enableVtpm }}'
                - name: enableIntegrityMonitoring
                  value: '{{ enableIntegrityMonitoring }}'
            - name: confidentialInstanceConfig
              value:
                - name: enableConfidentialCompute
                  value: '{{ enableConfidentialCompute }}'
        - name: masterConfig
          value:
            - name: numInstances
              value: '{{ numInstances }}'
            - name: imageUri
              value: '{{ imageUri }}'
            - name: machineTypeUri
              value: '{{ machineTypeUri }}'
            - name: diskConfig
              value:
                - name: bootDiskType
                  value: '{{ bootDiskType }}'
                - name: bootDiskSizeGb
                  value: '{{ bootDiskSizeGb }}'
                - name: numLocalSsds
                  value: '{{ numLocalSsds }}'
                - name: localSsdInterface
                  value: '{{ localSsdInterface }}'
                - name: bootDiskProvisionedIops
                  value: '{{ bootDiskProvisionedIops }}'
                - name: bootDiskProvisionedThroughput
                  value: '{{ bootDiskProvisionedThroughput }}'
            - name: preemptibility
              value: '{{ preemptibility }}'
            - name: accelerators
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: minCpuPlatform
              value: '{{ minCpuPlatform }}'
            - name: minNumInstances
              value: '{{ minNumInstances }}'
            - name: instanceFlexibilityPolicy
              value:
                - name: instanceSelectionList
                  value:
                    - name: $ref
                      value: '{{ $ref }}'
            - name: startupConfig
              value:
                - name: requiredRegistrationFraction
                  value: '{{ requiredRegistrationFraction }}'
        - name: softwareConfig
          value:
            - name: imageVersion
              value: '{{ imageVersion }}'
            - name: properties
              value: '{{ properties }}'
            - name: optionalComponents
              value:
                - name: type
                  value: '{{ type }}'
                - name: enumDescriptions
                  value: '{{ enumDescriptions }}'
                - name: enum
                  value: '{{ enum }}'
        - name: initializationActions
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: encryptionConfig
          value:
            - name: gcePdKmsKeyName
              value: '{{ gcePdKmsKeyName }}'
            - name: kmsKey
              value: '{{ kmsKey }}'
        - name: autoscalingConfig
          value:
            - name: policyUri
              value: '{{ policyUri }}'
        - name: securityConfig
          value:
            - name: kerberosConfig
              value:
                - name: enableKerberos
                  value: '{{ enableKerberos }}'
                - name: rootPrincipalPasswordUri
                  value: '{{ rootPrincipalPasswordUri }}'
                - name: kmsKeyUri
                  value: '{{ kmsKeyUri }}'
                - name: keystoreUri
                  value: '{{ keystoreUri }}'
                - name: truststoreUri
                  value: '{{ truststoreUri }}'
                - name: keystorePasswordUri
                  value: '{{ keystorePasswordUri }}'
                - name: keyPasswordUri
                  value: '{{ keyPasswordUri }}'
                - name: truststorePasswordUri
                  value: '{{ truststorePasswordUri }}'
                - name: crossRealmTrustRealm
                  value: '{{ crossRealmTrustRealm }}'
                - name: crossRealmTrustKdc
                  value: '{{ crossRealmTrustKdc }}'
                - name: crossRealmTrustAdminServer
                  value: '{{ crossRealmTrustAdminServer }}'
                - name: crossRealmTrustSharedPasswordUri
                  value: '{{ crossRealmTrustSharedPasswordUri }}'
                - name: kdcDbKeyUri
                  value: '{{ kdcDbKeyUri }}'
                - name: tgtLifetimeHours
                  value: '{{ tgtLifetimeHours }}'
                - name: realm
                  value: '{{ realm }}'
            - name: identityConfig
              value:
                - name: userServiceAccountMapping
                  value: '{{ userServiceAccountMapping }}'
        - name: lifecycleConfig
          value:
            - name: idleDeleteTtl
              value: '{{ idleDeleteTtl }}'
            - name: autoDeleteTime
              value: '{{ autoDeleteTime }}'
            - name: autoDeleteTtl
              value: '{{ autoDeleteTtl }}'
        - name: endpointConfig
          value:
            - name: enableHttpPortAccess
              value: '{{ enableHttpPortAccess }}'
        - name: metastoreConfig
          value:
            - name: dataprocMetastoreService
              value: '{{ dataprocMetastoreService }}'
        - name: gkeClusterConfig
          value:
            - name: namespacedGkeDeploymentTarget
              value:
                - name: targetGkeCluster
                  value: '{{ targetGkeCluster }}'
                - name: clusterNamespace
                  value: '{{ clusterNamespace }}'
            - name: gkeClusterTarget
              value: '{{ gkeClusterTarget }}'
            - name: nodePoolTarget
              value:
                - name: $ref
                  value: '{{ $ref }}'
        - name: dataprocMetricConfig
          value:
            - name: metrics
              value:
                - name: $ref
                  value: '{{ $ref }}'
        - name: auxiliaryNodeGroups
          value:
            - name: $ref
              value: '{{ $ref }}'
    - name: virtualClusterConfig
      value:
        - name: stagingBucket
          value: '{{ stagingBucket }}'
        - name: kubernetesClusterConfig
          value:
            - name: kubernetesNamespace
              value: '{{ kubernetesNamespace }}'
            - name: kubernetesSoftwareConfig
              value:
                - name: componentVersion
                  value: '{{ componentVersion }}'
                - name: properties
                  value: '{{ properties }}'
        - name: auxiliaryServicesConfig
          value:
            - name: sparkHistoryServerConfig
              value:
                - name: dataprocCluster
                  value: '{{ dataprocCluster }}'
    - name: labels
      value: '{{ labels }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clusters</code> resource.

```sql
/*+ update */
UPDATE google.dataproc.clusters
SET 
projectId = '{{ projectId }}',
clusterName = '{{ clusterName }}',
config = '{{ config }}',
virtualClusterConfig = '{{ virtualClusterConfig }}',
labels = '{{ labels }}'
WHERE 
clusterName = '{{ clusterName }}'
AND projectId = '{{ projectId }}'
AND region = '{{ region }}';
```

## `DELETE` example

Deletes the specified <code>clusters</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataproc.clusters
WHERE clusterName = '{{ clusterName }}'
AND projectId = '{{ projectId }}'
AND region = '{{ region }}';
```
