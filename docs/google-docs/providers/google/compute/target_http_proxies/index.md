---
title: target_http_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - target_http_proxies
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

Creates, updates, deletes, gets or lists a <code>target_http_proxies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_http_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.target_http_proxies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a TargetHttpProxy. An up-to-date fingerprint must be provided in order to patch/update the TargetHttpProxy; otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the TargetHttpProxy. |
| <CopyableCode code="httpKeepAliveTimeoutSec" /> | `integer` | Specifies how long to keep a connection open, after completing a response, while there is no matching traffic (in seconds). If an HTTP keep-alive is not specified, a default value (610 seconds) will be used. For global external Application Load Balancers, the minimum allowed value is 5 seconds and the maximum allowed value is 1200 seconds. For classic Application Load Balancers, this option is not supported. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of resource. Always compute#targetHttpProxy for target HTTP proxies. |
| <CopyableCode code="proxyBind" /> | `boolean` | This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set to INTERNAL_SELF_MANAGED. When this field is set to true, Envoy proxies set up inbound traffic interception and bind to the IP address and port specified in the forwarding rule. This is generally useful when using Traffic Director to configure Envoy as a gateway or middle proxy (in other words, not a sidecar proxy). The Envoy proxy listens for inbound requests and handles requests when it receives them. The default is false. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the regional Target HTTP Proxy resides. This field is not applicable to global Target HTTP Proxies. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="urlMap" /> | `string` | URL to the UrlMap resource that defines the mapping from URL to the BackendService. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, targetHttpProxy" /> | Returns the specified TargetHttpProxy resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of TargetHttpProxy resources available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a TargetHttpProxy resource in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, targetHttpProxy" /> | Deletes the specified TargetHttpProxy resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project, targetHttpProxy" /> | Patches the specified TargetHttpProxy resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
| <CopyableCode code="set_url_map" /> | `EXEC` | <CopyableCode code="project, targetHttpProxy" /> | Changes the URL map for TargetHttpProxy. |

## `SELECT` examples

Retrieves the list of TargetHttpProxy resources available to the specified project.

```sql
SELECT
id,
name,
description,
creationTimestamp,
fingerprint,
httpKeepAliveTimeoutSec,
kind,
proxyBind,
region,
selfLink,
urlMap
FROM google.compute.target_http_proxies
WHERE project = '{{ project }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>target_http_proxies</code> resource.

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
INSERT INTO google.compute.target_http_proxies (
project,
name,
description,
urlMap,
region,
proxyBind,
fingerprint,
httpKeepAliveTimeoutSec
)
SELECT 
'{{ project }}',
'{{ name }}',
'{{ description }}',
'{{ urlMap }}',
'{{ region }}',
{{ proxyBind }},
'{{ fingerprint }}',
'{{ httpKeepAliveTimeoutSec }}'
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
    - name: urlMap
      value: string
    - name: region
      value: string
    - name: proxyBind
      value: boolean
    - name: fingerprint
      value: string
    - name: httpKeepAliveTimeoutSec
      value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>target_http_proxies</code> resource.

```sql
/*+ update */
UPDATE google.compute.target_http_proxies
SET 
name = '{{ name }}',
description = '{{ description }}',
urlMap = '{{ urlMap }}',
region = '{{ region }}',
proxyBind = true|false,
fingerprint = '{{ fingerprint }}',
httpKeepAliveTimeoutSec = '{{ httpKeepAliveTimeoutSec }}'
WHERE 
project = '{{ project }}'
AND targetHttpProxy = '{{ targetHttpProxy }}';
```

## `DELETE` example

Deletes the specified <code>target_http_proxies</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.target_http_proxies
WHERE project = '{{ project }}'
AND targetHttpProxy = '{{ targetHttpProxy }}';
```
