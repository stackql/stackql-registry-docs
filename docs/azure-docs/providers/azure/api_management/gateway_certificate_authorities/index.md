---
title: gateway_certificate_authorities
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_certificate_authorities
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

Creates, updates, deletes, gets or lists a <code>gateway_certificate_authorities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_certificate_authorities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.gateway_certificate_authorities" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gateway_certificate_authorities', value: 'view', },
        { label: 'gateway_certificate_authorities', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="certificateId" /> | `text` | field from the `properties` object |
| <CopyableCode code="gatewayId" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_trusted" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Gateway certificate authority details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateId, gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Get assigned Gateway Certificate Authority details. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Lists the collection of Certificate Authorities for the specified Gateway entity. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateId, gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Assign Certificate entity to Gateway entity as Certificate Authority. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, certificateId, gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Remove relationship between Certificate Authority and Gateway entity. |

## `SELECT` examples

Lists the collection of Certificate Authorities for the specified Gateway entity.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gateway_certificate_authorities', value: 'view', },
        { label: 'gateway_certificate_authorities', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
certificateId,
gatewayId,
is_trusted,
resourceGroupName,
serviceName,
subscriptionId
FROM azure.api_management.vw_gateway_certificate_authorities
WHERE gatewayId = '{{ gatewayId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.gateway_certificate_authorities
WHERE gatewayId = '{{ gatewayId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gateway_certificate_authorities</code> resource.

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
INSERT INTO azure.api_management.gateway_certificate_authorities (
certificateId,
gatewayId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ certificateId }}',
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
        - name: isTrusted
          value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>gateway_certificate_authorities</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.gateway_certificate_authorities
WHERE If-Match = '{{ If-Match }}'
AND certificateId = '{{ certificateId }}'
AND gatewayId = '{{ gatewayId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
