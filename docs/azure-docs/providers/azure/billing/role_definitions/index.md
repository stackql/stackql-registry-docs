---
title: role_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - role_definitions
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

Creates, updates, deletes, gets or lists a <code>role_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.role_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_definitions', value: 'view', },
        { label: 'role_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="customerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="permissions" /> | `text` | field from the `properties` object |
| <CopyableCode code="roleDefinitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a role definition. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName, roleDefinitionName" /> | Gets the definition for a role on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement. |
| <CopyableCode code="get_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, roleDefinitionName" /> | Gets the definition for a role on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="get_by_customer" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, customerName, roleDefinitionName" /> | Gets the definition for a role on a customer. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
| <CopyableCode code="get_by_department" /> | `SELECT` | <CopyableCode code="billingAccountName, departmentName, roleDefinitionName" /> | Gets the definition for a role on a department. The operation is supported for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="get_by_enrollment_account" /> | `SELECT` | <CopyableCode code="billingAccountName, enrollmentAccountName, roleDefinitionName" /> | Gets the definition for a role on an enrollment account. The operation is supported for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the role definitions for a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the role definitions for a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement. |
| <CopyableCode code="list_by_customer" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, customerName" /> | Lists the role definitions for a customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement. |
| <CopyableCode code="list_by_department" /> | `SELECT` | <CopyableCode code="billingAccountName, departmentName" /> | List the definition for a department. The operation is supported for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="list_by_enrollment_account" /> | `SELECT` | <CopyableCode code="billingAccountName, enrollmentAccountName" /> | List the definition for an enrollment account. The operation is supported for billing accounts with agreement type Enterprise Agreement. |

## `SELECT` examples

Lists the role definitions for a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_definitions', value: 'view', },
        { label: 'role_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
billingAccountName,
billingProfileName,
customerName,
permissions,
roleDefinitionName,
role_name,
tags
FROM azure.billing.vw_role_definitions
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.role_definitions
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>

