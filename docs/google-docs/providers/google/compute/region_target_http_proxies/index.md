---
title: region_target_http_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - region_target_http_proxies
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
<tr><td><b>Name</b></td><td><code>region_target_http_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_target_http_proxies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a TargetHttpProxy. An up-to-date fingerprint must be provided in order to patch/update the TargetHttpProxy; otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the TargetHttpProxy. |
| `urlMap` | `string` | URL to the UrlMap resource that defines the mapping from URL to the BackendService. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#targetHttpProxy for target HTTP proxies. |
| `proxyBind` | `boolean` | This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set to INTERNAL_SELF_MANAGED. When this field is set to true, Envoy proxies set up inbound traffic interception and bind to the IP address and port specified in the forwarding rule. This is generally useful when using Traffic Director to configure Envoy as a gateway or middle proxy (in other words, not a sidecar proxy). The Envoy proxy listens for inbound requests and handles requests when it receives them. The default is false. |
| `region` | `string` | [Output Only] URL of the region where the regional Target HTTP Proxy resides. This field is not applicable to global Target HTTP Proxies. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `regionTargetHttpProxies_get` | `SELECT` | `project, region, targetHttpProxy` | Returns the specified TargetHttpProxy resource in the specified region. Gets a list of available target HTTP proxies by making a list() request. |
| `regionTargetHttpProxies_list` | `SELECT` | `project, region` | Retrieves the list of TargetHttpProxy resources available to the specified project in the specified region. |
| `regionTargetHttpProxies_insert` | `INSERT` | `project, region` | Creates a TargetHttpProxy resource in the specified project and region using the data included in the request. |
| `regionTargetHttpProxies_delete` | `DELETE` | `project, region, targetHttpProxy` | Deletes the specified TargetHttpProxy resource. |
| `regionTargetHttpProxies_setUrlMap` | `EXEC` | `project, region, targetHttpProxy` | Changes the URL map for TargetHttpProxy. |
