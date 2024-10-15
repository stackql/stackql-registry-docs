---
title: ip_communities
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_communities
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

Creates, updates, deletes, gets or lists a <code>ip_communities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_communities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.ip_communities" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ip_communities', value: 'view', },
        { label: 'ip_communities', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipCommunityName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_community_rules" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | IP Community Properties defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ipCommunityName, resourceGroupName, subscriptionId" /> | Implements an IP Community GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Implements IP Communities list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Implements IP Communities list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="ipCommunityName, resourceGroupName, subscriptionId, data__properties" /> | Implements an IP Community PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ipCommunityName, resourceGroupName, subscriptionId" /> | Implements IP Community DELETE method. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="ipCommunityName, resourceGroupName, subscriptionId" /> | API to update certain properties of the IP Community resource. |

## `SELECT` examples

Implements IP Communities list by subscription GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ip_communities', value: 'view', },
        { label: 'ip_communities', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrative_state,
annotation,
configuration_state,
ipCommunityName,
ip_community_rules,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.managed_network_fabric.vw_ip_communities
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.ip_communities
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ip_communities</code> resource.

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
INSERT INTO azure.managed_network_fabric.ip_communities (
ipCommunityName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ ipCommunityName }}',
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
        - name: ipCommunityRules
          value:
            - - name: action
                value: []
              - name: sequenceNumber
                value: integer
              - name: wellKnownCommunities
                value:
                  - string
              - name: communityMembers
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

Updates a <code>ip_communities</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.ip_communities
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
ipCommunityName = '{{ ipCommunityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>ip_communities</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.ip_communities
WHERE ipCommunityName = '{{ ipCommunityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
