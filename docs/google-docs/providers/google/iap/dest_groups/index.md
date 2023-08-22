---
title: dest_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - dest_groups
  - iap
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
<tr><td><b>Name</b></td><td><code>dest_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iap.dest_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Immutable. Identifier for the TunnelDestGroup. Must be unique within the project and contain only lower case letters (a-z) and dashes (-). |
| `fqdns` | `array` | Unordered list. List of FQDNs that this group applies to. |
| `cidrs` | `array` | Unordered list. List of CIDRs that this group applies to. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `destGroupsId, locationsId, projectsId` | Retrieves an existing TunnelDestGroup. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists the existing TunnelDestGroups. To group across all locations, use a `-` as the location ID. For example: `/v1/projects/123/iap_tunnel/locations/-/destGroups` |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new TunnelDestGroup. |
| `delete` | `DELETE` | `destGroupsId, locationsId, projectsId` | Deletes a TunnelDestGroup. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists the existing TunnelDestGroups. To group across all locations, use a `-` as the location ID. For example: `/v1/projects/123/iap_tunnel/locations/-/destGroups` |
| `patch` | `EXEC` | `destGroupsId, locationsId, projectsId` | Updates a TunnelDestGroup. |
