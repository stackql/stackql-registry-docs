---
title: attestors
hide_title: false
hide_table_of_contents: false
keywords:
  - attestors
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
<tr><td><b>Name</b></td><td><code>attestors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.binaryauthorization.attestors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name, in the format: `projects/*/attestors/*`. This field may not be updated. |
| `description` | `string` | Optional. A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs. |
| `etag` | `string` | Optional. A checksum, returned by the server, that can be sent on update requests to ensure the attestor has an up-to-date value before attempting to update it. See https://google.aip.dev/154. |
| `updateTime` | `string` | Output only. Time when the attestor was last updated. |
| `userOwnedGrafeasNote` | `object` | An user owned Grafeas note references a Grafeas Attestation.Authority Note created by the user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `attestorsId, projectsId` | Gets an attestor. Returns NOT_FOUND if the attestor does not exist. |
| `list` | `SELECT` | `projectsId` | Lists attestors. Returns INVALID_ARGUMENT if the project does not exist. |
| `create` | `INSERT` | `projectsId` | Creates an attestor, and returns a copy of the new attestor. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the attestor already exists. |
| `delete` | `DELETE` | `attestorsId, projectsId` | Deletes an attestor. Returns NOT_FOUND if the attestor does not exist. |
| `_list` | `EXEC` | `projectsId` | Lists attestors. Returns INVALID_ARGUMENT if the project does not exist. |
| `update` | `EXEC` | `attestorsId, projectsId` | Updates an attestor. Returns NOT_FOUND if the attestor does not exist. |
| `validate_attestation_occurrence` | `EXEC` | `attestorsId, projectsId` | Returns whether the given Attestation for the given image URI was signed by the given Attestor |
