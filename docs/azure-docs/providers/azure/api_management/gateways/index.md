---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
  - api_management
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

Creates, updates, deletes, gets or lists a <code>gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gateways', value: 'view', },
        { label: 'gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="gatewayId" /> | `text` | field from the `properties` object |
| <CopyableCode code="location_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the Gateway contract. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the Gateway specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of gateways registered with service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates a Gateway to be used in Api Management instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific Gateway. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the gateway specified by its identifier. |
| <CopyableCode code="generate_token" /> | `EXEC` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId, data__expiry, data__keyType" /> | Gets the Shared Access Authorization Token for the gateway. |
| <CopyableCode code="invalidate_debug_credentials" /> | `EXEC` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Action is invalidating all debug credentials issued for gateway. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId, data__keyType" /> | Regenerates specified gateway key invalidating any tokens created with it. |

## `SELECT` examples

Lists a collection of gateways registered with service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gateways', value: 'view', },
        { label: 'gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
gatewayId,
location_data,
resourceGroupName,
serviceName,
subscriptionId
FROM azure.api_management.vw_gateways
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.gateways
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gateways</code> resource.

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
INSERT INTO azure.api_management.gateways (
gatewayId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ gatewayId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: locationData
          value:
            - name: name
              value: string
            - name: city
              value: string
            - name: district
              value: string
            - name: countryOrRegion
              value: string
        - name: description
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>gateways</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.gateways
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND gatewayId = '{{ gatewayId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.gateways
WHERE If-Match = '{{ If-Match }}'
AND gatewayId = '{{ gatewayId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
