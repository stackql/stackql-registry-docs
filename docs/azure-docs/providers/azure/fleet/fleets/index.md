---
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
  - fleet
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

Creates, updates, deletes, gets or lists a <code>fleets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fleet.fleets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_fleets', value: 'view', },
        { label: 'fleets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="fleetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hub_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Fleet properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | Gets a Fleet. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists fleets in the specified subscription and resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists fleets in the specified subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | Creates or updates a Fleet. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | Delete a Fleet |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | Update a Fleet |

## `SELECT` examples

Lists fleets in the specified subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_fleets', value: 'view', },
        { label: 'fleets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
e_tag,
fleetName,
hub_profile,
identity,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.fleet.vw_fleets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
eTag,
identity,
location,
properties,
tags
FROM azure.fleet.fleets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>fleets</code> resource.

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
INSERT INTO azure.fleet.fleets (
fleetName,
resourceGroupName,
subscriptionId,
properties,
identity,
tags,
location
)
SELECT 
'{{ fleetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: hubProfile
          value:
            - name: dnsPrefix
              value: string
            - name: apiServerAccessProfile
              value:
                - name: enablePrivateCluster
                  value: boolean
            - name: agentProfile
              value:
                - name: subnetId
                  value: []
                - name: vmSize
                  value: string
            - name: fqdn
              value: string
            - name: kubernetesVersion
              value: string
            - name: portalFqdn
              value: string
    - name: eTag
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>fleets</code> resource.

```sql
/*+ update */
UPDATE azure.fleet.fleets
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>fleets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.fleet.fleets
WHERE fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
