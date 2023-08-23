---
title: sources
hide_title: false
hide_table_of_contents: false
keywords:
  - sources
  - vmmigration
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
<tr><td><b>Name</b></td><td><code>sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The Source name. |
| `description` | `string` | User-provided description of the source. |
| `labels` | `object` | The labels of the source. |
| `updateTime` | `string` | Output only. The update time timestamp. |
| `vmware` | `object` | VmwareSourceDetails message describes a specific source details for the vmware source type. |
| `aws` | `object` | AwsSourceDetails message describes a specific source details for the AWS source type. |
| `createTime` | `string` | Output only. The create time timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, sourcesId` | Gets details of a single Source. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Sources in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Source in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, sourcesId` | Deletes a single Source. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists Sources in a given project and location. |
| `patch` | `EXEC` | `locationsId, projectsId, sourcesId` | Updates the parameters of a single Source. |
