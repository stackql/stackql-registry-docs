---
title: target_grpc_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - target_grpc_proxies
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

Creates, updates, deletes, gets or lists a <code>target_grpc_proxies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_grpc_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.target_grpc_proxies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource type. The server generates this identifier. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a TargetGrpcProxy. An up-to-date fingerprint must be provided in order to patch/update the TargetGrpcProxy; otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the TargetGrpcProxy. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#targetGrpcProxy for target grpc proxies. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="selfLinkWithId" /> | `string` | [Output Only] Server-defined URL with id for the resource. |
| <CopyableCode code="urlMap" /> | `string` | URL to the UrlMap resource that defines the mapping from URL to the BackendService. The protocol field in the BackendService must be set to GRPC. |
| <CopyableCode code="validateForProxyless" /> | `boolean` | If true, indicates that the BackendServices referenced by the urlMap may be accessed by gRPC applications without using a sidecar proxy. This will enable configuration checks on urlMap and its referenced BackendServices to not allow unsupported features. A gRPC application must use "xds:///" scheme in the target URI of the service it is connecting to. If false, indicates that the BackendServices referenced by the urlMap will be accessed by gRPC applications via a sidecar proxy. In this case, a gRPC application must not use "xds:///" scheme in the target URI of the service it is connecting to |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, targetGrpcProxy" /> | Returns the specified TargetGrpcProxy resource in the given scope. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Lists the TargetGrpcProxies for a project in the given scope. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a TargetGrpcProxy in the specified project in the given scope using the parameters that are included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, targetGrpcProxy" /> | Deletes the specified TargetGrpcProxy in the given scope |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project, targetGrpcProxy" /> | Patches the specified TargetGrpcProxy resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |

## `SELECT` examples

Lists the TargetGrpcProxies for a project in the given scope.

```sql
SELECT
id,
name,
description,
creationTimestamp,
fingerprint,
kind,
selfLink,
selfLinkWithId,
urlMap,
validateForProxyless
FROM google.compute.target_grpc_proxies
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>target_grpc_proxies</code> resource.

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
INSERT INTO google.compute.target_grpc_proxies (
project,
kind,
id,
creationTimestamp,
name,
description,
selfLink,
selfLinkWithId,
urlMap,
validateForProxyless,
fingerprint
)
SELECT 
'{{ project }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ selfLink }}',
'{{ selfLinkWithId }}',
'{{ urlMap }}',
true|false,
'{{ fingerprint }}'
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
    - name: selfLinkWithId
      value: '{{ selfLinkWithId }}'
    - name: urlMap
      value: '{{ urlMap }}'
    - name: validateForProxyless
      value: '{{ validateForProxyless }}'
    - name: fingerprint
      value: '{{ fingerprint }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>target_grpc_proxies</code> resource.

```sql
/*+ update */
UPDATE google.compute.target_grpc_proxies
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
selfLink = '{{ selfLink }}',
selfLinkWithId = '{{ selfLinkWithId }}',
urlMap = '{{ urlMap }}',
validateForProxyless = true|false,
fingerprint = '{{ fingerprint }}'
WHERE 
project = '{{ project }}'
AND targetGrpcProxy = '{{ targetGrpcProxy }}';
```

## `DELETE` example

Deletes the specified <code>target_grpc_proxies</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.target_grpc_proxies
WHERE project = '{{ project }}'
AND targetGrpcProxy = '{{ targetGrpcProxy }}';
```
