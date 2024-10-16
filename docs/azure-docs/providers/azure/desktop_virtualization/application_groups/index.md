---
title: application_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - application_groups
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>application_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.application_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_groups', value: 'view', },
        { label: 'application_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_group_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_pc_resource" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_pool_arm_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="kind" /> | `text` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | Plan for the resource. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="show_in_feed" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspace_arm_path" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="managedBy" /> | `string` | The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource. |
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | Schema for ApplicationGroup properties. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationGroupName, resourceGroupName, subscriptionId" /> | Get an application group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List applicationGroups. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List applicationGroups in subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationGroupName, resourceGroupName, subscriptionId, data__properties" /> | Create or update an applicationGroup. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationGroupName, resourceGroupName, subscriptionId" /> | Remove an applicationGroup. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="applicationGroupName, resourceGroupName, subscriptionId" /> | Update an applicationGroup. |

## `SELECT` examples

List applicationGroups in subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_groups', value: 'view', },
        { label: 'application_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
applicationGroupName,
application_group_type,
cloud_pc_resource,
etag,
friendly_name,
host_pool_arm_path,
identity,
kind,
managed_by,
object_id,
plan,
resourceGroupName,
show_in_feed,
sku,
subscriptionId,
workspace_arm_path
FROM azure.desktop_virtualization.vw_application_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
identity,
kind,
managedBy,
plan,
properties,
sku
FROM azure.desktop_virtualization.application_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application_groups</code> resource.

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
INSERT INTO azure.desktop_virtualization.application_groups (
applicationGroupName,
resourceGroupName,
subscriptionId,
data__properties,
managedBy,
kind,
identity,
sku,
plan,
properties
)
SELECT 
'{{ applicationGroupName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ managedBy }}',
'{{ kind }}',
'{{ identity }}',
'{{ sku }}',
'{{ plan }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: managedBy
      value: string
    - name: kind
      value: string
    - name: etag
      value: string
    - name: identity
      value: string
    - name: sku
      value: string
    - name: plan
      value: string
    - name: properties
      value:
        - name: objectId
          value: string
        - name: description
          value: string
        - name: friendlyName
          value: string
        - name: hostPoolArmPath
          value: string
        - name: workspaceArmPath
          value: string
        - name: applicationGroupType
          value: string
        - name: cloudPcResource
          value: boolean
        - name: showInFeed
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>application_groups</code> resource.

```sql
/*+ update */
UPDATE azure.desktop_virtualization.application_groups
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
applicationGroupName = '{{ applicationGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>application_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.desktop_virtualization.application_groups
WHERE applicationGroupName = '{{ applicationGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
