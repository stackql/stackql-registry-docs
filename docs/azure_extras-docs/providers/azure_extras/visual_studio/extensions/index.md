---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - visual_studio
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

Creates, updates, deletes, gets or lists a <code>extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.visual_studio.extensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier of the resource. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="plan" /> | `object` | Plan data for an extension resource. |
| <CopyableCode code="properties" /> | `object` | Resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountResourceName, extensionResourceName, resourceGroupName, subscriptionId" /> | Gets the details of an extension associated with a Visual Studio Team Services account resource. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountResourceName, resourceGroupName, subscriptionId" /> | Gets the details of the extension resources created within the resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountResourceName, extensionResourceName, resourceGroupName, subscriptionId" /> | Registers the extension with a Visual Studio Team Services account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountResourceName, extensionResourceName, resourceGroupName, subscriptionId" /> | Removes an extension resource registration for a Visual Studio Team Services account. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountResourceName, extensionResourceName, resourceGroupName, subscriptionId" /> | Updates an existing extension registration for the Visual Studio Team Services account. |

## `SELECT` examples

Gets the details of the extension resources created within the resource group.


```sql
SELECT
id,
name,
location,
plan,
properties,
tags,
type
FROM azure_extras.visual_studio.extensions
WHERE accountResourceName = '{{ accountResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>extensions</code> resource.

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
INSERT INTO azure_extras.visual_studio.extensions (
accountResourceName,
extensionResourceName,
resourceGroupName,
subscriptionId,
location,
plan,
properties,
tags
)
SELECT 
'{{ accountResourceName }}',
'{{ extensionResourceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ plan }}',
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
    - name: plan
      value:
        - name: name
          value: string
        - name: product
          value: string
        - name: promotionCode
          value: string
        - name: publisher
          value: string
        - name: version
          value: string
    - name: properties
      value: object
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>extensions</code> resource.

```sql
/*+ update */
UPDATE azure_extras.visual_studio.extensions
SET 
location = '{{ location }}',
plan = '{{ plan }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
accountResourceName = '{{ accountResourceName }}'
AND extensionResourceName = '{{ extensionResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>extensions</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.visual_studio.extensions
WHERE accountResourceName = '{{ accountResourceName }}'
AND extensionResourceName = '{{ extensionResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
