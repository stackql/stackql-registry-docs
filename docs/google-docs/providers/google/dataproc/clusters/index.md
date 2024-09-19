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
      value: string
    - name: clusterName
      value: string
    - name: config
      value:
        - name: configBucket
          value: string
        - name: tempBucket
          value: string
        - name: gceClusterConfig
          value:
            - name: zoneUri
              value: string
            - name: networkUri
              value: string
            - name: subnetworkUri
              value: string
            - name: internalIpOnly
              value: boolean
            - name: privateIpv6GoogleAccess
              value: string
            - name: serviceAccount
              value: string
            - name: serviceAccountScopes
              value:
                - string
            - name: tags
              value:
                - string
            - name: metadata
              value: object
            - name: reservationAffinity
              value:
                - name: consumeReservationType
                  value: string
                - name: key
                  value: string
                - name: values
                  value:
                    - string
            - name: nodeGroupAffinity
              value:
                - name: nodeGroupUri
                  value: string
            - name: shieldedInstanceConfig
              value:
                - name: enableSecureBoot
                  value: boolean
                - name: enableVtpm
                  value: boolean
                - name: enableIntegrityMonitoring
                  value: boolean
            - name: confidentialInstanceConfig
              value:
                - name: enableConfidentialCompute
                  value: boolean
        - name: masterConfig
          value:
            - name: numInstances
              value: integer
            - name: instanceNames
              value:
                - string
            - name: instanceReferences
              value:
                - - name: instanceName
                    value: string
                  - name: instanceId
                    value: string
                  - name: publicKey
                    value: string
                  - name: publicEciesKey
                    value: string
            - name: imageUri
              value: string
            - name: machineTypeUri
              value: string
            - name: diskConfig
              value:
                - name: bootDiskType
                  value: string
                - name: bootDiskSizeGb
                  value: integer
                - name: numLocalSsds
                  value: integer
                - name: localSsdInterface
                  value: string
                - name: bootDiskProvisionedIops
                  value: string
                - name: bootDiskProvisionedThroughput
                  value: string
            - name: isPreemptible
              value: boolean
            - name: preemptibility
              value: string
            - name: managedGroupConfig
              value:
                - name: instanceTemplateName
                  value: string
                - name: instanceGroupManagerName
                  value: string
                - name: instanceGroupManagerUri
                  value: string
            - name: accelerators
              value:
                - - name: acceleratorTypeUri
                    value: string
                  - name: acceleratorCount
                    value: integer
            - name: minCpuPlatform
              value: string
            - name: minNumInstances
              value: integer
            - name: instanceFlexibilityPolicy
              value:
                - name: instanceSelectionList
                  value:
                    - - name: machineTypes
                        value:
                          - string
                      - name: rank
                        value: integer
                - name: instanceSelectionResults
                  value:
                    - - name: machineType
                        value: string
                      - name: vmCount
                        value: integer
            - name: startupConfig
              value:
                - name: requiredRegistrationFraction
                  value: number
        - name: softwareConfig
          value:
            - name: imageVersion
              value: string
            - name: properties
              value: object
            - name: optionalComponents
              value:
                - string
        - name: initializationActions
          value:
            - - name: executableFile
                value: string
              - name: executionTimeout
                value: string
        - name: encryptionConfig
          value:
            - name: gcePdKmsKeyName
              value: string
            - name: kmsKey
              value: string
        - name: autoscalingConfig
          value:
            - name: policyUri
              value: string
        - name: securityConfig
          value:
            - name: kerberosConfig
              value:
                - name: enableKerberos
                  value: boolean
                - name: rootPrincipalPasswordUri
                  value: string
                - name: kmsKeyUri
                  value: string
                - name: keystoreUri
                  value: string
                - name: truststoreUri
                  value: string
                - name: keystorePasswordUri
                  value: string
                - name: keyPasswordUri
                  value: string
                - name: truststorePasswordUri
                  value: string
                - name: crossRealmTrustRealm
                  value: string
                - name: crossRealmTrustKdc
                  value: string
                - name: crossRealmTrustAdminServer
                  value: string
                - name: crossRealmTrustSharedPasswordUri
                  value: string
                - name: kdcDbKeyUri
                  value: string
                - name: tgtLifetimeHours
                  value: integer
                - name: realm
                  value: string
            - name: identityConfig
              value:
                - name: userServiceAccountMapping
                  value: object
        - name: lifecycleConfig
          value:
            - name: idleDeleteTtl
              value: string
            - name: autoDeleteTime
              value: string
            - name: autoDeleteTtl
              value: string
            - name: idleStartTime
              value: string
        - name: endpointConfig
          value:
            - name: httpPorts
              value: object
            - name: enableHttpPortAccess
              value: boolean
        - name: metastoreConfig
          value:
            - name: dataprocMetastoreService
              value: string
        - name: gkeClusterConfig
          value:
            - name: namespacedGkeDeploymentTarget
              value:
                - name: targetGkeCluster
                  value: string
                - name: clusterNamespace
                  value: string
            - name: gkeClusterTarget
              value: string
            - name: nodePoolTarget
              value:
                - - name: nodePool
                    value: string
                  - name: roles
                    value:
                      - string
                  - name: nodePoolConfig
                    value:
                      - name: config
                        value:
                          - name: machineType
                            value: string
                          - name: localSsdCount
                            value: integer
                          - name: preemptible
                            value: boolean
                          - name: accelerators
                            value:
                              - - name: acceleratorCount
                                  value: string
                                - name: acceleratorType
                                  value: string
                                - name: gpuPartitionSize
                                  value: string
                          - name: minCpuPlatform
                            value: string
                          - name: bootDiskKmsKey
                            value: string
                          - name: spot
                            value: boolean
                      - name: locations
                        value:
                          - string
                      - name: autoscaling
                        value:
                          - name: minNodeCount
                            value: integer
                          - name: maxNodeCount
                            value: integer
        - name: dataprocMetricConfig
          value:
            - name: metrics
              value:
                - - name: metricSource
                    value: string
                  - name: metricOverrides
                    value:
                      - string
        - name: auxiliaryNodeGroups
          value:
            - - name: nodeGroup
                value:
                  - name: name
                    value: string
                  - name: roles
                    value:
                      - string
                  - name: labels
                    value: object
              - name: nodeGroupId
                value: string
    - name: virtualClusterConfig
      value:
        - name: stagingBucket
          value: string
        - name: kubernetesClusterConfig
          value:
            - name: kubernetesNamespace
              value: string
            - name: kubernetesSoftwareConfig
              value:
                - name: componentVersion
                  value: object
                - name: properties
                  value: object
        - name: auxiliaryServicesConfig
          value:
            - name: sparkHistoryServerConfig
              value:
                - name: dataprocCluster
                  value: string
    - name: labels
      value: object
    - name: status
      value:
        - name: state
          value: string
        - name: detail
          value: string
        - name: stateStartTime
          value: string
        - name: substate
          value: string
    - name: statusHistory
      value:
        - - name: state
            value: string
          - name: detail
            value: string
          - name: stateStartTime
            value: string
          - name: substate
            value: string
    - name: clusterUuid
      value: string
    - name: metrics
      value:
        - name: hdfsMetrics
          value: object
        - name: yarnMetrics
          value: object

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
