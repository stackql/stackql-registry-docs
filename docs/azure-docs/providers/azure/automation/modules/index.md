---
title: modules
hide_title: false
hide_table_of_contents: false
keywords:
  - modules
  - automation
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

Creates, updates, deletes, gets or lists a <code>modules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.modules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_modules', value: 'view', },
        { label: 'modules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="activity_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Gets the etag of the resource. |
| <CopyableCode code="is_composite" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_global" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="moduleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="size_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Gets the etag of the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Definition of the module property type. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, moduleName, resourceGroupName, subscriptionId" /> | Retrieve the module identified by module name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of modules. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, moduleName, resourceGroupName, subscriptionId, data__properties" /> | Create or Update the module identified by module name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, moduleName, resourceGroupName, subscriptionId" /> | Delete the module by name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="automationAccountName, moduleName, resourceGroupName, subscriptionId" /> | Update the module identified by module name. |

## `SELECT` examples

Retrieve a list of modules.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_modules', value: 'view', },
        { label: 'modules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
activity_count,
automationAccountName,
content_link,
creation_time,
error,
etag,
is_composite,
is_global,
last_modified_time,
location,
moduleName,
provisioning_state,
resourceGroupName,
size_in_bytes,
subscriptionId,
tags,
version
FROM azure.automation.vw_modules
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
tags
FROM azure.automation.modules
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>modules</code> resource.

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
INSERT INTO azure.automation.modules (
automationAccountName,
moduleName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
name,
location,
tags
)
SELECT 
'{{ automationAccountName }}',
'{{ moduleName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ name }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: contentLink
          value:
            - name: uri
              value: string
            - name: contentHash
              value:
                - name: algorithm
                  value: string
                - name: value
                  value: string
            - name: version
              value: string
    - name: name
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>modules</code> resource.

```sql
/*+ update */
UPDATE azure.automation.modules
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
automationAccountName = '{{ automationAccountName }}'
AND moduleName = '{{ moduleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>modules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.modules
WHERE automationAccountName = '{{ automationAccountName }}'
AND moduleName = '{{ moduleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
