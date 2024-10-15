---
title: associated_tenants
hide_title: false
hide_table_of_contents: false
keywords:
  - associated_tenants
  - billing
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

Creates, updates, deletes, gets or lists a <code>associated_tenants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>associated_tenants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.associated_tenants" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_associated_tenants', value: 'view', },
        { label: 'associated_tenants', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="associatedTenantName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_management_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_billing_request_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_management_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | An associated tenant. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="associatedTenantName, billingAccountName" /> | Gets an associated tenant by ID. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the associated tenants that can collaborate with the billing account on commerce activities like viewing and downloading invoices, managing payments, making purchases, and managing or provisioning licenses. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="associatedTenantName, billingAccountName" /> | Create or update an associated tenant for the billing account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="associatedTenantName, billingAccountName" /> | Deletes an associated tenant for a billing account. |

## `SELECT` examples

Lists the associated tenants that can collaborate with the billing account on commerce activities like viewing and downloading invoices, managing payments, making purchases, and managing or provisioning licenses.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_associated_tenants', value: 'view', },
        { label: 'associated_tenants', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
associatedTenantName,
billingAccountName,
billing_management_state,
display_name,
provisioning_billing_request_id,
provisioning_management_state,
provisioning_state,
tags,
tenant_id
FROM azure.billing.vw_associated_tenants
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.associated_tenants
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>associated_tenants</code> resource.

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
INSERT INTO azure.billing.associated_tenants (
associatedTenantName,
billingAccountName,
tags,
properties
)
SELECT 
'{{ associatedTenantName }}',
'{{ billingAccountName }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: displayName
          value: string
        - name: tenantId
          value: string
        - name: billingManagementState
          value: string
        - name: provisioningManagementState
          value: string
        - name: provisioningBillingRequestId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>associated_tenants</code> resource.

```sql
/*+ delete */
DELETE FROM azure.billing.associated_tenants
WHERE associatedTenantName = '{{ associatedTenantName }}'
AND billingAccountName = '{{ billingAccountName }}';
```
