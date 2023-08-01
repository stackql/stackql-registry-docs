---
title: tag_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_keys
  - cloudresourcemanager
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
<tr><td><b>Name</b></td><td><code>tag_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudresourcemanager.tag_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A pagination token returned from a previous call to `ListTagKeys` that indicates from where listing should continue. |
| `tagKeys` | `array` | List of TagKeys that live under the specified parent in the request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `tagKeysId` | Retrieves a TagKey. This method will return `PERMISSION_DENIED` if the key does not exist or the user does not have permission to view it. |
| `list` | `SELECT` |  | Lists all TagKeys for a parent resource. |
| `create` | `INSERT` |  | Creates a new TagKey. If another request with the same parameters is sent while the original request is in process, the second request will receive an error. A maximum of 1000 TagKeys can exist under a parent at any given time. |
| `delete` | `DELETE` | `tagKeysId` | Deletes a TagKey. The TagKey cannot be deleted if it has any child TagValues. |
| `patch` | `EXEC` | `tagKeysId` | Updates the attributes of the TagKey resource. |
