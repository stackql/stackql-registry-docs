---
title: springbootsites
hide_title: false
hide_table_of_contents: false
keywords:
  - springbootsites
  - off_azure_springboot
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

Creates, updates, deletes, gets or lists a <code>springbootsites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>springbootsites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.off_azure_springboot.springbootsites" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_springbootsites', value: 'view', },
        { label: 'springbootsites', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="master_site_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="migrate_project_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="springbootsitesName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The extended location definition. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The springbootsites resource definition. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, springbootsitesName, subscriptionId" /> | Get a springbootsites resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List springbootsites resource by resourceGroup. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List springbootsites resource by subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, springbootsitesName, subscriptionId, data__location" /> | Create a springbootsites resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, springbootsitesName, subscriptionId" /> | Delete a springbootsites resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, springbootsitesName, subscriptionId" /> | Update a springbootsites resource. |
| <CopyableCode code="trigger_refresh_site" /> | `EXEC` | <CopyableCode code="resourceGroupName, springbootsitesName, subscriptionId" /> | Trigger refresh springbootsites action |

## `SELECT` examples

List springbootsites resource by subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_springbootsites', value: 'view', },
        { label: 'springbootsites', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
extended_location,
location,
master_site_id,
migrate_project_id,
provisioning_state,
resourceGroupName,
springbootsitesName,
subscriptionId,
tags
FROM azure_extras.off_azure_springboot.vw_springbootsites
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure_extras.off_azure_springboot.springbootsites
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>springbootsites</code> resource.

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
INSERT INTO azure_extras.off_azure_springboot.springbootsites (
resourceGroupName,
springbootsitesName,
subscriptionId,
data__location,
tags,
location,
properties,
extendedLocation
)
SELECT 
'{{ resourceGroupName }}',
'{{ springbootsitesName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ extendedLocation }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: masterSiteId
          value: string
        - name: migrateProjectId
          value: string
        - name: provisioningState
          value: string
    - name: extendedLocation
      value:
        - name: type
          value: string
        - name: name
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>springbootsites</code> resource.

```sql
/*+ update */
UPDATE azure_extras.off_azure_springboot.springbootsites
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND springbootsitesName = '{{ springbootsitesName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>springbootsites</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.off_azure_springboot.springbootsites
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND springbootsitesName = '{{ springbootsitesName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
