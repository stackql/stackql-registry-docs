---
title: target_https_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - target_https_proxies
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

Creates, updates, deletes or gets an <code>target_https_proxy</code> resource or lists <code>target_https_proxies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_https_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.target_https_proxies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="authorizationPolicy" /> | `string` | Optional. A URL referring to a networksecurity.AuthorizationPolicy resource that describes how the proxy should authorize inbound traffic. If left blank, access will not be restricted by an authorization policy. Refer to the AuthorizationPolicy resource for additional details. authorizationPolicy only applies to a global TargetHttpsProxy attached to globalForwardingRules with the loadBalancingScheme set to INTERNAL_SELF_MANAGED. Note: This field currently has no impact. |
| <CopyableCode code="certificateMap" /> | `string` | URL of a certificate map that identifies a certificate map associated with the given target proxy. This field can only be set for Global external Application Load Balancer or Classic Application Load Balancer. For other products use Certificate Manager Certificates instead. If set, sslCertificates will be ignored. Accepted format is //certificatemanager.googleapis.com/projects/{project }/locations/{location}/certificateMaps/{resourceName}. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a TargetHttpsProxy. An up-to-date fingerprint must be provided in order to patch the TargetHttpsProxy; otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the TargetHttpsProxy. |
| <CopyableCode code="httpKeepAliveTimeoutSec" /> | `integer` | Specifies how long to keep a connection open, after completing a response, while there is no matching traffic (in seconds). If an HTTP keep-alive is not specified, a default value (610 seconds) will be used. For global external Application Load Balancers, the minimum allowed value is 5 seconds and the maximum allowed value is 1200 seconds. For classic Application Load Balancers, this option is not supported. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of resource. Always compute#targetHttpsProxy for target HTTPS proxies. |
| <CopyableCode code="proxyBind" /> | `boolean` | This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set to INTERNAL_SELF_MANAGED. When this field is set to true, Envoy proxies set up inbound traffic interception and bind to the IP address and port specified in the forwarding rule. This is generally useful when using Traffic Director to configure Envoy as a gateway or middle proxy (in other words, not a sidecar proxy). The Envoy proxy listens for inbound requests and handles requests when it receives them. The default is false. |
| <CopyableCode code="quicOverride" /> | `string` | Specifies the QUIC override policy for this TargetHttpsProxy resource. This setting determines whether the load balancer attempts to negotiate QUIC with clients. You can specify NONE, ENABLE, or DISABLE. - When quic-override is set to NONE, Google manages whether QUIC is used. - When quic-override is set to ENABLE, the load balancer uses QUIC when possible. - When quic-override is set to DISABLE, the load balancer doesn't use QUIC. - If the quic-override flag is not specified, NONE is implied.  |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the regional TargetHttpsProxy resides. This field is not applicable to global TargetHttpsProxies. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="serverTlsPolicy" /> | `string` | Optional. A URL referring to a networksecurity.ServerTlsPolicy resource that describes how the proxy should authenticate inbound traffic. serverTlsPolicy only applies to a global TargetHttpsProxy attached to globalForwardingRules with the loadBalancingScheme set to INTERNAL_SELF_MANAGED or EXTERNAL or EXTERNAL_MANAGED. For details which ServerTlsPolicy resources are accepted with INTERNAL_SELF_MANAGED and which with EXTERNAL, EXTERNAL_MANAGED loadBalancingScheme consult ServerTlsPolicy documentation. If left blank, communications are not encrypted. |
| <CopyableCode code="sslCertificates" /> | `array` | URLs to SslCertificate resources that are used to authenticate connections between users and the load balancer. At least one SSL certificate must be specified. SslCertificates do not apply when the load balancing scheme is set to INTERNAL_SELF_MANAGED. The URLs should refer to a SSL Certificate resource or Certificate Manager Certificate resource. Mixing Classic Certificates and Certificate Manager Certificates is not allowed. Certificate Manager Certificates must include the certificatemanager API. Certificate Manager Certificates are not supported by Global external Application Load Balancer or Classic Application Load Balancer, use certificate_map instead. Currently, you may specify up to 15 Classic SSL Certificates. Certificate Manager Certificates accepted formats are: - //certificatemanager.googleapis.com/projects/{project}/locations/{ location}/certificates/{resourceName}. - https://certificatemanager.googleapis.com/v1alpha1/projects/{project }/locations/{location}/certificates/{resourceName}.  |
| <CopyableCode code="sslPolicy" /> | `string` | URL of SslPolicy resource that will be associated with the TargetHttpsProxy resource. If not set, the TargetHttpsProxy resource has no SSL policy configured. |
| <CopyableCode code="tlsEarlyData" /> | `string` |  Specifies whether TLS 1.3 0-RTT Data ("Early Data") should be accepted for this service. Early Data allows a TLS resumption handshake to include the initial application payload (a HTTP request) alongside the handshake, reducing the effective round trips to "zero". This applies to TLS 1.3 connections over TCP (HTTP/2) as well as over UDP (QUIC/h3). This can improve application performance, especially on networks where interruptions may be common, such as on mobile. Requests with Early Data will have the "Early-Data" HTTP header set on the request, with a value of "1", to allow the backend to determine whether Early Data was included. Note: TLS Early Data may allow requests to be replayed, as the data is sent to the backend before the handshake has fully completed. Applications that allow idempotent HTTP methods to make non-idempotent changes, such as a GET request updating a database, should not accept Early Data on those requests, and reject requests with the "Early-Data: 1" HTTP header by returning a HTTP 425 (Too Early) status code, in order to remain RFC compliant. The default value is DISABLED. |
| <CopyableCode code="urlMap" /> | `string` | A fully-qualified or valid partial URL to the UrlMap resource that defines the mapping from URL to the BackendService. For example, the following are all valid URLs for specifying a URL map: - https://www.googleapis.compute/v1/projects/project/global/urlMaps/ url-map - projects/project/global/urlMaps/url-map - global/urlMaps/url-map  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, targetHttpsProxy" /> | Returns the specified TargetHttpsProxy resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of TargetHttpsProxy resources available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a TargetHttpsProxy resource in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, targetHttpsProxy" /> | Deletes the specified TargetHttpsProxy resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project, targetHttpsProxy" /> | Patches the specified TargetHttpsProxy resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
| <CopyableCode code="set_certificate_map" /> | `EXEC` | <CopyableCode code="project, targetHttpsProxy" /> | Changes the Certificate Map for TargetHttpsProxy. |
| <CopyableCode code="set_quic_override" /> | `EXEC` | <CopyableCode code="project, targetHttpsProxy" /> | Sets the QUIC override policy for TargetHttpsProxy. |
| <CopyableCode code="set_ssl_certificates" /> | `EXEC` | <CopyableCode code="project, targetHttpsProxy" /> | Replaces SslCertificates for TargetHttpsProxy. |
| <CopyableCode code="set_ssl_policy" /> | `EXEC` | <CopyableCode code="project, targetHttpsProxy" /> | Sets the SSL policy for TargetHttpsProxy. The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the HTTPS proxy load balancer. They do not affect the connection between the load balancer and the backends. |
| <CopyableCode code="set_url_map" /> | `EXEC` | <CopyableCode code="project, targetHttpsProxy" /> | Changes the URL map for TargetHttpsProxy. |

