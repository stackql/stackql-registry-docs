---
title: evaluations
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluations
  - workloadmanager
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
<tr><td><b>Id</b></td><td><code>google.workloadmanager.evaluations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | name of resource names have the form 'projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/evaluations/&#123;evaluation_id&#125;' |
| `description` | `string` | Description of the Evaluation |
| `ruleNames` | `array` | the name of the rule |
| `labels` | `object` | Labels as key value pairs |
| `ruleVersions` | `array` | Output only. [Output only] The updated rule ids if exist. |
| `createTime` | `string` | Output only. [Output only] Create time stamp |
| `resourceFilter` | `object` | Message describing resource filters |
| `updateTime` | `string` | Output only. [Output only] Update time stamp |
| `resourceStatus` | `object` | Message describing resource status |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_evaluations_get` | `SELECT` | `evaluationsId, locationsId, projectsId` | Gets details of a single Evaluation. |
| `projects_locations_evaluations_list` | `SELECT` | `locationsId, projectsId` | Lists Evaluations in a given project and location. |
| `projects_locations_evaluations_create` | `INSERT` | `locationsId, projectsId` | Creates a new Evaluation in a given project and location. |
