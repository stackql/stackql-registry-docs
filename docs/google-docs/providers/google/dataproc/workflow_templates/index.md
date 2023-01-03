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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.workflow_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | Output only. The resource name of the workflow template, as described in https://cloud.google.com/apis/design/resource_names. For projects.regions.workflowTemplates, the resource name of the template has the following format: projects/{project_id}/regions/{region}/workflowTemplates/{template_id} For projects.locations.workflowTemplates, the resource name of the template has the following format: projects/{project_id}/locations/{location}/workflowTemplates/{template_id} |
| `dagTimeout` | `string` | Optional. Timeout duration for the DAG of jobs, expressed in seconds (see JSON representation of duration (https://developers.google.com/protocol-buffers/docs/proto3#json)). The timeout duration must be from 10 minutes ("600s") to 24 hours ("86400s"). The timer begins when the first job is submitted. If the workflow is running at the end of the timeout period, any remaining jobs are cancelled, the workflow is ended, and if the workflow was running on a managed cluster, the cluster is deleted. |
| `jobs` | `array` | Required. The Directed Acyclic Graph of Jobs to submit. |
| `version` | `integer` | Optional. Used to perform a consistent read-modify-write.This field should be left blank for a CreateWorkflowTemplate request. It is required for an UpdateWorkflowTemplate request, and must match the current server version. A typical update template flow would fetch the current template with a GetWorkflowTemplate request, which will return the current template with the version field filled in with the current server version. The user updates other fields in the template, then returns it as part of the UpdateWorkflowTemplate request. |
| `labels` | `object` | Optional. The labels to associate with this template. These labels will be propagated to all jobs and clusters created by the workflow instance.Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt).Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt).No more than 32 labels can be associated with a template. |
| `createTime` | `string` | Output only. The time template was created. |
| `parameters` | `array` | Optional. Template parameters whose values are substituted into the template. Values for parameters must be provided when the template is instantiated. |
| `placement` | `object` | Specifies workflow execution target.Either managed_cluster or cluster_selector is required. |
| `updateTime` | `string` | Output only. The time template was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_workflowTemplates_get` | `SELECT` | `locationsId, projectsId, workflowTemplatesId` | Retrieves the latest workflow template.Can retrieve previously instantiated template by specifying optional version parameter. |
| `projects_locations_workflowTemplates_list` | `SELECT` | `locationsId, projectsId` | Lists workflows that match the specified filter in the request. |
| `projects_regions_workflowTemplates_get` | `SELECT` | `projectsId, regionsId, workflowTemplatesId` | Retrieves the latest workflow template.Can retrieve previously instantiated template by specifying optional version parameter. |
| `projects_regions_workflowTemplates_list` | `SELECT` | `projectsId, regionsId` | Lists workflows that match the specified filter in the request. |
| `projects_locations_workflowTemplates_create` | `INSERT` | `locationsId, projectsId` | Creates new workflow template. |
| `projects_regions_workflowTemplates_create` | `INSERT` | `projectsId, regionsId` | Creates new workflow template. |
| `projects_locations_workflowTemplates_delete` | `DELETE` | `locationsId, projectsId, workflowTemplatesId` | Deletes a workflow template. It does not cancel in-progress workflows. |
| `projects_regions_workflowTemplates_delete` | `DELETE` | `projectsId, regionsId, workflowTemplatesId` | Deletes a workflow template. It does not cancel in-progress workflows. |
| `projects_locations_workflowTemplates_instantiate` | `EXEC` | `locationsId, projectsId, workflowTemplatesId` | Instantiates a template and begins execution.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| `projects_locations_workflowTemplates_instantiateInline` | `EXEC` | `locationsId, projectsId` | Instantiates a template and begins execution.This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| `projects_locations_workflowTemplates_update` | `EXEC` | `locationsId, projectsId, workflowTemplatesId` | Updates (replaces) workflow template. The updated template must contain version that matches the current server version. |
| `projects_regions_workflowTemplates_instantiate` | `EXEC` | `projectsId, regionsId, workflowTemplatesId` | Instantiates a template and begins execution.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| `projects_regions_workflowTemplates_instantiateInline` | `EXEC` | `projectsId, regionsId` | Instantiates a template and begins execution.This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| `projects_regions_workflowTemplates_update` | `EXEC` | `projectsId, regionsId, workflowTemplatesId` | Updates (replaces) workflow template. The updated template must contain version that matches the current server version. |
