---
title: virtual_network_links
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_links
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

Creates, updates, deletes, gets or lists a <code>virtual_network_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_network_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.private_dns.virtual_network_links" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_links', value: 'view', },
        { label: 'virtual_network_links', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `text` | The ETag of the virtual network link. |
| <CopyableCode code="location" /> | `text` | The Azure Region where the resource lives |
| <CopyableCode code="privateZoneName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="resolution_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="virtualNetworkLinkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_network_link_state" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The ETag of the virtual network link. |
| <CopyableCode code="location" /> | `string` | The Azure Region where the resource lives |
| <CopyableCode code="properties" /> | `object` | Represents the properties of the Private DNS zone. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId, virtualNetworkLinkName" /> | Gets a virtual network link to the specified Private DNS zone. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Lists the virtual network links to the specified Private DNS zone. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId, virtualNetworkLinkName" /> | Creates or updates a virtual network link to the specified Private DNS zone. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId, virtualNetworkLinkName" /> | Deletes a virtual network link to the specified Private DNS zone. WARNING: In case of a registration virtual network, all auto-registered DNS records in the zone for the virtual network will also be deleted. This operation cannot be undone. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId, virtualNetworkLinkName" /> | Updates a virtual network link to the specified Private DNS zone. |

## `SELECT` examples

Lists the virtual network links to the specified Private DNS zone.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_links', value: 'view', },
        { label: 'virtual_network_links', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
etag,
location,
privateZoneName,
provisioning_state,
registration_enabled,
resolution_policy,
resourceGroupName,
subscriptionId,
tags,
virtualNetworkLinkName,
virtual_network,
virtual_network_link_state
FROM azure.private_dns.vw_virtual_network_links
WHERE privateZoneName = '{{ privateZoneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
tags
FROM azure.private_dns.virtual_network_links
WHERE privateZoneName = '{{ privateZoneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_network_links</code> resource.

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
INSERT INTO azure.private_dns.virtual_network_links (
privateZoneName,
resourceGroupName,
subscriptionId,
virtualNetworkLinkName,
etag,
properties,
tags,
location
)
SELECT 
'{{ privateZoneName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualNetworkLinkName }}',
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
        - name: virtualNetwork
          value:
            - name: id
              value: string
        - name: registrationEnabled
          value: boolean
        - name: resolutionPolicy
          value: string
        - name: virtualNetworkLinkState
          value: string
        - name: provisioningState
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_network_links</code> resource.

```sql
/*+ update */
UPDATE azure.private_dns.virtual_network_links
SET 
etag = '{{ etag }}',
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}'
WHERE 
privateZoneName = '{{ privateZoneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkLinkName = '{{ virtualNetworkLinkName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_network_links</code> resource.

```sql
/*+ delete */
DELETE FROM azure.private_dns.virtual_network_links
WHERE privateZoneName = '{{ privateZoneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkLinkName = '{{ virtualNetworkLinkName }}';
```
