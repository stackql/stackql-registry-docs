---
title: resource_record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_record_sets
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
<tr><td><b>Name</b></td><td><code>resource_record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dns.resource_record_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `rrsets` | `array` | The resource record set resources. |
| `header` | `object` | Elements common to every response. |
| `kind` | `string` | Type of resource. |
| `nextPageToken` | `string` | The presence of this field indicates that there exist more results following your last page of results in pagination order. To fetch them, make another list request using this value as your pagination token. This lets you retrieve complete contents of even larger collections, one page at a time. However, if the contents of the collection change between the first and last paginated list request, the set of elements returned are an inconsistent view of the collection. You cannot retrieve a consistent snapshot of a collection larger than the maximum page size. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `managedZone, name, project, type` | Fetches the representation of an existing ResourceRecordSet. |
| `list` | `SELECT` | `managedZone, project` | Enumerates ResourceRecordSets that you have created but not yet deleted. |
| `create` | `INSERT` | `managedZone, project` | Creates a new ResourceRecordSet. |
| `delete` | `DELETE` | `managedZone, name, project, type` | Deletes a previously created ResourceRecordSet. |
| `patch` | `EXEC` | `managedZone, name, project, type` | Applies a partial update to an existing ResourceRecordSet. |
