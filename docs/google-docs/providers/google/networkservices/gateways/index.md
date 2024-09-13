---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
  - networkservices
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

Creates, updates, deletes or gets an <code>gateway</code> resource or lists <code>gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkservices.gateways" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the Gateway resource. It matches pattern `projects/*/locations/*/gateways/`. |
| <CopyableCode code="description" /> | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| <CopyableCode code="addresses" /> | `array` | Optional. Zero or one IPv4 or IPv6 address on which the Gateway will receive the traffic. When no address is provided, an IP from the subnetwork is allocated This field only applies to gateways of type 'SECURE_WEB_GATEWAY'. Gateways of type 'OPEN_MESH' listen on 0.0.0.0 for IPv4 and :: for IPv6. |
| <CopyableCode code="certificateUrls" /> | `array` | Optional. A fully-qualified Certificates URL reference. The proxy presents a Certificate (selected based on SNI) when establishing a TLS connection. This feature only applies to gateways of type 'SECURE_WEB_GATEWAY'. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="envoyHeaders" /> | `string` | Optional. Determines if envoy will insert internal debug headers into upstream requests. Other Envoy headers may still be injected. By default, envoy will not insert any debug headers. |
| <CopyableCode code="gatewaySecurityPolicy" /> | `string` | Optional. A fully-qualified GatewaySecurityPolicy URL reference. Defines how a server should apply security policy to inbound (VM to Proxy) initiated connections. For example: `projects/*/locations/*/gatewaySecurityPolicies/swg-policy`. This policy is specific to gateways of type 'SECURE_WEB_GATEWAY'. |
| <CopyableCode code="ipVersion" /> | `string` | Optional. The IP Version that will be used by this gateway. Valid options are IPV4 or IPV6. Default is IPV4. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of label tags associated with the Gateway resource. |
| <CopyableCode code="network" /> | `string` | Optional. The relative resource name identifying the VPC network that is using this configuration. For example: `projects/*/global/networks/network-1`. Currently, this field is specific to gateways of type 'SECURE_WEB_GATEWAY'. |
| <CopyableCode code="ports" /> | `array` | Required. One or more port numbers (1-65535), on which the Gateway will receive traffic. The proxy binds to the specified ports. Gateways of type 'SECURE_WEB_GATEWAY' are limited to 1 port. Gateways of type 'OPEN_MESH' listen on 0.0.0.0 for IPv4 and :: for IPv6 and support multiple ports. |
| <CopyableCode code="routingMode" /> | `string` | Optional. The routing mode of the Gateway. This field is configurable only for gateways of type SECURE_WEB_GATEWAY. This field is required for gateways of type SECURE_WEB_GATEWAY. |
| <CopyableCode code="scope" /> | `string` | Optional. Scope determines how configuration across multiple Gateway instances are merged. The configuration for multiple Gateway instances with the same scope will be merged as presented as a single coniguration to the proxy/load balancer. Max length 64 characters. Scope should start with a letter and can only have letters, numbers, hyphens. |
| <CopyableCode code="selfLink" /> | `string` | Output only. Server-defined URL of this resource |
| <CopyableCode code="serverTlsPolicy" /> | `string` | Optional. A fully-qualified ServerTLSPolicy URL reference. Specifies how TLS traffic is terminated. If empty, TLS termination is disabled. |
| <CopyableCode code="subnetwork" /> | `string` | Optional. The relative resource name identifying the subnetwork in which this SWG is allocated. For example: `projects/*/regions/us-central1/subnetworks/network-1` Currently, this field is specific to gateways of type 'SECURE_WEB_GATEWAY". |
| <CopyableCode code="type" /> | `string` | Immutable. The type of the customer managed gateway. This field is required. If unspecified, an error is returned. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewaysId, locationsId, projectsId" /> | Gets details of a single Gateway. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Gateways in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Gateway in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gatewaysId, locationsId, projectsId" /> | Deletes a single Gateway. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="gatewaysId, locationsId, projectsId" /> | Updates the parameters of a single Gateway. |

## `SELECT` examples

Lists Gateways in a given project and location.

```sql
SELECT
name,
description,
addresses,
certificateUrls,
createTime,
envoyHeaders,
gatewaySecurityPolicy,
ipVersion,
labels,
network,
ports,
routingMode,
scope,
selfLink,
serverTlsPolicy,
subnetwork,
type,
updateTime
FROM google.networkservices.gateways
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gateways</code> resource.

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
INSERT INTO google.networkservices.gateways (
locationsId,
projectsId,
name,
selfLink,
createTime,
updateTime,
labels,
description,
type,
addresses,
ports,
scope,
serverTlsPolicy,
certificateUrls,
gatewaySecurityPolicy,
network,
subnetwork,
ipVersion,
envoyHeaders,
routingMode
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ selfLink }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ description }}',
'{{ type }}',
'{{ addresses }}',
'{{ ports }}',
'{{ scope }}',
'{{ serverTlsPolicy }}',
'{{ certificateUrls }}',
'{{ gatewaySecurityPolicy }}',
'{{ network }}',
'{{ subnetwork }}',
'{{ ipVersion }}',
'{{ envoyHeaders }}',
'{{ routingMode }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: description
        value: '{{ description }}'
      - name: type
        value: '{{ type }}'
      - name: addresses
        value: '{{ addresses }}'
      - name: ports
        value: '{{ ports }}'
      - name: scope
        value: '{{ scope }}'
      - name: serverTlsPolicy
        value: '{{ serverTlsPolicy }}'
      - name: certificateUrls
        value: '{{ certificateUrls }}'
      - name: gatewaySecurityPolicy
        value: '{{ gatewaySecurityPolicy }}'
      - name: network
        value: '{{ network }}'
      - name: subnetwork
        value: '{{ subnetwork }}'
      - name: ipVersion
        value: '{{ ipVersion }}'
      - name: envoyHeaders
        value: '{{ envoyHeaders }}'
      - name: routingMode
        value: '{{ routingMode }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a gateway only if the necessary resources are available.

```sql
UPDATE google.networkservices.gateways
SET 
name = '{{ name }}',
selfLink = '{{ selfLink }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
description = '{{ description }}',
type = '{{ type }}',
addresses = '{{ addresses }}',
ports = '{{ ports }}',
scope = '{{ scope }}',
serverTlsPolicy = '{{ serverTlsPolicy }}',
certificateUrls = '{{ certificateUrls }}',
gatewaySecurityPolicy = '{{ gatewaySecurityPolicy }}',
network = '{{ network }}',
subnetwork = '{{ subnetwork }}',
ipVersion = '{{ ipVersion }}',
envoyHeaders = '{{ envoyHeaders }}',
routingMode = '{{ routingMode }}'
WHERE 
gatewaysId = '{{ gatewaysId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified gateway resource.

```sql
DELETE FROM google.networkservices.gateways
WHERE gatewaysId = '{{ gatewaysId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
