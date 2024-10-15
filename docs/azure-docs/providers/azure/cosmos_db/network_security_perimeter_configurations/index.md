---
title: network_security_perimeter_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_configurations
  - cosmos_db
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.network_security_perimeter_configurations" /></td></tr>
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
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkSecurityPerimeterConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_security_perimeter" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_issues" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_association" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Network security configuration properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, networkSecurityPerimeterConfigurationName, resourceGroupName, subscriptionId" /> | Gets effective Network Security Perimeter Configuration for association |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets list of effective Network Security Perimeter Configuration for cosmos db account |
| <CopyableCode code="reconcile" /> | `EXEC` | <CopyableCode code="accountName, networkSecurityPerimeterConfigurationName, resourceGroupName, subscriptionId" /> | Refreshes any information about the association. |

## `SELECT` examples

Gets list of effective Network Security Perimeter Configuration for cosmos db account

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
accountName,
networkSecurityPerimeterConfigurationName,
network_security_perimeter,
profile,
provisioning_issues,
provisioning_state,
resourceGroupName,
resource_association,
subscriptionId
FROM azure.cosmos_db.vw_network_security_perimeter_configurations
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cosmos_db.network_security_perimeter_configurations
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

