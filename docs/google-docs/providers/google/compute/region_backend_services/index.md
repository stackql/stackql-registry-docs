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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>region_backend_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_backend_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_backend_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="affinityCookieTtlSec" /> | `integer` | Lifetime of cookies in seconds. This setting is applicable to Application Load Balancers and Traffic Director and requires GENERATED_COOKIE or HTTP_COOKIE session affinity. If set to 0, the cookie is non-persistent and lasts only until the end of the browser session (or equivalent). The maximum allowed value is two weeks (1,209,600). Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true. |
| <CopyableCode code="backends" /> | `array` | The list of backends that serve this BackendService. |
| <CopyableCode code="cdnPolicy" /> | `object` | Message containing Cloud CDN configuration for a backend service. |
| <CopyableCode code="circuitBreakers" /> | `object` | Settings controlling the volume of requests, connections and retries to this backend service. |
| <CopyableCode code="compressionMode" /> | `string` | Compress text responses using Brotli or gzip compression, based on the client's Accept-Encoding header. |
| <CopyableCode code="connectionDraining" /> | `object` | Message containing connection draining configuration. |
| <CopyableCode code="connectionTrackingPolicy" /> | `object` | Connection Tracking configuration for this BackendService. |
| <CopyableCode code="consistentHash" /> | `object` | This message defines settings for a consistent hash style load balancer. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="customRequestHeaders" /> | `array` | Headers that the load balancer adds to proxied requests. See [Creating custom headers](https://cloud.google.com/load-balancing/docs/custom-headers). |
| <CopyableCode code="customResponseHeaders" /> | `array` | Headers that the load balancer adds to proxied responses. See [Creating custom headers](https://cloud.google.com/load-balancing/docs/custom-headers). |
| <CopyableCode code="edgeSecurityPolicy" /> | `string` | [Output Only] The resource URL for the edge security policy associated with this backend service. |
| <CopyableCode code="enableCDN" /> | `boolean` | If true, enables Cloud CDN for the backend service of a global external Application Load Balancer. |
| <CopyableCode code="failoverPolicy" /> | `object` | For load balancers that have configurable failover: [Internal passthrough Network Load Balancers](https://cloud.google.com/load-balancing/docs/internal/failover-overview) and [external passthrough Network Load Balancers](https://cloud.google.com/load-balancing/docs/network/networklb-failover-overview). On failover or failback, this field indicates whether connection draining will be honored. Google Cloud has a fixed connection draining timeout of 10 minutes. A setting of true terminates existing TCP connections to the active pool during failover and failback, immediately draining traffic. A setting of false allows existing TCP connections to persist, even on VMs no longer in the active pool, for up to the duration of the connection draining timeout (10 minutes). |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a BackendService. An up-to-date fingerprint must be provided in order to update the BackendService, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a BackendService. |
| <CopyableCode code="healthChecks" /> | `array` | The list of URLs to the healthChecks, httpHealthChecks (legacy), or httpsHealthChecks (legacy) resource for health checking this backend service. Not all backend services support legacy health checks. See Load balancer guide. Currently, at most one health check can be specified for each backend service. Backend services with instance group or zonal NEG backends must have a health check. Backend services with internet or serverless NEG backends must not have a health check. |
| <CopyableCode code="iap" /> | `object` | Identity-Aware Proxy |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of resource. Always compute#backendService for backend services. |
| <CopyableCode code="loadBalancingScheme" /> | `string` | Specifies the load balancer type. A backend service created for one type of load balancer cannot be used with another. For more information, refer to Choosing a load balancer. |
| <CopyableCode code="localityLbPolicies" /> | `array` | A list of locality load-balancing policies to be used in order of preference. When you use localityLbPolicies, you must set at least one value for either the localityLbPolicies[].policy or the localityLbPolicies[].customPolicy field. localityLbPolicies overrides any value set in the localityLbPolicy field. For an example of how to use this field, see Define a list of preferred policies. Caution: This field and its children are intended for use in a service mesh that includes gRPC clients only. Envoy proxies can't use backend services that have this configuration. |
| <CopyableCode code="localityLbPolicy" /> | `string` | The load balancing algorithm used within the scope of the locality. The possible values are: - ROUND_ROBIN: This is a simple policy in which each healthy backend is selected in round robin order. This is the default. - LEAST_REQUEST: An O(1) algorithm which selects two random healthy hosts and picks the host which has fewer active requests. - RING_HASH: The ring/modulo hash load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a host from a set of N hosts only affects 1/N of the requests. - RANDOM: The load balancer selects a random healthy host. - ORIGINAL_DESTINATION: Backend host is selected based on the client connection metadata, i.e., connections are opened to the same address as the destination address of the incoming connection before the connection was redirected to the load balancer. - MAGLEV: used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash but has faster table lookup build times and host selection times. For more information about Maglev, see https://ai.google/research/pubs/pub44824 This field is applicable to either: - A regional backend service with the service_protocol set to HTTP, HTTPS, or HTTP2, and load_balancing_scheme set to INTERNAL_MANAGED. - A global backend service with the load_balancing_scheme set to INTERNAL_SELF_MANAGED, INTERNAL_MANAGED, or EXTERNAL_MANAGED. If sessionAffinity is not configured—that is, if session affinity remains at the default value of NONE—then the default value for localityLbPolicy is ROUND_ROBIN. If session affinity is set to a value other than NONE, then the default value for localityLbPolicy is MAGLEV. Only ROUND_ROBIN and RING_HASH are supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true. |
| <CopyableCode code="logConfig" /> | `object` | The available logging options for the load balancer traffic served by this backend service. |
| <CopyableCode code="maxStreamDuration" /> | `object` | A Duration represents a fixed-length span of time represented as a count of seconds and fractions of seconds at nanosecond resolution. It is independent of any calendar and concepts like "day" or "month". Range is approximately 10,000 years. |
| <CopyableCode code="metadatas" /> | `object` | Deployment metadata associated with the resource to be set by a GKE hub controller and read by the backend RCTH |
| <CopyableCode code="network" /> | `string` | The URL of the network to which this backend service belongs. This field can only be specified when the load balancing scheme is set to INTERNAL. |
| <CopyableCode code="outlierDetection" /> | `object` | Settings controlling the eviction of unhealthy hosts from the load balancing pool for the backend service. |
| <CopyableCode code="port" /> | `integer` | Deprecated in favor of portName. The TCP port to connect on the backend. The default value is 80. For internal passthrough Network Load Balancers and external passthrough Network Load Balancers, omit port. |
| <CopyableCode code="portName" /> | `string` | A named port on a backend instance group representing the port for communication to the backend VMs in that group. The named port must be [defined on each backend instance group](https://cloud.google.com/load-balancing/docs/backend-service#named_ports). This parameter has no meaning if the backends are NEGs. For internal passthrough Network Load Balancers and external passthrough Network Load Balancers, omit port_name. |
| <CopyableCode code="protocol" /> | `string` | The protocol this BackendService uses to communicate with backends. Possible values are HTTP, HTTPS, HTTP2, TCP, SSL, UDP or GRPC. depending on the chosen load balancer or Traffic Director configuration. Refer to the documentation for the load balancers or for Traffic Director for more information. Must be set to GRPC when the backend service is referenced by a URL map that is bound to target gRPC proxy. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the regional backend service resides. This field is not applicable to global backend services. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| <CopyableCode code="securityPolicy" /> | `string` | [Output Only] The resource URL for the security policy associated with this backend service. |
| <CopyableCode code="securitySettings" /> | `object` | The authentication and authorization settings for a BackendService. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="serviceBindings" /> | `array` | URLs of networkservices.ServiceBinding resources. Can only be set if load balancing scheme is INTERNAL_SELF_MANAGED. If set, lists of backends and health checks must be both empty. |
| <CopyableCode code="serviceLbPolicy" /> | `string` | URL to networkservices.ServiceLbPolicy resource. Can only be set if load balancing scheme is EXTERNAL, EXTERNAL_MANAGED, INTERNAL_MANAGED or INTERNAL_SELF_MANAGED and the scope is global. |
| <CopyableCode code="sessionAffinity" /> | `string` | Type of session affinity to use. The default is NONE. Only NONE and HEADER_FIELD are supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true. For more details, see: [Session Affinity](https://cloud.google.com/load-balancing/docs/backend-service#session_affinity). |
| <CopyableCode code="subsetting" /> | `object` | Subsetting configuration for this BackendService. Currently this is applicable only for Internal TCP/UDP load balancing, Internal HTTP(S) load balancing and Traffic Director. |
| <CopyableCode code="timeoutSec" /> | `integer` | The backend service timeout has a different meaning depending on the type of load balancer. For more information see, Backend service settings. The default is 30 seconds. The full range of timeout values allowed goes from 1 through 2,147,483,647 seconds. This value can be overridden in the PathMatcher configuration of the UrlMap that references this backend service. Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true. Instead, use maxStreamDuration. |
| <CopyableCode code="usedBy" /> | `array` | [Output Only] List of resources referencing given backend service. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backendService, project, region" /> | Returns the specified regional BackendService resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves the list of regional BackendService resources available to the specified project in the given region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a regional BackendService resource in the specified project using the data included in the request. For more information, see Backend services overview. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backendService, project, region" /> | Deletes the specified regional BackendService resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="backendService, project, region" /> | Updates the specified regional BackendService resource with the data included in the request. For more information, see Understanding backend services This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="backendService, project, region" /> | Updates the specified regional BackendService resource with the data included in the request. For more information, see Backend services overview . |
| <CopyableCode code="set_security_policy" /> | `EXEC` | <CopyableCode code="backendService, project, region" /> | Sets the Google Cloud Armor security policy for the specified backend service. For more information, see Google Cloud Armor Overview |

## `SELECT` examples

Retrieves the list of regional BackendService resources available to the specified project in the given region.

```sql
SELECT
id,
name,
description,
affinityCookieTtlSec,
backends,
cdnPolicy,
circuitBreakers,
compressionMode,
connectionDraining,
connectionTrackingPolicy,
consistentHash,
creationTimestamp,
customRequestHeaders,
customResponseHeaders,
edgeSecurityPolicy,
enableCDN,
failoverPolicy,
fingerprint,
healthChecks,
iap,
kind,
loadBalancingScheme,
localityLbPolicies,
localityLbPolicy,
logConfig,
maxStreamDuration,
metadatas,
network,
outlierDetection,
port,
portName,
protocol,
region,
securityPolicy,
securitySettings,
selfLink,
serviceBindings,
serviceLbPolicy,
sessionAffinity,
subsetting,
timeoutSec,
usedBy
FROM google.compute.region_backend_services
WHERE project = '{{ project }}'
AND region = '{{ region }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_backend_services</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.compute.region_backend_services (
project,
region,
kind,
id,
creationTimestamp,
name,
description,
selfLink,
backends,
healthChecks,
timeoutSec,
port,
protocol,
fingerprint,
portName,
enableCDN,
sessionAffinity,
affinityCookieTtlSec,
region,
failoverPolicy,
loadBalancingScheme,
connectionDraining,
iap,
cdnPolicy,
customRequestHeaders,
customResponseHeaders,
securityPolicy,
edgeSecurityPolicy,
logConfig,
securitySettings,
localityLbPolicy,
consistentHash,
circuitBreakers,
outlierDetection,
network,
subsetting,
connectionTrackingPolicy,
maxStreamDuration,
compressionMode,
serviceLbPolicy,
serviceBindings,
localityLbPolicies,
metadatas,
usedBy
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ selfLink }}',
'{{ backends }}',
'{{ healthChecks }}',
'{{ timeoutSec }}',
'{{ port }}',
'{{ protocol }}',
'{{ fingerprint }}',
'{{ portName }}',
true|false,
'{{ sessionAffinity }}',
'{{ affinityCookieTtlSec }}',
'{{ region }}',
'{{ failoverPolicy }}',
'{{ loadBalancingScheme }}',
'{{ connectionDraining }}',
'{{ iap }}',
'{{ cdnPolicy }}',
'{{ customRequestHeaders }}',
'{{ customResponseHeaders }}',
'{{ securityPolicy }}',
'{{ edgeSecurityPolicy }}',
'{{ logConfig }}',
'{{ securitySettings }}',
'{{ localityLbPolicy }}',
'{{ consistentHash }}',
'{{ circuitBreakers }}',
'{{ outlierDetection }}',
'{{ network }}',
'{{ subsetting }}',
'{{ connectionTrackingPolicy }}',
'{{ maxStreamDuration }}',
'{{ compressionMode }}',
'{{ serviceLbPolicy }}',
'{{ serviceBindings }}',
'{{ localityLbPolicies }}',
'{{ metadatas }}',
'{{ usedBy }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: '{{ kind }}'
    - name: id
      value: '{{ id }}'
    - name: creationTimestamp
      value: '{{ creationTimestamp }}'
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: selfLink
      value: '{{ selfLink }}'
    - name: backends
      value: '{{ backends }}'
    - name: healthChecks
      value: '{{ healthChecks }}'
    - name: timeoutSec
      value: '{{ timeoutSec }}'
    - name: port
      value: '{{ port }}'
    - name: protocol
      value: '{{ protocol }}'
    - name: fingerprint
      value: '{{ fingerprint }}'
    - name: portName
      value: '{{ portName }}'
    - name: enableCDN
      value: '{{ enableCDN }}'
    - name: sessionAffinity
      value: '{{ sessionAffinity }}'
    - name: affinityCookieTtlSec
      value: '{{ affinityCookieTtlSec }}'
    - name: region
      value: '{{ region }}'
    - name: failoverPolicy
      value: '{{ failoverPolicy }}'
    - name: loadBalancingScheme
      value: '{{ loadBalancingScheme }}'
    - name: connectionDraining
      value: '{{ connectionDraining }}'
    - name: iap
      value: '{{ iap }}'
    - name: cdnPolicy
      value: '{{ cdnPolicy }}'
    - name: customRequestHeaders
      value: '{{ customRequestHeaders }}'
    - name: customResponseHeaders
      value: '{{ customResponseHeaders }}'
    - name: securityPolicy
      value: '{{ securityPolicy }}'
    - name: edgeSecurityPolicy
      value: '{{ edgeSecurityPolicy }}'
    - name: logConfig
      value: '{{ logConfig }}'
    - name: securitySettings
      value: '{{ securitySettings }}'
    - name: localityLbPolicy
      value: '{{ localityLbPolicy }}'
    - name: consistentHash
      value: '{{ consistentHash }}'
    - name: circuitBreakers
      value: '{{ circuitBreakers }}'
    - name: outlierDetection
      value: '{{ outlierDetection }}'
    - name: network
      value: '{{ network }}'
    - name: subsetting
      value: '{{ subsetting }}'
    - name: connectionTrackingPolicy
      value: '{{ connectionTrackingPolicy }}'
    - name: maxStreamDuration
      value: '{{ maxStreamDuration }}'
    - name: compressionMode
      value: '{{ compressionMode }}'
    - name: serviceLbPolicy
      value: '{{ serviceLbPolicy }}'
    - name: serviceBindings
      value: '{{ serviceBindings }}'
    - name: localityLbPolicies
      value: '{{ localityLbPolicies }}'
    - name: metadatas
      value: '{{ metadatas }}'
    - name: usedBy
      value: '{{ usedBy }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>region_backend_services</code> resource.

```sql
/*+ update */
UPDATE google.compute.region_backend_services
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
selfLink = '{{ selfLink }}',
backends = '{{ backends }}',
healthChecks = '{{ healthChecks }}',
timeoutSec = '{{ timeoutSec }}',
port = '{{ port }}',
protocol = '{{ protocol }}',
fingerprint = '{{ fingerprint }}',
portName = '{{ portName }}',
enableCDN = true|false,
sessionAffinity = '{{ sessionAffinity }}',
affinityCookieTtlSec = '{{ affinityCookieTtlSec }}',
region = '{{ region }}',
failoverPolicy = '{{ failoverPolicy }}',
loadBalancingScheme = '{{ loadBalancingScheme }}',
connectionDraining = '{{ connectionDraining }}',
iap = '{{ iap }}',
cdnPolicy = '{{ cdnPolicy }}',
customRequestHeaders = '{{ customRequestHeaders }}',
customResponseHeaders = '{{ customResponseHeaders }}',
securityPolicy = '{{ securityPolicy }}',
edgeSecurityPolicy = '{{ edgeSecurityPolicy }}',
logConfig = '{{ logConfig }}',
securitySettings = '{{ securitySettings }}',
localityLbPolicy = '{{ localityLbPolicy }}',
consistentHash = '{{ consistentHash }}',
circuitBreakers = '{{ circuitBreakers }}',
outlierDetection = '{{ outlierDetection }}',
network = '{{ network }}',
subsetting = '{{ subsetting }}',
connectionTrackingPolicy = '{{ connectionTrackingPolicy }}',
maxStreamDuration = '{{ maxStreamDuration }}',
compressionMode = '{{ compressionMode }}',
serviceLbPolicy = '{{ serviceLbPolicy }}',
serviceBindings = '{{ serviceBindings }}',
localityLbPolicies = '{{ localityLbPolicies }}',
metadatas = '{{ metadatas }}',
usedBy = '{{ usedBy }}'
WHERE 
backendService = '{{ backendService }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```

## `UPDATE` example

Replaces all fields in the specified <code>region_backend_services</code> resource.

```sql
/*+ update */
REPLACE google.compute.region_backend_services
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
selfLink = '{{ selfLink }}',
backends = '{{ backends }}',
healthChecks = '{{ healthChecks }}',
timeoutSec = '{{ timeoutSec }}',
port = '{{ port }}',
protocol = '{{ protocol }}',
fingerprint = '{{ fingerprint }}',
portName = '{{ portName }}',
enableCDN = true|false,
sessionAffinity = '{{ sessionAffinity }}',
affinityCookieTtlSec = '{{ affinityCookieTtlSec }}',
region = '{{ region }}',
failoverPolicy = '{{ failoverPolicy }}',
loadBalancingScheme = '{{ loadBalancingScheme }}',
connectionDraining = '{{ connectionDraining }}',
iap = '{{ iap }}',
cdnPolicy = '{{ cdnPolicy }}',
customRequestHeaders = '{{ customRequestHeaders }}',
customResponseHeaders = '{{ customResponseHeaders }}',
securityPolicy = '{{ securityPolicy }}',
edgeSecurityPolicy = '{{ edgeSecurityPolicy }}',
logConfig = '{{ logConfig }}',
securitySettings = '{{ securitySettings }}',
localityLbPolicy = '{{ localityLbPolicy }}',
consistentHash = '{{ consistentHash }}',
circuitBreakers = '{{ circuitBreakers }}',
outlierDetection = '{{ outlierDetection }}',
network = '{{ network }}',
subsetting = '{{ subsetting }}',
connectionTrackingPolicy = '{{ connectionTrackingPolicy }}',
maxStreamDuration = '{{ maxStreamDuration }}',
compressionMode = '{{ compressionMode }}',
serviceLbPolicy = '{{ serviceLbPolicy }}',
serviceBindings = '{{ serviceBindings }}',
localityLbPolicies = '{{ localityLbPolicies }}',
metadatas = '{{ metadatas }}',
usedBy = '{{ usedBy }}'
WHERE 
backendService = '{{ backendService }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```

## `DELETE` example

Deletes the specified <code>region_backend_services</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.region_backend_services
WHERE backendService = '{{ backendService }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
