---
title: hyperv_host_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - hyperv_host_controllers
  - migrate
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

Creates, updates, deletes, gets or lists a <code>hyperv_host_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hyperv_host_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.hyperv_host_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hyperv_host_controllers', value: 'view', },
        { label: 'hyperv_host_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_as_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of Hyperv Host |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostName, resourceGroupName, siteName, subscriptionId" /> | Get a HypervHost |
| <CopyableCode code="list_by_hyperv_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List HypervHost resources by HypervSite |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="hostName, resourceGroupName, siteName, subscriptionId" /> | Create a HypervHost |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostName, resourceGroupName, siteName, subscriptionId" /> | Delete a HypervHost |

## `SELECT` examples

List HypervHost resources by HypervSite

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hyperv_host_controllers', value: 'view', },
        { label: 'hyperv_host_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
created_timestamp,
errors,
fqdn,
hostName,
provisioning_state,
resourceGroupName,
run_as_account_id,
siteName,
subscriptionId,
updated_timestamp,
version
FROM azure.migrate.vw_hyperv_host_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.hyperv_host_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hyperv_host_controllers</code> resource.

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
INSERT INTO azure.migrate.hyperv_host_controllers (
hostName,
resourceGroupName,
siteName,
subscriptionId,
properties
)
SELECT 
'{{ hostName }}',
'{{ resourceGroupName }}',
'{{ siteName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: createdTimestamp
          value: string
        - name: updatedTimestamp
          value: string
        - name: fqdn
          value: string
        - name: runAsAccountId
          value: string
        - name: version
          value: string
        - name: errors
          value:
            - - name: message
                value: string
              - name: messageParameters
                value: object
              - name: applianceName
                value: string
              - name: id
                value: integer
              - name: code
                value: string
              - name: possibleCauses
                value: string
              - name: recommendedAction
                value: string
              - name: severity
                value: string
              - name: summaryMessage
                value: string
              - name: source
                value: []
              - name: updatedTimeStamp
                value: string
              - name: runAsAccountId
                value: string
              - name: discoveryScope
                value: []
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>hyperv_host_controllers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.migrate.hyperv_host_controllers
WHERE hostName = '{{ hostName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
