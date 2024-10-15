---
title: fabrics
hide_title: false
hide_table_of_contents: false
keywords:
  - fabrics
  - data_replication
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

Creates, updates, deletes, gets or lists a <code>fabrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fabrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_replication.fabrics" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_fabrics', value: 'view', },
        { label: 'fabrics', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name of the resource. |
| <CopyableCode code="custom_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="health" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Gets or sets the location of the fabric. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Gets or sets the resource tags. |
| <CopyableCode code="type" /> | `text` | Gets or sets the type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of the resource. |
| <CopyableCode code="location" /> | `string` | Gets or sets the location of the fabric. |
| <CopyableCode code="properties" /> | `object` | Fabric model properties. |
| <CopyableCode code="systemData" /> | `object` | System data required to be defined for Azure resources. |
| <CopyableCode code="tags" /> | `object` | Gets or sets the resource tags. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, resourceGroupName, subscriptionId" /> | Gets the details of the fabric. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets the list of fabrics in the given subscription and resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the list of fabrics in the given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fabricName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Creates the fabric. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fabricName, resourceGroupName, subscriptionId" /> | Removes the fabric. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="fabricName, resourceGroupName, subscriptionId" /> | Performs update on the fabric. |

## `SELECT` examples

Gets the list of fabrics in the given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_fabrics', value: 'view', },
        { label: 'fabrics', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
custom_properties,
fabricName,
health,
health_errors,
location,
provisioning_state,
resourceGroupName,
service_endpoint,
service_resource_id,
subscriptionId,
system_data,
tags,
type
FROM azure.data_replication.vw_fabrics
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
systemData,
tags,
type
FROM azure.data_replication.fabrics
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>fabrics</code> resource.

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
INSERT INTO azure.data_replication.fabrics (
fabricName,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ fabricName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: serviceEndpoint
          value: string
        - name: serviceResourceId
          value: string
        - name: health
          value: string
        - name: healthErrors
          value:
            - - name: affectedResourceType
                value: string
              - name: affectedResourceCorrelationIds
                value:
                  - string
              - name: childErrors
                value:
                  - - name: code
                      value: string
                    - name: healthCategory
                      value: string
                    - name: category
                      value: string
                    - name: severity
                      value: string
                    - name: source
                      value: string
                    - name: creationTime
                      value: string
                    - name: isCustomerResolvable
                      value: boolean
                    - name: summary
                      value: string
                    - name: message
                      value: string
                    - name: causes
                      value: string
                    - name: recommendation
                      value: string
              - name: code
                value: string
              - name: healthCategory
                value: string
              - name: category
                value: string
              - name: severity
                value: string
              - name: source
                value: string
              - name: creationTime
                value: string
              - name: isCustomerResolvable
                value: boolean
              - name: summary
                value: string
              - name: message
                value: string
              - name: causes
                value: string
              - name: recommendation
                value: string
        - name: customProperties
          value:
            - name: instanceType
              value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>fabrics</code> resource.

```sql
/*+ update */
UPDATE azure.data_replication.fabrics
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
fabricName = '{{ fabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>fabrics</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_replication.fabrics
WHERE fabricName = '{{ fabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
