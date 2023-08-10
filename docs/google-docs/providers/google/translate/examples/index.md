---
title: examples
hide_title: false
hide_table_of_contents: false
keywords:
  - examples
  - translate
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
<tr><td><b>Name</b></td><td><code>examples</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.translate.examples</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the example, in form of `projects/&#123;project-number-or-id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/examples/&#123;example_id&#125;' |
| `usage` | `string` | Output only. Usage of the sentence pair. Options are TRAIN\|VALIDATION\|TEST. |
| `sourceText` | `string` | Sentence in source language. |
| `targetText` | `string` | Sentence in target language. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_datasets_examples_list` | `SELECT` | `datasetsId, locationsId, projectsId` |
| `_projects_locations_datasets_examples_list` | `EXEC` | `datasetsId, locationsId, projectsId` |
