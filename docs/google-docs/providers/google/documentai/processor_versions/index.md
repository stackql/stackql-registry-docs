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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | The resource name of the processor version. Format: `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}` |
| `kmsKeyVersionName` | `string` | The KMS key version with which data is encrypted. |
| `state` | `string` | The state of the processor version. |
| `createTime` | `string` | The time the processor version was created. |
| `deprecationInfo` | `object` | Information about the upcoming deprecation of this processor version. |
| `displayName` | `string` | The display name of the processor version. |
| `googleManaged` | `boolean` | Denotes that this ProcessorVersion is managed by google. |
| `kmsKeyName` | `string` | The KMS key name used for encryption. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_processors_processorVersions_get` | `SELECT` | `locationsId, processorVersionsId, processorsId, projectsId` | Gets a processor version detail. |
| `projects_locations_processors_processorVersions_list` | `SELECT` | `locationsId, processorsId, projectsId` | Lists all versions of a processor. |
| `projects_locations_processors_processorVersions_delete` | `DELETE` | `locationsId, processorVersionsId, processorsId, projectsId` | Deletes the processor version, all artifacts under the processor version will be deleted. |
| `projects_locations_processors_processorVersions_batchProcess` | `EXEC` | `locationsId, processorVersionsId, processorsId, projectsId` | LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format. |
| `projects_locations_processors_processorVersions_deploy` | `EXEC` | `locationsId, processorVersionsId, processorsId, projectsId` | Deploys the processor version. |
| `projects_locations_processors_processorVersions_process` | `EXEC` | `locationsId, processorVersionsId, processorsId, projectsId` | Processes a single document. |
| `projects_locations_processors_processorVersions_undeploy` | `EXEC` | `locationsId, processorVersionsId, processorsId, projectsId` | Undeploys the processor version. |
