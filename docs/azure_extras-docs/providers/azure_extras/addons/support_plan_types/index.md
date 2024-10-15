---
title: support_plan_types
hide_title: false
hide_table_of_contents: false
keywords:
  - support_plan_types
  - addons
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

Creates, updates, deletes, gets or lists a <code>support_plan_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>support_plan_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.addons.support_plan_types" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_support_plan_types', value: 'view', },
        { label: 'support_plan_types', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The id of the ARM resource, e.g. "/subscriptions/{id}/providers/Microsoft.Addons/supportProvider/{supportProviderName}/supportPlanTypes/{planTypeName}". |
| <CopyableCode code="name" /> | `string` | The name of the Canonical support plan, i.e. "essential", "standard" or "advanced". |
| <CopyableCode code="planTypeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="providerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `string` | Microsoft.Addons/supportProvider |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The id of the ARM resource, e.g. "/subscriptions/{id}/providers/Microsoft.Addons/supportProvider/{supportProviderName}/supportPlanTypes/{planTypeName}". |
| <CopyableCode code="name" /> | `string` | The name of the Canonical support plan, i.e. "essential", "standard" or "advanced". |
| <CopyableCode code="properties" /> | `object` | The properties of the Canonical support plan. |
| <CopyableCode code="type" /> | `string` | Microsoft.Addons/supportProvider |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="planTypeName, providerName, subscriptionId" /> | Returns whether or not the canonical support plan of type {type} is enabled for the subscription. |
| <CopyableCode code="list_info" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns the canonical support plan information for all types for the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="planTypeName, providerName, subscriptionId" /> | Creates or updates the Canonical support plan of type {type} for the subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="planTypeName, providerName, subscriptionId" /> | Cancels the Canonical support plan of type {type} for the subscription. |

## `SELECT` examples

Returns the canonical support plan information for all types for the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_support_plan_types', value: 'view', },
        { label: 'support_plan_types', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
planTypeName,
providerName,
provisioning_state,
subscriptionId,
type
FROM azure_extras.addons.vw_support_plan_types
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure_extras.addons.support_plan_types
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>support_plan_types</code> resource.

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
INSERT INTO azure_extras.addons.support_plan_types (
planTypeName,
providerName,
subscriptionId
)
SELECT 
'{{ planTypeName }}',
'{{ providerName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>support_plan_types</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.addons.support_plan_types
WHERE planTypeName = '{{ planTypeName }}'
AND providerName = '{{ providerName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
