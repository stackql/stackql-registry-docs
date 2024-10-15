---
title: volume_quota_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_quota_rules
  - netapp
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

Creates, updates, deletes, gets or lists a <code>volume_quota_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_quota_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.volume_quota_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volume_quota_rules', value: 'view', },
        { label: 'volume_quota_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="poolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="quota_size_in_ki_bs" /> | `text` | field from the `properties` object |
| <CopyableCode code="quota_target" /> | `text` | field from the `properties` object |
| <CopyableCode code="quota_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="volumeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="volumeQuotaRuleName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Volume Quota Rule properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName, volumeQuotaRuleName" /> | Get details of the specified quota rule |
| <CopyableCode code="list_by_volume" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | List all quota rules associated with the volume |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName, volumeQuotaRuleName" /> | Create the specified quota rule within the given volume |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName, volumeQuotaRuleName" /> | Delete quota rule |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName, volumeQuotaRuleName" /> | Patch a quota rule |

## `SELECT` examples

List all quota rules associated with the volume

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volume_quota_rules', value: 'view', },
        { label: 'volume_quota_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
location,
poolName,
provisioning_state,
quota_size_in_ki_bs,
quota_target,
quota_type,
resourceGroupName,
subscriptionId,
tags,
volumeName,
volumeQuotaRuleName
FROM azure_isv.netapp.vw_volume_quota_rules
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_isv.netapp.volume_quota_rules
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>volume_quota_rules</code> resource.

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
INSERT INTO azure_isv.netapp.volume_quota_rules (
accountName,
poolName,
resourceGroupName,
subscriptionId,
volumeName,
volumeQuotaRuleName,
tags,
location,
properties
)
SELECT 
'{{ accountName }}',
'{{ poolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ volumeName }}',
'{{ volumeQuotaRuleName }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
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
        - name: provisioningState
          value: []
        - name: quotaSizeInKiBs
          value: integer
        - name: quotaType
          value: string
        - name: quotaTarget
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>volume_quota_rules</code> resource.

```sql
/*+ update */
UPDATE azure_isv.netapp.volume_quota_rules
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}'
AND volumeQuotaRuleName = '{{ volumeQuotaRuleName }}';
```

## `DELETE` example

Deletes the specified <code>volume_quota_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.netapp.volume_quota_rules
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}'
AND volumeQuotaRuleName = '{{ volumeQuotaRuleName }}';
```
