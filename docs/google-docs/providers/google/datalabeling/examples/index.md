---
title: examples
hide_title: false
hide_table_of_contents: false
keywords:
  - examples
  - datalabeling
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
<tr><td><b>Id</b></td><td><code>google.datalabeling.examples</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the example, in format of: projects/&#123;project_id&#125;/datasets/&#123;dataset_id&#125;/annotatedDatasets/ &#123;annotated_dataset_id&#125;/examples/&#123;example_id&#125; |
| `textPayload` | `object` | Container of information about a piece of text. |
| `videoPayload` | `object` | Container of information of a video. |
| `annotations` | `array` | Output only. Annotations for the piece of data in Example. One piece of data can have multiple annotations. |
| `imagePayload` | `object` | Container of information about an image. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_datasets_annotated_datasets_examples_get` | `SELECT` | `annotatedDatasetsId, datasetsId, examplesId, projectsId` | Gets an example by resource name, including both data and annotation. |
| `projects_datasets_annotated_datasets_examples_list` | `SELECT` | `annotatedDatasetsId, datasetsId, projectsId` | Lists examples in an annotated dataset. Pagination is supported. |
| `_projects_datasets_annotated_datasets_examples_list` | `EXEC` | `annotatedDatasetsId, datasetsId, projectsId` | Lists examples in an annotated dataset. Pagination is supported. |
