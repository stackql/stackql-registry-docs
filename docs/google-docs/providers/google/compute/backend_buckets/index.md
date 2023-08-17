---
title: backend_buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - backend_buckets
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
<tr><td><b>Name</b></td><td><code>backend_buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.backend_buckets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] Unique identifier for the resource; defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional textual description of the resource; provided by the client when the resource is created. |
| `customResponseHeaders` | `array` | Headers that the Application Load Balancer should add to proxied responses. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `compressionMode` | `string` | Compress text responses using Brotli or gzip compression, based on the client's Accept-Encoding header. |
| `enableCdn` | `boolean` | If true, enable Cloud CDN for this BackendBucket. |
| `cdnPolicy` | `object` | Message containing Cloud CDN configuration for a backend bucket. |
| `bucketName` | `string` | Cloud Storage bucket name. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `edgeSecurityPolicy` | `string` | [Output Only] The resource URL for the edge security policy associated with this backend bucket. |
| `kind` | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backendBucket, project` | Returns the specified BackendBucket resource. |
| `list` | `SELECT` | `project` | Retrieves the list of BackendBucket resources available to the specified project. |
| `insert` | `INSERT` | `project` | Creates a BackendBucket resource in the specified project using the data included in the request. |
| `delete` | `DELETE` | `backendBucket, project` | Deletes the specified BackendBucket resource. |
| `_list` | `EXEC` | `project` | Retrieves the list of BackendBucket resources available to the specified project. |
| `patch` | `EXEC` | `backendBucket, project` | Updates the specified BackendBucket resource with the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| `set_edge_security_policy` | `EXEC` | `backendBucket, project` | Sets the edge security policy for the specified backend bucket. |
| `update` | `EXEC` | `backendBucket, project` | Updates the specified BackendBucket resource with the data included in the request. |
