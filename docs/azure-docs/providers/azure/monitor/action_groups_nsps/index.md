---
title: action_groups_nsps
hide_title: false
hide_table_of_contents: false
keywords:
  - action_groups_nsps
  - monitor
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

Creates, updates, deletes, gets or lists a <code>action_groups_nsps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>action_groups_nsps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.action_groups_nsps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_action_groups_nsps', value: 'view', },
        { label: 'action_groups_nsps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="actionGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkSecurityPerimeterConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_security_perimeter" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_issues" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_association" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="properties" /> | `object` | Network security configuration properties. |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionGroupName, networkSecurityPerimeterConfigurationName, resourceGroupName, subscriptionId" /> | Gets a specified NSP configuration for specified action group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="actionGroupName, resourceGroupName, subscriptionId" /> | Gets a list of NSP configurations for specified action group. |

## `SELECT` examples

Gets a list of NSP configurations for specified action group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_action_groups_nsps', value: 'view', },
        { label: 'action_groups_nsps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
actionGroupName,
networkSecurityPerimeterConfigurationName,
network_security_perimeter,
profile,
provisioning_issues,
provisioning_state,
resourceGroupName,
resource_association,
subscriptionId,
type
FROM azure.monitor.vw_action_groups_nsps
WHERE actionGroupName = '{{ actionGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.monitor.action_groups_nsps
WHERE actionGroupName = '{{ actionGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

