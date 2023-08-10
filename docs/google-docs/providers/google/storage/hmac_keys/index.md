---
title: hmac_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - hmac_keys
  - storage
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
<tr><td><b>Name</b></td><td><code>hmac_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storage.hmac_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the HMAC key, including the Project ID and the Access ID. |
| `state` | `string` | The state of the key. Can be one of ACTIVE, INACTIVE, or DELETED. |
| `updated` | `string` | The last modification time of the HMAC key metadata in RFC 3339 format. |
| `etag` | `string` | HTTP 1.1 Entity tag for the HMAC key. |
| `selfLink` | `string` | The link to this resource. |
| `projectId` | `string` | Project ID owning the service account to which the key authenticates. |
| `timeCreated` | `string` | The creation time of the HMAC key in RFC 3339 format. |
| `accessId` | `string` | The ID of the HMAC Key. |
| `kind` | `string` | The kind of item this is. For HMAC Key metadata, this is always storage#hmacKeyMetadata. |
| `serviceAccountEmail` | `string` | The email address of the key's associated service account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accessId, projectId` | Retrieves an HMAC key's metadata |
| `list` | `SELECT` | `projectId` | Retrieves a list of HMAC keys matching the criteria. |
| `create` | `INSERT` | `projectId, serviceAccountEmail` | Creates a new HMAC key for the specified service account. |
| `delete` | `DELETE` | `accessId, projectId` | Deletes an HMAC key. |
| `_list` | `EXEC` | `projectId` | Retrieves a list of HMAC keys matching the criteria. |
| `update` | `EXEC` | `accessId, projectId` | Updates the state of an HMAC key. See the HMAC Key resource descriptor for valid states. |
