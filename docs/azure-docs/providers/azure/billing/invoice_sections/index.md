---
title: invoice_sections
hide_title: false
hide_table_of_contents: false
keywords:
  - invoice_sections
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

Creates, updates, deletes, gets or lists a <code>invoice_sections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invoice_sections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.invoice_sections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_invoice_sections', value: 'view', },
        { label: 'invoice_sections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoiceSectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reason_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
| <CopyableCode code="target_cloud" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | An invoice section. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Gets an invoice section by its ID. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the invoice sections that a user has access to. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Creates or updates an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Deletes an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="validate_delete_eligibility" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Validates if the invoice section can be deleted. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |

## `SELECT` examples

Lists the invoice sections that a user has access to. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_invoice_sections', value: 'view', },
        { label: 'invoice_sections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
billingAccountName,
billingProfileName,
display_name,
invoiceSectionName,
provisioning_state,
reason_code,
state,
system_id,
tags,
target_cloud
FROM azure.billing.vw_invoice_sections
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.invoice_sections
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>invoice_sections</code> resource.

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
INSERT INTO azure.billing.invoice_sections (
billingAccountName,
billingProfileName,
invoiceSectionName,
tags,
properties
)
SELECT 
'{{ billingAccountName }}',
'{{ billingProfileName }}',
'{{ invoiceSectionName }}',
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
        - name: state
          value: string
        - name: reasonCode
          value: string
        - name: systemId
          value: string
        - name: targetCloud
          value: string
        - name: tags
          value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>invoice_sections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.billing.invoice_sections
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}'
AND invoiceSectionName = '{{ invoiceSectionName }}';
```
