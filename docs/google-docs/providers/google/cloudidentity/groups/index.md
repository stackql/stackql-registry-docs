---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - cloudidentity
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudidentity.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `groups` | `array` | Groups returned in response to list request. The results are not sorted. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results available for listing. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `groupsId` | Retrieves a `Group`. |
| `list` | `SELECT` |  | Lists the `Group` resources under a customer or namespace. |
| `create` | `INSERT` |  | Creates a Group. |
| `delete` | `DELETE` | `groupsId` | Deletes a `Group`. |
| `lookup` | `EXEC` |  | Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a `Group` by its `EntityKey`. |
| `patch` | `EXEC` | `groupsId` | Updates a `Group`. |
| `search` | `EXEC` |  | Searches for `Group` resources matching a specified query. |
