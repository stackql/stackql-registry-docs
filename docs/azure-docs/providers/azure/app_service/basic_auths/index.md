---
title: basic_auths
hide_title: false
hide_table_of_contents: false
keywords:
  - basic_auths
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

Creates, updates, deletes, gets or lists a <code>basic_auths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>basic_auths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.basic_auths" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | StaticSiteBasicAuthPropertiesARMResource resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="basicAuthName, name, resourceGroupName, subscriptionId" /> | Description for Gets the basic auth properties for a static site. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets the basic auth properties for a static site as a collection. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="basicAuthName, name, resourceGroupName, subscriptionId" /> | Description for Adds or updates basic auth for a static site. |

## `SELECT` examples

Description for Gets the basic auth properties for a static site as a collection.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.basic_auths
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>basic_auths</code> resource.

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
INSERT INTO azure.app_service.basic_auths (
basicAuthName,
name,
resourceGroupName,
subscriptionId,
kind,
properties
)
SELECT 
'{{ basicAuthName }}',
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
        - name: password
          value: string
        - name: secretUrl
          value: string
        - name: applicableEnvironmentsMode
          value: string
        - name: environments
          value:
            - string
        - name: secretState
          value: string

```
</TabItem>
</Tabs>
