---
title: ekm_config
hide_title: false
hide_table_of_contents: false
keywords:
  - ekm_config
  - cloudkms
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
<tr><td><b>Name</b></td><td><code>ekm_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudkms.ekm_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for the EkmConfig in the format `projects/*/locations/*/ekmConfig`. |
| `defaultEkmConnection` | `string` | Optional. Resource name of the default EkmConnection. Setting this field to the empty string removes the default. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_ekm_config` | `SELECT` | `locationsId, projectsId` | Returns the EkmConfig singleton resource for a given project and location. |
| `update_ekm_config` | `EXEC` | `locationsId, projectsId` | Updates the EkmConfig singleton resource for a given project and location. |
