---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
  - service_fabric_mesh
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_mesh.gateways" /></td></tr>
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
| <CopyableCode code="destination_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="gatewayResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="http" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tcp" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | This type describes properties of a gateway resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayResourceName, resourceGroupName, subscriptionId" /> | Gets the information about the gateway resource with the given name. The information include the description and other properties of the gateway. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the Gateway. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the gateway. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="gatewayResourceName, resourceGroupName, subscriptionId, data__properties" /> | Creates a gateway resource with the specified name, description and properties. If a gateway resource with the same name exists, then it is updated with the specified description and properties. Use gateway resources to create a gateway for public connectivity for services within your application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gatewayResourceName, resourceGroupName, subscriptionId" /> | Deletes the gateway resource identified by the name. |

## `SELECT` examples

Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the gateway.

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
destination_network,
gatewayResourceName,
http,
ip_address,
location,
provisioning_state,
resourceGroupName,
source_network,
status,
status_details,
subscriptionId,
tags,
tcp
FROM azure.service_fabric_mesh.vw_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.service_fabric_mesh.gateways
WHERE subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.service_fabric_mesh.gateways (
gatewayResourceName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ gatewayResourceName }}',
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
        - name: provisioningState
          value: string
        - name: description
          value: string
        - name: sourceNetwork
          value:
            - name: name
              value: string
            - name: endpointRefs
              value:
                - - name: name
                    value: string
        - name: tcp
          value:
            - - name: name
                value: string
              - name: port
                value: integer
              - name: destination
                value:
                  - name: applicationName
                    value: string
                  - name: serviceName
                    value: string
                  - name: endpointName
                    value: string
        - name: http
          value:
            - - name: name
                value: string
              - name: port
                value: integer
              - name: hosts
                value:
                  - - name: name
                      value: string
                    - name: routes
                      value:
                        - - name: name
                            value: string
                          - name: match
                            value:
                              - name: path
                                value:
                                  - name: value
                                    value: string
                                  - name: rewrite
                                    value: string
                                  - name: type
                                    value: string
                              - name: headers
                                value:
                                  - - name: name
                                      value: string
                                    - name: value
                                      value: string
                                    - name: type
                                      value: string
        - name: status
          value: []
        - name: statusDetails
          value: string
        - name: ipAddress
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_fabric_mesh.gateways
WHERE gatewayResourceName = '{{ gatewayResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
