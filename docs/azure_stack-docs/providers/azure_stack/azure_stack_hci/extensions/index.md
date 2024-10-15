---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - azure_stack_hci
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

Creates, updates, deletes, gets or lists a <code>extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.extensions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_extensions', value: 'view', },
        { label: 'extensions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aggregate_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="arcSettingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="extensionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="extension_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="per_node_extension_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Status of Arc Extension for a particular node in HCI Cluster. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId" /> | Get particular Arc Extension of HCI Cluster. |
| <CopyableCode code="list_by_arc_setting" /> | `SELECT` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | List all Extensions under ArcSetting resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId" /> | Create Extension for HCI cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId" /> | Delete particular Arc Extension of HCI Cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId" /> | Update Extension for HCI cluster. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId" /> | Upgrade a particular Arc Extension of HCI Cluster. |

## `SELECT` examples

List all Extensions under ArcSetting resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_extensions', value: 'view', },
        { label: 'extensions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aggregate_state,
arcSettingName,
clusterName,
extensionName,
extension_parameters,
managed_by,
per_node_extension_details,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure_stack.azure_stack_hci.vw_extensions
WHERE arcSettingName = '{{ arcSettingName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_stack.azure_stack_hci.extensions
WHERE arcSettingName = '{{ arcSettingName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>extensions</code> resource.

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
INSERT INTO azure_stack.azure_stack_hci.extensions (
arcSettingName,
clusterName,
extensionName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ arcSettingName }}',
'{{ clusterName }}',
'{{ extensionName }}',
'{{ resourceGroupName }}',
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
        - name: provisioningState
          value: string
        - name: extensionParameters
          value:
            - name: forceUpdateTag
              value: string
            - name: publisher
              value: string
            - name: type
              value: string
            - name: typeHandlerVersion
              value: string
            - name: autoUpgradeMinorVersion
              value: boolean
            - name: settings
              value: object
            - name: protectedSettings
              value: object
            - name: enableAutomaticUpgrade
              value: boolean
        - name: aggregateState
          value: string
        - name: perNodeExtensionDetails
          value:
            - - name: name
                value: string
              - name: extension
                value: string
              - name: typeHandlerVersion
                value: string
              - name: state
                value: string
              - name: instanceView
                value:
                  - name: name
                    value: string
                  - name: type
                    value: string
                  - name: typeHandlerVersion
                    value: string
                  - name: status
                    value:
                      - name: code
                        value: string
                      - name: level
                        value: string
                      - name: displayStatus
                        value: string
                      - name: message
                        value: string
                      - name: time
                        value: string
        - name: managedBy
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>extensions</code> resource.

```sql
/*+ update */
UPDATE azure_stack.azure_stack_hci.extensions
SET 
properties = '{{ properties }}'
WHERE 
arcSettingName = '{{ arcSettingName }}'
AND clusterName = '{{ clusterName }}'
AND extensionName = '{{ extensionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>extensions</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.extensions
WHERE arcSettingName = '{{ arcSettingName }}'
AND clusterName = '{{ clusterName }}'
AND extensionName = '{{ extensionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
