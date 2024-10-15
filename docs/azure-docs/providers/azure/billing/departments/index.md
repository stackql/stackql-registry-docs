---
title: departments
hide_title: false
hide_table_of_contents: false
keywords:
  - departments
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

Creates, updates, deletes, gets or lists a <code>departments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>departments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.departments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_departments', value: 'view', },
        { label: 'departments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cost_center" /> | `text` | field from the `properties` object |
| <CopyableCode code="departmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Optional grouping of enrollment accounts to segment costs into logical groupings and set budgets. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName, departmentName" /> | Gets a department by ID. The operation is supported only for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the departments that a user has access to. The operation is supported only for billing accounts with agreement type Enterprise Agreement. |

## `SELECT` examples

Lists the departments that a user has access to. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_departments', value: 'view', },
        { label: 'departments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
billingAccountName,
cost_center,
departmentName,
display_name,
status,
tags
FROM azure.billing.vw_departments
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.departments
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>

