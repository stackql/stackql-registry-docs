---
title: managed_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_zones
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
<tr><td><b>Name</b></td><td><code>managed_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dns.managed_zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The presence of this field indicates that there exist more results following your last page of results in pagination order. To fetch them, make another list request using this value as your page token. This lets you the complete contents of even very large collections one page at a time. However, if the contents of the collection change between the first and last paginated list request, the set of all elements returned are an inconsistent view of the collection. You cannot retrieve a consistent snapshot of a collection larger than the maximum page size. |
| `header` | `object` | Elements common to every response. |
| `kind` | `string` | Type of resource. |
| `managedZones` | `array` | The managed zone resources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `managedZone, project` | Fetches the representation of an existing ManagedZone. |
| `list` | `SELECT` | `project` | Enumerates ManagedZones that have been created but not yet deleted. |
| `create` | `INSERT` | `project` | Creates a new ManagedZone. |
| `delete` | `DELETE` | `managedZone, project` | Deletes a previously created ManagedZone. |
| `patch` | `EXEC` | `managedZone, project` | Applies a partial update to an existing ManagedZone. |
| `update` | `EXEC` | `managedZone, project` | Updates an existing ManagedZone. |
