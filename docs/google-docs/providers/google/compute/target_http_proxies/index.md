---
title: target_http_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - target_http_proxies
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
<tr><td><b>Name</b></td><td><code>target_http_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.target_http_proxies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `urlMap` | `string` | URL to the UrlMap resource that defines the mapping from URL to the BackendService. |
| `region` | `string` | [Output Only] URL of the region where the regional Target HTTP Proxy resides. This field is not applicable to global Target HTTP Proxies. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#targetHttpProxy for target HTTP proxies. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a TargetHttpProxy. An up-to-date fingerprint must be provided in order to patch/update the TargetHttpProxy; otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the TargetHttpProxy. |
| `proxyBind` | `boolean` | This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set to INTERNAL_SELF_MANAGED. When this field is set to true, Envoy proxies set up inbound traffic interception and bind to the IP address and port specified in the forwarding rule. This is generally useful when using Traffic Director to configure Envoy as a gateway or middle proxy (in other words, not a sidecar proxy). The Envoy proxy listens for inbound requests and handles requests when it receives them. The default is false. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `targetHttpProxies_get` | `SELECT` | `project, targetHttpProxy` | Returns the specified TargetHttpProxy resource. Gets a list of available target HTTP proxies by making a list() request. |
| `targetHttpProxies_list` | `SELECT` | `project` | Retrieves the list of TargetHttpProxy resources available to the specified project. |
| `targetHttpProxies_insert` | `INSERT` | `project` | Creates a TargetHttpProxy resource in the specified project using the data included in the request. |
| `targetHttpProxies_delete` | `DELETE` | `project, targetHttpProxy` | Deletes the specified TargetHttpProxy resource. |
| `targetHttpProxies_patch` | `EXEC` | `project, targetHttpProxy` | Patches the specified TargetHttpProxy resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
| `targetHttpProxies_setUrlMap` | `EXEC` | `project, targetHttpProxy` | Changes the URL map for TargetHttpProxy. |
