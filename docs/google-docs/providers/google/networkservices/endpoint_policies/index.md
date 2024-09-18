---
title: endpoint_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_policies
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

Creates, updates, deletes, gets or lists a <code>endpoint_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkservices.endpoint_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the EndpointPolicy resource. It matches pattern `projects/{project}/locations/global/endpointPolicies/{endpoint_policy}`. |
| <CopyableCode code="description" /> | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| <CopyableCode code="authorizationPolicy" /> | `string` | Optional. This field specifies the URL of AuthorizationPolicy resource that applies authorization policies to the inbound traffic at the matched endpoints. Refer to Authorization. If this field is not specified, authorization is disabled(no authz checks) for this endpoint. |
| <CopyableCode code="clientTlsPolicy" /> | `string` | Optional. A URL referring to a ClientTlsPolicy resource. ClientTlsPolicy can be set to specify the authentication for traffic from the proxy to the actual endpoints. More specifically, it is applied to the outgoing traffic from the proxy to the endpoint. This is typically used for sidecar model where the proxy identifies itself as endpoint to the control plane, with the connection between sidecar and endpoint requiring authentication. If this field is not set, authentication is disabled(open). Applicable only when EndpointPolicyType is SIDECAR_PROXY. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="endpointMatcher" /> | `object` | A definition of a matcher that selects endpoints to which the policies should be applied. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of label tags associated with the EndpointPolicy resource. |
| <CopyableCode code="serverTlsPolicy" /> | `string` | Optional. A URL referring to ServerTlsPolicy resource. ServerTlsPolicy is used to determine the authentication policy to be applied to terminate the inbound traffic at the identified backends. If this field is not set, authentication is disabled(open) for this endpoint. |
| <CopyableCode code="trafficPortSelector" /> | `object` | Specification of a port-based selector. |
| <CopyableCode code="type" /> | `string` | Required. The type of endpoint policy. This is primarily used to validate the configuration. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointPoliciesId, locationsId, projectsId" /> | Gets details of a single EndpointPolicy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists EndpointPolicies in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new EndpointPolicy in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointPoliciesId, locationsId, projectsId" /> | Deletes a single EndpointPolicy. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="endpointPoliciesId, locationsId, projectsId" /> | Updates the parameters of a single EndpointPolicy. |

## `SELECT` examples

Lists EndpointPolicies in a given project and location.

```sql
SELECT
name,
description,
authorizationPolicy,
clientTlsPolicy,
createTime,
endpointMatcher,
labels,
serverTlsPolicy,
trafficPortSelector,
type,
updateTime
FROM google.networkservices.endpoint_policies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoint_policies</code> resource.

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
INSERT INTO google.networkservices.endpoint_policies (
locationsId,
projectsId,
name,
labels,
type,
authorizationPolicy,
endpointMatcher,
trafficPortSelector,
description,
serverTlsPolicy,
clientTlsPolicy
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ labels }}',
'{{ type }}',
'{{ authorizationPolicy }}',
'{{ endpointMatcher }}',
'{{ trafficPortSelector }}',
'{{ description }}',
'{{ serverTlsPolicy }}',
'{{ clientTlsPolicy }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
createTime: string
updateTime: string
labels: object
type: string
authorizationPolicy: string
endpointMatcher:
  metadataLabelMatcher:
    metadataLabelMatchCriteria: string
    metadataLabels:
      - labelName: string
        labelValue: string
trafficPortSelector:
  ports:
    - type: string
description: string
serverTlsPolicy: string
clientTlsPolicy: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>endpoint_policies</code> resource.

```sql
/*+ update */
UPDATE google.networkservices.endpoint_policies
SET 
name = '{{ name }}',
labels = '{{ labels }}',
type = '{{ type }}',
authorizationPolicy = '{{ authorizationPolicy }}',
endpointMatcher = '{{ endpointMatcher }}',
trafficPortSelector = '{{ trafficPortSelector }}',
description = '{{ description }}',
serverTlsPolicy = '{{ serverTlsPolicy }}',
clientTlsPolicy = '{{ clientTlsPolicy }}'
WHERE 
endpointPoliciesId = '{{ endpointPoliciesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>endpoint_policies</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkservices.endpoint_policies
WHERE endpointPoliciesId = '{{ endpointPoliciesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
