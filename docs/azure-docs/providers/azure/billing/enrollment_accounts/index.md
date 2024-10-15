---
title: enrollment_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - enrollment_accounts
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

Creates, updates, deletes, gets or lists a <code>enrollment_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enrollment_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.enrollment_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_enrollment_accounts', value: 'view', },
        { label: 'enrollment_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_owner" /> | `text` | field from the `properties` object |
| <CopyableCode code="auth_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cost_center" /> | `text` | field from the `properties` object |
| <CopyableCode code="departmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="department_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="department_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="enrollmentAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_dev_test_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | It is an organizational hierarchy within a billing account to administer and manage azure costs. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName, enrollmentAccountName" /> | Gets an enrollment account by ID. The operation is supported only for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="get_by_department" /> | `SELECT` | <CopyableCode code="billingAccountName, departmentName, enrollmentAccountName" /> | Gets an enrollment account by department. The operation is supported only for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the enrollment accounts for a billing account. The operation is supported only for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="list_by_department" /> | `SELECT` | <CopyableCode code="billingAccountName, departmentName" /> | Lists the enrollment accounts for a department. The operation is supported only for billing accounts with agreement type Enterprise Agreement. |

## `SELECT` examples

Lists the enrollment accounts for a billing account. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_enrollment_accounts', value: 'view', },
        { label: 'enrollment_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
account_owner,
auth_type,
billingAccountName,
cost_center,
departmentName,
department_display_name,
department_id,
display_name,
end_date,
enrollmentAccountName,
is_dev_test_enabled,
start_date,
status,
tags
FROM azure.billing.vw_enrollment_accounts
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.enrollment_accounts
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>

