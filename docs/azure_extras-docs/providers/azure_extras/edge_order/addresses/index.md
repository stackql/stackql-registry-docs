---
title: addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - addresses
  - edge_order
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

Creates, updates, deletes, gets or lists a <code>addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edge_order.addresses" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_addresses', value: 'view', },
        { label: 'addresses', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="addressName" /> | `text` | field from the `properties` object |
| <CopyableCode code="address_classification" /> | `text` | field from the `properties` object |
| <CopyableCode code="address_validation_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="contact_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shipping_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Address Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="addressName, resourceGroupName, subscriptionId" /> | Get information about the specified address. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the addresses available under the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the addresses available under the subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="addressName, resourceGroupName, subscriptionId, data__properties" /> | Create a new address with the specified parameters. Existing address cannot be updated with this API and should
instead be updated with the Update address API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="addressName, resourceGroupName, subscriptionId" /> | Delete an address. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="addressName, resourceGroupName, subscriptionId" /> | Update the properties of an existing address. |

## `SELECT` examples

List all the addresses available under the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_addresses', value: 'view', },
        { label: 'addresses', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
addressName,
address_classification,
address_validation_status,
contact_details,
location,
provisioning_state,
resourceGroupName,
shipping_address,
subscriptionId,
tags
FROM azure_extras.edge_order.vw_addresses
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_extras.edge_order.addresses
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>addresses</code> resource.

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
INSERT INTO azure_extras.edge_order.addresses (
addressName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ addressName }}',
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
        - name: addressClassification
          value: []
        - name: shippingAddress
          value:
            - name: streetAddress1
              value: string
            - name: streetAddress2
              value: string
            - name: streetAddress3
              value: string
            - name: city
              value: string
            - name: stateOrProvince
              value: string
            - name: country
              value: string
            - name: postalCode
              value: string
            - name: zipExtendedCode
              value: string
            - name: companyName
              value: string
            - name: addressType
              value: string
        - name: contactDetails
          value:
            - name: contactName
              value: string
            - name: phone
              value: string
            - name: phoneExtension
              value: string
            - name: mobile
              value: string
            - name: emailList
              value:
                - string
        - name: addressValidationStatus
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>addresses</code> resource.

```sql
/*+ update */
UPDATE azure_extras.edge_order.addresses
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
addressName = '{{ addressName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>addresses</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.edge_order.addresses
WHERE addressName = '{{ addressName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
