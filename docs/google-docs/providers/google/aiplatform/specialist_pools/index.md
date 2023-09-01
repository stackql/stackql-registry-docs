---
title: specialist_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - specialist_pools
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
<tr><td><b>Name</b></td><td><code>specialist_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.specialist_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the SpecialistPool. |
| `displayName` | `string` | Required. The user-defined name of the SpecialistPool. The name can be up to 128 characters long and can consist of any UTF-8 characters. This field should be unique on project-level. |
| `pendingDataLabelingJobs` | `array` | Output only. The resource name of the pending data labeling jobs. |
| `specialistManagerEmails` | `array` | The email addresses of the managers in the SpecialistPool. |
| `specialistManagersCount` | `integer` | Output only. The number of managers in this SpecialistPool. |
| `specialistWorkerEmails` | `array` | The email addresses of workers in the SpecialistPool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, specialistPoolsId` | Gets a SpecialistPool. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists SpecialistPools in a Location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a SpecialistPool. |
| `delete` | `DELETE` | `locationsId, projectsId, specialistPoolsId` | Deletes a SpecialistPool as well as all Specialists in the pool. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists SpecialistPools in a Location. |
| `patch` | `EXEC` | `locationsId, projectsId, specialistPoolsId` | Updates a SpecialistPool. |
