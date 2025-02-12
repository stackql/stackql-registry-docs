---
title: managers
hide_title: false
hide_table_of_contents: false
keywords:
  - managers
  - storsimple_8000_series
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

Creates, updates, deletes, gets or lists a <code>managers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.managers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managers', value: 'view', },
        { label: 'managers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource ID. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="cis_intrinsic_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag of the manager. |
| <CopyableCode code="location" /> | `text` | The geo location of the resource. |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags attached to the resource. |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | The etag of the manager. |
| <CopyableCode code="location" /> | `string` | The geo location of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of the StorSimple Manager. |
| <CopyableCode code="tags" /> | `object` | The tags attached to the resource. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified manager name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves all the managers in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves all the managers in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Creates or updates the manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Deletes the manager. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Updates the StorSimple Manager. |
| <CopyableCode code="regenerate_activation_key" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Re-generates and returns the activation key of the manager. |

## `SELECT` examples

Retrieves all the managers in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managers', value: 'view', },
        { label: 'managers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
cis_intrinsic_settings,
etag,
location,
managerName,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags,
type
FROM azure_extras.storsimple_8000_series.vw_managers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure_extras.storsimple_8000_series.managers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managers</code> resource.

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
INSERT INTO azure_extras.storsimple_8000_series.managers (
managerName,
resourceGroupName,
subscriptionId,
location,
tags,
properties,
etag
)
SELECT 
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: cisIntrinsicSettings
          value:
            - name: type
              value: string
        - name: sku
          value:
            - name: name
              value: string
        - name: provisioningState
          value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>managers</code> resource.

```sql
/*+ update */
UPDATE azure_extras.storsimple_8000_series.managers
SET 
tags = '{{ tags }}'
WHERE 
managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>managers</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_8000_series.managers
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
