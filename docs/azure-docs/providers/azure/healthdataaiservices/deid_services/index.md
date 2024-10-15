---
title: deid_services
hide_title: false
hide_table_of_contents: false
keywords:
  - deid_services
  - healthdataaiservices
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

Creates, updates, deletes, gets or lists a <code>deid_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deid_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.healthdataaiservices.deid_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deid_services', value: 'view', },
        { label: 'deid_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="deidServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of the HealthDataAIServices DeidService. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deidServiceName, resourceGroupName, subscriptionId" /> | Get a DeidService |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List DeidService resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List DeidService resources by subscription ID |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deidServiceName, resourceGroupName, subscriptionId" /> | Create a DeidService |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deidServiceName, resourceGroupName, subscriptionId" /> | Delete a DeidService |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deidServiceName, resourceGroupName, subscriptionId" /> | Update a DeidService |

## `SELECT` examples

List DeidService resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deid_services', value: 'view', },
        { label: 'deid_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
deidServiceName,
identity,
location,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
service_url,
subscriptionId,
tags
FROM azure.healthdataaiservices.vw_deid_services
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
FROM azure.healthdataaiservices.deid_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deid_services</code> resource.

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
INSERT INTO azure.healthdataaiservices.deid_services (
deidServiceName,
resourceGroupName,
subscriptionId,
properties,
identity,
tags,
location
)
SELECT 
'{{ deidServiceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
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
        - name: serviceUrl
          value: string
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
        - name: publicNetworkAccess
          value: []
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>deid_services</code> resource.

```sql
/*+ update */
UPDATE azure.healthdataaiservices.deid_services
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
deidServiceName = '{{ deidServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>deid_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.healthdataaiservices.deid_services
WHERE deidServiceName = '{{ deidServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
