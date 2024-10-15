---
title: network_tap_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - network_tap_rules
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>network_tap_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_tap_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_tap_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_tap_rules', value: 'view', },
        { label: 'network_tap_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="dynamic_match_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_synced_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="match_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkTapRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_tap_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="polling_interval_in_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tap_rules_url" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Tap Rule Properties defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkTapRuleName, resourceGroupName, subscriptionId" /> | Get Network Tap Rule resource details. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the Network Tap Rule resources in the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the Network Tap Rule resources in the given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkTapRuleName, resourceGroupName, subscriptionId, data__properties" /> | Create Network Tap Rule resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkTapRuleName, resourceGroupName, subscriptionId" /> | Delete Network Tap Rule resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkTapRuleName, resourceGroupName, subscriptionId" /> | Update certain properties of the Network Tap Rule resource. |
| <CopyableCode code="resync" /> | `EXEC` | <CopyableCode code="networkTapRuleName, resourceGroupName, subscriptionId" /> | Implements the operation to the underlying resources. |
| <CopyableCode code="validate_configuration" /> | `EXEC` | <CopyableCode code="networkTapRuleName, resourceGroupName, subscriptionId" /> | Implements the operation to the underlying resources. |

## `SELECT` examples

List all the Network Tap Rule resources in the given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_tap_rules', value: 'view', },
        { label: 'network_tap_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrative_state,
annotation,
configuration_state,
configuration_type,
dynamic_match_configurations,
last_synced_time,
location,
match_configurations,
networkTapRuleName,
network_tap_id,
polling_interval_in_seconds,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
tap_rules_url
FROM azure.managed_network_fabric.vw_network_tap_rules
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.network_tap_rules
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_tap_rules</code> resource.

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
INSERT INTO azure.managed_network_fabric.network_tap_rules (
networkTapRuleName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ networkTapRuleName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
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
        - name: annotation
          value: string
        - name: configurationType
          value: string
        - name: tapRulesUrl
          value: string
        - name: matchConfigurations
          value:
            - - name: matchConfigurationName
                value: string
              - name: sequenceNumber
                value: integer
              - name: ipAddressType
                value: []
              - name: matchConditions
                value:
                  - - name: encapsulationType
                      value: string
                    - name: portCondition
                      value:
                        - name: portType
                          value: string
                        - name: layer4Protocol
                          value: string
                        - name: ports
                          value:
                            - string
                        - name: portGroupNames
                          value:
                            - string
                    - name: protocolTypes
                      value:
                        - string
                    - name: vlanMatchCondition
                      value:
                        - name: vlans
                          value:
                            - string
                        - name: innerVlans
                          value:
                            - string
                        - name: vlanGroupNames
                          value:
                            - string
                    - name: ipCondition
                      value:
                        - name: type
                          value: string
                        - name: prefixType
                          value: string
                        - name: ipPrefixValues
                          value:
                            - string
                        - name: ipGroupNames
                          value:
                            - string
              - name: actions
                value:
                  - - name: type
                      value: string
                    - name: truncate
                      value: string
                    - name: isTimestampEnabled
                      value: []
                    - name: destinationId
                      value: string
                    - name: matchConfigurationName
                      value: string
        - name: dynamicMatchConfigurations
          value:
            - - name: ipGroups
                value:
                  - - name: name
                      value: string
                    - name: ipPrefixes
                      value:
                        - string
              - name: vlanGroups
                value:
                  - - name: name
                      value: string
                    - name: vlans
                      value:
                        - string
              - name: portGroups
                value:
                  - - name: name
                      value: string
                    - name: ports
                      value:
                        - string
        - name: networkTapId
          value: string
        - name: pollingIntervalInSeconds
          value: integer
        - name: lastSyncedTime
          value: string
        - name: configurationState
          value: []
        - name: provisioningState
          value: []
        - name: administrativeState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_tap_rules</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.network_tap_rules
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
networkTapRuleName = '{{ networkTapRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_tap_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.network_tap_rules
WHERE networkTapRuleName = '{{ networkTapRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
