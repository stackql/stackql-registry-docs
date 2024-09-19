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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>target_ssl_proxies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_ssl_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.target_ssl_proxies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="certificateMap" /> | `string` | URL of a certificate map that identifies a certificate map associated with the given target proxy. This field can only be set for global target proxies. If set, sslCertificates will be ignored. Accepted format is //certificatemanager.googleapis.com/projects/{project }/locations/{location}/certificateMaps/{resourceName}. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#targetSslProxy for target SSL proxies. |
| <CopyableCode code="proxyHeader" /> | `string` | Specifies the type of proxy header to append before sending data to the backend, either NONE or PROXY_V1. The default is NONE. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="service" /> | `string` | URL to the BackendService resource. |
| <CopyableCode code="sslCertificates" /> | `array` | URLs to SslCertificate resources that are used to authenticate connections to Backends. At least one SSL certificate must be specified. Currently, you may specify up to 15 SSL certificates. sslCertificates do not apply when the load balancing scheme is set to INTERNAL_SELF_MANAGED. |
| <CopyableCode code="sslPolicy" /> | `string` | URL of SslPolicy resource that will be associated with the TargetSslProxy resource. If not set, the TargetSslProxy resource will not have any SSL policy configured. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, targetSslProxy" /> | Returns the specified TargetSslProxy resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of TargetSslProxy resources available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a TargetSslProxy resource in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, targetSslProxy" /> | Deletes the specified TargetSslProxy resource. |
| <CopyableCode code="set_backend_service" /> | `EXEC` | <CopyableCode code="project, targetSslProxy" /> | Changes the BackendService for TargetSslProxy. |
| <CopyableCode code="set_certificate_map" /> | `EXEC` | <CopyableCode code="project, targetSslProxy" /> | Changes the Certificate Map for TargetSslProxy. |
| <CopyableCode code="set_proxy_header" /> | `EXEC` | <CopyableCode code="project, targetSslProxy" /> | Changes the ProxyHeaderType for TargetSslProxy. |
| <CopyableCode code="set_ssl_certificates" /> | `EXEC` | <CopyableCode code="project, targetSslProxy" /> | Changes SslCertificates for TargetSslProxy. |
| <CopyableCode code="set_ssl_policy" /> | `EXEC` | <CopyableCode code="project, targetSslProxy" /> | Sets the SSL policy for TargetSslProxy. The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the load balancer. They do not affect the connection between the load balancer and the backends. |

## `SELECT` examples

Retrieves the list of TargetSslProxy resources available to the specified project.

```sql
SELECT
id,
name,
description,
certificateMap,
creationTimestamp,
kind,
proxyHeader,
selfLink,
service,
sslCertificates,
sslPolicy
FROM google.compute.target_ssl_proxies
WHERE project = '{{ project }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>target_ssl_proxies</code> resource.

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
INSERT INTO google.compute.target_ssl_proxies (
project,
name,
description,
service,
sslCertificates,
certificateMap,
proxyHeader,
sslPolicy
)
SELECT 
'{{ project }}',
'{{ name }}',
'{{ description }}',
'{{ service }}',
'{{ sslCertificates }}',
'{{ certificateMap }}',
'{{ proxyHeader }}',
'{{ sslPolicy }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: id
      value: string
    - name: creationTimestamp
      value: string
    - name: name
      value: string
    - name: description
      value: string
    - name: selfLink
      value: string
    - name: service
      value: string
    - name: sslCertificates
      value:
        - string
    - name: certificateMap
      value: string
    - name: proxyHeader
      value: string
    - name: sslPolicy
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>target_ssl_proxies</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.target_ssl_proxies
WHERE project = '{{ project }}'
AND targetSslProxy = '{{ targetSslProxy }}';
```
