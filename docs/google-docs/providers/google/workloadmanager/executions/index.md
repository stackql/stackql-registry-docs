---
title: executions
hide_title: false
hide_table_of_contents: false
keywords:
  - executions
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
<tr><td><b>Name</b></td><td><code>executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workloadmanager.executions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of execution resource. The format is projects/&#123;project&#125;/locations/&#123;location&#125;/evaluations/&#123;evaluation&#125;/executions/&#123;execution&#125; |
| `labels` | `object` | Labels as key value pairs |
| `runType` | `string` | type represent whether the execution executed directly by user or scheduled according evaluation.schedule field. |
| `startTime` | `string` | Output only. [Output only] Start time stamp |
| `state` | `string` | Output only. [Output only] State |
| `endTime` | `string` | Output only. [Output only] End time stamp |
| `evaluationId` | `string` | Output only. [Output only] Evaluation ID |
| `inventoryTime` | `string` | Output only. [Output only] Inventory time stamp |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `evaluationsId, executionsId, locationsId, projectsId` | Gets details of a single Execution. |
| `list` | `SELECT` | `evaluationsId, locationsId, projectsId` | Lists Executions in a given project and location. |
| `_list` | `EXEC` | `evaluationsId, locationsId, projectsId` | Lists Executions in a given project and location. |
| `run` | `EXEC` | `evaluationsId, locationsId, projectsId` | Creates a new Execution in a given project and location. |
