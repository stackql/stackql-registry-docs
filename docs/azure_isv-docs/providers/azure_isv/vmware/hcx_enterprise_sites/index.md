---
title: hcx_enterprise_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - hcx_enterprise_sites
  - vmware
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

Creates, updates, deletes, gets or lists a <code>hcx_enterprise_sites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hcx_enterprise_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware.hcx_enterprise_sites" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hcx_enterprise_sites', value: 'view', },
        { label: 'hcx_enterprise_sites', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="activation_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="hcxEnterpriseSiteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateCloudName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The properties of an HCX Enterprise Site |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hcxEnterpriseSiteName, privateCloudName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hcxEnterpriseSiteName, privateCloudName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hcxEnterpriseSiteName, privateCloudName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hcx_enterprise_sites', value: 'view', },
        { label: 'hcx_enterprise_sites', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
activation_key,
hcxEnterpriseSiteName,
privateCloudName,
resourceGroupName,
status,
subscriptionId,
type
FROM azure_isv.vmware.vw_hcx_enterprise_sites
WHERE privateCloudName = '{{ privateCloudName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure_isv.vmware.hcx_enterprise_sites
WHERE privateCloudName = '{{ privateCloudName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hcx_enterprise_sites</code> resource.

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
INSERT INTO azure_isv.vmware.hcx_enterprise_sites (
hcxEnterpriseSiteName,
privateCloudName,
resourceGroupName,
subscriptionId
)
SELECT 
'{{ hcxEnterpriseSiteName }}',
'{{ privateCloudName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}'
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
    - name: properties
      value:
        - name: activationKey
          value: string
        - name: status
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>hcx_enterprise_sites</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.vmware.hcx_enterprise_sites
WHERE hcxEnterpriseSiteName = '{{ hcxEnterpriseSiteName }}'
AND privateCloudName = '{{ privateCloudName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
