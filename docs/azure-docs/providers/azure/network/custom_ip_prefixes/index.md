---
title: custom_ip_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_ip_prefixes
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

Creates, updates, deletes, gets or lists a <code>custom_ip_prefixes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_ip_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.custom_ip_prefixes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_ip_prefixes', value: 'view', },
        { label: 'custom_ip_prefixes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="asn" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="child_custom_ip_prefixes" /> | `text` | field from the `properties` object |
| <CopyableCode code="cidr" /> | `text` | field from the `properties` object |
| <CopyableCode code="commissioned_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="customIpPrefixName" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_ip_prefix_parent" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="express_route_advertise" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="failed_reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="geo" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="no_internet_advertise" /> | `text` | field from the `properties` object |
| <CopyableCode code="prefix_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_prefixes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="signed_message" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Custom IP prefix properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customIpPrefixName, resourceGroupName, subscriptionId" /> | Gets the specified custom IP prefix in a specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all custom IP prefixes in a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the custom IP prefixes in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="customIpPrefixName, resourceGroupName, subscriptionId" /> | Creates or updates a custom IP prefix. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customIpPrefixName, resourceGroupName, subscriptionId" /> | Deletes the specified custom IP prefix. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="customIpPrefixName, resourceGroupName, subscriptionId" /> | Updates custom IP prefix tags. |

## `SELECT` examples

Gets all the custom IP prefixes in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_ip_prefixes', value: 'view', },
        { label: 'custom_ip_prefixes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
asn,
authorization_message,
child_custom_ip_prefixes,
cidr,
commissioned_state,
customIpPrefixName,
custom_ip_prefix_parent,
etag,
express_route_advertise,
extended_location,
failed_reason,
geo,
location,
no_internet_advertise,
prefix_type,
provisioning_state,
public_ip_prefixes,
resourceGroupName,
resource_guid,
signed_message,
subscriptionId,
tags,
type,
zones
FROM azure.network.vw_custom_ip_prefixes
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
tags,
type,
zones
FROM azure.network.custom_ip_prefixes
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_ip_prefixes</code> resource.

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
INSERT INTO azure.network.custom_ip_prefixes (
customIpPrefixName,
resourceGroupName,
subscriptionId,
extendedLocation,
properties,
zones,
id,
location,
tags
)
SELECT 
'{{ customIpPrefixName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ extendedLocation }}',
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
    - name: properties
      value:
        - name: asn
          value: string
        - name: cidr
          value: string
        - name: signedMessage
          value: string
        - name: authorizationMessage
          value: string
        - name: customIpPrefixParent
          value:
            - name: id
              value: string
        - name: childCustomIpPrefixes
          value:
            - - name: id
                value: string
        - name: commissionedState
          value: string
        - name: expressRouteAdvertise
          value: boolean
        - name: geo
          value: string
        - name: noInternetAdvertise
          value: boolean
        - name: prefixType
          value: string
        - name: publicIpPrefixes
          value:
            - - name: id
                value: string
        - name: resourceGuid
          value: string
        - name: failedReason
          value: string
        - name: provisioningState
          value: []
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

Deletes the specified <code>custom_ip_prefixes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.custom_ip_prefixes
WHERE customIpPrefixName = '{{ customIpPrefixName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
