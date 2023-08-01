---
title: changes
hide_title: false
hide_table_of_contents: false
keywords:
  - changes
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
<tr><td><b>Name</b></td><td><code>changes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dns.changes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `changes` | `array` | The requested changes. |
| `header` | `object` | Elements common to every response. |
| `kind` | `string` | Type of resource. |
| `nextPageToken` | `string` | The presence of this field indicates that there exist more results following your last page of results in pagination order. To fetch them, make another list request using this value as your pagination token. This lets you retrieve the complete contents of even very large collections one page at a time. However, if the contents of the collection change between the first and last paginated list request, the set of all elements returned are an inconsistent view of the collection. You cannot retrieve a "snapshot" of collections larger than the maximum page size. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `changeId, managedZone, project` | Fetches the representation of an existing Change. |
| `list` | `SELECT` | `managedZone, project` | Enumerates Changes to a ResourceRecordSet collection. |
| `create` | `INSERT` | `managedZone, project` | Atomically updates the ResourceRecordSet collection. |
