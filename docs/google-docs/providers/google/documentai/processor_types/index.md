---
title: processor_types
hide_title: false
hide_table_of_contents: false
keywords:
  - processor_types
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
<tr><td><b>Name</b></td><td><code>processor_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.documentai.processor_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the processor type. Format: `projects/&#123;project&#125;/processorTypes/&#123;processor_type&#125;` |
| `allowCreation` | `boolean` | Whether the processor type allows creation. If true, users can create a processor of this processor type. Otherwise, users need to request access. |
| `availableLocations` | `array` | The locations in which this processor is available. |
| `category` | `string` | The processor category, used by UI to group processor types. |
| `launchStage` | `string` | Launch stage of the processor type |
| `sampleDocumentUris` | `array` | A set of Cloud Storage URIs of sample documents for this processor. |
| `type` | `string` | The processor type, e.g., `OCR_PROCESSOR`, `INVOICE_PROCESSOR`, etc. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_processorTypes_get` | `SELECT` | `locationsId, processorTypesId, projectsId` | Gets a processor type detail. |
| `projects_locations_processorTypes_list` | `SELECT` | `locationsId, projectsId` | Lists the processor types that exist. |
