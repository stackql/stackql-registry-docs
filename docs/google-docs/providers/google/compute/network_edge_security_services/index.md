---
title: network_edge_security_services
hide_title: false
hide_table_of_contents: false
keywords:
  - network_edge_security_services
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
<tr><td><b>Name</b></td><td><code>network_edge_security_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.network_edge_security_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a NetworkEdgeSecurityService. An up-to-date fingerprint must be provided in order to update the NetworkEdgeSecurityService, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a NetworkEdgeSecurityService. |
| `kind` | `string` | [Output only] Type of the resource. Always compute#networkEdgeSecurityService for NetworkEdgeSecurityServices |
| `selfLinkWithId` | `string` | [Output Only] Server-defined URL for this resource with the resource id. |
| `region` | `string` | [Output Only] URL of the region where the resource resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `securityPolicy` | `string` | The resource URL for the network edge security service associated with this network edge security service. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `networkEdgeSecurityServices_aggregatedList` | `SELECT` | `project` | Retrieves the list of all NetworkEdgeSecurityService resources available to the specified project. |
| `networkEdgeSecurityServices_get` | `SELECT` | `networkEdgeSecurityService, project, region` | Gets a specified NetworkEdgeSecurityService. |
| `networkEdgeSecurityServices_insert` | `INSERT` | `project, region` | Creates a new service in the specified project using the data included in the request. |
| `networkEdgeSecurityServices_delete` | `DELETE` | `networkEdgeSecurityService, project, region` | Deletes the specified service. |
| `networkEdgeSecurityServices_patch` | `EXEC` | `networkEdgeSecurityService, project, region` | Patches the specified policy with the data included in the request. |
