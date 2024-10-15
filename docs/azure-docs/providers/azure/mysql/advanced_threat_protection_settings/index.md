---
title: advanced_threat_protection_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - advanced_threat_protection_settings
  - mysql
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

Creates, updates, deletes, gets or lists a <code>advanced_threat_protection_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>advanced_threat_protection_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.advanced_threat_protection_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_advanced_threat_protection_settings', value: 'view', },
        { label: 'advanced_threat_protection_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="advancedThreatProtectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of an Advanced Threat Protection setting. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="advancedThreatProtectionName, resourceGroupName, serverName, subscriptionId" /> | Get a server's Advanced Threat Protection state |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server's Advanced Threat Protection states. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="advancedThreatProtectionName, resourceGroupName, serverName, subscriptionId" /> | Updates a server's Advanced Threat Protection state. |
| <CopyableCode code="update_put" /> | `EXEC` | <CopyableCode code="advancedThreatProtectionName, resourceGroupName, serverName, subscriptionId" /> | Updates a server's Advanced Threat Protection state. |

## `SELECT` examples

Gets a list of server's Advanced Threat Protection states.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_advanced_threat_protection_settings', value: 'view', },
        { label: 'advanced_threat_protection_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
advancedThreatProtectionName,
creation_time,
provisioning_state,
resourceGroupName,
serverName,
state,
subscriptionId
FROM azure.mysql.vw_advanced_threat_protection_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.mysql.advanced_threat_protection_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>advanced_threat_protection_settings</code> resource.

```sql
/*+ update */
UPDATE azure.mysql.advanced_threat_protection_settings
SET 
properties = '{{ properties }}'
WHERE 
advancedThreatProtectionName = '{{ advancedThreatProtectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
