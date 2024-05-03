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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hmac_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storage.hmac_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the HMAC key, including the Project ID and the Access ID. |
| <CopyableCode code="accessId" /> | `string` | The ID of the HMAC Key. |
| <CopyableCode code="etag" /> | `string` | HTTP 1.1 Entity tag for the HMAC key. |
| <CopyableCode code="kind" /> | `string` | The kind of item this is. For HMAC Key metadata, this is always storage#hmacKeyMetadata. |
| <CopyableCode code="projectId" /> | `string` | Project ID owning the service account to which the key authenticates. |
| <CopyableCode code="selfLink" /> | `string` | The link to this resource. |
| <CopyableCode code="serviceAccountEmail" /> | `string` | The email address of the key's associated service account. |
| <CopyableCode code="state" /> | `string` | The state of the key. Can be one of ACTIVE, INACTIVE, or DELETED. |
| <CopyableCode code="timeCreated" /> | `string` | The creation time of the HMAC key in RFC 3339 format. |
| <CopyableCode code="updated" /> | `string` | The last modification time of the HMAC key metadata in RFC 3339 format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessId, projectId" /> | Retrieves an HMAC key's metadata |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectId" /> | Retrieves a list of HMAC keys matching the criteria. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectId, serviceAccountEmail" /> | Creates a new HMAC key for the specified service account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessId, projectId" /> | Deletes an HMAC key. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="projectId" /> | Retrieves a list of HMAC keys matching the criteria. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accessId, projectId" /> | Updates the state of an HMAC key. See the HMAC Key resource descriptor for valid states. |
