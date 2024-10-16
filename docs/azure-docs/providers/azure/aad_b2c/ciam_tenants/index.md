---
title: ciam_tenants
hide_title: false
hide_table_of_contents: false
keywords:
  - ciam_tenants
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

Creates, updates, deletes, gets or lists a <code>ciam_tenants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ciam_tenants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aad_b2c.ciam_tenants" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ciam_tenants', value: 'view', },
        { label: 'ciam_tenants', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | An identifier that represents the Azure AD for customers tenant resource. |
| <CopyableCode code="name" /> | `text` | The name of the Azure AD for customers tenant resource. |
| <CopyableCode code="billing_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_tenant_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location in which the resource is hosted and data resides. Can be one of 'United States', 'Europe', 'Asia Pacific', or 'Australia'. Refer to [this documentation](https://aka.ms/ciam-data-location) for more information. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | SKU properties of the Azure AD for customers tenant. Learn more about Azure AD for customers billing at [https://aka.ms/ciambilling](https://aka.ms/ciambilling). |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource Tags |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the Azure AD for customers tenant resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the Azure AD for customers tenant resource. |
| <CopyableCode code="name" /> | `string` | The name of the Azure AD for customers tenant resource. |
| <CopyableCode code="location" /> | `string` | The location in which the resource is hosted and data resides. Can be one of 'United States', 'Europe', 'Asia Pacific', or 'Australia'. Refer to [this documentation](https://aka.ms/ciam-data-location) for more information. |
| <CopyableCode code="properties" /> | `object` | Properties of the Azure AD for customers tenant Azure resource. |
| <CopyableCode code="sku" /> | `object` | SKU properties of the Azure AD for customers tenant. Learn more about Azure AD for customers billing at [https://aka.ms/ciambilling](https://aka.ms/ciambilling). |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource Tags |
| <CopyableCode code="type" /> | `string` | The type of the Azure AD for customers tenant resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get the Azure AD for customers tenant resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the Azure AD for customers tenants resources in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all the Azure AD for customers tenant resources in a subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, data__location, data__properties, data__sku" /> | Initiates an async request to create both the Azure AD for customers tenant and the corresponding Azure resource linked to a subscription. Note: Please check name availability before creating a new tenant |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Initiates an async operation to delete the Azure AD for customers tenant and Azure resource. The resource deletion can only happen as the last step in [the tenant deletion process](https://aka.ms/delete-ciam-tenant). |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Update the Azure AD for customers tenant resource. |

## `SELECT` examples

Get all the Azure AD for customers tenant resources in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ciam_tenants', value: 'view', },
        { label: 'ciam_tenants', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
billing_config,
create_tenant_properties,
domain_name,
location,
provisioning_state,
resourceGroupName,
resourceName,
sku,
subscriptionId,
system_data,
tags,
tenant_id,
type
FROM azure.aad_b2c.vw_ciam_tenants
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
FROM azure.aad_b2c.ciam_tenants
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ciam_tenants</code> resource.

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
INSERT INTO azure.aad_b2c.ciam_tenants (
resourceGroupName,
resourceName,
subscriptionId,
data__location,
data__properties,
data__sku,
location,
sku,
properties,
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
'{{ sku }}',
'{{ properties }}',
'{{ tags }}'
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
    - name: type
      value: string
    - name: location
      value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: createTenantProperties
          value:
            - name: displayName
              value: string
            - name: countryCode
              value: string
        - name: domainName
          value: string
        - name: billingConfig
          value:
            - name: billingType
              value: string
            - name: effectiveStartDateUtc
              value: string
        - name: tenantId
          value: string
    - name: tags
      value: object
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>ciam_tenants</code> resource.

```sql
/*+ update */
UPDATE azure.aad_b2c.ciam_tenants
SET 
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>ciam_tenants</code> resource.

```sql
/*+ delete */
DELETE FROM azure.aad_b2c.ciam_tenants
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
