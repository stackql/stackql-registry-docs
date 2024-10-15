---
title: configurations_coordinators
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations_coordinators
  - postgresql_hsc
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

Creates, updates, deletes, gets or lists a <code>configurations_coordinators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configurations_coordinators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql_hsc.configurations_coordinators" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configurations_coordinators', value: 'view', },
        { label: 'configurations_coordinators', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="allowed_values" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_value" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="requires_restart" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a configuration. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, configurationName, resourceGroupName, subscriptionId" /> | Gets information of a configuration for coordinator. |

## `SELECT` examples

Gets information of a configuration for coordinator.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configurations_coordinators', value: 'view', },
        { label: 'configurations_coordinators', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
allowed_values,
clusterName,
configurationName,
data_type,
default_value,
provisioning_state,
requires_restart,
resourceGroupName,
source,
subscriptionId,
value
FROM azure.postgresql_hsc.vw_configurations_coordinators
WHERE clusterName = '{{ clusterName }}'
AND configurationName = '{{ configurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.postgresql_hsc.configurations_coordinators
WHERE clusterName = '{{ clusterName }}'
AND configurationName = '{{ configurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

