---
title: data_manager_for_agriculture_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_manager_for_agriculture_resources
  - ag_food_platform
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

Creates, updates, deletes, gets or lists a <code>data_manager_for_agriculture_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_manager_for_agriculture_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.ag_food_platform.data_manager_for_agriculture_resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_manager_for_agriculture_resources', value: 'view', },
        { label: 'data_manager_for_agriculture_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dataManagerForAgricultureResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="instance_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sensor_integration" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Data Manager For Agriculture ARM Resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Get DataManagerForAgriculture resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the DataManagerForAgriculture instances for a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the DataManagerForAgriculture instances for a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Create or update Data Manager For Agriculture resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Delete a Data Manager For Agriculture resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Update a Data Manager For Agriculture resource. |

## `SELECT` examples

Lists the DataManagerForAgriculture instances for a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_manager_for_agriculture_resources', value: 'view', },
        { label: 'data_manager_for_agriculture_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dataManagerForAgricultureResourceName,
identity,
instance_uri,
location,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
sensor_integration,
subscriptionId,
tags
FROM azure_extras.ag_food_platform.vw_data_manager_for_agriculture_resources
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure_extras.ag_food_platform.data_manager_for_agriculture_resources
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_manager_for_agriculture_resources</code> resource.

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
INSERT INTO azure_extras.ag_food_platform.data_manager_for_agriculture_resources (
dataManagerForAgricultureResourceName,
resourceGroupName,
subscriptionId,
tags,
location,
identity,
properties
)
SELECT 
'{{ dataManagerForAgricultureResourceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ identity }}',
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
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: instanceUri
          value: string
        - name: provisioningState
          value: string
        - name: sensorIntegration
          value:
            - name: enabled
              value: string
            - name: provisioningState
              value: string
            - name: provisioningInfo
              value:
                - name: error
                  value:
                    - name: code
                      value: string
                    - name: message
                      value: string
                    - name: target
                      value: string
                    - name: details
                      value:
                        - - name: code
                            value: string
                          - name: message
                            value: string
                          - name: target
                            value: string
                          - name: details
                            value:
                              - - name: code
                                  value: string
                                - name: message
                                  value: string
                                - name: target
                                  value: string
                                - name: details
                                  value:
                                    - - name: code
                                        value: string
                                      - name: message
                                        value: string
                                      - name: target
                                        value: string
                                      - name: details
                                        value:
                                          - - name: code
                                              value: string
                                            - name: message
                                              value: string
                                            - name: target
                                              value: string
                                            - name: details
                                              value:
                                                - - name: code
                                                    value: string
                                                  - name: message
                                                    value: string
                                                  - name: target
                                                    value: string
                                                  - name: details
                                                    value:
                                                      - - name: code
                                                          value: string
                                                        - name: message
                                                          value: string
                                                        - name: target
                                                          value: string
                                                        - name: details
                                                          value:
                                                            - []
                                                        - name: additionalInfo
                                                          value:
                                                            - []
                                                  - name: additionalInfo
                                                    value:
                                                      - - name: type
                                                          value: string
                                                        - name: info
                                                          value: object
                                            - name: additionalInfo
                                              value:
                                                - - name: type
                                                    value: string
                                                  - name: info
                                                    value: object
                                      - name: additionalInfo
                                        value:
                                          - - name: type
                                              value: string
                                            - name: info
                                              value: object
                                - name: additionalInfo
                                  value:
                                    - - name: type
                                        value: string
                                      - name: info
                                        value: object
                          - name: additionalInfo
                            value:
                              - - name: type
                                  value: string
                                - name: info
                                  value: object
                    - name: additionalInfo
                      value:
                        - - name: type
                            value: string
                          - name: info
                            value: object
        - name: publicNetworkAccess
          value: []
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: groupIds
                    value:
                      - string
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: []
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: []
              - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: systemData
                value:
                  - name: createdBy
                    value: string
                  - name: createdByType
                    value: string
                  - name: createdAt
                    value: string
                  - name: lastModifiedBy
                    value: string
                  - name: lastModifiedByType
                    value: string
                  - name: lastModifiedAt
                    value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>data_manager_for_agriculture_resources</code> resource.

```sql
/*+ update */
UPDATE azure_extras.ag_food_platform.data_manager_for_agriculture_resources
SET 
location = '{{ location }}',
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
dataManagerForAgricultureResourceName = '{{ dataManagerForAgricultureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>data_manager_for_agriculture_resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.ag_food_platform.data_manager_for_agriculture_resources
WHERE dataManagerForAgricultureResourceName = '{{ dataManagerForAgricultureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
