---
title: connector_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_applications
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

Creates, updates, deletes, gets or lists a <code>connector_applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.connector_applications" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connector_applications', value: 'view', },
        { label: 'connector_applications', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="condition_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="securityConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes properties of an application |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationId, resourceGroupName, securityConnectorName, subscriptionId" /> | Get a specific application for the requested scope by applicationId |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, securityConnectorName, subscriptionId" /> | Get a list of all relevant applications over a security connector level scope |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationId, resourceGroupName, securityConnectorName, subscriptionId" /> | Creates or update a security Application on the given security connector. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationId, resourceGroupName, securityConnectorName, subscriptionId" /> | Delete an Application over a given scope |

## `SELECT` examples

Get a list of all relevant applications over a security connector level scope

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connector_applications', value: 'view', },
        { label: 'connector_applications', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
applicationId,
condition_sets,
display_name,
resourceGroupName,
securityConnectorName,
source_resource_type,
subscriptionId,
type
FROM azure.security.vw_connector_applications
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.connector_applications
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connector_applications</code> resource.

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
INSERT INTO azure.security.connector_applications (
applicationId,
resourceGroupName,
securityConnectorName,
subscriptionId,
properties
)
SELECT 
'{{ applicationId }}',
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
    - name: properties
      value:
        - name: displayName
          value: string
        - name: description
          value: string
        - name: sourceResourceType
          value: string
        - name: conditionSets
          value:
            - []
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>connector_applications</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.connector_applications
WHERE applicationId = '{{ applicationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
