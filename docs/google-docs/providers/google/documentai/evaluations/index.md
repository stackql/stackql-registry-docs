---
title: evaluations
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluations
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
<tr><td><b>Name</b></td><td><code>evaluations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.documentai.evaluations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the evaluation. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/processors/&#123;processor&#125;/processorVersions/&#123;processor_version&#125;/evaluations/&#123;evaluation&#125;` |
| `allEntitiesMetrics` | `object` | Metrics across multiple confidence levels. |
| `createTime` | `string` | The time that the evaluation was created. |
| `documentCounters` | `object` | Evaluation counters for the documents that were used. |
| `entityMetrics` | `object` | Metrics across confidence levels, for different entities. |
| `kmsKeyName` | `string` | The KMS key name used for encryption. |
| `kmsKeyVersionName` | `string` | The KMS key version with which data is encrypted. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_processors_processor_versions_evaluations_get` | `SELECT` | `evaluationsId, locationsId, processorVersionsId, processorsId, projectsId` | Retrieves a specific evaluation. |
| `projects_locations_processors_processor_versions_evaluations_list` | `SELECT` | `locationsId, processorVersionsId, processorsId, projectsId` | Retrieves a set of evaluations for a given processor version. |
| `_projects_locations_processors_processor_versions_evaluations_list` | `EXEC` | `locationsId, processorVersionsId, processorsId, projectsId` | Retrieves a set of evaluations for a given processor version. |
