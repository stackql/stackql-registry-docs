---
title: appliances_upgrade_graphs
hide_title: false
hide_table_of_contents: false
keywords:
  - appliances_upgrade_graphs
  - resource_connector
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

Creates, updates, deletes, gets or lists a <code>appliances_upgrade_graphs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>appliances_upgrade_graphs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_connector.appliances_upgrade_graphs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_appliances_upgrade_graphs', value: 'view', },
        { label: 'appliances_upgrade_graphs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The appliance resource path |
| <CopyableCode code="name" /> | `text` | The release train name. |
| <CopyableCode code="appliance_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_versions" /> | `text` | field from the `properties` object |
| <CopyableCode code="upgradeGraph" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The appliance resource path |
| <CopyableCode code="name" /> | `string` | The release train name. |
| <CopyableCode code="properties" /> | `object` | The Upgrade Graph Properties for appliance. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, upgradeGraph" /> | Gets the upgrade graph of an Appliance with a specified resource group and name and specific release train. |

## `SELECT` examples

Gets the upgrade graph of an Appliance with a specified resource group and name and specific release train.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_appliances_upgrade_graphs', value: 'view', },
        { label: 'appliances_upgrade_graphs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
appliance_version,
resourceGroupName,
resourceName,
subscriptionId,
supported_versions,
upgradeGraph
FROM azure.resource_connector.vw_appliances_upgrade_graphs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND upgradeGraph = '{{ upgradeGraph }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties
FROM azure.resource_connector.appliances_upgrade_graphs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND upgradeGraph = '{{ upgradeGraph }}';
```
</TabItem></Tabs>

