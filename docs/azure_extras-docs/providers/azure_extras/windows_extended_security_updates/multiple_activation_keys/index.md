---
title: multiple_activation_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - multiple_activation_keys
  - windows_extended_security_updates
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

Creates, updates, deletes, gets or lists a <code>multiple_activation_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multiple_activation_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.windows_extended_security_updates.multiple_activation_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | MAK key specific properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="multipleActivationKeyName, resourceGroupName, subscriptionId" /> | Get a MAK key. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all Multiple Activation Keys (MAK) created for a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all Multiple Activation Keys (MAK) in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="multipleActivationKeyName, resourceGroupName, subscriptionId" /> | Create a MAK key. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="multipleActivationKeyName, resourceGroupName, subscriptionId" /> | Delete a MAK key. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="multipleActivationKeyName, resourceGroupName, subscriptionId" /> | Update a MAK key. |

## `SELECT` examples

List all Multiple Activation Keys (MAK) created for a subscription.


```sql
SELECT
location,
properties,
tags
FROM azure_extras.windows_extended_security_updates.multiple_activation_keys
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>multiple_activation_keys</code> resource.

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
INSERT INTO azure_extras.windows_extended_security_updates.multiple_activation_keys (
multipleActivationKeyName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ multipleActivationKeyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
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
        - name: multipleActivationKey
          value: string
        - name: expirationDate
          value: string
        - name: osType
          value: string
        - name: supportType
          value: string
        - name: installedServerNumber
          value: integer
        - name: agreementNumber
          value: string
        - name: isEligible
          value: boolean
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>multiple_activation_keys</code> resource.

```sql
/*+ update */
UPDATE azure_extras.windows_extended_security_updates.multiple_activation_keys
SET 
tags = '{{ tags }}'
WHERE 
multipleActivationKeyName = '{{ multipleActivationKeyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>multiple_activation_keys</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.windows_extended_security_updates.multiple_activation_keys
WHERE multipleActivationKeyName = '{{ multipleActivationKeyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
