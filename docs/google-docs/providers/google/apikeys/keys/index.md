---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - apikeys
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apikeys.keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the key. The `name` has the form: `projects//locations/global/keys/`. For example: `projects/123456867718/locations/global/keys/b7ff1f9f-8275-410a-94dd-3855ee9b5dd2` NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| <CopyableCode code="annotations" /> | `object` | Annotations is an unstructured key-value map stored with a policy that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. |
| <CopyableCode code="createTime" /> | `string` | Output only. A timestamp identifying the time this key was originally created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. A timestamp when this key was deleted. If the resource is not deleted, this must be empty. |
| <CopyableCode code="displayName" /> | `string` | Human-readable display name of this key that you can modify. The maximum length is 63 characters. |
| <CopyableCode code="etag" /> | `string` | Output only. A checksum computed by the server based on the current value of the Key resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. See https://google.aip.dev/154. |
| <CopyableCode code="keyString" /> | `string` | Output only. An encrypted and signed value held by this key. This field can be accessed only through the `GetKeyString` method. |
| <CopyableCode code="restrictions" /> | `object` | Describes the restrictions on the key. |
| <CopyableCode code="uid" /> | `string` | Output only. Unique id in UUID4 format. |
| <CopyableCode code="updateTime" /> | `string` | Output only. A timestamp identifying the time this key was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keysId, locationsId, projectsId" /> | Gets the metadata for an API key. The key string of the API key isn't included in the response. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the API keys owned by a project. The key string of the API key isn't included in the response. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new API key. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keysId, locationsId, projectsId" /> | Deletes an API key. Deleted key can be retrieved within 30 days of deletion. Afterward, key will be purged from the project. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="keysId, locationsId, projectsId" /> | Patches the modifiable fields of an API key. The key string of the API key isn't included in the response. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists the API keys owned by a project. The key string of the API key isn't included in the response. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| <CopyableCode code="lookup_key" /> | `EXEC` |  | Find the parent project and resource name of the API key that matches the key string in the request. If the API key has been purged, resource name will not be set. The service account must have the `apikeys.keys.lookup` permission on the parent project. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="keysId, locationsId, projectsId" /> | Undeletes an API key which was deleted within 30 days. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
