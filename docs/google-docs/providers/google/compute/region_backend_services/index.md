---
title: region_backend_services
hide_title: false
hide_table_of_contents: false
keywords:
  - region_backend_services
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
<tr><td><b>Name</b></td><td><code>region_backend_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_backend_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `localityLbPolicies` | `array` | A list of locality load balancing policies to be used in order of preference. Either the policy or the customPolicy field should be set. Overrides any value set in the localityLbPolicy field. localityLbPolicies is only supported when the BackendService is referenced by a URL Map that is referenced by a target gRPC proxy that has the validateForProxyless field set to true. |
| `cdnPolicy` | `object` | Message containing Cloud CDN configuration for a backend service. |
| `region` | `string` | [Output Only] URL of the region where the regional backend service resides. This field is not applicable to global backend services. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `securitySettings` | `object` | The authentication and authorization settings for a BackendService. |
| `failoverPolicy` | `object` | For load balancers that have configurable failover: [Internal TCP/UDP Load Balancing](https://cloud.google.com/load-balancing/docs/internal/failover-overview) and [external TCP/UDP Load Balancing](https://cloud.google.com/load-balancing/docs/network/networklb-failover-overview). On failover or failback, this field indicates whether connection draining will be honored. Google Cloud has a fixed connection draining timeout of 10 minutes. A setting of true terminates existing TCP connections to the active pool during failover and failback, immediately draining traffic. A setting of false allows existing TCP connections to persist, even on VMs no longer in the active pool, for up to the duration of the connection draining timeout (10 minutes). |
| `customResponseHeaders` | `array` | Headers that the load balancer adds to proxied responses. See [Creating custom headers](https://cloud.google.com/load-balancing/docs/custom-headers). |
| `enableCDN` | `boolean` | If true, enables Cloud CDN for the backend service of an external HTTP(S) load balancer. |
| `logConfig` | `object` | The available logging options for the load balancer traffic served by this backend service. |
| `subsetting` | `object` | Subsetting configuration for this BackendService. Currently this is applicable only for Internal TCP/UDP load balancing, Internal HTTP(S) load balancing and Traffic Director. |
| `healthChecks` | `array` | The list of URLs to the healthChecks, httpHealthChecks (legacy), or httpsHealthChecks (legacy) resource for health checking this backend service. Not all backend services support legacy health checks. See Load balancer guide. Currently, at most one health check can be specified for each backend service. Backend services with instance group or zonal NEG backends must have a health check. Backend services with internet or serverless NEG backends must not have a health check. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `localityLbPolicy` | `string` | The load balancing algorithm used within the scope of the locality. The possible values are: - ROUND_ROBIN: This is a simple policy in which each healthy backend is selected in round robin order. This is the default. - LEAST_REQUEST: An O(1) algorithm which selects two random healthy hosts and picks the host which has fewer active requests. - RING_HASH: The ring/modulo hash load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a host from a set of N hosts only affects 1/N of the requests. - RANDOM: The load balancer selects a random healthy host. - ORIGINAL_DESTINATION: Backend host is selected based on the client connection metadata, i.e., connections are opened to the same address as the destination address of the incoming connection before the connection was redirected to the load balancer. - MAGLEV: used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash but has faster table lookup build times and host selection times. For more information about Maglev, see https://ai.google/research/pubs/pub44824 This field is applicable to either: - A regional backend service with the service_protocol set to HTTP, HTTPS, or HTTP2, and load_balancing_scheme set to INTERNAL_MANAGED. - A global backend service with the load_balancing_scheme set to INTERNAL_SELF_MANAGED. If sessionAffinity is not NONE, and this field is not set to MAGLEV or RING_HASH, session affinity settings will not take effect. Only ROUND_ROBIN and RING_HASH are supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true. |
| `connectionDraining` | `object` | Message containing connection draining configuration. |
| `sessionAffinity` | `string` | Type of session affinity to use. The default is NONE. Only NONE and HEADER_FIELD are supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true. For more details, see: [Session Affinity](https://cloud.google.com/load-balancing/docs/backend-service#session_affinity). |
| `circuitBreakers` | `object` | Settings controlling the volume of requests, connections and retries to this backend service. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a BackendService. An up-to-date fingerprint must be provided in order to update the BackendService, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a BackendService. |
| `backends` | `array` | The list of backends that serve this BackendService. |
| `port` | `integer` | Deprecated in favor of portName. The TCP port to connect on the backend. The default value is 80. For Internal TCP/UDP Load Balancing and Network Load Balancing, omit port. |
| `serviceBindings` | `array` | URLs of networkservices.ServiceBinding resources. Can only be set if load balancing scheme is INTERNAL_SELF_MANAGED. If set, lists of backends and health checks must be both empty. |
| `outlierDetection` | `object` | Settings controlling the eviction of unhealthy hosts from the load balancing pool for the backend service. |
| `portName` | `string` | A named port on a backend instance group representing the port for communication to the backend VMs in that group. The named port must be [defined on each backend instance group](https://cloud.google.com/load-balancing/docs/backend-service#named_ports). This parameter has no meaning if the backends are NEGs. For Internal TCP/UDP Load Balancing and Network Load Balancing, omit port_name. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#backendService for backend services. |
| `iap` | `object` | Identity-Aware Proxy |
| `connectionTrackingPolicy` | `object` | Connection Tracking configuration for this BackendService. |
| `maxStreamDuration` | `object` | A Duration represents a fixed-length span of time represented as a count of seconds and fractions of seconds at nanosecond resolution. It is independent of any calendar and concepts like "day" or "month". Range is approximately 10,000 years. |
| `consistentHash` | `object` | This message defines settings for a consistent hash style load balancer. |
| `protocol` | `string` | The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, SSL, UDP or GRPC. depending on the chosen load balancer or Traffic Director configuration. Refer to the documentation for the load balancers or for Traffic Director for more information. Must be set to GRPC when the backend service is referenced by a URL map that is bound to target gRPC proxy. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `affinityCookieTtlSec` | `integer` | Lifetime of cookies in seconds. This setting is applicable to external and internal HTTP(S) load balancers and Traffic Director and requires GENERATED_COOKIE or HTTP_COOKIE session affinity. If set to 0, the cookie is non-persistent and lasts only until the end of the browser session (or equivalent). The maximum allowed value is two weeks (1,209,600). Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true. |
| `loadBalancingScheme` | `string` | Specifies the load balancer type. A backend service created for one type of load balancer cannot be used with another. For more information, refer to Choosing a load balancer. |
| `customRequestHeaders` | `array` | Headers that the load balancer adds to proxied requests. See [Creating custom headers](https://cloud.google.com/load-balancing/docs/custom-headers). |
| `timeoutSec` | `integer` | The backend service timeout has a different meaning depending on the type of load balancer. For more information see, Backend service settings. The default is 30 seconds. The full range of timeout values allowed goes from 1 through 2,147,483,647 seconds. This value can be overridden in the PathMatcher configuration of the UrlMap that references this backend service. Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true. Instead, use maxStreamDuration. |
| `edgeSecurityPolicy` | `string` | [Output Only] The resource URL for the edge security policy associated with this backend service. |
| `securityPolicy` | `string` | [Output Only] The resource URL for the security policy associated with this backend service. |
| `network` | `string` | The URL of the network to which this backend service belongs. This field can only be specified when the load balancing scheme is set to INTERNAL. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `regionBackendServices_get` | `SELECT` | `backendService, project, region` | Returns the specified regional BackendService resource. |
| `regionBackendServices_list` | `SELECT` | `project, region` | Retrieves the list of regional BackendService resources available to the specified project in the given region. |
| `regionBackendServices_insert` | `INSERT` | `project, region` | Creates a regional BackendService resource in the specified project using the data included in the request. For more information, see Backend services overview. |
| `regionBackendServices_delete` | `DELETE` | `backendService, project, region` | Deletes the specified regional BackendService resource. |
| `regionBackendServices_patch` | `EXEC` | `backendService, project, region` | Updates the specified regional BackendService resource with the data included in the request. For more information, see Understanding backend services This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| `regionBackendServices_update` | `EXEC` | `backendService, project, region` | Updates the specified regional BackendService resource with the data included in the request. For more information, see Backend services overview . |
