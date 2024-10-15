---
title: certificate_orders_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_orders_certificates
  - app_service
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

Creates, updates, deletes, gets or lists a <code>certificate_orders_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_orders_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.certificate_orders_certificates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_certificate_orders_certificates', value: 'view', },
        { label: 'certificate_orders_certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource Name. |
| <CopyableCode code="certificateOrderName" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_secret_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of resource. |
| <CopyableCode code="location" /> | `text` | Resource Location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | Key Vault container for a certificate that is purchased through Azure. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateOrderName, name, resourceGroupName, subscriptionId" /> | Description for Get the certificate associated with a certificate order. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for List all certificates associated with a certificate order. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateOrderName, name, resourceGroupName, subscriptionId" /> | Description for Creates or updates a certificate and associates with key vault secret. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateOrderName, name, resourceGroupName, subscriptionId" /> | Description for Delete the certificate associated with a certificate order. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="certificateOrderName, name, resourceGroupName, subscriptionId" /> | Description for Creates or updates a certificate and associates with key vault secret. |

## `SELECT` examples

Description for List all certificates associated with a certificate order.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_certificate_orders_certificates', value: 'view', },
        { label: 'certificate_orders_certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
certificateOrderName,
key_vault_id,
key_vault_secret_name,
kind,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.app_service.vw_certificate_orders_certificates
WHERE certificateOrderName = '{{ certificateOrderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
location,
properties,
tags,
type
FROM azure.app_service.certificate_orders_certificates
WHERE certificateOrderName = '{{ certificateOrderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate_orders_certificates</code> resource.

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
INSERT INTO azure.app_service.certificate_orders_certificates (
certificateOrderName,
name,
resourceGroupName,
subscriptionId,
kind,
location,
tags,
properties
)
SELECT 
'{{ certificateOrderName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: keyVaultId
          value: string
        - name: keyVaultSecretName
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>certificate_orders_certificates</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.certificate_orders_certificates
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
certificateOrderName = '{{ certificateOrderName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>certificate_orders_certificates</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.certificate_orders_certificates
WHERE certificateOrderName = '{{ certificateOrderName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
