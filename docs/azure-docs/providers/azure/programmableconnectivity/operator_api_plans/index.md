---
title: operator_api_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - operator_api_plans
  - programmableconnectivity
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

Creates, updates, deletes, gets or lists a <code>operator_api_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operator_api_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.programmableconnectivity.operator_api_plans" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_operator_api_plans', value: 'view', },
        { label: 'operator_api_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="camara_api_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="limits" /> | `text` | field from the `properties` object |
| <CopyableCode code="marketplace_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="markets" /> | `text` | field from the `properties` object |
| <CopyableCode code="operatorApiPlanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="operator_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="operator_regions" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_locations" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Operator API Plan properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operatorApiPlanName, subscriptionId" /> | Get an OperatorApiPlan resource by name. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List OperatorApiPlan resources by subscription ID. |

## `SELECT` examples

List OperatorApiPlan resources by subscription ID.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_operator_api_plans', value: 'view', },
        { label: 'operator_api_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
camara_api_name,
limits,
marketplace_properties,
markets,
operatorApiPlanName,
operator_name,
operator_regions,
provisioning_state,
subscriptionId,
supported_locations
FROM azure.programmableconnectivity.vw_operator_api_plans
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.programmableconnectivity.operator_api_plans
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

