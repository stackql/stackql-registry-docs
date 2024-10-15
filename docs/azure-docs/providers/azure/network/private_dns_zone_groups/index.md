---
title: private_dns_zone_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - private_dns_zone_groups
  - network
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

Creates, updates, deletes, gets or lists a <code>private_dns_zone_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_dns_zone_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.private_dns_zone_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_dns_zone_groups', value: 'view', },
        { label: 'private_dns_zone_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="privateDnsZoneGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateEndpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_dns_zone_configs" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the private dns zone group. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateDnsZoneGroupName, privateEndpointName, resourceGroupName, subscriptionId" /> | Gets the private dns zone group resource by specified private dns zone group name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateEndpointName, resourceGroupName, subscriptionId" /> | Gets all private dns zone groups in a private endpoint. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateDnsZoneGroupName, privateEndpointName, resourceGroupName, subscriptionId" /> | Creates or updates a private dns zone group in the specified private endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateDnsZoneGroupName, privateEndpointName, resourceGroupName, subscriptionId" /> | Deletes the specified private dns zone group. |

## `SELECT` examples

Gets all private dns zone groups in a private endpoint.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_dns_zone_groups', value: 'view', },
        { label: 'private_dns_zone_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
privateDnsZoneGroupName,
privateEndpointName,
private_dns_zone_configs,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.network.vw_private_dns_zone_groups
WHERE privateEndpointName = '{{ privateEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties
FROM azure.network.private_dns_zone_groups
WHERE privateEndpointName = '{{ privateEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_dns_zone_groups</code> resource.

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
INSERT INTO azure.network.private_dns_zone_groups (
privateDnsZoneGroupName,
privateEndpointName,
resourceGroupName,
subscriptionId,
name,
properties,
id
)
SELECT 
'{{ privateDnsZoneGroupName }}',
'{{ privateEndpointName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ name }}',
'{{ properties }}',
'{{ id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: etag
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: privateDnsZoneConfigs
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: privateDnsZoneId
                    value: string
                  - name: recordSets
                    value:
                      - - name: recordType
                          value: string
                        - name: recordSetName
                          value: string
                        - name: fqdn
                          value: string
                        - name: ttl
                          value: integer
                        - name: ipAddresses
                          value:
                            - string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>private_dns_zone_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.private_dns_zone_groups
WHERE privateDnsZoneGroupName = '{{ privateDnsZoneGroupName }}'
AND privateEndpointName = '{{ privateEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
