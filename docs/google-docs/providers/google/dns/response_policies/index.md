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
| `id` | `string` | Unique identifier for the resource; defined by the server (output only). |
| `description` | `string` | User-provided description for this Response Policy. |
| `labels` | `object` | User labels. |
| `networks` | `array` | List of network names specifying networks to which this policy is applied. |
| `responsePolicyName` | `string` | User assigned name for this Response Policy. |
| `gkeClusters` | `array` | The list of Google Kubernetes Engine clusters to which this response policy is applied. |
| `kind` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project, responsePolicy` | Fetches the representation of an existing Response Policy. |
| `list` | `SELECT` | `project` | Enumerates all Response Policies associated with a project. |
| `create` | `INSERT` | `project` | Creates a new Response Policy |
| `delete` | `DELETE` | `project, responsePolicy` | Deletes a previously created Response Policy. Fails if the response policy is non-empty or still being referenced by a network. |
| `_list` | `EXEC` | `project` | Enumerates all Response Policies associated with a project. |
| `patch` | `EXEC` | `project, responsePolicy` | Applies a partial update to an existing Response Policy. |
| `update` | `EXEC` | `project, responsePolicy` | Updates an existing Response Policy. |
