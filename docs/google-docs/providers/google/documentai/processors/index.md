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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>processors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.documentai.processors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Immutable. The resource name of the processor. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/processors/&#123;processor&#125;` |
| <CopyableCode code="createTime" /> | `string` | The time the processor was created. |
| <CopyableCode code="defaultProcessorVersion" /> | `string` | The default processor version. |
| <CopyableCode code="displayName" /> | `string` | The display name of the processor. |
| <CopyableCode code="kmsKeyName" /> | `string` | The [KMS key](https://cloud.google.com/security-key-management) used for encryption and decryption in CMEK scenarios. |
| <CopyableCode code="processEndpoint" /> | `string` | Output only. Immutable. The http endpoint that can be called to invoke processing. |
| <CopyableCode code="processorVersionAliases" /> | `array` | Output only. The processor version aliases. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the processor. |
| <CopyableCode code="type" /> | `string` | The processor type, such as: `OCR_PROCESSOR`, `INVOICE_PROCESSOR`. To get a list of processor types, see FetchProcessorTypes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_processors_get" /> | `SELECT` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Gets a processor detail. |
| <CopyableCode code="projects_locations_processors_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all processors which belong to this project. |
| <CopyableCode code="projects_locations_processors_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a processor from the ProcessorType provided. The processor will be at `ENABLED` state by default after its creation. |
| <CopyableCode code="projects_locations_processors_delete" /> | `DELETE` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor. |
| <CopyableCode code="_projects_locations_processors_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all processors which belong to this project. |
| <CopyableCode code="projects_locations_processors_batch_process" /> | `EXEC` | <CopyableCode code="locationsId, processorsId, projectsId" /> | LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format. |
| <CopyableCode code="projects_locations_processors_disable" /> | `EXEC` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Disables a processor |
| <CopyableCode code="projects_locations_processors_enable" /> | `EXEC` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Enables a processor |
| <CopyableCode code="projects_locations_processors_process" /> | `EXEC` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Processes a single document. |
| <CopyableCode code="projects_locations_processors_set_default_processor_version" /> | `EXEC` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Set the default (active) version of a Processor that will be used in ProcessDocument and BatchProcessDocuments. |
