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

Creates, updates, deletes or gets an <code>workflow_template</code> resource or lists <code>workflow_templates</code> in a region

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
| <CopyableCode code="projects_locations_workflow_templates_instantiate" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, workflowTemplatesId" /> | Instantiates a template and begins execution.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| <CopyableCode code="projects_locations_workflow_templates_instantiate_inline" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Instantiates a template and begins execution.This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| <CopyableCode code="projects_locations_workflow_templates_update" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, workflowTemplatesId" /> | Updates (replaces) workflow template. The updated template must contain version that matches the current server version. |
| <CopyableCode code="projects_regions_workflow_templates_instantiate" /> | `EXEC` | <CopyableCode code="projectsId, regionsId, workflowTemplatesId" /> | Instantiates a template and begins execution.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| <CopyableCode code="projects_regions_workflow_templates_instantiate_inline" /> | `EXEC` | <CopyableCode code="projectsId, regionsId" /> | Instantiates a template and begins execution.This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| <CopyableCode code="projects_regions_workflow_templates_update" /> | `EXEC` | <CopyableCode code="projectsId, regionsId, workflowTemplatesId" /> | Updates (replaces) workflow template. The updated template must contain version that matches the current server version. |

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
id,
name,
version,
createTime,
updateTime,
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
'{{ id }}',
'{{ name }}',
'{{ version }}',
'{{ createTime }}',
'{{ updateTime }}',
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
resources:
  - name: instance
    props:
      - name: id
        value: '{{ id }}'
      - name: name
        value: '{{ name }}'
      - name: version
        value: '{{ version }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: placement
        value: '{{ placement }}'
      - name: jobs
        value: '{{ jobs }}'
      - name: parameters
        value: '{{ parameters }}'
      - name: dagTimeout
        value: '{{ dagTimeout }}'
      - name: encryptionConfig
        value: '{{ encryptionConfig }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified workflow_template resource.

```sql
DELETE FROM google.dataproc.workflow_templates
WHERE projectsId = '{{ projectsId }}'
AND regionsId = '{{ regionsId }}'
AND workflowTemplatesId = '{{ workflowTemplatesId }}';
```
