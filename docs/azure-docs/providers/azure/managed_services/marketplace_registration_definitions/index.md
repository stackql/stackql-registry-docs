---
title: marketplace_registration_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_registration_definitions
  - managed_services
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

Creates, updates, deletes, gets or lists a <code>marketplace_registration_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>marketplace_registration_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_services.marketplace_registration_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_marketplace_registration_definitions', value: 'view', },
        { label: 'marketplace_registration_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The fully qualified path of the marketplace registration definition. |
| <CopyableCode code="name" /> | `text` | The name of the marketplace registration definition. |
| <CopyableCode code="authorizations" /> | `text` | field from the `properties` object |
| <CopyableCode code="eligible_authorizations" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="marketplaceIdentifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | Plan for the resource. |
| <CopyableCode code="plan_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the Azure resource (Microsoft.ManagedServices/marketplaceRegistrationDefinitions). |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified path of the marketplace registration definition. |
| <CopyableCode code="name" /> | `string` | The name of the marketplace registration definition. |
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of the marketplace registration definition. |
| <CopyableCode code="type" /> | `string` | The type of the Azure resource (Microsoft.ManagedServices/marketplaceRegistrationDefinitions). |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="marketplaceIdentifier, scope" /> | Get the marketplace registration definition for the marketplace identifier. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Gets a list of the marketplace registration definitions for the marketplace identifier. |

## `SELECT` examples

Gets a list of the marketplace registration definitions for the marketplace identifier.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_marketplace_registration_definitions', value: 'view', },
        { label: 'marketplace_registration_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
authorizations,
eligible_authorizations,
managed_by_tenant_id,
marketplaceIdentifier,
offer_display_name,
plan,
plan_display_name,
publisher_display_name,
scope,
type
FROM azure.managed_services.vw_marketplace_registration_definitions
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
plan,
properties,
type
FROM azure.managed_services.marketplace_registration_definitions
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>

