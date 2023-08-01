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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.workflow_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `templates` | `array` | Output only. WorkflowTemplates list. |
| `nextPageToken` | `string` | Output only. This token is included in the response if there are more results to fetch. To fetch additional results, provide this value as the page_token in a subsequent ListWorkflowTemplatesRequest. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_workflow_templates_list` | `SELECT` | `locationsId, projectsId` | Lists workflows that match the specified filter in the request. |
| `projects_regions_workflow_templates_list` | `SELECT` | `projectsId, regionsId` | Lists workflows that match the specified filter in the request. |
| `projects_locations_workflow_templates_create` | `INSERT` | `locationsId, projectsId` | Creates new workflow template. |
| `projects_regions_workflow_templates_create` | `INSERT` | `projectsId, regionsId` | Creates new workflow template. |
| `projects_locations_workflow_templates_delete` | `DELETE` | `locationsId, projectsId, workflowTemplatesId` | Deletes a workflow template. It does not cancel in-progress workflows. |
| `projects_regions_workflow_templates_delete` | `DELETE` | `projectsId, regionsId, workflowTemplatesId` | Deletes a workflow template. It does not cancel in-progress workflows. |
| `projects_locations_workflow_templates_get` | `EXEC` | `locationsId, projectsId, workflowTemplatesId` | Retrieves the latest workflow template.Can retrieve previously instantiated template by specifying optional version parameter. |
| `projects_locations_workflow_templates_instantiate` | `EXEC` | `locationsId, projectsId, workflowTemplatesId` | Instantiates a template and begins execution.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| `projects_locations_workflow_templates_instantiate_inline` | `EXEC` | `locationsId, projectsId` | Instantiates a template and begins execution.This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| `projects_locations_workflow_templates_update` | `EXEC` | `locationsId, projectsId, workflowTemplatesId` | Updates (replaces) workflow template. The updated template must contain version that matches the current server version. |
| `projects_regions_workflow_templates_get` | `EXEC` | `projectsId, regionsId, workflowTemplatesId` | Retrieves the latest workflow template.Can retrieve previously instantiated template by specifying optional version parameter. |
| `projects_regions_workflow_templates_instantiate` | `EXEC` | `projectsId, regionsId, workflowTemplatesId` | Instantiates a template and begins execution.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| `projects_regions_workflow_templates_instantiate_inline` | `EXEC` | `projectsId, regionsId` | Instantiates a template and begins execution.This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| `projects_regions_workflow_templates_update` | `EXEC` | `projectsId, regionsId, workflowTemplatesId` | Updates (replaces) workflow template. The updated template must contain version that matches the current server version. |
