---
title: server_advanced_threat_protection_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - server_advanced_threat_protection_settings
  - sql
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

Creates, updates, deletes, gets or lists a <code>server_advanced_threat_protection_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_advanced_threat_protection_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_advanced_threat_protection_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_advanced_threat_protection_settings', value: 'view', },
        { label: 'server_advanced_threat_protection_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="advancedThreatProtectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of an Advanced Threat Protection state. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="advancedThreatProtectionName, resourceGroupName, serverName, subscriptionId" /> | Get a server's Advanced Threat Protection state. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Get a list of the server's Advanced Threat Protection states. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="advancedThreatProtectionName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates an Advanced Threat Protection state. |

## `SELECT` examples

Get a list of the server's Advanced Threat Protection states.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_advanced_threat_protection_settings', value: 'view', },
        { label: 'server_advanced_threat_protection_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
advancedThreatProtectionName,
creation_time,
resourceGroupName,
serverName,
state,
subscriptionId,
system_data
FROM azure.sql.vw_server_advanced_threat_protection_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.sql.server_advanced_threat_protection_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_advanced_threat_protection_settings</code> resource.

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
INSERT INTO azure.sql.server_advanced_threat_protection_settings (
advancedThreatProtectionName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ advancedThreatProtectionName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: state
          value: string
        - name: creationTime
          value: string

```
</TabItem>
</Tabs>
