---
title: elastic_sans
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_sans
  - elastic_san
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

Creates, updates, deletes, gets or lists a <code>elastic_sans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>elastic_sans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.elastic_san.elastic_sans" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_elastic_sans', value: 'view', },
        { label: 'elastic_sans', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availability_zones" /> | `text` | field from the `properties` object |
| <CopyableCode code="base_size_tib" /> | `text` | field from the `properties` object |
| <CopyableCode code="elasticSanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_capacity_size_tib" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="total_iops" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_mbps" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_size_tib" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_volume_size_gib" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_group_count" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Elastic San response properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId" /> | Get a ElasticSan. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of ElasticSan in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of ElasticSans in a subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Create ElasticSan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId" /> | Delete a Elastic San. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId" /> | Update a Elastic San. |

## `SELECT` examples

Gets a list of ElasticSans in a subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_elastic_sans', value: 'view', },
        { label: 'elastic_sans', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
availability_zones,
base_size_tib,
elasticSanName,
extended_capacity_size_tib,
location,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
sku,
subscriptionId,
tags,
total_iops,
total_mbps,
total_size_tib,
total_volume_size_gib,
volume_group_count
FROM azure.elastic_san.vw_elastic_sans
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.elastic_san.elastic_sans
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>elastic_sans</code> resource.

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
INSERT INTO azure.elastic_san.elastic_sans (
elasticSanName,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ elasticSanName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
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
        - name: sku
          value:
            - name: name
              value: string
            - name: tier
              value: []
            - name: size
              value: string
            - name: family
              value: string
            - name: capacity
              value: integer
        - name: availabilityZones
          value:
            - []
        - name: provisioningState
          value: []
        - name: baseSizeTiB
          value: integer
        - name: extendedCapacitySizeTiB
          value: integer
        - name: totalVolumeSizeGiB
          value: integer
        - name: volumeGroupCount
          value: integer
        - name: totalIops
          value: integer
        - name: totalMBps
          value: integer
        - name: totalSizeTiB
          value: integer
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: []
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: groupIds
                    value:
                      - string
              - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: systemData
                value:
                  - name: createdBy
                    value: string
                  - name: createdByType
                    value: string
                  - name: createdAt
                    value: string
                  - name: lastModifiedBy
                    value: string
                  - name: lastModifiedByType
                    value: string
                  - name: lastModifiedAt
                    value: string
        - name: publicNetworkAccess
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>elastic_sans</code> resource.

```sql
/*+ update */
UPDATE azure.elastic_san.elastic_sans
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
elasticSanName = '{{ elasticSanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>elastic_sans</code> resource.

```sql
/*+ delete */
DELETE FROM azure.elastic_san.elastic_sans
WHERE elasticSanName = '{{ elasticSanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
