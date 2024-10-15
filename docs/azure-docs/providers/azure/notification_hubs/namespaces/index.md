---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - notification_hubs
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

Creates, updates, deletes, gets or lists a <code>namespaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.notification_hubs.namespaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_namespaces', value: 'view', },
        { label: 'namespaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="critical" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_center" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="metric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="namespaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="namespace_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_acls" /> | `text` | field from the `properties` object |
| <CopyableCode code="pns_credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="region" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_region" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_unit" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_bus_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="updated_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="zone_redundancy" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Represents namespace properties. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, data__location, data__sku" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="check_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name" /> |  |
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, data__policyKey" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_namespaces', value: 'view', },
        { label: 'namespaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
created_at,
critical,
data_center,
enabled,
location,
metric_id,
namespaceName,
namespace_type,
network_acls,
pns_credentials,
private_endpoint_connections,
provisioning_state,
public_network_access,
region,
replication_region,
resourceGroupName,
scale_unit,
service_bus_endpoint,
sku,
status,
subscriptionId,
subscription_id,
tags,
updated_at,
zone_redundancy
FROM azure.notification_hubs.vw_namespaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags
FROM azure.notification_hubs.namespaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>namespaces</code> resource.

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
INSERT INTO azure.notification_hubs.namespaces (
namespaceName,
resourceGroupName,
subscriptionId,
data__location,
data__sku,
tags,
location,
sku,
properties
)
SELECT 
'{{ namespaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__sku }}',
'{{ tags }}',
'{{ location }}',
'{{ sku }}',
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
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: []
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: properties
      value:
        - name: name
          value: string
        - name: provisioningState
          value: []
        - name: status
          value: []
        - name: enabled
          value: boolean
        - name: critical
          value: boolean
        - name: subscriptionId
          value: string
        - name: region
          value: string
        - name: metricId
          value: string
        - name: createdAt
          value: string
        - name: updatedAt
          value: string
        - name: namespaceType
          value: []
        - name: replicationRegion
          value: []
        - name: zoneRedundancy
          value: []
        - name: networkAcls
          value:
            - name: ipRules
              value:
                - - name: ipMask
                    value: string
                  - name: rights
                    value:
                      - []
            - name: publicNetworkRule
              value:
                - name: rights
                  value:
                    - []
        - name: pnsCredentials
          value:
            - name: admCredential
              value:
                - name: properties
                  value:
                    - name: clientId
                      value: string
                    - name: clientSecret
                      value: string
                    - name: authTokenUrl
                      value: string
            - name: apnsCredential
              value:
                - name: properties
                  value:
                    - name: apnsCertificate
                      value: string
                    - name: certificateKey
                      value: string
                    - name: endpoint
                      value: string
                    - name: thumbprint
                      value: string
                    - name: keyId
                      value: string
                    - name: appName
                      value: string
                    - name: appId
                      value: string
                    - name: token
                      value: string
            - name: baiduCredential
              value:
                - name: properties
                  value:
                    - name: baiduApiKey
                      value: string
                    - name: baiduEndPoint
                      value: string
                    - name: baiduSecretKey
                      value: string
            - name: browserCredential
              value:
                - name: properties
                  value:
                    - name: subject
                      value: string
                    - name: vapidPrivateKey
                      value: string
                    - name: vapidPublicKey
                      value: string
            - name: gcmCredential
              value:
                - name: properties
                  value:
                    - name: gcmEndpoint
                      value: string
                    - name: googleApiKey
                      value: string
            - name: mpnsCredential
              value:
                - name: properties
                  value:
                    - name: mpnsCertificate
                      value: string
                    - name: certificateKey
                      value: string
                    - name: thumbprint
                      value: string
            - name: wnsCredential
              value:
                - name: properties
                  value:
                    - name: packageSid
                      value: string
                    - name: secretKey
                      value: string
                    - name: windowsLiveEndpoint
                      value: string
                    - name: certificateKey
                      value: string
                    - name: wnsCertificate
                      value: string
            - name: xiaomiCredential
              value:
                - name: properties
                  value:
                    - name: appSecret
                      value: string
                    - name: endpoint
                      value: string
            - name: fcmV1Credential
              value:
                - name: properties
                  value:
                    - name: clientEmail
                      value: string
                    - name: privateKey
                      value: string
                    - name: projectId
                      value: string
        - name: serviceBusEndpoint
          value: string
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: provisioningState
                    value: []
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: groupIds
                    value:
                      - string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: []
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
        - name: scaleUnit
          value: string
        - name: dataCenter
          value: string
        - name: publicNetworkAccess
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>namespaces</code> resource.

```sql
/*+ update */
UPDATE azure.notification_hubs.namespaces
SET 
sku = '{{ sku }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>namespaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.notification_hubs.namespaces
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
