---
title: public_ip_addresses_cloud_service_public_ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - public_ip_addresses_cloud_service_public_ip_addresses
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

Creates, updates, deletes, gets or lists a <code>public_ip_addresses_cloud_service_public_ip_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_ip_addresses_cloud_service_public_ip_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.public_ip_addresses_cloud_service_public_ip_addresses" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_public_ip_addresses_cloud_service_public_ip_addresses', value: 'view', },
        { label: 'public_ip_addresses_cloud_service_public_ip_addresses', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="cloudServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ddos_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="delete_option" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="idle_timeout_in_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="linked_public_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="migration_phase" /> | `text` | field from the `properties` object |
| <CopyableCode code="nat_gateway" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkInterfaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publicIpAddressName" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_address_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_allocation_method" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="roleInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_public_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | SKU of a public IP address. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="zones" /> | `text` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation complex type. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Public IP address properties. |
| <CopyableCode code="sku" /> | `object` | SKU of a public IP address. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudServiceName, ipConfigurationName, networkInterfaceName, publicIpAddressName, resourceGroupName, roleInstanceName, subscriptionId" /> | Get the specified public IP address in a cloud service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Gets information about all public IP addresses on a cloud service level. |

## `SELECT` examples

Gets information about all public IP addresses on a cloud service level.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_public_ip_addresses_cloud_service_public_ip_addresses', value: 'view', },
        { label: 'public_ip_addresses_cloud_service_public_ip_addresses', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
cloudServiceName,
ddos_settings,
delete_option,
dns_settings,
etag,
extended_location,
idle_timeout_in_minutes,
ipConfigurationName,
ip_address,
ip_configuration,
ip_tags,
linked_public_ip_address,
location,
migration_phase,
nat_gateway,
networkInterfaceName,
provisioning_state,
publicIpAddressName,
public_ip_address_version,
public_ip_allocation_method,
public_ip_prefix,
resourceGroupName,
resource_guid,
roleInstanceName,
service_public_ip_address,
sku,
subscriptionId,
tags,
type,
zones
FROM azure.network.vw_public_ip_addresses_cloud_service_public_ip_addresses
WHERE cloudServiceName = '{{ cloudServiceName }}'
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
extendedLocation,
location,
properties,
sku,
tags,
type,
zones
FROM azure.network.public_ip_addresses_cloud_service_public_ip_addresses
WHERE cloudServiceName = '{{ cloudServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

