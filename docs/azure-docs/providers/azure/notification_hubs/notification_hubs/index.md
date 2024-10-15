---
title: notification_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_hubs
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

Creates, updates, deletes, gets or lists a <code>notification_hubs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.notification_hubs.notification_hubs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_notification_hubs', value: 'view', },
        { label: 'notification_hubs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="adm_credential" /> | `text` | field from the `properties` object |
| <CopyableCode code="apns_credential" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="baidu_credential" /> | `text` | field from the `properties` object |
| <CopyableCode code="browser_credential" /> | `text` | field from the `properties` object |
| <CopyableCode code="daily_max_active_devices" /> | `text` | field from the `properties` object |
| <CopyableCode code="fcm_v1_credential" /> | `text` | field from the `properties` object |
| <CopyableCode code="gcm_credential" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mpns_credential" /> | `text` | field from the `properties` object |
| <CopyableCode code="namespaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="notificationHubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_ttl" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="wns_credential" /> | `text` | field from the `properties` object |
| <CopyableCode code="xiaomi_credential" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | NotificationHub properties. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namespaceName, notificationHubName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="namespaceName, notificationHubName, resourceGroupName, subscriptionId, data__location" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="namespaceName, notificationHubName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="namespaceName, notificationHubName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="check_notification_hub_availability" /> | `EXEC` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, data__name" /> |  |
| <CopyableCode code="debug_send" /> | `EXEC` | <CopyableCode code="namespaceName, notificationHubName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="authorizationRuleName, namespaceName, notificationHubName, resourceGroupName, subscriptionId, data__policyKey" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_notification_hubs', value: 'view', },
        { label: 'notification_hubs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
adm_credential,
apns_credential,
authorization_rules,
baidu_credential,
browser_credential,
daily_max_active_devices,
fcm_v1_credential,
gcm_credential,
location,
mpns_credential,
namespaceName,
notificationHubName,
registration_ttl,
resourceGroupName,
sku,
subscriptionId,
tags,
wns_credential,
xiaomi_credential
FROM azure.notification_hubs.vw_notification_hubs
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags
FROM azure.notification_hubs.notification_hubs
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notification_hubs</code> resource.

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
INSERT INTO azure.notification_hubs.notification_hubs (
namespaceName,
notificationHubName,
resourceGroupName,
subscriptionId,
data__location,
tags,
location,
properties,
sku
)
SELECT 
'{{ namespaceName }}',
'{{ notificationHubName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ sku }}'
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
        - name: name
          value: string
        - name: registrationTtl
          value: string
        - name: authorizationRules
          value:
            - - name: rights
                value:
                  - []
              - name: primaryKey
                value: string
              - name: secondaryKey
                value: string
              - name: keyName
                value: string
              - name: modifiedTime
                value: string
              - name: createdTime
                value: string
              - name: claimType
                value: string
              - name: claimValue
                value: string
              - name: revision
                value: integer
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
        - name: dailyMaxActiveDevices
          value: integer
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>notification_hubs</code> resource.

```sql
/*+ update */
UPDATE azure.notification_hubs.notification_hubs
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
namespaceName = '{{ namespaceName }}'
AND notificationHubName = '{{ notificationHubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>notification_hubs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.notification_hubs.notification_hubs
WHERE namespaceName = '{{ namespaceName }}'
AND notificationHubName = '{{ notificationHubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
