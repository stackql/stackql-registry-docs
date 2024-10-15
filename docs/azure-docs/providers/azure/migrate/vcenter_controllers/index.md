---
title: vcenter_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - vcenter_controllers
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

Creates, updates, deletes, gets or lists a <code>vcenter_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vcenter_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.vcenter_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vcenter_controllers', value: 'view', },
        { label: 'vcenter_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="perf_statistics_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="port" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_as_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="vcenterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of VMwareSiteResource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, vcenterName" /> | Get a Vcenter |
| <CopyableCode code="list_by_vmware_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List Vcenter resources by VmwareSite |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, vcenterName" /> | Create a Vcenter |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, vcenterName" /> | Delete a Vcenter |

## `SELECT` examples

List Vcenter resources by VmwareSite

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vcenter_controllers', value: 'view', },
        { label: 'vcenter_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
created_timestamp,
errors,
fqdn,
friendly_name,
instance_uuid,
perf_statistics_level,
port,
provisioning_state,
resourceGroupName,
run_as_account_id,
siteName,
subscriptionId,
updated_timestamp,
vcenterName,
version
FROM azure.migrate.vw_vcenter_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.vcenter_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vcenter_controllers</code> resource.

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
INSERT INTO azure.migrate.vcenter_controllers (
resourceGroupName,
siteName,
subscriptionId,
vcenterName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ siteName }}',
'{{ subscriptionId }}',
'{{ vcenterName }}',
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
        - name: runAsAccountId
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
        - name: createdTimestamp
          value: string
        - name: updatedTimestamp
          value: string
        - name: fqdn
          value: string
        - name: port
          value: string
        - name: version
          value: string
        - name: perfStatisticsLevel
          value: string
        - name: instanceUuid
          value: string
        - name: friendlyName
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>vcenter_controllers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.migrate.vcenter_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vcenterName = '{{ vcenterName }}';
```
