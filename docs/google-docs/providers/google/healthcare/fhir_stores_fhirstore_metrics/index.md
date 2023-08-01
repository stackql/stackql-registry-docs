---
title: fhir_stores_fhirstore_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_stores_fhirstore_metrics
  - healthcare
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
<tr><td><b>Name</b></td><td><code>fhir_stores_fhirstore_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.fhir_stores_fhirstore_metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the FHIR store to get metrics for, in the format `projects/&#123;project_id&#125;/datasets/&#123;dataset_id&#125;/fhirStores/&#123;fhir_store_id&#125;`. |
| `metrics` | `array` | List of FhirStoreMetric by resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_fhirstore_metrics` | `SELECT` | `datasetsId, fhirStoresId, locationsId, projectsId` |
