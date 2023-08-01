---
title: response_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - response_policies
  - dns
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
<tr><td><b>Name</b></td><td><code>response_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dns.response_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `header` | `object` | Elements common to every response. |
| `nextPageToken` | `string` | The presence of this field indicates that more results exist following your last page of results in pagination order. To fetch them, make another list request by using this value as your page token. This lets you view the complete contents of even very large collections one page at a time. However, if the contents of the collection change between the first and last paginated list request, the set of all elements returned are an inconsistent view of the collection. You cannot retrieve a consistent snapshot of a collection larger than the maximum page size. |
| `responsePolicies` | `array` | The Response Policy resources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project, responsePolicy` | Fetches the representation of an existing Response Policy. |
| `list` | `SELECT` | `project` | Enumerates all Response Policies associated with a project. |
| `create` | `INSERT` | `project` | Creates a new Response Policy |
| `delete` | `DELETE` | `project, responsePolicy` | Deletes a previously created Response Policy. Fails if the response policy is non-empty or still being referenced by a network. |
| `patch` | `EXEC` | `project, responsePolicy` | Applies a partial update to an existing Response Policy. |
| `update` | `EXEC` | `project, responsePolicy` | Updates an existing Response Policy. |
