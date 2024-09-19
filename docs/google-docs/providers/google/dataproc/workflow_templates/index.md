---
title: workflow_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_templates
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

Creates, updates, deletes, gets or lists a <code>workflow_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataproc.workflow_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the workflow template, as described in https://cloud.google.com/apis/design/resource_names. For projects.regions.workflowTemplates, the resource name of the template has the following format: projects/{project_id}/regions/{region}/workflowTemplates/{template_id} For projects.locations.workflowTemplates, the resource name of the template has the following format: projects/{project_id}/locations/{location}/workflowTemplates/{template_id} |
| <CopyableCode code="createTime" /> | `string` | Output only. The time template was created. |
| <CopyableCode code="dagTimeout" /> | `string` | Optional. Timeout duration for the DAG of jobs, expressed in seconds (see JSON representation of duration (https://developers.google.com/protocol-buffers/docs/proto3#json)). The timeout duration must be from 10 minutes ("600s") to 24 hours ("86400s"). The timer begins when the first job is submitted. If the workflow is running at the end of the timeout period, any remaining jobs are cancelled, the workflow is ended, and if the workflow was running on a managed cluster, the cluster is deleted. |
| <CopyableCode code="encryptionConfig" /> | `object` | Encryption settings for encrypting workflow template job arguments. |
| <CopyableCode code="jobs" /> | `array` | Required. The Directed Acyclic Graph of Jobs to submit. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels to associate with this template. These labels will be propagated to all jobs and clusters created by the workflow instance.Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt).Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt).No more than 32 labels can be associated with a template. |
| <CopyableCode code="parameters" /> | `array` | Optional. Template parameters whose values are substituted into the template. Values for parameters must be provided when the template is instantiated. |
| <CopyableCode code="placement" /> | `object` | Specifies workflow execution target.Either managed_cluster or cluster_selector is required. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time template was last updated. |
| <CopyableCode code="version" /> | `integer` | Optional. Used to perform a consistent read-modify-write.This field should be left blank for a CreateWorkflowTemplate request. It is required for an UpdateWorkflowTemplate request, and must match the current server version. A typical update template flow would fetch the current template with a GetWorkflowTemplate request, which will return the current template with the version field filled in with the current server version. The user updates other fields in the template, then returns it as part of the UpdateWorkflowTemplate request. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_workflow_templates_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, workflowTemplatesId" /> | Retrieves the latest workflow template.Can retrieve previously instantiated template by specifying optional version parameter. |
| <CopyableCode code="projects_locations_workflow_templates_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists workflows that match the specified filter in the request. |
| <CopyableCode code="projects_regions_workflow_templates_get" /> | `SELECT` | <CopyableCode code="projectsId, regionsId, workflowTemplatesId" /> | Retrieves the latest workflow template.Can retrieve previously instantiated template by specifying optional version parameter. |
| <CopyableCode code="projects_regions_workflow_templates_list" /> | `SELECT` | <CopyableCode code="projectsId, regionsId" /> | Lists workflows that match the specified filter in the request. |
| <CopyableCode code="projects_locations_workflow_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates new workflow template. |
| <CopyableCode code="projects_regions_workflow_templates_create" /> | `INSERT` | <CopyableCode code="projectsId, regionsId" /> | Creates new workflow template. |
| <CopyableCode code="projects_locations_workflow_templates_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, workflowTemplatesId" /> | Deletes a workflow template. It does not cancel in-progress workflows. |
| <CopyableCode code="projects_regions_workflow_templates_delete" /> | `DELETE` | <CopyableCode code="projectsId, regionsId, workflowTemplatesId" /> | Deletes a workflow template. It does not cancel in-progress workflows. |
| <CopyableCode code="projects_locations_workflow_templates_update" /> | `REPLACE` | <CopyableCode code="locationsId, projectsId, workflowTemplatesId" /> | Updates (replaces) workflow template. The updated template must contain version that matches the current server version. |
| <CopyableCode code="projects_regions_workflow_templates_update" /> | `REPLACE` | <CopyableCode code="projectsId, regionsId, workflowTemplatesId" /> | Updates (replaces) workflow template. The updated template must contain version that matches the current server version. |
| <CopyableCode code="projects_locations_workflow_templates_instantiate" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, workflowTemplatesId" /> | Instantiates a template and begins execution.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| <CopyableCode code="projects_locations_workflow_templates_instantiate_inline" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Instantiates a template and begins execution.This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| <CopyableCode code="projects_regions_workflow_templates_instantiate" /> | `EXEC` | <CopyableCode code="projectsId, regionsId, workflowTemplatesId" /> | Instantiates a template and begins execution.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| <CopyableCode code="projects_regions_workflow_templates_instantiate_inline" /> | `EXEC` | <CopyableCode code="projectsId, regionsId" /> | Instantiates a template and begins execution.This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |

## `SELECT` examples

Lists workflows that match the specified filter in the request.

