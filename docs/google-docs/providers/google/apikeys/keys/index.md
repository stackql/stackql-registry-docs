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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apikeys.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the key. The `name` has the form: `projects//locations/global/keys/`. For example: `projects/123456867718/locations/global/keys/b7ff1f9f-8275-410a-94dd-3855ee9b5dd2` NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| `restrictions` | `object` | Describes the restrictions on the key. |
| `uid` | `string` | Output only. Unique id in UUID4 format. |
| `annotations` | `object` | Annotations is an unstructured key-value map stored with a policy that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. |
| `createTime` | `string` | Output only. A timestamp identifying the time this key was originally created. |
| `deleteTime` | `string` | Output only. A timestamp when this key was deleted. If the resource is not deleted, this must be empty. |
| `displayName` | `string` | Human-readable display name of this key that you can modify. The maximum length is 63 characters. |
| `etag` | `string` | Output only. A checksum computed by the server based on the current value of the Key resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. See https://google.aip.dev/154. |
| `updateTime` | `string` | Output only. A timestamp identifying the time this key was last updated. |
| `keyString` | `string` | Output only. An encrypted and signed value held by this key. This field can be accessed only through the `GetKeyString` method. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_keys_get` | `SELECT` | `keysId, locationsId, projectsId` | Gets the metadata for an API key. The key string of the API key isn't included in the response. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| `projects_locations_keys_list` | `SELECT` | `locationsId, projectsId` | Lists the API keys owned by a project. The key string of the API key isn't included in the response. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| `projects_locations_keys_create` | `INSERT` | `locationsId, projectsId` | Creates a new API key. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| `projects_locations_keys_delete` | `DELETE` | `keysId, locationsId, projectsId` | Deletes an API key. Deleted key can be retrieved within 30 days of deletion. Afterward, key will be purged from the project. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| `lookupKey` | `EXEC` |  | Find the parent project and resource name of the API key that matches the key string in the request. If the API key has been purged, resource name will not be set. The service account must have the `apikeys.keys.lookup` permission on the parent project. |
| `projects_locations_keys_patch` | `EXEC` | `keysId, locationsId, projectsId` | Patches the modifiable fields of an API key. The key string of the API key isn't included in the response. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| `projects_locations_keys_undelete` | `EXEC` | `keysId, locationsId, projectsId` | Undeletes an API key which was deleted within 30 days. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
