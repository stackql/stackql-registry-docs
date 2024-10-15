---
title: gateway_hostname_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_hostname_configurations
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

Creates, updates, deletes, gets or lists a <code>gateway_hostname_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_hostname_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.gateway_hostname_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gateway_hostname_configurations', value: 'view', },
        { label: 'gateway_hostname_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="certificate_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="gatewayId" /> | `text` | field from the `properties` object |
| <CopyableCode code="hcId" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostname" /> | `text` | field from the `properties` object |
| <CopyableCode code="http2_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="negotiate_client_certificate" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tls10_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="tls11_enabled" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Gateway hostname configuration details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayId, hcId, resourceGroupName, serviceName, subscriptionId" /> | Get details of a hostname configuration |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Lists the collection of hostname configurations for the specified gateway. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayId, hcId, resourceGroupName, serviceName, subscriptionId" /> | Creates of updates hostname configuration for a Gateway. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, gatewayId, hcId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified hostname configuration from the specified Gateway. |

## `SELECT` examples

Lists the collection of hostname configurations for the specified gateway.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gateway_hostname_configurations', value: 'view', },
        { label: 'gateway_hostname_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
certificate_id,
gatewayId,
hcId,
hostname,
http2_enabled,
negotiate_client_certificate,
resourceGroupName,
serviceName,
subscriptionId,
tls10_enabled,
tls11_enabled
FROM azure.api_management.vw_gateway_hostname_configurations
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
FROM azure.api_management.gateway_hostname_configurations
WHERE gatewayId = '{{ gatewayId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gateway_hostname_configurations</code> resource.

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
INSERT INTO azure.api_management.gateway_hostname_configurations (
gatewayId,
hcId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ gatewayId }}',
'{{ hcId }}',
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
        - name: hostname
          value: string
        - name: certificateId
          value: string
        - name: negotiateClientCertificate
          value: boolean
        - name: tls10Enabled
          value: boolean
        - name: tls11Enabled
          value: boolean
        - name: http2Enabled
          value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>gateway_hostname_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.gateway_hostname_configurations
WHERE If-Match = '{{ If-Match }}'
AND gatewayId = '{{ gatewayId }}'
AND hcId = '{{ hcId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
