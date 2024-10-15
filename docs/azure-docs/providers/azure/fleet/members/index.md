---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
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

Creates, updates, deletes, gets or lists a <code>members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fleet.members" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_members', value: 'view', },
        { label: 'members', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cluster_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="fleetMemberName" /> | `text` | field from the `properties` object |
| <CopyableCode code="fleetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="group" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| <CopyableCode code="properties" /> | `object` | A member of the Fleet. It contains a reference to an existing Kubernetes cluster on Azure. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fleetMemberName, fleetName, resourceGroupName, subscriptionId" /> | Get a FleetMember |
| <CopyableCode code="list_by_fleet" /> | `SELECT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | List FleetMember resources by Fleet |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fleetMemberName, fleetName, resourceGroupName, subscriptionId" /> | Create a FleetMember |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fleetMemberName, fleetName, resourceGroupName, subscriptionId" /> | Delete a FleetMember |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="fleetMemberName, fleetName, resourceGroupName, subscriptionId" /> | Update a FleetMember |

## `SELECT` examples

List FleetMember resources by Fleet

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_members', value: 'view', },
        { label: 'members', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cluster_resource_id,
e_tag,
fleetMemberName,
fleetName,
group,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.fleet.vw_members
WHERE fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
eTag,
properties
FROM azure.fleet.members
WHERE fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>members</code> resource.

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
INSERT INTO azure.fleet.members (
fleetMemberName,
fleetName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ fleetMemberName }}',
'{{ fleetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: clusterResourceId
          value: []
        - name: group
          value: string
        - name: provisioningState
          value: []
    - name: eTag
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>members</code> resource.

```sql
/*+ update */
UPDATE azure.fleet.members
SET 
properties = '{{ properties }}'
WHERE 
fleetMemberName = '{{ fleetMemberName }}'
AND fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>members</code> resource.

```sql
/*+ delete */
DELETE FROM azure.fleet.members
WHERE fleetMemberName = '{{ fleetMemberName }}'
AND fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
