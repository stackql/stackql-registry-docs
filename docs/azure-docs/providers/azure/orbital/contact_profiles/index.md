---
title: contact_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_profiles
  - orbital
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

Creates, updates, deletes, gets or lists a <code>contact_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.orbital.contact_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the contact profile resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="contactProfileName, resourceGroupName, subscriptionId" /> | Gets the specified contact Profile in a specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns list of contact profiles by Resource Group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns list of contact profiles by Subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="contactProfileName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a contact profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="contactProfileName, resourceGroupName, subscriptionId" /> | Deletes a specified contact profile resource. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="contactProfileName, resourceGroupName, subscriptionId" /> | Updates the specified contact profile tags. |

## `SELECT` examples

Returns list of contact profiles by Subscription.


```sql
SELECT
location,
properties,
tags
FROM azure.orbital.contact_profiles
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>contact_profiles</code> resource.

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
INSERT INTO azure.orbital.contact_profiles (
contactProfileName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ contactProfileName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>contact_profiles</code> resource.

```sql
/*+ delete */
DELETE FROM azure.orbital.contact_profiles
WHERE contactProfileName = '{{ contactProfileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
