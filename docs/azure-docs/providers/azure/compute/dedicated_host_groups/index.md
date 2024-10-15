---
title: dedicated_host_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_host_groups
  - compute
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

Creates, updates, deletes, gets or lists a <code>dedicated_host_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dedicated_host_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.dedicated_host_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dedicated_host_groups', value: 'view', },
        { label: 'dedicated_host_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="additional_capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hosts" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_view" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="platform_fault_domain_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_automatic_placement" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="zones" /> | `text` | Availability Zone to use for this host group. Only single zone is supported. The zone can be assigned only during creation. If not provided, the group supports all zones in the region. If provided, enforces each host in the group to be in the same zone. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Dedicated Host Group Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
| <CopyableCode code="zones" /> | `array` | Availability Zone to use for this host group. Only single zone is supported. The zone can be assigned only during creation. If not provided, the group supports all zones in the region. If provided, enforces each host in the group to be in the same zone. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostGroupName, resourceGroupName, subscriptionId" /> | Retrieves information about a dedicated host group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the dedicated host groups in the specified resource group. Use the nextLink property in the response to get the next page of dedicated host groups. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the dedicated host groups in the subscription. Use the nextLink property in the response to get the next page of dedicated host groups. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hostGroupName, resourceGroupName, subscriptionId" /> | Create or update a dedicated host group. For details of Dedicated Host and Dedicated Host Groups please see [Dedicated Host Documentation] (https://go.microsoft.com/fwlink/?linkid=2082596) |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostGroupName, resourceGroupName, subscriptionId" /> | Delete a dedicated host group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="hostGroupName, resourceGroupName, subscriptionId" /> | Update an dedicated host group. |

## `SELECT` examples

Lists all of the dedicated host groups in the subscription. Use the nextLink property in the response to get the next page of dedicated host groups.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dedicated_host_groups', value: 'view', },
        { label: 'dedicated_host_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
additional_capabilities,
hostGroupName,
hosts,
instance_view,
location,
platform_fault_domain_count,
resourceGroupName,
subscriptionId,
support_automatic_placement,
tags,
type,
zones
FROM azure.compute.vw_dedicated_host_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type,
zones
FROM azure.compute.dedicated_host_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dedicated_host_groups</code> resource.

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
INSERT INTO azure.compute.dedicated_host_groups (
hostGroupName,
resourceGroupName,
subscriptionId,
properties,
zones,
location,
tags
)
SELECT 
'{{ hostGroupName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ zones }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: platformFaultDomainCount
          value: integer
        - name: hosts
          value:
            - - name: id
                value: string
        - name: instanceView
          value:
            - name: hosts
              value:
                - - name: name
                    value: string
                  - name: assetId
                    value: string
                  - name: availableCapacity
                    value:
                      - name: allocatableVMs
                        value:
                          - - name: vmSize
                              value: string
                            - name: count
                              value: number
                  - name: statuses
                    value:
                      - - name: code
                          value: string
                        - name: level
                          value: string
                        - name: displayStatus
                          value: string
                        - name: message
                          value: string
                        - name: time
                          value: string
        - name: supportAutomaticPlacement
          value: boolean
        - name: additionalCapabilities
          value:
            - name: ultraSSDEnabled
              value: boolean
    - name: zones
      value:
        - string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dedicated_host_groups</code> resource.

```sql
/*+ update */
UPDATE azure.compute.dedicated_host_groups
SET 
properties = '{{ properties }}',
zones = '{{ zones }}',
tags = '{{ tags }}'
WHERE 
hostGroupName = '{{ hostGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>dedicated_host_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.dedicated_host_groups
WHERE hostGroupName = '{{ hostGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
