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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apikeys.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `keys` | `array` | A list of API keys. |
| `nextPageToken` | `string` | The pagination token for the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `keysId, locationsId, projectsId` | Gets the metadata for an API key. The key string of the API key isn't included in the response. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists the API keys owned by a project. The key string of the API key isn't included in the response. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new API key. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| `delete` | `DELETE` | `keysId, locationsId, projectsId` | Deletes an API key. Deleted key can be retrieved within 30 days of deletion. Afterward, key will be purged from the project. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| `lookup_key` | `EXEC` |  | Find the parent project and resource name of the API key that matches the key string in the request. If the API key has been purged, resource name will not be set. The service account must have the `apikeys.keys.lookup` permission on the parent project. |
| `patch` | `EXEC` | `keysId, locationsId, projectsId` | Patches the modifiable fields of an API key. The key string of the API key isn't included in the response. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| `undelete` | `EXEC` | `keysId, locationsId, projectsId` | Undeletes an API key which was deleted within 30 days. NOTE: Key is a global resource; hence the only supported value for location is `global`. |
