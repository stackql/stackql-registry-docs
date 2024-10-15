---
title: watchers
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers
  - db_watcher
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

Creates, updates, deletes, gets or lists a <code>watchers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>watchers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.db_watcher.watchers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_watchers', value: 'view', },
        { label: 'watchers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="datastore" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_alert_rule_identity_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="watcherName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The RP specific properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, watcherName" /> | Get a Watcher |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List Watcher resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Watcher resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, watcherName" /> | Create a Watcher |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, watcherName" /> | Delete a Watcher |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, watcherName" /> | Update a Watcher |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, watcherName" /> | The action to start monitoring all targets configured for a database watcher. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, watcherName" /> | The action to stop monitoring all targets configured for a database watcher. |

## `SELECT` examples

List Watcher resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_watchers', value: 'view', },
        { label: 'watchers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
datastore,
default_alert_rule_identity_resource_id,
identity,
location,
provisioning_state,
resourceGroupName,
status,
subscriptionId,
tags,
watcherName
FROM azure.db_watcher.vw_watchers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.db_watcher.watchers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>watchers</code> resource.

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
INSERT INTO azure.db_watcher.watchers (
resourceGroupName,
subscriptionId,
watcherName,
properties,
identity,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ watcherName }}',
'{{ properties }}',
'{{ identity }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: datastore
          value:
            - name: adxClusterResourceId
              value: string
            - name: kustoClusterDisplayName
              value: string
            - name: kustoClusterUri
              value: string
            - name: kustoDataIngestionUri
              value: string
            - name: kustoDatabaseName
              value: string
            - name: kustoManagementUrl
              value: string
            - name: kustoOfferingType
              value: []
        - name: status
          value: []
        - name: provisioningState
          value: []
        - name: defaultAlertRuleIdentityResourceId
          value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>watchers</code> resource.

```sql
/*+ update */
UPDATE azure.db_watcher.watchers
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watcherName = '{{ watcherName }}';
```

## `DELETE` example

Deletes the specified <code>watchers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.db_watcher.watchers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watcherName = '{{ watcherName }}';
```
