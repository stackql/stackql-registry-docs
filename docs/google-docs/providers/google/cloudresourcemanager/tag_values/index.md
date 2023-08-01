---
title: tag_values
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_values
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
<tr><td><b>Name</b></td><td><code>tag_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudresourcemanager.tag_values</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A pagination token returned from a previous call to `ListTagValues` that indicates from where listing should continue. This is currently not used, but the server may at any point start supplying a valid token. |
| `tagValues` | `array` | A possibly paginated list of TagValues that are direct descendants of the specified parent TagKey. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `tagValuesId` | Retrieves a TagValue. This method will return `PERMISSION_DENIED` if the value does not exist or the user does not have permission to view it. |
| `list` | `SELECT` |  | Lists all TagValues for a specific TagKey. |
| `create` | `INSERT` |  | Creates a TagValue as a child of the specified TagKey. If a another request with the same parameters is sent while the original request is in process the second request will receive an error. A maximum of 1000 TagValues can exist under a TagKey at any given time. |
| `delete` | `DELETE` | `tagValuesId` | Deletes a TagValue. The TagValue cannot have any bindings when it is deleted. |
| `patch` | `EXEC` | `tagValuesId` | Updates the attributes of the TagValue resource. |
