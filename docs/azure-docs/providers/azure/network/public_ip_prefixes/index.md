---
title: public_ip_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - public_ip_prefixes
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

Creates, updates, deletes, gets or lists a <code>public_ip_prefixes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_ip_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.public_ip_prefixes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_public_ip_prefixes', value: 'view', },
        { label: 'public_ip_prefixes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="custom_ip_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancer_frontend_ip_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="nat_gateway" /> | `text` | field from the `properties` object |
| <CopyableCode code="prefix_length" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publicIpPrefixName" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_address_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | SKU of a public IP prefix. |
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
| <CopyableCode code="properties" /> | `object` | Public IP prefix properties. |
| <CopyableCode code="sku" /> | `object` | SKU of a public IP prefix. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="publicIpPrefixName, resourceGroupName, subscriptionId" /> | Gets the specified public IP prefix in a specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all public IP prefixes in a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the public IP prefixes in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="publicIpPrefixName, resourceGroupName, subscriptionId" /> | Creates or updates a static or dynamic public IP prefix. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="publicIpPrefixName, resourceGroupName, subscriptionId" /> | Deletes the specified public IP prefix. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="publicIpPrefixName, resourceGroupName, subscriptionId" /> | Updates public IP prefix tags. |

## `SELECT` examples

Gets all the public IP prefixes in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_public_ip_prefixes', value: 'view', },
        { label: 'public_ip_prefixes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
custom_ip_prefix,
etag,
extended_location,
ip_prefix,
ip_tags,
load_balancer_frontend_ip_configuration,
location,
nat_gateway,
prefix_length,
provisioning_state,
publicIpPrefixName,
public_ip_address_version,
public_ip_addresses,
resourceGroupName,
resource_guid,
sku,
subscriptionId,
tags,
type,
zones
FROM azure.network.vw_public_ip_prefixes
WHERE subscriptionId = '{{ subscriptionId }}';
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
FROM azure.network.public_ip_prefixes
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>public_ip_prefixes</code> resource.

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
INSERT INTO azure.network.public_ip_prefixes (
publicIpPrefixName,
resourceGroupName,
subscriptionId,
extendedLocation,
sku,
properties,
zones,
id,
location,
tags
)
SELECT 
'{{ publicIpPrefixName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ extendedLocation }}',
'{{ sku }}',
'{{ properties }}',
'{{ zones }}',
'{{ id }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
    - name: properties
      value:
        - name: publicIPAddressVersion
          value: []
        - name: ipTags
          value:
            - - name: ipTagType
                value: string
              - name: tag
                value: string
        - name: prefixLength
          value: integer
        - name: ipPrefix
          value: string
        - name: publicIPAddresses
          value:
            - - name: id
                value: string
        - name: loadBalancerFrontendIpConfiguration
          value:
            - name: id
              value: string
        - name: resourceGuid
          value: string
        - name: provisioningState
          value: []
        - name: natGateway
          value:
            - name: sku
              value:
                - name: name
                  value: string
            - name: properties
              value:
                - name: idleTimeoutInMinutes
                  value: integer
                - name: publicIpAddresses
                  value:
                    - - name: id
                        value: string
                - name: publicIpPrefixes
                  value:
                    - - name: id
                        value: string
                - name: subnets
                  value:
                    - - name: id
                        value: string
                - name: resourceGuid
                  value: string
            - name: zones
              value:
                - string
            - name: etag
              value: string
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
    - name: etag
      value: string
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

## `DELETE` example

Deletes the specified <code>public_ip_prefixes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.public_ip_prefixes
WHERE publicIpPrefixName = '{{ publicIpPrefixName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
