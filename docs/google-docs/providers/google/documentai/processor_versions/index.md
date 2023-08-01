---
title: processor_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - processor_versions
  - documentai
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
<tr><td><b>Name</b></td><td><code>processor_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.documentai.processor_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `processorVersions` | `array` | The list of processors. |
| `nextPageToken` | `string` | Points to the next processor, otherwise empty. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_processors_processor_versions_get` | `SELECT` | `locationsId, processorVersionsId, processorsId, projectsId` | Gets a processor version detail. |
| `projects_locations_processors_processor_versions_list` | `SELECT` | `locationsId, processorsId, projectsId` | Lists all versions of a processor. |
| `projects_locations_processors_processor_versions_delete` | `DELETE` | `locationsId, processorVersionsId, processorsId, projectsId` | Deletes the processor version, all artifacts under the processor version will be deleted. |
| `projects_locations_processors_processor_versions_batch_process` | `EXEC` | `locationsId, processorVersionsId, processorsId, projectsId` | LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format. |
| `projects_locations_processors_processor_versions_deploy` | `EXEC` | `locationsId, processorVersionsId, processorsId, projectsId` | Deploys the processor version. |
| `projects_locations_processors_processor_versions_evaluate_processor_version` | `EXEC` | `locationsId, processorVersionsId, processorsId, projectsId` | Evaluates a ProcessorVersion against annotated documents, producing an Evaluation. |
| `projects_locations_processors_processor_versions_process` | `EXEC` | `locationsId, processorVersionsId, processorsId, projectsId` | Processes a single document. |
| `projects_locations_processors_processor_versions_train` | `EXEC` | `locationsId, processorsId, projectsId` | Trains a new processor version. Operation metadata is returned as TrainProcessorVersionMetadata. |
| `projects_locations_processors_processor_versions_undeploy` | `EXEC` | `locationsId, processorVersionsId, processorsId, projectsId` | Undeploys the processor version. |
