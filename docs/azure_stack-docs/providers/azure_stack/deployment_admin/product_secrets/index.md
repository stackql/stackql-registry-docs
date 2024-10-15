---
title: product_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - product_secrets
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

Creates, updates, deletes, gets or lists a <code>product_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.deployment_admin.product_secrets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_product_secrets', value: 'view', },
        { label: 'product_secrets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="expires_after" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="packageId" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="secretName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret_descriptor" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of product secret. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packageId, secretName, subscriptionId" /> | Returns the specific product secret. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="packageId, subscriptionId" /> | Returns an array of product secrets. |
| <CopyableCode code="set" /> | `EXEC` | <CopyableCode code="packageId, secretName, subscriptionId" /> | Imports a product secret. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="packageId, secretName, subscriptionId" /> | Validates a product secret. |

## `SELECT` examples

Returns an array of product secrets.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_product_secrets', value: 'view', },
        { label: 'product_secrets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
expires_after,
location,
packageId,
provisioning_state,
secretName,
secret_descriptor,
secret_kind,
secret_state,
subscriptionId,
type
FROM azure_stack.deployment_admin.vw_product_secrets
WHERE packageId = '{{ packageId }}'
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
FROM azure_stack.deployment_admin.product_secrets
WHERE packageId = '{{ packageId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

