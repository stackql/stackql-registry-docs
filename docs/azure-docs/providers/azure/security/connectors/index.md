---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
  - security
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

Creates, updates, deletes, gets or lists a <code>connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.connectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connectors', value: 'view', },
        { label: 'connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="environment_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="environment_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hierarchy_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="hierarchy_identifier_trial_end_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="offerings" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="securityConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A set of properties that defines the security connector configuration. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, securityConnectorName, subscriptionId" /> | Retrieves details of a specific security connector |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the security connectors in the specified subscription. Use the 'nextLink' property in the response to get the next page of security connectors for the specified subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the security connectors in the specified resource group. Use the 'nextLink' property in the response to get the next page of security connectors for the specified resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, securityConnectorName, subscriptionId" /> | Creates or updates a security connector. If a security connector is already created and a subsequent request is issued for the same security connector id, then it will be updated. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, securityConnectorName, subscriptionId" /> | Deletes a security connector. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, securityConnectorName, subscriptionId" /> | Updates a security connector |

## `SELECT` examples

Lists all the security connectors in the specified subscription. Use the 'nextLink' property in the response to get the next page of security connectors for the specified subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connectors', value: 'view', },
        { label: 'connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
environment_data,
environment_name,
hierarchy_identifier,
hierarchy_identifier_trial_end_date,
offerings,
resourceGroupName,
securityConnectorName,
subscriptionId,
system_data
FROM azure.security.vw_connectors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.security.connectors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connectors</code> resource.

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
INSERT INTO azure.security.connectors (
resourceGroupName,
securityConnectorName,
subscriptionId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ securityConnectorName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
    - name: properties
      value:
        - name: hierarchyIdentifier
          value: string
        - name: hierarchyIdentifierTrialEndDate
          value: string
        - name: environmentName
          value: string
        - name: offerings
          value:
            - - name: offeringType
                value: string
              - name: description
                value: string
        - name: environmentData
          value:
            - name: environmentType
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connectors</code> resource.

```sql
/*+ update */
UPDATE azure.security.connectors
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>connectors</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.connectors
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
