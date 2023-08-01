---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dns.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `header` | `object` | Elements common to every response. |
| `kind` | `string` | Type of resource. |
| `nextPageToken` | `string` | The presence of this field indicates that there exist more results following your last page of results in pagination order. To fetch them, make another list request using this value as your page token. This lets you the complete contents of even very large collections one page at a time. However, if the contents of the collection change between the first and last paginated list request, the set of all elements returned are an inconsistent view of the collection. You cannot retrieve a consistent snapshot of a collection larger than the maximum page size. |
| `policies` | `array` | The policy resources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `policy, project` | Fetches the representation of an existing Policy. |
| `list` | `SELECT` | `project` | Enumerates all Policies associated with a project. |
| `create` | `INSERT` | `project` | Creates a new Policy. |
| `delete` | `DELETE` | `policy, project` | Deletes a previously created Policy. Fails if the policy is still being referenced by a network. |
| `patch` | `EXEC` | `policy, project` | Applies a partial update to an existing Policy. |
| `update` | `EXEC` | `policy, project` | Updates an existing Policy. |
