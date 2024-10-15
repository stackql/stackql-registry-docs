---
title: product_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - product_packages
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

Creates, updates, deletes, gets or lists a <code>product_packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.deployment_admin.product_packages" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_product_packages', value: 'view', },
        { label: 'product_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="file_container_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deployable" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_updatable" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="packageId" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_deployment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties for Product package. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packageId, subscriptionId" /> | Retrieves the specific product package details. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns an array of product packages. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="packageId, subscriptionId" /> | Creates a new product package. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="packageId, subscriptionId" /> | Deletes a product package. |

## `SELECT` examples

Returns an array of product packages.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_product_packages', value: 'view', },
        { label: 'product_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
file_container_id,
is_deployable,
is_updatable,
location,
packageId,
product_deployment_id,
provisioning_state,
subscriptionId,
type
FROM azure_stack.deployment_admin.vw_product_packages
WHERE subscriptionId = '{{ subscriptionId }}';
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
FROM azure_stack.deployment_admin.product_packages
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>product_packages</code> resource.

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
INSERT INTO azure_stack.deployment_admin.product_packages (
packageId,
subscriptionId,
properties
)
SELECT 
'{{ packageId }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: fileContainerId
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>product_packages</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.deployment_admin.product_packages
WHERE packageId = '{{ packageId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
