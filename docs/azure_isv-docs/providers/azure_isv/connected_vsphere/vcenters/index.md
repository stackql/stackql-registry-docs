---
title: vcenters
hide_title: false
hide_table_of_contents: false
keywords:
  - vcenters
  - connected_vsphere
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

Creates, updates, deletes, gets or lists a <code>vcenters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vcenters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.connected_vsphere.vcenters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vcenters', value: 'view', },
        { label: 'vcenters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the Id. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name. |
| <CopyableCode code="connection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_resource_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="location" /> | `text` | Gets or sets the location. |
| <CopyableCode code="port" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="statuses" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Gets or sets the Resource tags. |
| <CopyableCode code="type" /> | `text` | Gets or sets the type of the resource. |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="vcenterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name. |
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="location" /> | `string` | Gets or sets the location. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a VCenter. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Gets or sets the Resource tags. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vcenterName" /> | Implements vCenter GET method. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List of vCenters in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List of vCenters in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vcenterName, data__location, data__properties" /> | Create Or Update vCenter. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vcenterName" /> | Implements vCenter DELETE method. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, vcenterName" /> | API to update certain properties of the vCenter resource. |

## `SELECT` examples

List of vCenters in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vcenters', value: 'view', },
        { label: 'vcenters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
connection_status,
credentials,
custom_resource_name,
extended_location,
fqdn,
instance_uuid,
kind,
location,
port,
provisioning_state,
resourceGroupName,
statuses,
subscriptionId,
system_data,
tags,
type,
uuid,
vcenterName,
version
FROM azure_isv.connected_vsphere.vw_vcenters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
extendedLocation,
kind,
location,
properties,
systemData,
tags,
type
FROM azure_isv.connected_vsphere.vcenters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vcenters</code> resource.

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
INSERT INTO azure_isv.connected_vsphere.vcenters (
resourceGroupName,
subscriptionId,
vcenterName,
data__location,
data__properties,
properties,
location,
extendedLocation,
systemData,
tags,
kind
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vcenterName }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ location }}',
'{{ extendedLocation }}',
'{{ systemData }}',
'{{ tags }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: uuid
          value: string
        - name: fqdn
          value: string
        - name: port
          value: integer
        - name: version
          value: string
        - name: instanceUuid
          value: string
        - name: connectionStatus
          value: string
        - name: customResourceName
          value: string
        - name: credentials
          value:
            - name: username
              value: string
            - name: password
              value: string
        - name: statuses
          value:
            - - name: type
                value: string
              - name: status
                value: string
              - name: reason
                value: string
              - name: message
                value: string
              - name: severity
                value: string
              - name: lastUpdatedAt
                value: string
        - name: provisioningState
          value: []
    - name: location
      value: string
    - name: extendedLocation
      value:
        - name: type
          value: string
        - name: name
          value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: tags
      value: object
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: kind
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>vcenters</code> resource.

```sql
/*+ update */
UPDATE azure_isv.connected_vsphere.vcenters
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vcenterName = '{{ vcenterName }}';
```

## `DELETE` example

Deletes the specified <code>vcenters</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.connected_vsphere.vcenters
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vcenterName = '{{ vcenterName }}';
```