```sql
SELECT
id,
name,
createTime,
dagTimeout,
encryptionConfig,
jobs,
labels,
parameters,
placement,
updateTime,
version
FROM google.dataproc.workflow_templates
WHERE projectsId = '{{ projectsId }}'
AND regionsId = '{{ regionsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workflow_templates</code> resource.

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
INSERT INTO google.dataproc.workflow_templates (
projectsId,
regionsId,
version,
labels,
placement,
jobs,
parameters,
dagTimeout,
encryptionConfig
)
SELECT 
'{{ projectsId }}',
'{{ regionsId }}',
'{{ version }}',
'{{ labels }}',
'{{ placement }}',
'{{ jobs }}',
'{{ parameters }}',
'{{ dagTimeout }}',
'{{ encryptionConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: version
      value: integer
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: placement
      value:
        - name: managedCluster
          value:
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
            - name: labels
              value: object
        - name: clusterSelector
          value:
            - name: zone
              value: string
            - name: clusterLabels
              value: object
    - name: jobs
      value:
        - - name: stepId
            value: string
          - name: hadoopJob
            value:
              - name: mainJarFileUri
                value: string
              - name: mainClass
                value: string
              - name: args
                value:
                  - string
              - name: jarFileUris
                value:
                  - string
              - name: fileUris
                value:
                  - string
              - name: archiveUris
                value:
                  - string
              - name: properties
                value: object
              - name: loggingConfig
                value:
                  - name: driverLogLevels
                    value: object
          - name: sparkJob
            value:
              - name: mainJarFileUri
                value: string
              - name: mainClass
                value: string
              - name: args
                value:
                  - string
              - name: jarFileUris
                value:
                  - string
              - name: fileUris
                value:
                  - string
              - name: archiveUris
                value:
                  - string
              - name: properties
                value: object
          - name: pysparkJob
            value:
              - name: mainPythonFileUri
                value: string
              - name: args
                value:
                  - string
              - name: pythonFileUris
                value:
                  - string
              - name: jarFileUris
                value:
                  - string
              - name: fileUris
                value:
                  - string
              - name: archiveUris
                value:
                  - string
              - name: properties
                value: object
          - name: hiveJob
            value:
              - name: queryFileUri
                value: string
              - name: queryList
                value:
                  - name: queries
                    value:
                      - string
              - name: continueOnFailure
                value: boolean
              - name: scriptVariables
                value: object
              - name: properties
                value: object
              - name: jarFileUris
                value:
                  - string
          - name: pigJob
            value:
              - name: queryFileUri
                value: string
              - name: continueOnFailure
                value: boolean
              - name: scriptVariables
                value: object
              - name: properties
                value: object
              - name: jarFileUris
                value:
                  - string
          - name: sparkRJob
            value:
              - name: mainRFileUri
                value: string
              - name: args
                value:
                  - string
              - name: fileUris
                value:
                  - string
              - name: archiveUris
                value:
                  - string
              - name: properties
                value: object
          - name: sparkSqlJob
            value:
              - name: queryFileUri
                value: string
              - name: scriptVariables
                value: object
              - name: properties
                value: object
              - name: jarFileUris
                value:
                  - string
          - name: prestoJob
            value:
              - name: queryFileUri
                value: string
              - name: continueOnFailure
                value: boolean
              - name: outputFormat
                value: string
              - name: clientTags
                value:
                  - string
              - name: properties
                value: object
          - name: trinoJob
            value:
              - name: queryFileUri
                value: string
              - name: continueOnFailure
                value: boolean
              - name: outputFormat
                value: string
              - name: clientTags
                value:
                  - string
              - name: properties
                value: object
          - name: flinkJob
            value:
              - name: mainJarFileUri
                value: string
              - name: mainClass
                value: string
              - name: args
                value:
                  - string
              - name: jarFileUris
                value:
                  - string
              - name: savepointUri
                value: string
              - name: properties
                value: object
          - name: labels
            value: object
          - name: scheduling
            value:
              - name: maxFailuresPerHour
                value: integer
              - name: maxFailuresTotal
                value: integer
          - name: prerequisiteStepIds
            value:
              - string
    - name: parameters
      value:
        - - name: name
            value: string
          - name: fields
            value:
              - string
          - name: description
            value: string
          - name: validation
            value:
              - name: regex
                value:
                  - name: regexes
                    value:
                      - string
              - name: values
                value:
                  - name: values
                    value:
                      - string
    - name: dagTimeout
      value: string
    - name: encryptionConfig
      value:
        - name: kmsKey
          value: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>workflow_templates</code> resource.

```sql
/*+ update */
REPLACE google.dataproc.workflow_templates
SET 
version = '{{ version }}',
labels = '{{ labels }}',
placement = '{{ placement }}',
jobs = '{{ jobs }}',
parameters = '{{ parameters }}',
dagTimeout = '{{ dagTimeout }}',
encryptionConfig = '{{ encryptionConfig }}'
WHERE 
projectsId = '{{ projectsId }}'
AND regionsId = '{{ regionsId }}'
AND workflowTemplatesId = '{{ workflowTemplatesId }}';
```

## `DELETE` example

Deletes the specified <code>workflow_templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataproc.workflow_templates
WHERE projectsId = '{{ projectsId }}'
AND regionsId = '{{ regionsId }}'
AND workflowTemplatesId = '{{ workflowTemplatesId }}';
```
