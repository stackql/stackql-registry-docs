---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - elastic
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

Creates, updates, deletes, gets or lists a <code>monitors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.monitors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_monitors', value: 'view', },
        { label: 'monitors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ARM id of the monitor resource. |
| <CopyableCode code="name" /> | `text` | Name of the monitor resource. |
| <CopyableCode code="elastic_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="generate_api_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity properties. |
| <CopyableCode code="liftr_resource_category" /> | `text` | field from the `properties` object |
| <CopyableCode code="liftr_resource_preference" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the monitor resource |
| <CopyableCode code="monitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitoring_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="saa_s_azure_subscription_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Microsoft.Elastic SKU. |
| <CopyableCode code="source_campaign_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_campaign_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the monitor resource. |
| <CopyableCode code="type" /> | `text` | The type of the monitor resource. |
| <CopyableCode code="user_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ARM id of the monitor resource. |
| <CopyableCode code="name" /> | `string` | Name of the monitor resource. |
| <CopyableCode code="identity" /> | `object` | Identity properties. |
| <CopyableCode code="location" /> | `string` | The location of the monitor resource |
| <CopyableCode code="properties" /> | `object` | Properties specific to the monitor resource. |
| <CopyableCode code="sku" /> | `object` | Microsoft.Elastic SKU. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The tags of the monitor resource. |
| <CopyableCode code="type" /> | `string` | The type of the monitor resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, data__location" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_monitors', value: 'view', },
        { label: 'monitors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
elastic_properties,
generate_api_key,
identity,
liftr_resource_category,
liftr_resource_preference,
location,
monitorName,
monitoring_status,
plan_details,
provisioning_state,
resourceGroupName,
saa_s_azure_subscription_status,
sku,
source_campaign_id,
source_campaign_name,
subscriptionId,
subscription_state,
system_data,
tags,
type,
user_info,
version
FROM azure_isv.elastic.vw_monitors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type
FROM azure_isv.elastic.monitors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>monitors</code> resource.

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
INSERT INTO azure_isv.elastic.monitors (
monitorName,
resourceGroupName,
subscriptionId,
data__location,
sku,
properties,
identity,
tags,
location
)
SELECT 
'{{ monitorName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ sku }}',
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: sku
      value:
        - name: name
          value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: monitoringStatus
          value: []
        - name: elasticProperties
          value:
            - name: elasticCloudUser
              value:
                - name: emailAddress
                  value: string
                - name: id
                  value: string
                - name: elasticCloudSsoDefaultUrl
                  value: string
            - name: elasticCloudDeployment
              value:
                - name: name
                  value: string
                - name: deploymentId
                  value: string
                - name: azureSubscriptionId
                  value: string
                - name: elasticsearchRegion
                  value: string
                - name: elasticsearchServiceUrl
                  value: string
                - name: kibanaServiceUrl
                  value: string
                - name: kibanaSsoUrl
                  value: string
        - name: userInfo
          value:
            - name: firstName
              value: string
            - name: lastName
              value: string
            - name: companyName
              value: string
            - name: emailAddress
              value: string
            - name: companyInfo
              value:
                - name: domain
                  value: string
                - name: business
                  value: string
                - name: employeesNumber
                  value: string
                - name: state
                  value: string
                - name: country
                  value: string
        - name: planDetails
          value:
            - name: offerID
              value: string
            - name: publisherID
              value: string
            - name: termID
              value: string
            - name: planID
              value: string
            - name: planName
              value: string
        - name: version
          value: string
        - name: subscriptionState
          value: string
        - name: saaSAzureSubscriptionStatus
          value: string
        - name: sourceCampaignName
          value: string
        - name: sourceCampaignId
          value: string
        - name: liftrResourceCategory
          value: []
        - name: liftrResourcePreference
          value: integer
        - name: generateApiKey
          value: boolean
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
    - name: tags
      value: object
    - name: location
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

Updates a <code>monitors</code> resource.

```sql
/*+ update */
UPDATE azure_isv.elastic.monitors
SET 
tags = '{{ tags }}'
WHERE 
monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>monitors</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.elastic.monitors
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
