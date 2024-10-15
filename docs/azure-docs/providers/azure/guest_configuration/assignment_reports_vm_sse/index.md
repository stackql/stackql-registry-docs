---
title: assignment_reports_vm_sse
hide_title: false
hide_table_of_contents: false
keywords:
  - assignment_reports_vm_sse
  - guest_configuration
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

Creates, updates, deletes, gets or lists a <code>assignment_reports_vm_sse</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignment_reports_vm_sse</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.guest_configuration.assignment_reports_vm_sse" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assignment_reports_vm_sse', value: 'view', },
        { label: 'assignment_reports_vm_sse', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ARM resource id of the report for the guest configuration assignment. |
| <CopyableCode code="name" /> | `text` | GUID that identifies the guest configuration assignment report under a subscription, resource group. |
| <CopyableCode code="assignment" /> | `text` | field from the `properties` object |
| <CopyableCode code="compliance_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="details" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="report_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmssName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmss_resource_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ARM resource id of the report for the guest configuration assignment. |
| <CopyableCode code="name" /> | `string` | GUID that identifies the guest configuration assignment report under a subscription, resource group. |
| <CopyableCode code="properties" /> | `object` | Report for the guest configuration assignment. Report contains information such as compliance status, reason, and more. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, name, resourceGroupName, subscriptionId, vmssName" /> | Get a report for the VMSS guest configuration assignment, by reportId. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, vmssName" /> | List all reports for the VMSS guest configuration assignment, latest report first. |

## `SELECT` examples

List all reports for the VMSS guest configuration assignment, latest report first.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assignment_reports_vm_sse', value: 'view', },
        { label: 'assignment_reports_vm_sse', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
assignment,
compliance_status,
details,
end_time,
report_id,
resourceGroupName,
start_time,
subscriptionId,
vm,
vmssName,
vmss_resource_id
FROM azure.guest_configuration.vw_assignment_reports_vm_sse
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmssName = '{{ vmssName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties
FROM azure.guest_configuration.assignment_reports_vm_sse
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmssName = '{{ vmssName }}';
```
</TabItem></Tabs>

