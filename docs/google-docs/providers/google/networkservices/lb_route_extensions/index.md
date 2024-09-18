---
title: lb_route_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - lb_route_extensions
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

Creates, updates, deletes, gets or lists a <code>lb_route_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lb_route_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkservices.lb_route_extensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Identifier. Name of the `LbRouteExtension` resource in the following format: `projects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}`. |
| <CopyableCode code="description" /> | `string` | Optional. A human-readable description of the resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="extensionChains" /> | `array` | Required. A set of ordered extension chains that contain the match conditions and extensions to execute. Match conditions for each extension chain are evaluated in sequence for a given request. The first extension chain that has a condition that matches the request is executed. Any subsequent extension chains do not execute. Limited to 5 extension chains per resource. |
| <CopyableCode code="forwardingRules" /> | `array` | Required. A list of references to the forwarding rules to which this service extension is attached to. At least one forwarding rule is required. There can be only one `LbRouteExtension` resource per forwarding rule. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of labels associated with the `LbRouteExtension` resource. The format must comply with [the requirements for labels](https://cloud.google.com/compute/docs/labeling-resources#requirements) for Google Cloud resources. |
| <CopyableCode code="loadBalancingScheme" /> | `string` | Required. All backend services and forwarding rules referenced by this extension must share the same load balancing scheme. Supported values: `INTERNAL_MANAGED`, `EXTERNAL_MANAGED`. For more information, refer to [Choosing a load balancer](https://cloud.google.com/load-balancing/docs/backend-service). |
| <CopyableCode code="metadata" /> | `object` | Optional. The metadata provided here is included as part of the `metadata_context` (of type `google.protobuf.Struct`) in the `ProcessingRequest` message sent to the extension server. The metadata is available under the namespace `com.google.lb_route_extension.`. The following variables are supported in the metadata Struct: `{forwarding_rule_id}` - substituted with the forwarding rule's fully qualified resource name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="lbRouteExtensionsId, locationsId, projectsId" /> | Gets details of the specified `LbRouteExtension` resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists `LbRouteExtension` resources in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new `LbRouteExtension` resource in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="lbRouteExtensionsId, locationsId, projectsId" /> | Deletes the specified `LbRouteExtension` resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="lbRouteExtensionsId, locationsId, projectsId" /> | Updates the parameters of the specified `LbRouteExtension` resource. |

## `SELECT` examples

Lists `LbRouteExtension` resources in a given project and location.

```sql
SELECT
name,
description,
createTime,
extensionChains,
forwardingRules,
labels,
loadBalancingScheme,
metadata,
updateTime
FROM google.networkservices.lb_route_extensions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>lb_route_extensions</code> resource.

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
INSERT INTO google.networkservices.lb_route_extensions (
locationsId,
projectsId,
name,
description,
labels,
forwardingRules,
extensionChains,
loadBalancingScheme,
metadata
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ labels }}',
'{{ forwardingRules }}',
'{{ extensionChains }}',
'{{ loadBalancingScheme }}',
'{{ metadata }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
createTime: string
updateTime: string
description: string
labels: object
forwardingRules:
  - type: string
extensionChains:
  - name: string
    matchCondition:
      celExpression: string
    extensions:
      - name: string
        authority: string
        service: string
        supportedEvents:
          - type: string
            enumDescriptions: string
            enum: string
        timeout: string
        failOpen: boolean
        forwardHeaders:
          - type: string
loadBalancingScheme: string
metadata: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>lb_route_extensions</code> resource.

```sql
/*+ update */
UPDATE google.networkservices.lb_route_extensions
SET 
name = '{{ name }}',
description = '{{ description }}',
labels = '{{ labels }}',
forwardingRules = '{{ forwardingRules }}',
extensionChains = '{{ extensionChains }}',
loadBalancingScheme = '{{ loadBalancingScheme }}',
metadata = '{{ metadata }}'
WHERE 
lbRouteExtensionsId = '{{ lbRouteExtensionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>lb_route_extensions</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkservices.lb_route_extensions
WHERE lbRouteExtensionsId = '{{ lbRouteExtensionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
