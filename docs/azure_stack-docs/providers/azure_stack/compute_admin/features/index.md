---
title: features
hide_title: false
hide_table_of_contents: false
keywords:
  - features
  - compute_admin
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

Creates, updates, deletes, gets or lists a <code>features</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.compute_admin.features" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_features', value: 'view', },
        { label: 'features', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="enabled_tenant_subscription_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="featureName" /> | `text` | field from the `properties` object |
| <CopyableCode code="feature_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="global_feature_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of features. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureName, location, subscriptionId" /> | Get an existing feature. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Get a list of existing features. |

## `SELECT` examples

Get a list of existing features.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_features', value: 'view', },
        { label: 'features', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
enabled_tenant_subscription_ids,
featureName,
feature_name,
global_feature_settings,
location,
subscriptionId,
type
FROM azure_stack.compute_admin.vw_features
WHERE location = '{{ location }}'
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
FROM azure_stack.compute_admin.features
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

