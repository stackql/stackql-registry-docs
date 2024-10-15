---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - windows_iot
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.windows_iot.services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="admin_domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
| <CopyableCode code="location" /> | `text` | The Azure Region where the resource lives |
| <CopyableCode code="notes" /> | `text` | field from the `properties` object |
| <CopyableCode code="quantity" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
| <CopyableCode code="location" /> | `string` | The Azure Region where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a Windows IoT Device Service. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Get the non-security related metadata of a Windows IoT Device Service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all the IoT hubs in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the IoT hubs in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Create or update the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values in a new body to update the Windows IoT Device Service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Delete a Windows IoT Device Service. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Updates the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values in a new body to update the Windows IoT Device Service. |
| <CopyableCode code="check_device_service_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name" /> | Check if a Windows IoT Device Service name is available. |

## `SELECT` examples

Get all the IoT hubs in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
admin_domain_name,
billing_domain_name,
deviceName,
etag,
location,
notes,
quantity,
resourceGroupName,
start_date,
subscriptionId,
tags
FROM azure_extras.windows_iot.vw_services
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
FROM azure_extras.windows_iot.services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>services</code> resource.

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
INSERT INTO azure_extras.windows_iot.services (
deviceName,
resourceGroupName,
subscriptionId,
etag,
properties,
tags,
location
)
SELECT 
'{{ deviceName }}',
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
        - name: notes
          value: string
        - name: startDate
          value: string
        - name: quantity
          value: integer
        - name: billingDomainName
          value: string
        - name: adminDomainName
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>services</code> resource.

```sql
/*+ update */
UPDATE azure_extras.windows_iot.services
SET 
etag = '{{ etag }}',
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}'
WHERE 
deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>services</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.windows_iot.services
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
