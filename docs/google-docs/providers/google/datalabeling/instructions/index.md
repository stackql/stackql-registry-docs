---
title: instructions
hide_title: false
hide_table_of_contents: false
keywords:
  - instructions
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
<tr><td><b>Name</b></td><td><code>instructions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalabeling.instructions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Instruction resource name, format: projects/&#123;project_id&#125;/instructions/&#123;instruction_id&#125; |
| `description` | `string` | Optional. User-provided description of the instruction. The description can be up to 10000 characters long. |
| `displayName` | `string` | Required. The display name of the instruction. Maximum of 64 characters. |
| `createTime` | `string` | Output only. Creation time of instruction. |
| `updateTime` | `string` | Output only. Last update time of instruction. |
| `dataType` | `string` | Required. The data type of this instruction. |
| `pdfInstruction` | `object` | Instruction from a PDF file. |
| `csvInstruction` | `object` | Deprecated: this instruction format is not supported any more. Instruction from a CSV file. |
| `blockingResources` | `array` | Output only. The names of any related resources that are blocking changes to the instruction. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_instructions_get` | `SELECT` | `instructionsId, projectsId` | Gets an instruction by resource name. |
| `projects_instructions_list` | `SELECT` | `projectsId` | Lists instructions for a project. Pagination is supported. |
| `projects_instructions_create` | `INSERT` | `projectsId` | Creates an instruction for how data should be labeled. |
| `projects_instructions_delete` | `DELETE` | `instructionsId, projectsId` | Deletes an instruction object by resource name. |
