---
title: target_ssl_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - target_ssl_proxies
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
<tr><td><b>Name</b></td><td><code>target_ssl_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.target_ssl_proxies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `certificateMap` | `string` | URL of a certificate map that identifies a certificate map associated with the given target proxy. This field can only be set for global target proxies. If set, sslCertificates will be ignored. Accepted format is //certificatemanager.googleapis.com/projects/&#123;project &#125;/locations/&#123;location&#125;/certificateMaps/&#123;resourceName&#125;. |
| `proxyHeader` | `string` | Specifies the type of proxy header to append before sending data to the backend, either NONE or PROXY_V1. The default is NONE. |
| `sslPolicy` | `string` | URL of SslPolicy resource that will be associated with the TargetSslProxy resource. If not set, the TargetSslProxy resource will not have any SSL policy configured. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `sslCertificates` | `array` | URLs to SslCertificate resources that are used to authenticate connections to Backends. At least one SSL certificate must be specified. Currently, you may specify up to 15 SSL certificates. sslCertificates do not apply when the load balancing scheme is set to INTERNAL_SELF_MANAGED. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#targetSslProxy for target SSL proxies. |
| `service` | `string` | URL to the BackendService resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project, targetSslProxy` | Returns the specified TargetSslProxy resource. |
| `list` | `SELECT` | `project` | Retrieves the list of TargetSslProxy resources available to the specified project. |
| `insert` | `INSERT` | `project` | Creates a TargetSslProxy resource in the specified project using the data included in the request. |
| `delete` | `DELETE` | `project, targetSslProxy` | Deletes the specified TargetSslProxy resource. |
| `set_backend_service` | `EXEC` | `project, targetSslProxy` | Changes the BackendService for TargetSslProxy. |
| `set_certificate_map` | `EXEC` | `project, targetSslProxy` | Changes the Certificate Map for TargetSslProxy. |
| `set_proxy_header` | `EXEC` | `project, targetSslProxy` | Changes the ProxyHeaderType for TargetSslProxy. |
| `set_ssl_certificates` | `EXEC` | `project, targetSslProxy` | Changes SslCertificates for TargetSslProxy. |
| `set_ssl_policy` | `EXEC` | `project, targetSslProxy` | Sets the SSL policy for TargetSslProxy. The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the SSL proxy load balancer. They do not affect the connection between the load balancer and the backends. |
