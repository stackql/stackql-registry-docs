---
title: iot_security_solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_security_solutions
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

Creates, updates, deletes, gets or lists a <code>iot_security_solutions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iot_security_solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.iot_security_solutions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iot_security_solutions', value: 'view', },
        { label: 'iot_security_solutions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="additional_workspaces" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_discovered_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="disabled_data_sources" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="export" /> | `text` | field from the `properties` object |
| <CopyableCode code="iot_hubs" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="recommendations_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="solutionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="unmasked_ip_logging_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_defined_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspace" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | Security Solution setting data |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | User this method to get details of a specific IoT Security solution based on solution name |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Use this method to get the list IoT Security solutions organized by resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Use this method to get the list of IoT Security solutions by subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Use this method to create or update yours IoT Security solution |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Use this method to delete yours IoT Security solution |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Use this method to update existing IoT Security solution tags or user defined resources. To update other fields use the CreateOrUpdate method. |

## `SELECT` examples

Use this method to get the list of IoT Security solutions by subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iot_security_solutions', value: 'view', },
        { label: 'iot_security_solutions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
additional_workspaces,
auto_discovered_resources,
disabled_data_sources,
display_name,
export,
iot_hubs,
location,
recommendations_configuration,
resourceGroupName,
solutionName,
status,
subscriptionId,
system_data,
tags,
type,
unmasked_ip_logging_status,
user_defined_resources,
workspace
FROM azure.security.vw_iot_security_solutions
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
FROM azure.security.iot_security_solutions
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>iot_security_solutions</code> resource.

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
INSERT INTO azure.security.iot_security_solutions (
resourceGroupName,
solutionName,
subscriptionId,
location,
properties,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ solutionName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ properties }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: properties
      value:
        - name: workspace
          value: string
        - name: displayName
          value: string
        - name: status
          value: string
        - name: export
          value:
            - string
        - name: disabledDataSources
          value:
            - string
        - name: iotHubs
          value:
            - string
        - name: userDefinedResources
          value:
            - name: query
              value: string
            - name: querySubscriptions
              value:
                - string
        - name: autoDiscoveredResources
          value:
            - string
        - name: recommendationsConfiguration
          value: []
        - name: unmaskedIpLoggingStatus
          value: string
        - name: additionalWorkspaces
          value:
            - - name: workspace
                value: string
              - name: type
                value: string
              - name: dataTypes
                value:
                  - string
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>iot_security_solutions</code> resource.

```sql
/*+ update */
UPDATE azure.security.iot_security_solutions
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND solutionName = '{{ solutionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>iot_security_solutions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.iot_security_solutions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND solutionName = '{{ solutionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
