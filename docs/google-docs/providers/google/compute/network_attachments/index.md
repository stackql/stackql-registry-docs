---
title: network_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - network_attachments
  - compute
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
<tr><td><b>Name</b></td><td><code>network_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.network_attachments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource type. The server generates this identifier. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `selfLinkWithId` | `string` | [Output Only] Server-defined URL for this resource's resource id. |
| `producerRejectLists` | `array` | Projects that are not allowed to connect to this network attachment. The project can be specified using its id or number. |
| `kind` | `string` | [Output Only] Type of the resource. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. An up-to-date fingerprint must be provided in order to patch. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `subnetworks` | `array` | An array of URLs where each entry is the URL of a subnet provided by the service consumer to use for endpoints in the producers that connect to this network attachment. |
| `producerAcceptLists` | `array` | Projects that are allowed to connect to this network attachment. The project can be specified using its id or number. |
| `region` | `string` | [Output Only] URL of the region where the network attachment resides. This field applies only to the region resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `connectionPreference` | `string` |  |
| `network` | `string` | [Output Only] The URL of the network which the Network Attachment belongs to. Practically it is inferred by fetching the network of the first subnetwork associated. Because it is required that all the subnetworks must be from the same network, it is assured that the Network Attachment belongs to the same network as all the subnetworks. |
| `connectionEndpoints` | `array` | [Output Only] An array of connections for all the producers connected to this network attachment. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `aggregated_list` | `SELECT` | `project` | Retrieves the list of all NetworkAttachment resources, regional and global, available to the specified project. |
| `get` | `SELECT` | `networkAttachment, project, region` | Returns the specified NetworkAttachment resource in the given scope. |
| `list` | `SELECT` | `project, region` | Lists the NetworkAttachments for a project in the given scope. |
| `insert` | `INSERT` | `project, region` | Creates a NetworkAttachment in the specified project in the given scope using the parameters that are included in the request. |
| `delete` | `DELETE` | `networkAttachment, project, region` | Deletes the specified NetworkAttachment in the given scope |
| `_aggregated_list` | `EXEC` | `project` | Retrieves the list of all NetworkAttachment resources, regional and global, available to the specified project. |
