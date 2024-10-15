---
title: log_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - log_profiles
  - monitor
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

Creates, updates, deletes, gets or lists a <code>log_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.log_profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_log_profiles', value: 'view', },
        { label: 'log_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="categories" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="logProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_bus_rule_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| <CopyableCode code="type" /> | `text` | Azure resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | The log profile properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="logProfileName, subscriptionId" /> | Gets the log profile. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List the log profiles. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="logProfileName, subscriptionId, data__properties" /> | Create or update a log profile in Azure Monitoring REST API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="logProfileName, subscriptionId" /> | Deletes the log profile. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="logProfileName, subscriptionId" /> | Updates an existing LogProfilesResource. To update other fields use the CreateOrUpdate method. |

## `SELECT` examples

List the log profiles.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_log_profiles', value: 'view', },
        { label: 'log_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
categories,
location,
locations,
logProfileName,
retention_policy,
service_bus_rule_id,
storage_account_id,
subscriptionId,
system_data,
tags,
type
FROM azure.monitor.vw_log_profiles
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
FROM azure.monitor.log_profiles
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>log_profiles</code> resource.

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
INSERT INTO azure.monitor.log_profiles (
logProfileName,
subscriptionId,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ logProfileName }}',
'{{ subscriptionId }}',
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object
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
        - name: storageAccountId
          value: string
        - name: serviceBusRuleId
          value: string
        - name: locations
          value:
            - string
        - name: categories
          value:
            - string
        - name: retentionPolicy
          value:
            - name: enabled
              value: boolean
            - name: days
              value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>log_profiles</code> resource.

```sql
/*+ update */
UPDATE azure.monitor.log_profiles
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
logProfileName = '{{ logProfileName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>log_profiles</code> resource.

```sql
/*+ delete */
DELETE FROM azure.monitor.log_profiles
WHERE logProfileName = '{{ logProfileName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
