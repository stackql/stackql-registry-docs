---
title: private_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - private_zones
  - private_dns
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

Creates, updates, deletes, gets or lists a <code>private_zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.private_dns.private_zones" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_zones', value: 'view', },
        { label: 'private_zones', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `text` | The ETag of the zone. |
| <CopyableCode code="internal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The Azure Region where the resource lives |
| <CopyableCode code="max_number_of_record_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_number_of_virtual_network_links" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_number_of_virtual_network_links_with_registration" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_record_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_virtual_network_links" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_virtual_network_links_with_registration" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateZoneName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The ETag of the zone. |
| <CopyableCode code="location" /> | `string` | The Azure Region where the resource lives |
| <CopyableCode code="properties" /> | `object` | Represents the properties of the Private DNS zone. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Gets a Private DNS zone. Retrieves the zone properties, but not the virtual networks links or the record sets within the zone. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the Private DNS zones in all resource groups in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the Private DNS zones within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Creates or updates a Private DNS zone. Does not modify Links to virtual networks or DNS records within the zone. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Deletes a Private DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone. Private DNS zone cannot be deleted unless all virtual network links to it are removed. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Updates a Private DNS zone. Does not modify virtual network links or DNS records within the zone. |

## `SELECT` examples

Lists the Private DNS zones in all resource groups in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_zones', value: 'view', },
        { label: 'private_zones', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
etag,
internal_id,
location,
max_number_of_record_sets,
max_number_of_virtual_network_links,
max_number_of_virtual_network_links_with_registration,
number_of_record_sets,
number_of_virtual_network_links,
number_of_virtual_network_links_with_registration,
privateZoneName,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.private_dns.vw_private_zones
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
tags
FROM azure.private_dns.private_zones
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_zones</code> resource.

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
INSERT INTO azure.private_dns.private_zones (
privateZoneName,
resourceGroupName,
subscriptionId,
etag,
properties,
tags,
location
)
SELECT 
'{{ privateZoneName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ etag }}',
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
    - name: etag
      value: string
    - name: properties
      value:
        - name: maxNumberOfRecordSets
          value: integer
        - name: numberOfRecordSets
          value: integer
        - name: maxNumberOfVirtualNetworkLinks
          value: integer
        - name: numberOfVirtualNetworkLinks
          value: integer
        - name: maxNumberOfVirtualNetworkLinksWithRegistration
          value: integer
        - name: numberOfVirtualNetworkLinksWithRegistration
          value: integer
        - name: provisioningState
          value: string
        - name: internalId
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>private_zones</code> resource.

```sql
/*+ update */
UPDATE azure.private_dns.private_zones
SET 
etag = '{{ etag }}',
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}'
WHERE 
privateZoneName = '{{ privateZoneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>private_zones</code> resource.

```sql
/*+ delete */
DELETE FROM azure.private_dns.private_zones
WHERE privateZoneName = '{{ privateZoneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
