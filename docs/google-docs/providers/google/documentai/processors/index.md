---
title: processors
hide_title: false
hide_table_of_contents: false
keywords:
  - processors
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
<tr><td><b>Name</b></td><td><code>processors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.documentai.processors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Immutable. The resource name of the processor. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/processors/&#123;processor&#125;` |
| `processEndpoint` | `string` | Output only. Immutable. The http endpoint that can be called to invoke processing. |
| `processorVersionAliases` | `array` | Output only. The processor version aliases. |
| `displayName` | `string` | The display name of the processor. |
| `defaultProcessorVersion` | `string` | The default processor version. |
| `state` | `string` | Output only. The state of the processor. |
| `type` | `string` | The processor type, such as: `OCR_PROCESSOR`, `INVOICE_PROCESSOR`. To get a list of processor types, see FetchProcessorTypes. |
| `kmsKeyName` | `string` | The [KMS key](https://cloud.google.com/security-key-management) used for encryption and decryption in CMEK scenarios. |
| `createTime` | `string` | The time the processor was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_processors_get` | `SELECT` | `locationsId, processorsId, projectsId` | Gets a processor detail. |
| `projects_locations_processors_list` | `SELECT` | `locationsId, projectsId` | Lists all processors which belong to this project. |
| `projects_locations_processors_create` | `INSERT` | `locationsId, projectsId` | Creates a processor from the ProcessorType provided. The processor will be at `ENABLED` state by default after its creation. |
| `projects_locations_processors_delete` | `DELETE` | `locationsId, processorsId, projectsId` | Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor. |
| `_projects_locations_processors_list` | `EXEC` | `locationsId, projectsId` | Lists all processors which belong to this project. |
| `projects_locations_processors_batch_process` | `EXEC` | `locationsId, processorsId, projectsId` | LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format. |
| `projects_locations_processors_disable` | `EXEC` | `locationsId, processorsId, projectsId` | Disables a processor |
| `projects_locations_processors_enable` | `EXEC` | `locationsId, processorsId, projectsId` | Enables a processor |
| `projects_locations_processors_process` | `EXEC` | `locationsId, processorsId, projectsId` | Processes a single document. |
| `projects_locations_processors_set_default_processor_version` | `EXEC` | `locationsId, processorsId, projectsId` | Set the default (active) version of a Processor that will be used in ProcessDocument and BatchProcessDocuments. |
