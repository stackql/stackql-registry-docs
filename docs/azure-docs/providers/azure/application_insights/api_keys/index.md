---
title: api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - api_keys
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>api_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.api_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique ID of the API key inside an Application Insights component. It is auto generated when the API key is created. |
| <CopyableCode code="name" /> | `string` | The name of the API key. |
| <CopyableCode code="apiKey" /> | `string` | The API key value. It will be only return once when the API Key was created. |
| <CopyableCode code="createdDate" /> | `string` | The create date of this API key. |
| <CopyableCode code="linkedReadProperties" /> | `array` | The read access rights of this API Key. |
| <CopyableCode code="linkedWriteProperties" /> | `array` | The write access rights of this API Key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyId, resourceGroupName, resourceName, subscriptionId" /> | Get the API Key for this key id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets a list of API keys of an Application Insights component. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create an API Key of an Application Insights component. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keyId, resourceGroupName, resourceName, subscriptionId" /> | Delete an API Key of an Application Insights component. |

## `SELECT` examples

Gets a list of API keys of an Application Insights component.


```sql
SELECT
id,
name,
apiKey,
createdDate,
linkedReadProperties,
linkedWriteProperties
FROM azure.application_insights.api_keys
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_keys</code> resource.

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
INSERT INTO azure.application_insights.api_keys (
resourceGroupName,
resourceName,
subscriptionId,
name,
linkedReadProperties,
linkedWriteProperties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ name }}',
'{{ linkedReadProperties }}',
'{{ linkedWriteProperties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: linkedReadProperties
      value:
        - string
    - name: linkedWriteProperties
      value:
        - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>api_keys</code> resource.

```sql
/*+ delete */
DELETE FROM azure.application_insights.api_keys
WHERE keyId = '{{ keyId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
