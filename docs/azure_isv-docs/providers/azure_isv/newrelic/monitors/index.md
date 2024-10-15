---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - newrelic
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.newrelic.monitors" /></td></tr>
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
| <CopyableCode code="account_creation_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="liftr_resource_category" /> | `text` | field from the `properties` object |
| <CopyableCode code="liftr_resource_preference" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="marketplace_subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="marketplace_subscription_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitoring_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="new_relic_account_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="org_creation_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="saa_s_azure_subscription_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="user_info" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties specific to the NewRelic Monitor resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Get a NewRelicMonitorResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List NewRelicMonitorResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List NewRelicMonitorResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, data__properties" /> | Create a NewRelicMonitorResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, userEmail" /> | Delete a NewRelicMonitorResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Update a NewRelicMonitorResource |
| <CopyableCode code="refresh_ingestion_key" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Refreshes the ingestion key for all monitors linked to the same account associated to this monitor. |
| <CopyableCode code="resubscribe" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="switch_billing" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, data__userEmail" /> | Switches the billing for NewRelic monitor resource. |
| <CopyableCode code="vm_host_payload" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Returns the payload that needs to be passed in the request body for installing NewRelic agent on a VM. |

## `SELECT` examples

List NewRelicMonitorResource resources by subscription ID

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
account_creation_source,
identity,
liftr_resource_category,
liftr_resource_preference,
location,
marketplace_subscription_id,
marketplace_subscription_status,
monitorName,
monitoring_status,
new_relic_account_properties,
org_creation_source,
plan_data,
provisioning_state,
resourceGroupName,
saa_s_azure_subscription_status,
subscriptionId,
subscription_state,
tags,
user_info
FROM azure_isv.newrelic.vw_monitors
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
FROM azure_isv.newrelic.monitors
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
INSERT INTO azure_isv.newrelic.monitors (
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
        - name: provisioningState
          value: []
        - name: monitoringStatus
          value: []
        - name: marketplaceSubscriptionStatus
          value: []
        - name: marketplaceSubscriptionId
          value: string
        - name: newRelicAccountProperties
          value:
            - name: userId
              value: string
            - name: accountInfo
              value:
                - name: accountId
                  value: string
                - name: ingestionKey
                  value: []
                - name: region
                  value: string
            - name: organizationInfo
              value:
                - name: organizationId
                  value: string
            - name: singleSignOnProperties
              value:
                - name: singleSignOnState
                  value: []
                - name: enterpriseAppId
                  value: string
                - name: singleSignOnUrl
                  value: string
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
              value: []
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
        - name: orgCreationSource
          value: []
        - name: accountCreationSource
          value: []
        - name: subscriptionState
          value: string
        - name: saaSAzureSubscriptionStatus
          value: string
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

Updates a <code>monitors</code> resource.

```sql
/*+ update */
UPDATE azure_isv.newrelic.monitors
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>monitors</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.newrelic.monitors
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userEmail = '{{ userEmail }}';
```
