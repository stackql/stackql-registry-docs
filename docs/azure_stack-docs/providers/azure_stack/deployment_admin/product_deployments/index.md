---
title: product_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - product_deployments
  - deployment_admin
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

Creates, updates, deletes, gets or lists a <code>product_deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.deployment_admin.product_deployments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_product_deployments', value: 'view', },
        { label: 'product_deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="deployment" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="internal_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_successful_deployment" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="productId" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret_rotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="eTag" /> | `string` | entity tag |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Product deployment resource properties |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="productId, subscriptionId" /> | Invokes bootstrap action on the product deployment |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Invokes bootstrap action on the product deployment |

## `SELECT` examples

Invokes bootstrap action on the product deployment

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_product_deployments', value: 'view', },
        { label: 'product_deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
deployment,
e_tag,
error,
external_access,
internal_state,
last_successful_deployment,
location,
productId,
product_id,
provisioning_state,
secret_rotation,
status,
subscriptionId,
subscription_id,
type
FROM azure_stack.deployment_admin.vw_product_deployments
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
eTag,
location,
properties,
type
FROM azure_stack.deployment_admin.product_deployments
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

