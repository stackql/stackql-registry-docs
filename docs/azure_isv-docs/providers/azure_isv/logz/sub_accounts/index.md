---
title: sub_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - sub_accounts
  - logz
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

Creates, updates, deletes, gets or lists a <code>sub_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sub_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.logz.sub_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sub_accounts', value: 'view', },
        { label: 'sub_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ARM id of the monitor resource. |
| <CopyableCode code="name" /> | `text` | Name of the monitor resource. |
| <CopyableCode code="identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="liftr_resource_category" /> | `text` | field from the `properties` object |
| <CopyableCode code="liftr_resource_preference" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="logz_organization_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="marketplace_subscription_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitoring_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the monitor resource. |
| <CopyableCode code="user_info" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ARM id of the monitor resource. |
| <CopyableCode code="name" /> | `string` | Name of the monitor resource. |
| <CopyableCode code="identity" /> | `object` |  |
| <CopyableCode code="location" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Properties specific to the monitor resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | The type of the monitor resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subAccountName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="monitorName, resourceGroupName, subAccountName, subscriptionId, data__location" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, subAccountName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="monitorName, resourceGroupName, subAccountName, subscriptionId" /> |  |
| <CopyableCode code="vm_host_payload" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subAccountName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sub_accounts', value: 'view', },
        { label: 'sub_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
identity,
liftr_resource_category,
liftr_resource_preference,
location,
logz_organization_properties,
marketplace_subscription_status,
monitorName,
monitoring_status,
plan_data,
provisioning_state,
resourceGroupName,
subAccountName,
subscriptionId,
system_data,
tags,
type,
user_info
FROM azure_isv.logz.vw_sub_accounts
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
systemData,
tags,
type
FROM azure_isv.logz.sub_accounts
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sub_accounts</code> resource.

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
INSERT INTO azure_isv.logz.sub_accounts (
monitorName,
resourceGroupName,
subAccountName,
subscriptionId,
data__location,
properties,
identity,
tags,
location
)
SELECT 
'{{ monitorName }}',
'{{ resourceGroupName }}',
'{{ subAccountName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
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
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: monitoringStatus
          value: []
        - name: marketplaceSubscriptionStatus
          value: []
        - name: logzOrganizationProperties
          value:
            - name: companyName
              value: string
            - name: id
              value: string
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
              value: string
            - name: phoneNumber
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sub_accounts</code> resource.

```sql
/*+ update */
UPDATE azure_isv.logz.sub_accounts
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subAccountName = '{{ subAccountName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sub_accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.logz.sub_accounts
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subAccountName = '{{ subAccountName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
