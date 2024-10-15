---
title: access_control_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - access_control_lists
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

Creates, updates, deletes, gets or lists a <code>access_control_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_control_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.access_control_lists" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_control_lists', value: 'view', },
        { label: 'access_control_lists', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessControlListName" /> | `text` | field from the `properties` object |
| <CopyableCode code="acls_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="dynamic_match_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_synced_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="match_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Access Control List Properties defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessControlListName, resourceGroupName, subscriptionId" /> | Implements Access Control List GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Implements AccessControlLists list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Implements AccessControlLists list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accessControlListName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Implements Access Control List PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessControlListName, resourceGroupName, subscriptionId" /> | Implements Access Control List DELETE method. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accessControlListName, resourceGroupName, subscriptionId" /> | API to update certain properties of the Access Control List resource. |
| <CopyableCode code="resync" /> | `EXEC` | <CopyableCode code="accessControlListName, resourceGroupName, subscriptionId" /> | Implements the operation to the underlying resources. |
| <CopyableCode code="validate_configuration" /> | `EXEC` | <CopyableCode code="accessControlListName, resourceGroupName, subscriptionId" /> | Implements the operation to the underlying resources. |

## `SELECT` examples

Implements AccessControlLists list by subscription GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_control_lists', value: 'view', },
        { label: 'access_control_lists', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accessControlListName,
acls_url,
administrative_state,
annotation,
configuration_state,
configuration_type,
default_action,
dynamic_match_configurations,
last_synced_time,
location,
match_configurations,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.managed_network_fabric.vw_access_control_lists
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.access_control_lists
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_control_lists</code> resource.

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
INSERT INTO azure.managed_network_fabric.access_control_lists (
accessControlListName,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ accessControlListName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: annotation
          value: string
        - name: configurationType
          value: string
        - name: aclsUrl
          value: string
        - name: defaultAction
          value: []
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
                  - - name: etherTypes
                      value:
                        - string
                    - name: fragments
                      value:
                        - string
                    - name: ipLengths
                      value:
                        - string
                    - name: ttlValues
                      value:
                        - string
                    - name: dscpMarkings
                      value:
                        - string
                    - name: portCondition
                      value:
                        - name: flags
                          value:
                            - string
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
                    - name: counterName
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
        - name: lastSyncedTime
          value: string
        - name: configurationState
          value: []
        - name: provisioningState
          value: []
        - name: administrativeState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>access_control_lists</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.access_control_lists
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
accessControlListName = '{{ accessControlListName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>access_control_lists</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.access_control_lists
WHERE accessControlListName = '{{ accessControlListName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
