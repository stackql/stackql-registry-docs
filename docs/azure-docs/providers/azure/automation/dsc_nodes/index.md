---
title: dsc_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_nodes
  - automation
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

Creates, updates, deletes, gets or lists a <code>dsc_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dsc_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.dsc_nodes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dsc_nodes', value: 'view', },
        { label: 'dsc_nodes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="extension_handler" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_seen" /> | `text` | field from the `properties` object |
| <CopyableCode code="nodeId" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_count" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a DscNode |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, nodeId, resourceGroupName, subscriptionId" /> | Retrieve the dsc node identified by node id. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of dsc nodes. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, nodeId, resourceGroupName, subscriptionId" /> | Delete the dsc node identified by node id. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="automationAccountName, nodeId, resourceGroupName, subscriptionId" /> | Update the dsc node. |

## `SELECT` examples

Retrieve a list of dsc nodes.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dsc_nodes', value: 'view', },
        { label: 'dsc_nodes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
account_id,
automationAccountName,
etag,
extension_handler,
ip,
last_seen,
nodeId,
node_configuration,
node_id,
registration_time,
resourceGroupName,
status,
subscriptionId,
total_count
FROM azure.automation.vw_dsc_nodes
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.automation.dsc_nodes
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>dsc_nodes</code> resource.

```sql
/*+ update */
UPDATE azure.automation.dsc_nodes
SET 
nodeId = '{{ nodeId }}',
properties = '{{ properties }}'
WHERE 
automationAccountName = '{{ automationAccountName }}'
AND nodeId = '{{ nodeId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>dsc_nodes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.dsc_nodes
WHERE automationAccountName = '{{ automationAccountName }}'
AND nodeId = '{{ nodeId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
