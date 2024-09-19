---
title: region_target_tcp_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - region_target_tcp_proxies
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

Creates, updates, deletes, gets or lists a <code>region_target_tcp_proxies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_target_tcp_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_target_tcp_proxies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#targetTcpProxy for target TCP proxies. |
| <CopyableCode code="proxyBind" /> | `boolean` | This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set to INTERNAL_SELF_MANAGED. When this field is set to true, Envoy proxies set up inbound traffic interception and bind to the IP address and port specified in the forwarding rule. This is generally useful when using Traffic Director to configure Envoy as a gateway or middle proxy (in other words, not a sidecar proxy). The Envoy proxy listens for inbound requests and handles requests when it receives them. The default is false. |
| <CopyableCode code="proxyHeader" /> | `string` | Specifies the type of proxy header to append before sending data to the backend, either NONE or PROXY_V1. The default is NONE. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the regional TCP proxy resides. This field is not applicable to global TCP proxy. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="service" /> | `string` | URL to the BackendService resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, region, targetTcpProxy" /> | Returns the specified TargetTcpProxy resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves a list of TargetTcpProxy resources available to the specified project in a given region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a TargetTcpProxy resource in the specified project and region using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, region, targetTcpProxy" /> | Deletes the specified TargetTcpProxy resource. |

## `SELECT` examples

Retrieves a list of TargetTcpProxy resources available to the specified project in a given region.

```sql
SELECT
id,
name,
description,
creationTimestamp,
kind,
proxyBind,
proxyHeader,
region,
selfLink,
service
FROM google.compute.region_target_tcp_proxies
WHERE project = '{{ project }}'
AND region = '{{ region }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_target_tcp_proxies</code> resource.

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
INSERT INTO google.compute.region_target_tcp_proxies (
project,
region,
name,
description,
service,
proxyHeader,
proxyBind,
region
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ name }}',
'{{ description }}',
'{{ service }}',
'{{ proxyHeader }}',
{{ proxyBind }},
'{{ region }}'
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
    - name: proxyHeader
      value: string
    - name: proxyBind
      value: boolean
    - name: region
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>region_target_tcp_proxies</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.region_target_tcp_proxies
WHERE project = '{{ project }}'
AND region = '{{ region }}'
AND targetTcpProxy = '{{ targetTcpProxy }}';
```
