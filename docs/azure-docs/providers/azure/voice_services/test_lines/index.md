---
title: test_lines
hide_title: false
hide_table_of_contents: false
keywords:
  - test_lines
  - voice_services
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

Creates, updates, deletes, gets or lists a <code>test_lines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_lines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.voice_services.test_lines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_test_lines', value: 'view', },
        { label: 'test_lines', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="communicationsGatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="phone_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="purpose" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="testLineName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of the TestLine resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId, testLineName" /> | Get a TestLine |
| <CopyableCode code="list_by_communications_gateway" /> | `SELECT` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId" /> | List TestLine resources by CommunicationsGateway |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId, testLineName" /> | Create a TestLine |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId, testLineName" /> | Delete a TestLine |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId, testLineName" /> | Update a TestLine |

## `SELECT` examples

List TestLine resources by CommunicationsGateway

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_test_lines', value: 'view', },
        { label: 'test_lines', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
communicationsGatewayName,
location,
phone_number,
provisioning_state,
purpose,
resourceGroupName,
subscriptionId,
tags,
testLineName
FROM azure.voice_services.vw_test_lines
WHERE communicationsGatewayName = '{{ communicationsGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.voice_services.test_lines
WHERE communicationsGatewayName = '{{ communicationsGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>test_lines</code> resource.

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
INSERT INTO azure.voice_services.test_lines (
communicationsGatewayName,
resourceGroupName,
subscriptionId,
testLineName,
properties,
tags,
location
)
SELECT 
'{{ communicationsGatewayName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ testLineName }}',
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
        - name: provisioningState
          value: []
        - name: phoneNumber
          value: string
        - name: purpose
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>test_lines</code> resource.

```sql
/*+ update */
UPDATE azure.voice_services.test_lines
SET 
tags = '{{ tags }}'
WHERE 
communicationsGatewayName = '{{ communicationsGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testLineName = '{{ testLineName }}';
```

## `DELETE` example

Deletes the specified <code>test_lines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.voice_services.test_lines
WHERE communicationsGatewayName = '{{ communicationsGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testLineName = '{{ testLineName }}';
```
