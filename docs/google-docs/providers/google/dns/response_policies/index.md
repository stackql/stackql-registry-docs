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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `id` | `string` | Unique identifier for the resource; defined by the server (output only). |
| `description` | `string` | User-provided description for this Response Policy. |
| `kind` | `string` |  |
| `networks` | `array` | List of network names specifying networks to which this policy is applied. |
| `responsePolicyName` | `string` | User assigned name for this Response Policy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `responsePolicies_get` | `SELECT` | `project, responsePolicy` | Fetches the representation of an existing Response Policy. |
| `responsePolicies_list` | `SELECT` | `project` | Enumerates all Response Policies associated with a project. |
| `responsePolicies_create` | `INSERT` | `project` | Creates a new Response Policy |
| `responsePolicies_delete` | `DELETE` | `project, responsePolicy` | Deletes a previously created Response Policy. Fails if the response policy is non-empty or still being referenced by a network. |
| `responsePolicies_patch` | `EXEC` | `project, responsePolicy` | Applies a partial update to an existing Response Policy. |
| `responsePolicies_update` | `EXEC` | `project, responsePolicy` | Updates an existing Response Policy. |
