---
title: customization_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - customization_policies
  - vmware_cloud_simple
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

Creates, updates, deletes, gets or lists a <code>customization_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customization_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.customization_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_customization_policies', value: 'view', },
        { label: 'customization_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Customization policy azure id |
| <CopyableCode code="name" /> | `text` | Customization policy name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="customizationPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Azure region |
| <CopyableCode code="pcName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_cloud_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="regionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="specification" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Customization policy azure id |
| <CopyableCode code="name" /> | `string` | Customization policy name |
| <CopyableCode code="location" /> | `string` | Azure region |
| <CopyableCode code="properties" /> | `object` | The properties of Customization policy |
| <CopyableCode code="type" /> | `string` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customizationPolicyName, pcName, regionId, subscriptionId" /> | Returns customization policy by its name |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="pcName, regionId, subscriptionId" /> | Returns list of customization policies in region for private cloud |

## `SELECT` examples

Returns list of customization policies in region for private cloud

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_customization_policies', value: 'view', },
        { label: 'customization_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
customizationPolicyName,
location,
pcName,
private_cloud_id,
regionId,
specification,
subscriptionId,
type,
version
FROM azure_isv.vmware_cloud_simple.vw_customization_policies
WHERE pcName = '{{ pcName }}'
AND regionId = '{{ regionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure_isv.vmware_cloud_simple.customization_policies
WHERE pcName = '{{ pcName }}'
AND regionId = '{{ regionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

