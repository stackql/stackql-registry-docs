---
title: role_assignments_by_invoice_sections
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments_by_invoice_sections
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

Creates, updates, deletes, gets or lists a <code>role_assignments_by_invoice_sections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_assignments_by_invoice_sections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.role_assignments_by_invoice_sections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_assignments_by_invoice_sections', value: 'view', },
        { label: 'role_assignments_by_invoice_sections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingRoleAssignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_request_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by_principal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by_principal_puid" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by_principal_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by_user_email_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoiceSectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_section_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_section_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="modified_by_principal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="modified_by_principal_puid" /> | `text` | field from the `properties` object |
| <CopyableCode code="modified_by_principal_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="modified_by_user_email_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="modified_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_puid" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_tenant_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_definition_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
| <CopyableCode code="user_authentication_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_email_address" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of the billing role assignment. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, billingRoleAssignmentName, invoiceSectionName" /> | Gets a role assignment for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Lists the role assignments for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName, data__roleDefinitionId" /> | Adds a role assignment on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="billingAccountName, billingProfileName, billingRoleAssignmentName, invoiceSectionName" /> | Deletes a role assignment on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |

## `SELECT` examples

Lists the role assignments for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_assignments_by_invoice_sections', value: 'view', },
        { label: 'role_assignments_by_invoice_sections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
billingAccountName,
billingProfileName,
billingRoleAssignmentName,
billing_account_display_name,
billing_account_id,
billing_profile_display_name,
billing_profile_id,
billing_request_id,
created_by_principal_id,
created_by_principal_puid,
created_by_principal_tenant_id,
created_by_user_email_address,
created_on,
customer_display_name,
customer_id,
invoiceSectionName,
invoice_section_display_name,
invoice_section_id,
modified_by_principal_id,
modified_by_principal_puid,
modified_by_principal_tenant_id,
modified_by_user_email_address,
modified_on,
principal_display_name,
principal_id,
principal_puid,
principal_tenant_id,
principal_tenant_name,
principal_type,
provisioning_state,
role_definition_id,
scope,
tags,
user_authentication_type,
user_email_address
FROM azure.billing.vw_role_assignments_by_invoice_sections
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}'
AND invoiceSectionName = '{{ invoiceSectionName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.role_assignments_by_invoice_sections
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}'
AND invoiceSectionName = '{{ invoiceSectionName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>role_assignments_by_invoice_sections</code> resource.

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
INSERT INTO azure.billing.role_assignments_by_invoice_sections (
billingAccountName,
billingProfileName,
invoiceSectionName,
data__roleDefinitionId,
principalPuid,
principalId,
principalTenantId,
roleDefinitionId,
scope,
userAuthenticationType,
userEmailAddress
)
SELECT 
'{{ billingAccountName }}',
'{{ billingProfileName }}',
'{{ invoiceSectionName }}',
'{{ data__roleDefinitionId }}',
'{{ principalPuid }}',
'{{ principalId }}',
'{{ principalTenantId }}',
'{{ roleDefinitionId }}',
'{{ scope }}',
'{{ userAuthenticationType }}',
'{{ userEmailAddress }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: provisioningState
      value: string
    - name: createdOn
      value: string
    - name: createdByPrincipalTenantId
      value: string
    - name: createdByPrincipalId
      value: string
    - name: createdByPrincipalPuid
      value: string
    - name: createdByUserEmailAddress
      value: string
    - name: modifiedOn
      value: string
    - name: modifiedByPrincipalPuid
      value: string
    - name: modifiedByUserEmailAddress
      value: string
    - name: modifiedByPrincipalId
      value: string
    - name: modifiedByPrincipalTenantId
      value: string
    - name: principalPuid
      value: string
    - name: principalId
      value: string
    - name: principalTenantId
      value: string
    - name: roleDefinitionId
      value: string
    - name: scope
      value: string
    - name: userAuthenticationType
      value: string
    - name: userEmailAddress
      value: string
    - name: principalTenantName
      value: string
    - name: principalDisplayName
      value: string
    - name: principalType
      value: string
    - name: billingRequestId
      value: string
    - name: billingAccountId
      value: string
    - name: billingAccountDisplayName
      value: string
    - name: billingProfileId
      value: string
    - name: billingProfileDisplayName
      value: string
    - name: invoiceSectionId
      value: string
    - name: invoiceSectionDisplayName
      value: string
    - name: customerId
      value: string
    - name: customerDisplayName
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>role_assignments_by_invoice_sections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.billing.role_assignments_by_invoice_sections
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}'
AND billingRoleAssignmentName = '{{ billingRoleAssignmentName }}'
AND invoiceSectionName = '{{ invoiceSectionName }}';
```
