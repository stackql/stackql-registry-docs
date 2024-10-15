---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - dynatrace
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.dynatrace.monitors" /></td></tr>
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
| <CopyableCode code="dynatrace_environment_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | The properties of the managed service identities assigned to this resource. |
| <CopyableCode code="liftr_resource_category" /> | `text` | field from the `properties` object |
| <CopyableCode code="liftr_resource_preference" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="marketplace_subscription_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitoring_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="user_info" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The properties of the managed service identities assigned to this resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties specific to the monitor resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_subscription_id" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |

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
dynatrace_environment_properties,
identity,
liftr_resource_category,
liftr_resource_preference,
location,
marketplace_subscription_status,
monitorName,
monitoring_status,
plan_data,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
tags,
user_info
FROM azure_isv.dynatrace.vw_monitors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
systemData,
tags
FROM azure_isv.dynatrace.monitors
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
INSERT INTO azure_isv.dynatrace.monitors (
monitorName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
identity,
tags,
location
)
SELECT 
'{{ monitorName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: monitoringStatus
          value: []
        - name: marketplaceSubscriptionStatus
          value: []
        - name: dynatraceEnvironmentProperties
          value:
            - name: userId
              value: string
            - name: accountInfo
              value:
                - name: accountId
                  value: string
                - name: regionId
                  value: string
            - name: environmentInfo
              value:
                - name: environmentId
                  value: string
                - name: ingestionKey
                  value: string
                - name: logsIngestionEndpoint
                  value: string
                - name: landingURL
                  value: string
            - name: singleSignOnProperties
              value:
                - name: singleSignOnState
                  value: []
                - name: enterpriseAppId
                  value: string
                - name: singleSignOnUrl
                  value: string
                - name: aadDomains
                  value:
                    - string
                - name: provisioningState
                  value: []
        - name: userInfo
          value:
            - name: firstName
              value: string
            - name: lastName
              value: string
            - name: emailAddress
              value: []
            - name: phoneNumber
              value: string
            - name: country
              value: string
        - name: planData
          value:
            - name: usageType
              value: string
            - name: billingCycle
              value: string
            - name: planDetails
              value: string
            - name: effectiveDate
              value: string
        - name: liftrResourceCategory
          value: []
        - name: liftrResourcePreference
          value: integer
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
    - name: identity
      value:
        - name: tenantId
          value: string
        - name: principalId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: object
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>monitors</code> resource.

```sql
/*+ update */
UPDATE azure_isv.dynatrace.monitors
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
DELETE FROM azure_isv.dynatrace.monitors
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
