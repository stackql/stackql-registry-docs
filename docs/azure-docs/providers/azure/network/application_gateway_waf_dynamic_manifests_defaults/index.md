---
title: application_gateway_waf_dynamic_manifests_defaults
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateway_waf_dynamic_manifests_defaults
  - network
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

Creates, updates, deletes, gets or lists a <code>application_gateway_waf_dynamic_manifests_defaults</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_gateway_waf_dynamic_manifests_defaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.application_gateway_waf_dynamic_manifests_defaults" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_gateway_waf_dynamic_manifests_defaults', value: 'view', },
        { label: 'application_gateway_waf_dynamic_manifests_defaults', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="available_rule_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_rule_set" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | Properties of ApplicationGatewayWafDynamicManifest. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets the regional application gateway waf manifest. |

## `SELECT` examples

Gets the regional application gateway waf manifest.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_gateway_waf_dynamic_manifests_defaults', value: 'view', },
        { label: 'application_gateway_waf_dynamic_manifests_defaults', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
available_rule_sets,
default_rule_set,
location,
subscriptionId,
type
FROM azure.network.vw_application_gateway_waf_dynamic_manifests_defaults
WHERE location = '{{ location }}'
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
FROM azure.network.application_gateway_waf_dynamic_manifests_defaults
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

