---
title: lb_traffic_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - lb_traffic_extensions
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

Creates, updates, deletes, gets or lists a <code>lb_traffic_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lb_traffic_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkservices.lb_traffic_extensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Identifier. Name of the `LbTrafficExtension` resource in the following format: `projects/{project}/locations/{location}/lbTrafficExtensions/{lb_traffic_extension}`. |
| <CopyableCode code="description" /> | `string` | Optional. A human-readable description of the resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="extensionChains" /> | `array` | Required. A set of ordered extension chains that contain the match conditions and extensions to execute. Match conditions for each extension chain are evaluated in sequence for a given request. The first extension chain that has a condition that matches the request is executed. Any subsequent extension chains do not execute. Limited to 5 extension chains per resource. |
| <CopyableCode code="forwardingRules" /> | `array` | Required. A list of references to the forwarding rules to which this service extension is attached to. At least one forwarding rule is required. There can be only one `LBTrafficExtension` resource per forwarding rule. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of labels associated with the `LbTrafficExtension` resource. The format must comply with [the requirements for labels](https://cloud.google.com/compute/docs/labeling-resources#requirements) for Google Cloud resources. |
| <CopyableCode code="loadBalancingScheme" /> | `string` | Required. All backend services and forwarding rules referenced by this extension must share the same load balancing scheme. Supported values: `INTERNAL_MANAGED`, `EXTERNAL_MANAGED`. For more information, refer to [Choosing a load balancer](https://cloud.google.com/load-balancing/docs/backend-service). |
| <CopyableCode code="metadata" /> | `object` | Optional. The metadata provided here is included in the `ProcessingRequest.metadata_context.filter_metadata` map field. The metadata is available under the key `com.google.lb_traffic_extension.`. The following variables are supported in the metadata: `{forwarding_rule_id}` - substituted with the forwarding rule's fully qualified resource name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="lbTrafficExtensionsId, locationsId, projectsId" /> | Gets details of the specified `LbTrafficExtension` resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists `LbTrafficExtension` resources in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new `LbTrafficExtension` resource in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="lbTrafficExtensionsId, locationsId, projectsId" /> | Deletes the specified `LbTrafficExtension` resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="lbTrafficExtensionsId, locationsId, projectsId" /> | Updates the parameters of the specified `LbTrafficExtension` resource. |

## `SELECT` examples

Lists `LbTrafficExtension` resources in a given project and location.

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
FROM google.networkservices.lb_traffic_extensions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>lb_traffic_extensions</code> resource.

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
INSERT INTO google.networkservices.lb_traffic_extensions (
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
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: labels
      value: '{{ labels }}'
    - name: forwardingRules
      value:
        - name: type
          value: '{{ type }}'
    - name: extensionChains
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: loadBalancingScheme
      value: '{{ loadBalancingScheme }}'
    - name: metadata
      value: '{{ metadata }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>lb_traffic_extensions</code> resource.

```sql
/*+ update */
UPDATE google.networkservices.lb_traffic_extensions
SET 
name = '{{ name }}',
description = '{{ description }}',
labels = '{{ labels }}',
forwardingRules = '{{ forwardingRules }}',
extensionChains = '{{ extensionChains }}',
loadBalancingScheme = '{{ loadBalancingScheme }}',
metadata = '{{ metadata }}'
WHERE 
lbTrafficExtensionsId = '{{ lbTrafficExtensionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>lb_traffic_extensions</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkservices.lb_traffic_extensions
WHERE lbTrafficExtensionsId = '{{ lbTrafficExtensionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
