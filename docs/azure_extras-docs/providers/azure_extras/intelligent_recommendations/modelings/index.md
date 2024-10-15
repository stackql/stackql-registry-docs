---
title: modelings
hide_title: false
hide_table_of_contents: false
keywords:
  - modelings
  - intelligent_recommendations
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

Creates, updates, deletes, gets or lists a <code>modelings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>modelings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.intelligent_recommendations.modelings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Modeling resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, modelingName, resourceGroupName, subscriptionId" /> | Returns Modeling resources for a given name. |
| <CopyableCode code="list_by_account_resource" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Returns list of Modeling resources for a given Account name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, modelingName, resourceGroupName, subscriptionId" /> | Creates or updates Modeling resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, modelingName, resourceGroupName, subscriptionId" /> | Deletes Modeling resources of a given name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, modelingName, resourceGroupName, subscriptionId" /> | Updates Modeling resource details. |

## `SELECT` examples

Returns list of Modeling resources for a given Account name.


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure_extras.intelligent_recommendations.modelings
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>modelings</code> resource.

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
INSERT INTO azure_extras.intelligent_recommendations.modelings (
accountName,
modelingName,
resourceGroupName,
subscriptionId,
tags,
location,
properties,
systemData
)
SELECT 
'{{ accountName }}',
'{{ modelingName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ systemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: features
          value: string
        - name: frequency
          value: string
        - name: size
          value: string
        - name: inputData
          value:
            - name: connectionString
              value: string
        - name: provisioningState
          value: string
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>modelings</code> resource.

```sql
/*+ update */
UPDATE azure_extras.intelligent_recommendations.modelings
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND modelingName = '{{ modelingName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>modelings</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.intelligent_recommendations.modelings
WHERE accountName = '{{ accountName }}'
AND modelingName = '{{ modelingName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
