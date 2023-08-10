---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - binaryauthorization
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.binaryauthorization.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The relative resource name of the BinAuthz platform policy, in the form of `projects/*/platforms/*/policies/*`. |
| `description` | `string` | Optional. A description comment about the policy. |
| `gkePolicy` | `object` | A Binary Authorization policy for a GKE cluster. This is one type of policy that can occur as a `PlatformPolicy`. |
| `updateTime` | `string` | Output only. Time when the policy was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `platformsId, policiesId, projectsId` | Gets a platform policy. Returns NOT_FOUND if the policy doesn't exist. |
| `list` | `SELECT` | `platformsId, projectsId` | Lists platform policies owned by a project in the specified platform. Returns INVALID_ARGUMENT if the project or the platform doesn't exist. |
| `create` | `INSERT` | `platformsId, projectsId` | Creates a platform policy, and returns a copy of it. Returns NOT_FOUND if the project or platform doesn't exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the policy already exists, and INVALID_ARGUMENT if the policy contains a platform-specific policy that does not match the platform value specified in the URL. |
| `delete` | `DELETE` | `platformsId, policiesId, projectsId` | Deletes a platform policy. Returns NOT_FOUND if the policy doesn't exist. |
| `_list` | `EXEC` | `platformsId, projectsId` | Lists platform policies owned by a project in the specified platform. Returns INVALID_ARGUMENT if the project or the platform doesn't exist. |
| `replace_platform_policy` | `EXEC` | `platformsId, policiesId, projectsId` | Replaces a platform policy. Returns NOT_FOUND if the policy doesn't exist. |
