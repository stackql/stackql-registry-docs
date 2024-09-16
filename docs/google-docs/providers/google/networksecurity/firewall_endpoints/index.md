---
title: firewall_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_endpoints
  - networksecurity
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

Creates, updates, deletes, gets or lists a <code>firewall_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.firewall_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Identifier. name of resource |
| <CopyableCode code="description" /> | `string` | Optional. Description of the firewall endpoint. Max length 2048 characters. |
| <CopyableCode code="associatedNetworks" /> | `array` | Output only. List of networks that are associated with this endpoint in the local zone. This is a projection of the FirewallEndpointAssociations pointing at this endpoint. A network will only appear in this list after traffic routing is fully configured. Format: projects/{project}/global/networks/{name}. |
| <CopyableCode code="associations" /> | `array` | Output only. List of FirewallEndpointAssociations that are associated to this endpoint. An association will only appear in this list after traffic routing is fully configured. |
| <CopyableCode code="billingProjectId" /> | `string` | Required. Project to bill on endpoint uptime usage. |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time stamp |
| <CopyableCode code="labels" /> | `object` | Optional. Labels as key value pairs |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Whether reconciling is in progress, recommended per https://google.aip.dev/128. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the endpoint. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time stamp |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_firewall_endpoints_get" /> | `SELECT` | <CopyableCode code="firewallEndpointsId, locationsId, organizationsId" /> | Gets details of a single Endpoint. |
| <CopyableCode code="organizations_locations_firewall_endpoints_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists FirewallEndpoints in a given project and location. |
| <CopyableCode code="organizations_locations_firewall_endpoints_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a new FirewallEndpoint in a given project and location. |
| <CopyableCode code="organizations_locations_firewall_endpoints_delete" /> | `DELETE` | <CopyableCode code="firewallEndpointsId, locationsId, organizationsId" /> | Deletes a single Endpoint. |
| <CopyableCode code="organizations_locations_firewall_endpoints_patch" /> | `UPDATE` | <CopyableCode code="firewallEndpointsId, locationsId, organizationsId" /> | Update a single Endpoint. |

## `SELECT` examples

Lists FirewallEndpoints in a given project and location.

```sql
SELECT
name,
description,
associatedNetworks,
associations,
billingProjectId,
createTime,
labels,
reconciling,
state,
updateTime
FROM google.networksecurity.firewall_endpoints
WHERE locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>firewall_endpoints</code> resource.

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
INSERT INTO google.networksecurity.firewall_endpoints (
locationsId,
organizationsId,
name,
description,
labels,
billingProjectId
)
SELECT 
'{{ locationsId }}',
'{{ organizationsId }}',
'{{ name }}',
'{{ description }}',
'{{ labels }}',
'{{ billingProjectId }}'
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
    - name: billingProjectId
      value: '{{ billingProjectId }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>firewall_endpoints</code> resource.

```sql
/*+ update */
UPDATE google.networksecurity.firewall_endpoints
SET 
name = '{{ name }}',
description = '{{ description }}',
labels = '{{ labels }}',
billingProjectId = '{{ billingProjectId }}'
WHERE 
firewallEndpointsId = '{{ firewallEndpointsId }}'
AND locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `DELETE` example

Deletes the specified <code>firewall_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM google.networksecurity.firewall_endpoints
WHERE firewallEndpointsId = '{{ firewallEndpointsId }}'
AND locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}';
```
