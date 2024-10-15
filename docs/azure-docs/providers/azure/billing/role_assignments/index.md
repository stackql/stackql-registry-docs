---
title: role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments
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

Creates, updates, deletes, gets or lists a <code>role_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.role_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_assignments', value: 'view', },
        { label: 'role_assignments', value: 'resource', },
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
| <CopyableCode code="customerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_id" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName, billingRoleAssignmentName" /> | Gets a role assignment for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement. |
| <CopyableCode code="get_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, billingRoleAssignmentName" /> | Gets a role assignment for the caller on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="get_by_customer" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, billingRoleAssignmentName, customerName" /> | Gets a role assignment for the caller on a customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement. |
| <CopyableCode code="get_by_department" /> | `SELECT` | <CopyableCode code="billingAccountName, billingRoleAssignmentName, departmentName" /> | Gets a role assignment for the caller on a department. The operation is supported only for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="get_by_enrollment_account" /> | `SELECT` | <CopyableCode code="billingAccountName, billingRoleAssignmentName, enrollmentAccountName" /> | Gets a role assignment for the caller on a enrollment Account. The operation is supported only for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the role assignments for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the role assignments for the caller on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="list_by_customer" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, customerName" /> | Lists the role assignments for the caller on customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement. |
| <CopyableCode code="list_by_department" /> | `SELECT` | <CopyableCode code="billingAccountName, departmentName" /> | Lists the role assignments for the caller on a department. The operation is supported for billing accounts of type Enterprise Agreement. |
| <CopyableCode code="list_by_enrollment_account" /> | `SELECT` | <CopyableCode code="billingAccountName, enrollmentAccountName" /> | Lists the role assignments for the caller on a enrollment account. The operation is supported for billing accounts of type Enterprise Agreement. |
| <CopyableCode code="create_by_billing_account" /> | `INSERT` | <CopyableCode code="billingAccountName, data__roleDefinitionId" /> | Adds a role assignment on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="create_by_billing_profile" /> | `INSERT` | <CopyableCode code="billingAccountName, billingProfileName, data__roleDefinitionId" /> | Adds a role assignment on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="create_by_customer" /> | `INSERT` | <CopyableCode code="billingAccountName, billingProfileName, customerName, data__roleDefinitionId" /> | Adds a role assignment on a customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement. |
| <CopyableCode code="delete_by_billing_account" /> | `DELETE` | <CopyableCode code="billingAccountName, billingRoleAssignmentName" /> | Deletes a role assignment on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement. |
| <CopyableCode code="delete_by_billing_profile" /> | `DELETE` | <CopyableCode code="billingAccountName, billingProfileName, billingRoleAssignmentName" /> | Deletes a role assignment on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="delete_by_customer" /> | `DELETE` | <CopyableCode code="billingAccountName, billingProfileName, billingRoleAssignmentName, customerName" /> | Deletes a role assignment on a customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement. |
| <CopyableCode code="delete_by_department" /> | `DELETE` | <CopyableCode code="billingAccountName, billingRoleAssignmentName, departmentName" /> | Deletes a role assignment on a department. The operation is supported only for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="delete_by_enrollment_account" /> | `DELETE` | <CopyableCode code="billingAccountName, billingRoleAssignmentName, enrollmentAccountName" /> | Deletes a role assignment on a enrollment Account. The operation is supported only for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="resolve_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountName" /> | Lists the role assignments for the caller on a billing account while fetching user info for each role assignment. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement. |
| <CopyableCode code="resolve_by_billing_profile" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the role assignments for the caller on an billing profile while fetching user info for each role assignment. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="resolve_by_customer" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, customerName" /> | Lists the role assignments for the caller on a customer while fetching user info for each role assignment. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement. |
| <CopyableCode code="resolve_by_invoice_section" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Lists the role assignments for the caller on an invoice section while fetching user info for each role assignment. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |

## `SELECT` examples

Lists the role assignments for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_assignments', value: 'view', },
        { label: 'role_assignments', value: 'resource', },
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
customerName,
customer_display_name,
customer_id,
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
FROM azure.billing.vw_role_assignments
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.role_assignments
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>role_assignments</code> resource.

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
INSERT INTO azure.billing.role_assignments (
billingAccountName,
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

Deletes the specified <code>role_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.billing.role_assignments
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingRoleAssignmentName = '{{ billingRoleAssignmentName }}';
```
