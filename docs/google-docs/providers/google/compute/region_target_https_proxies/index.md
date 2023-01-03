---
title: region_target_https_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - region_target_https_proxies
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
<tr><td><b>Name</b></td><td><code>region_target_https_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_target_https_proxies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a TargetHttpsProxy. An up-to-date fingerprint must be provided in order to patch the TargetHttpsProxy; otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the TargetHttpsProxy. |
| `urlMap` | `string` | A fully-qualified or valid partial URL to the UrlMap resource that defines the mapping from URL to the BackendService. For example, the following are all valid URLs for specifying a URL map: - https://www.googleapis.compute/v1/projects/project/global/urlMaps/ url-map - projects/project/global/urlMaps/url-map - global/urlMaps/url-map  |
| `sslPolicy` | `string` | URL of SslPolicy resource that will be associated with the TargetHttpsProxy resource. If not set, the TargetHttpsProxy resource has no SSL policy configured. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `sslCertificates` | `array` | URLs to SslCertificate resources that are used to authenticate connections between users and the load balancer. At least one SSL certificate must be specified. Currently, you may specify up to 15 SSL certificates. sslCertificates do not apply when the load balancing scheme is set to INTERNAL_SELF_MANAGED. |
| `proxyBind` | `boolean` | This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set to INTERNAL_SELF_MANAGED. When this field is set to true, Envoy proxies set up inbound traffic interception and bind to the IP address and port specified in the forwarding rule. This is generally useful when using Traffic Director to configure Envoy as a gateway or middle proxy (in other words, not a sidecar proxy). The Envoy proxy listens for inbound requests and handles requests when it receives them. The default is false. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#targetHttpsProxy for target HTTPS proxies. |
| `serverTlsPolicy` | `string` | Optional. A URL referring to a networksecurity.ServerTlsPolicy resource that describes how the proxy should authenticate inbound traffic. serverTlsPolicy only applies to a global TargetHttpsProxy attached to globalForwardingRules with the loadBalancingScheme set to INTERNAL_SELF_MANAGED. If left blank, communications are not encrypted. Note: This field currently has no impact. |
| `quicOverride` | `string` | Specifies the QUIC override policy for this TargetHttpsProxy resource. This setting determines whether the load balancer attempts to negotiate QUIC with clients. You can specify NONE, ENABLE, or DISABLE. - When quic-override is set to NONE, Google manages whether QUIC is used. - When quic-override is set to ENABLE, the load balancer uses QUIC when possible. - When quic-override is set to DISABLE, the load balancer doesn't use QUIC. - If the quic-override flag is not specified, NONE is implied.  |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `region` | `string` | [Output Only] URL of the region where the regional TargetHttpsProxy resides. This field is not applicable to global TargetHttpsProxies. |
| `certificateMap` | `string` | URL of a certificate map that identifies a certificate map associated with the given target proxy. This field can only be set for global target proxies. If set, sslCertificates will be ignored. |
| `authorizationPolicy` | `string` | Optional. A URL referring to a networksecurity.AuthorizationPolicy resource that describes how the proxy should authorize inbound traffic. If left blank, access will not be restricted by an authorization policy. Refer to the AuthorizationPolicy resource for additional details. authorizationPolicy only applies to a global TargetHttpsProxy attached to globalForwardingRules with the loadBalancingScheme set to INTERNAL_SELF_MANAGED. Note: This field currently has no impact. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `regionTargetHttpsProxies_get` | `SELECT` | `project, region, targetHttpsProxy` | Returns the specified TargetHttpsProxy resource in the specified region. Gets a list of available target HTTP proxies by making a list() request. |
| `regionTargetHttpsProxies_list` | `SELECT` | `project, region` | Retrieves the list of TargetHttpsProxy resources available to the specified project in the specified region. |
| `regionTargetHttpsProxies_insert` | `INSERT` | `project, region` | Creates a TargetHttpsProxy resource in the specified project and region using the data included in the request. |
| `regionTargetHttpsProxies_delete` | `DELETE` | `project, region, targetHttpsProxy` | Deletes the specified TargetHttpsProxy resource. |
| `regionTargetHttpsProxies_patch` | `EXEC` | `project, region, targetHttpsProxy` | Patches the specified regional TargetHttpsProxy resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
| `regionTargetHttpsProxies_setSslCertificates` | `EXEC` | `project, region, targetHttpsProxy` | Replaces SslCertificates for TargetHttpsProxy. |
| `regionTargetHttpsProxies_setUrlMap` | `EXEC` | `project, region, targetHttpsProxy` | Changes the URL map for TargetHttpsProxy. |
