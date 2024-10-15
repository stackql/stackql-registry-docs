---
title: functions
hide_title: false
hide_table_of_contents: false
keywords:
  - functions
  - app_service
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

Creates, updates, deletes, gets or lists a <code>functions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.functions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | FunctionEnvelope resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="functionName, name, resourceGroupName, subscriptionId" /> | Description for Get function information by its ID for web site, or a deployment slot. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for List the functions for a web site, or a deployment slot. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="functionName, name, resourceGroupName, subscriptionId" /> | Description for Create function for web site, or a deployment slot. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="functionName, name, resourceGroupName, subscriptionId" /> | Description for Delete a function for web site, or a deployment slot. |

## `SELECT` examples

Description for List the functions for a web site, or a deployment slot.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.functions
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>functions</code> resource.

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
INSERT INTO azure.app_service.functions (
functionName,
name,
resourceGroupName,
subscriptionId,
kind,
properties
)
SELECT 
'{{ functionName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
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
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: function_app_id
          value: string
        - name: script_root_path_href
          value: string
        - name: script_href
          value: string
        - name: config_href
          value: string
        - name: test_data_href
          value: string
        - name: secrets_file_href
          value: string
        - name: href
          value: string
        - name: config
          value: object
        - name: files
          value: object
        - name: test_data
          value: string
        - name: invoke_url_template
          value: string
        - name: language
          value: string
        - name: isDisabled
          value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>functions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.functions
WHERE functionName = '{{ functionName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
