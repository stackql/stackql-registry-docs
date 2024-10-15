---
title: operator_api_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - operator_api_connections
  - programmableconnectivity
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

Creates, updates, deletes, gets or lists a <code>operator_api_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operator_api_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.programmableconnectivity.operator_api_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_operator_api_connections', value: 'view', },
        { label: 'operator_api_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_secret" /> | `text` | field from the `properties` object |
| <CopyableCode code="camara_api_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="configured_application" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="operatorApiConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="operator_api_plan_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="operator_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="saas_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Operator API Connection resource properties that cannot be updated once a resource has been created. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operatorApiConnectionName, resourceGroupName, subscriptionId" /> | Get an Operator API Connection. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List OperatorApiConnection resources by resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List OperatorApiConnection resources by subscription ID. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="operatorApiConnectionName, resourceGroupName, subscriptionId" /> | Create an Operator API Connection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="operatorApiConnectionName, resourceGroupName, subscriptionId" /> | Delete an Operator API Connection. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="operatorApiConnectionName, resourceGroupName, subscriptionId" /> | Update an Operator API Connection. |

## `SELECT` examples

List OperatorApiConnection resources by subscription ID.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_operator_api_connections', value: 'view', },
        { label: 'operator_api_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
account_type,
app_id,
app_secret,
camara_api_name,
configured_application,
gateway_id,
location,
operatorApiConnectionName,
operator_api_plan_id,
operator_name,
provisioning_state,
resourceGroupName,
saas_properties,
status,
subscriptionId,
tags
FROM azure.programmableconnectivity.vw_operator_api_connections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.programmableconnectivity.operator_api_connections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>operator_api_connections</code> resource.

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
INSERT INTO azure.programmableconnectivity.operator_api_connections (
operatorApiConnectionName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ operatorApiConnectionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
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
        - name: operatorApiPlanId
          value: string
        - name: saasProperties
          value:
            - name: saasSubscriptionId
              value: string
            - name: saasResourceId
              value: string
        - name: configuredApplication
          value:
            - name: name
              value: string
            - name: applicationDescription
              value: string
            - name: applicationType
              value: string
            - name: legalName
              value: string
            - name: organizationDescription
              value: string
            - name: taxNumber
              value: string
            - name: privacyContactEmailAddress
              value: string
        - name: appId
          value: string
        - name: gatewayId
          value: string
        - name: accountType
          value: []
        - name: appSecret
          value: string
        - name: operatorName
          value: string
        - name: camaraApiName
          value: string
        - name: provisioningState
          value: []
        - name: status
          value:
            - name: state
              value: string
            - name: reason
              value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>operator_api_connections</code> resource.

```sql
/*+ update */
UPDATE azure.programmableconnectivity.operator_api_connections
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
operatorApiConnectionName = '{{ operatorApiConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>operator_api_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.programmableconnectivity.operator_api_connections
WHERE operatorApiConnectionName = '{{ operatorApiConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
