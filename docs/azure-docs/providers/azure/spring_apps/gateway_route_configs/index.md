---
title: gateway_route_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_route_configs
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>gateway_route_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_route_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.gateway_route_configs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gateway_route_configs', value: 'view', },
        { label: 'gateway_route_configs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="app_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="filters" /> | `text` | field from the `properties` object |
| <CopyableCode code="gatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="open_api" /> | `text` | field from the `properties` object |
| <CopyableCode code="predicates" /> | `text` | field from the `properties` object |
| <CopyableCode code="protocol" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routeConfigName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routes" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sso_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | API route config of the Spring Cloud Gateway |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, routeConfigName, serviceName, subscriptionId" /> | Get the Spring Cloud Gateway route configs. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, serviceName, subscriptionId" /> | Handle requests to list all Spring Cloud Gateway route configs. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayName, resourceGroupName, routeConfigName, serviceName, subscriptionId" /> | Create the default Spring Cloud Gateway route configs or update the existing Spring Cloud Gateway route configs. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gatewayName, resourceGroupName, routeConfigName, serviceName, subscriptionId" /> | Delete the Spring Cloud Gateway route config. |

## `SELECT` examples

Handle requests to list all Spring Cloud Gateway route configs.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gateway_route_configs', value: 'view', },
        { label: 'gateway_route_configs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
app_resource_id,
filters,
gatewayName,
open_api,
predicates,
protocol,
provisioning_state,
resourceGroupName,
routeConfigName,
routes,
serviceName,
sso_enabled,
subscriptionId
FROM azure.spring_apps.vw_gateway_route_configs
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.gateway_route_configs
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gateway_route_configs</code> resource.

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
INSERT INTO azure.spring_apps.gateway_route_configs (
gatewayName,
resourceGroupName,
routeConfigName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ gatewayName }}',
'{{ resourceGroupName }}',
'{{ routeConfigName }}',
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
        - name: provisioningState
          value: string
        - name: appResourceId
          value: string
        - name: openApi
          value:
            - name: uri
              value: string
        - name: protocol
          value: string
        - name: routes
          value:
            - - name: title
                value: string
              - name: description
                value: string
              - name: uri
                value: string
              - name: ssoEnabled
                value: boolean
              - name: tokenRelay
                value: boolean
              - name: predicates
                value:
                  - string
              - name: filters
                value:
                  - string
              - name: order
                value: integer
              - name: tags
                value:
                  - string
        - name: ssoEnabled
          value: boolean
        - name: predicates
          value:
            - string
        - name: filters
          value:
            - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>gateway_route_configs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.gateway_route_configs
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND routeConfigName = '{{ routeConfigName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