## `SELECT` examples

Retrieves the list of TargetHttpsProxy resources available to the specified project.

```sql
SELECT
id,
name,
description,
authorizationPolicy,
certificateMap,
creationTimestamp,
fingerprint,
httpKeepAliveTimeoutSec,
kind,
proxyBind,
quicOverride,
region,
selfLink,
serverTlsPolicy,
sslCertificates,
sslPolicy,
tlsEarlyData,
urlMap
FROM google.compute.target_https_proxies
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>target_https_proxies</code> resource.

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
INSERT INTO google.compute.target_https_proxies (
project,
kind,
id,
creationTimestamp,
name,
description,
selfLink,
urlMap,
sslCertificates,
certificateMap,
quicOverride,
sslPolicy,
region,
proxyBind,
serverTlsPolicy,
authorizationPolicy,
fingerprint,
httpKeepAliveTimeoutSec,
tlsEarlyData
)
SELECT 
'{{ project }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ selfLink }}',
'{{ urlMap }}',
'{{ sslCertificates }}',
'{{ certificateMap }}',
'{{ quicOverride }}',
'{{ sslPolicy }}',
'{{ region }}',
true|false,
'{{ serverTlsPolicy }}',
'{{ authorizationPolicy }}',
'{{ fingerprint }}',
'{{ httpKeepAliveTimeoutSec }}',
'{{ tlsEarlyData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
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
      - name: urlMap
        value: '{{ urlMap }}'
      - name: sslCertificates
        value: '{{ sslCertificates }}'
      - name: certificateMap
        value: '{{ certificateMap }}'
      - name: quicOverride
        value: '{{ quicOverride }}'
      - name: sslPolicy
        value: '{{ sslPolicy }}'
      - name: region
        value: '{{ region }}'
      - name: proxyBind
        value: '{{ proxyBind }}'
      - name: serverTlsPolicy
        value: '{{ serverTlsPolicy }}'
      - name: authorizationPolicy
        value: '{{ authorizationPolicy }}'
      - name: fingerprint
        value: '{{ fingerprint }}'
      - name: httpKeepAliveTimeoutSec
        value: '{{ httpKeepAliveTimeoutSec }}'
      - name: tlsEarlyData
        value: '{{ tlsEarlyData }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a target_https_proxy only if the necessary resources are available.

```sql
UPDATE google.compute.target_https_proxies
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
selfLink = '{{ selfLink }}',
urlMap = '{{ urlMap }}',
sslCertificates = '{{ sslCertificates }}',
certificateMap = '{{ certificateMap }}',
quicOverride = '{{ quicOverride }}',
sslPolicy = '{{ sslPolicy }}',
region = '{{ region }}',
proxyBind = true|false,
serverTlsPolicy = '{{ serverTlsPolicy }}',
authorizationPolicy = '{{ authorizationPolicy }}',
fingerprint = '{{ fingerprint }}',
httpKeepAliveTimeoutSec = '{{ httpKeepAliveTimeoutSec }}',
tlsEarlyData = '{{ tlsEarlyData }}'
WHERE 
project = '{{ project }}'
AND targetHttpsProxy = '{{ targetHttpsProxy }}';
```

## `DELETE` example

Deletes the specified target_https_proxy resource.

```sql
DELETE FROM google.compute.target_https_proxies
WHERE project = '{{ project }}'
AND targetHttpsProxy = '{{ targetHttpsProxy }}';
```
