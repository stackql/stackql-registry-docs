---
title: network_security_perimeter_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_configurations
  - bot_service
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

Creates, updates, deletes, gets or lists a <code>network_security_perimeter_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_security_perimeter_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.network_security_perimeter_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_security_perimeter_configurations', value: 'view', },
        { label: 'network_security_perimeter_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified identifier of the resource |
| <CopyableCode code="name" /> | `text` | Name of the resource |
| <CopyableCode code="networkSecurityPerimeterConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_security_perimeter" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_issues" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_association" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the resource |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the resource |
| <CopyableCode code="name" /> | `string` | Name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of Network Security Perimeter configuration |
| <CopyableCode code="type" /> | `string` | Type of the resource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkSecurityPerimeterConfigurationName, resourceGroupName, resourceName, subscriptionId" /> | Gets the specified Network Security Perimeter configuration associated with the Bot. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | List Network Security Perimeter configurations associated with the Bot. |
| <CopyableCode code="reconcile" /> | `EXEC` | <CopyableCode code="networkSecurityPerimeterConfigurationName, resourceGroupName, resourceName, subscriptionId" /> | Reconcile the specified Network Security Perimeter configuration associated with the Bot. |

## `SELECT` examples

List Network Security Perimeter configurations associated with the Bot.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_security_perimeter_configurations', value: 'view', },
        { label: 'network_security_perimeter_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
networkSecurityPerimeterConfigurationName,
network_security_perimeter,
profile,
provisioning_issues,
provisioning_state,
resourceGroupName,
resourceName,
resource_association,
subscriptionId,
type
FROM azure.bot_service.vw_network_security_perimeter_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
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
FROM azure.bot_service.network_security_perimeter_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

