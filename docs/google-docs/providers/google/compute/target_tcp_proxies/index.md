---
title: target_tcp_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - target_tcp_proxies
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
<tr><td><b>Name</b></td><td><code>target_tcp_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.target_tcp_proxies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `region` | `string` | [Output Only] URL of the region where the regional TCP proxy resides. This field is not applicable to global TCP proxy. |
| `service` | `string` | URL to the BackendService resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#targetTcpProxy for target TCP proxies. |
| `proxyHeader` | `string` | Specifies the type of proxy header to append before sending data to the backend, either NONE or PROXY_V1. The default is NONE. |
| `proxyBind` | `boolean` | This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set to INTERNAL_SELF_MANAGED. When this field is set to true, Envoy proxies set up inbound traffic interception and bind to the IP address and port specified in the forwarding rule. This is generally useful when using Traffic Director to configure Envoy as a gateway or middle proxy (in other words, not a sidecar proxy). The Envoy proxy listens for inbound requests and handles requests when it receives them. The default is false. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project, targetTcpProxy` | Returns the specified TargetTcpProxy resource. |
| `list` | `SELECT` | `project` | Retrieves the list of TargetTcpProxy resources available to the specified project. |
| `insert` | `INSERT` | `project` | Creates a TargetTcpProxy resource in the specified project using the data included in the request. |
| `delete` | `DELETE` | `project, targetTcpProxy` | Deletes the specified TargetTcpProxy resource. |
| `set_backend_service` | `EXEC` | `project, targetTcpProxy` | Changes the BackendService for TargetTcpProxy. |
| `set_proxy_header` | `EXEC` | `project, targetTcpProxy` | Changes the ProxyHeaderType for TargetTcpProxy. |
