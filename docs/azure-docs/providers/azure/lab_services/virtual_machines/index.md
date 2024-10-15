---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - lab_services
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

Creates, updates, deletes, gets or lists a <code>virtual_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.virtual_machines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machines', value: 'view', },
        { label: 'virtual_machines', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="claimed_by_user_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_operation_error" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualMachineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Virtual machine resource properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, subscriptionId, virtualMachineName" /> | Returns the properties for a lab virtual machine. |
| <CopyableCode code="list_by_lab" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, subscriptionId" /> | Returns a list of all virtual machines for a lab. |
| <CopyableCode code="redeploy" /> | `EXEC` | <CopyableCode code="labName, resourceGroupName, subscriptionId, virtualMachineName" /> | Action to redeploy a lab virtual machine to a different compute node. For troubleshooting connectivity. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="labName, resourceGroupName, subscriptionId, virtualMachineName" /> | Re-image a lab virtual machine. The virtual machine will be deleted and recreated using the latest published snapshot of the reference environment of the lab. |
| <CopyableCode code="reset_password" /> | `EXEC` | <CopyableCode code="labName, resourceGroupName, subscriptionId, virtualMachineName, data__password, data__username" /> | Resets a lab virtual machine password. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="labName, resourceGroupName, subscriptionId, virtualMachineName" /> | Action to start a lab virtual machine. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="labName, resourceGroupName, subscriptionId, virtualMachineName" /> | Action to stop a lab virtual machine. |

## `SELECT` examples

Returns a list of all virtual machines for a lab.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machines', value: 'view', },
        { label: 'virtual_machines', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
claimed_by_user_id,
connection_profile,
labName,
provisioning_state,
resourceGroupName,
resource_operation_error,
state,
subscriptionId,
system_data,
virtualMachineName,
vm_type
FROM azure.lab_services.vw_virtual_machines
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.lab_services.virtual_machines
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

