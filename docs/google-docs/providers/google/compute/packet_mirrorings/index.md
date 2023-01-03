---
title: packet_mirrorings
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_mirrorings
  - compute
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
<tr><td><b>Name</b></td><td><code>packet_mirrorings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.packet_mirrorings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `priority` | `integer` | The priority of applying this configuration. Priority is used to break ties in cases where there is more than one matching rule. In the case of two rules that apply for a given Instance, the one with the lowest-numbered priority value wins. Default value is 1000. Valid range is 0 through 65535. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `collectorIlb` | `object` |  |
| `enable` | `string` | Indicates whether or not this packet mirroring takes effect. If set to FALSE, this packet mirroring policy will not be enforced on the network. The default is TRUE. |
| `region` | `string` | [Output Only] URI of the region where the packetMirroring resides. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `network` | `object` |  |
| `mirroredResources` | `object` |  |
| `filter` | `object` |  |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#packetMirroring for packet mirrorings. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `packetMirrorings_aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of packetMirrorings. |
| `packetMirrorings_get` | `SELECT` | `packetMirroring, project, region` | Returns the specified PacketMirroring resource. |
| `packetMirrorings_list` | `SELECT` | `project, region` | Retrieves a list of PacketMirroring resources available to the specified project and region. |
| `packetMirrorings_insert` | `INSERT` | `project, region` | Creates a PacketMirroring resource in the specified project and region using the data included in the request. |
| `packetMirrorings_delete` | `DELETE` | `packetMirroring, project, region` | Deletes the specified PacketMirroring resource. |
| `packetMirrorings_patch` | `EXEC` | `packetMirroring, project, region` | Patches the specified PacketMirroring resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
