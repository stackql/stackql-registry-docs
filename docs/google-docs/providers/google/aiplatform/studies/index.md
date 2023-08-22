---
title: studies
hide_title: false
hide_table_of_contents: false
keywords:
  - studies
  - aiplatform
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
<tr><td><b>Name</b></td><td><code>studies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.studies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of a study. The study's globally unique identifier. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/studies/&#123;study&#125;` |
| `state` | `string` | Output only. The detailed state of a Study. |
| `studySpec` | `object` | Represents specification of a Study. |
| `createTime` | `string` | Output only. Time at which the study was created. |
| `displayName` | `string` | Required. Describes the Study, default value is empty string. |
| `inactiveReason` | `string` | Output only. A human readable reason why the Study is inactive. This should be empty if a study is ACTIVE or COMPLETED. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, studiesId` | Gets a Study by name. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all the studies in a region for an associated project. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a Study. A resource name will be generated after creation of the Study. |
| `delete` | `DELETE` | `locationsId, projectsId, studiesId` | Deletes a Study. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists all the studies in a region for an associated project. |
| `lookup` | `EXEC` | `locationsId, projectsId` | Looks a study up using the user-defined display_name field instead of the fully qualified resource name. |
