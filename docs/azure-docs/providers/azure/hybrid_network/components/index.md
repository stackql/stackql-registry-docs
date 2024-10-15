---
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
  - hybrid_network
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

Creates, updates, deletes, gets or lists a <code>components</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.components" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_components', value: 'view', },
        { label: 'components', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="componentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkFunctionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The component properties of the network function. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="componentName, networkFunctionName, resourceGroupName, subscriptionId" /> | Gets information about the specified application instance resource. |
| <CopyableCode code="list_by_network_function" /> | `SELECT` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Lists all the component resources in a network function. |

## `SELECT` examples

Lists all the component resources in a network function.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_components', value: 'view', },
        { label: 'components', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
componentName,
deployment_profile,
deployment_status,
networkFunctionName,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.hybrid_network.vw_components
WHERE networkFunctionName = '{{ networkFunctionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.hybrid_network.components
WHERE networkFunctionName = '{{ networkFunctionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

