---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
  - reservations
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

Creates, updates, deletes, gets or lists a <code>quotas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.reservations.quotas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_quotas', value: 'view', },
        { label: 'quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The quota request ID. |
| <CopyableCode code="name" /> | `text` | The name of the quota request. |
| <CopyableCode code="current_value" /> | `text` | field from the `properties` object |
| <CopyableCode code="limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="properties" /> | `text` | Quota properties for the resource. |
| <CopyableCode code="providerId" /> | `text` | field from the `properties` object |
| <CopyableCode code="quota_period" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of resource. "Microsoft.Capacity/ServiceLimits" |
| <CopyableCode code="unit" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The quota request ID. |
| <CopyableCode code="name" /> | `string` | The name of the quota request. |
| <CopyableCode code="properties" /> | `object` | Quota properties for the resource. |
| <CopyableCode code="type" /> | `string` | Type of resource. "Microsoft.Capacity/ServiceLimits" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, providerId, resourceName, subscriptionId" /> | Get the current quota (service limit) and usage of a resource. You can use the response from the GET operation to submit quota update request. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, providerId, subscriptionId" /> | Gets a list of current quotas (service limits) and usage for all resources. The response from the list quota operation can be leveraged to request quota updates. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="location, providerId, resourceName, subscriptionId" /> | Create or update the quota (service limits) of a resource to the requested value.
 Steps:
  1. Make the Get request to get the quota information for specific resource.
  2. To increase the quota, update the limit field in the response from Get request to new value.
  3. Submit the JSON to the quota request API to update the quota.
  The Create quota request may be constructed as follows. The PUT operation can be used to update the quota. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="location, providerId, resourceName, subscriptionId" /> | Update the quota (service limits) of this resource to the requested value.
  • To get the quota information for specific resource, send a GET request.
  • To increase the quota, update the limit field from the GET response to a new value.
  • To update the quota value, submit the JSON response to the quota request API to update the quota.
  • To update the quota. use the PATCH operation. |

## `SELECT` examples

Gets a list of current quotas (service limits) and usage for all resources. The response from the list quota operation can be leveraged to request quota updates.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_quotas', value: 'view', },
        { label: 'quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
current_value,
limit,
location,
properties,
providerId,
quota_period,
resourceName,
resource_type,
subscriptionId,
type,
unit
FROM azure.reservations.vw_quotas
WHERE location = '{{ location }}'
AND providerId = '{{ providerId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.reservations.quotas
WHERE location = '{{ location }}'
AND providerId = '{{ providerId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>quotas</code> resource.

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
INSERT INTO azure.reservations.quotas (
location,
providerId,
resourceName,
subscriptionId,
properties
)
SELECT 
'{{ location }}',
'{{ providerId }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: limit
          value: integer
        - name: currentValue
          value: integer
        - name: unit
          value: string
        - name: name
          value:
            - name: value
              value: string
            - name: localizedValue
              value: string
        - name: resourceType
          value: []
        - name: quotaPeriod
          value: string
        - name: properties
          value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>quotas</code> resource.

```sql
/*+ update */
UPDATE azure.reservations.quotas
SET 
properties = '{{ properties }}'
WHERE 
location = '{{ location }}'
AND providerId = '{{ providerId }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
