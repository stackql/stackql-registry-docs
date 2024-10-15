---
title: b2c_tenants
hide_title: false
hide_table_of_contents: false
keywords:
  - b2c_tenants
  - aad_b2c
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

Creates, updates, deletes, gets or lists a <code>b2c_tenants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>b2c_tenants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aad_b2c.b2c_tenants" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_b2c_tenants', value: 'view', },
        { label: 'b2c_tenants', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | An identifier that represents the Azure AD B2C tenant resource. |
| <CopyableCode code="name" /> | `text` | The name of the Azure AD B2C tenant resource. |
| <CopyableCode code="billing_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_go_local_tenant" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location in which the resource is hosted and data resides. Can be one of 'United States', 'Europe', 'Asia Pacific', or 'Australia'. Refer to [this documentation](https://aka.ms/B2CDataResidency) for more information. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C billing at [aka.ms/b2cBilling](https://aka.ms/b2cBilling). |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource Tags |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the B2C tenant resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the Azure AD B2C tenant resource. |
| <CopyableCode code="name" /> | `string` | The name of the Azure AD B2C tenant resource. |
| <CopyableCode code="location" /> | `string` | The location in which the resource is hosted and data resides. Can be one of 'United States', 'Europe', 'Asia Pacific', or 'Australia'. Refer to [this documentation](https://aka.ms/B2CDataResidency) for more information. |
| <CopyableCode code="properties" /> | `object` | Properties of the Azure AD B2C tenant Azure resource. |
| <CopyableCode code="sku" /> | `object` | SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C billing at [aka.ms/b2cBilling](https://aka.ms/b2cBilling). |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource Tags |
| <CopyableCode code="type" /> | `string` | The type of the B2C tenant resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get the Azure AD B2C tenant resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the Azure AD B2C tenant resources in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all the Azure AD B2C tenant resources in a subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, data__location, data__properties, data__sku" /> | Initiates an async request to create both the Azure AD B2C tenant and the corresponding Azure resource linked to a subscription. Note: Please check name availability before creating a new tenant. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Initiates an async operation to delete the Azure AD B2C tenant and Azure resource. The resource deletion can only happen as the last step in [the tenant deletion process](https://aka.ms/deleteB2Ctenant).  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Update the Azure AD B2C tenant resource. |

## `SELECT` examples

Get all the Azure AD B2C tenant resources in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_b2c_tenants', value: 'view', },
        { label: 'b2c_tenants', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
billing_config,
is_go_local_tenant,
location,
resourceGroupName,
resourceName,
sku,
subscriptionId,
system_data,
tags,
tenant_id,
type
FROM azure.aad_b2c.vw_b2c_tenants
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
sku,
systemData,
tags,
type
FROM azure.aad_b2c.b2c_tenants
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>b2c_tenants</code> resource.

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
INSERT INTO azure.aad_b2c.b2c_tenants (
resourceGroupName,
resourceName,
subscriptionId,
data__location,
data__properties,
data__sku,
location,
properties,
sku,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ data__sku }}',
'{{ location }}',
'{{ properties }}',
'{{ sku }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: properties
      value:
        - name: createTenantProperties
          value:
            - name: displayName
              value: string
            - name: countryCode
              value: []
            - name: isGoLocalTenant
              value: []
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>b2c_tenants</code> resource.

```sql
/*+ update */
UPDATE azure.aad_b2c.b2c_tenants
SET 
sku = '{{ sku }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>b2c_tenants</code> resource.

```sql
/*+ delete */
DELETE FROM azure.aad_b2c.b2c_tenants
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
