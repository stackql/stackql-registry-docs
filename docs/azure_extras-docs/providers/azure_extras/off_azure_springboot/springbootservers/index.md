---
title: springbootservers
hide_title: false
hide_table_of_contents: false
keywords:
  - springbootservers
  - off_azure_springboot
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

Creates, updates, deletes, gets or lists a <code>springbootservers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>springbootservers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.off_azure_springboot.springbootservers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_springbootservers', value: 'view', },
        { label: 'springbootservers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="fqdn_and_ip_address_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="labels" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_arm_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="port" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spring_boot_apps" /> | `text` | field from the `properties` object |
| <CopyableCode code="springbootserversName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_apps" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The springbootservers resource definition. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, springbootserversName, subscriptionId" /> | List springbootservers resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List springbootservers resource by resourceGroup |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="siteName, subscriptionId" /> | List springbootservers resource by subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, siteName, springbootserversName, subscriptionId" /> | Create springbootservers resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, siteName, springbootserversName, subscriptionId" /> | Delete springbootservers resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, siteName, springbootserversName, subscriptionId" /> | Update springbootservers resource. |

## `SELECT` examples

List springbootservers resource by subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_springbootservers', value: 'view', },
        { label: 'springbootservers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
errors,
fqdn_and_ip_address_list,
labels,
machine_arm_id,
port,
provisioning_state,
resourceGroupName,
server,
siteName,
spring_boot_apps,
springbootserversName,
subscriptionId,
total_apps
FROM azure_extras.off_azure_springboot.vw_springbootservers
WHERE siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.off_azure_springboot.springbootservers
WHERE siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>springbootservers</code> resource.

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
INSERT INTO azure_extras.off_azure_springboot.springbootservers (
resourceGroupName,
siteName,
springbootserversName,
subscriptionId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ siteName }}',
'{{ springbootserversName }}',
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
        - name: port
          value: integer
        - name: server
          value: string
        - name: fqdnAndIpAddressList
          value:
            - string
        - name: machineArmId
          value: string
        - name: totalApps
          value: integer
        - name: springBootApps
          value: integer
        - name: errors
          value:
            - - name: id
                value: integer
              - name: code
                value: string
              - name: summaryMessage
                value: string
              - name: runAsAccountId
                value: string
              - name: message
                value: string
              - name: possibleCauses
                value: string
              - name: recommendedAction
                value: string
              - name: severity
                value: string
              - name: updatedTimeStamp
                value: string
        - name: provisioningState
          value: string
        - name: labels
          value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>springbootservers</code> resource.

```sql
/*+ update */
UPDATE azure_extras.off_azure_springboot.springbootservers
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND springbootserversName = '{{ springbootserversName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>springbootservers</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.off_azure_springboot.springbootservers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND springbootserversName = '{{ springbootserversName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
