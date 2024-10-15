---
title: ip_extended_communities
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_extended_communities
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

Creates, updates, deletes, gets or lists a <code>ip_extended_communities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_extended_communities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.ip_extended_communities" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ip_extended_communities', value: 'view', },
        { label: 'ip_extended_communities', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipExtendedCommunityName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_extended_community_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | IP Extended Community Properties defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ipExtendedCommunityName, resourceGroupName, subscriptionId" /> | Implements IP Extended Community GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Implements IpExtendedCommunities list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Implements IpExtendedCommunities list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="ipExtendedCommunityName, resourceGroupName, subscriptionId, data__properties" /> | Implements IP Extended Community PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ipExtendedCommunityName, resourceGroupName, subscriptionId" /> | Implements IP Extended Community DELETE method. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="ipExtendedCommunityName, resourceGroupName, subscriptionId" /> | API to update certain properties of the IP Extended Community resource. |

## `SELECT` examples

Implements IpExtendedCommunities list by subscription GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ip_extended_communities', value: 'view', },
        { label: 'ip_extended_communities', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrative_state,
annotation,
configuration_state,
ipExtendedCommunityName,
ip_extended_community_rules,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.managed_network_fabric.vw_ip_extended_communities
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.ip_extended_communities
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ip_extended_communities</code> resource.

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
INSERT INTO azure.managed_network_fabric.ip_extended_communities (
ipExtendedCommunityName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ ipExtendedCommunityName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: ipExtendedCommunityRules
          value:
            - - name: action
                value: []
              - name: sequenceNumber
                value: integer
              - name: routeTargets
                value:
                  - string
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

Updates a <code>ip_extended_communities</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.ip_extended_communities
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
ipExtendedCommunityName = '{{ ipExtendedCommunityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>ip_extended_communities</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.ip_extended_communities
WHERE ipExtendedCommunityName = '{{ ipExtendedCommunityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
