---
title: custom_resource_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_resource_providers
  - custom_providers
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

Creates, updates, deletes, gets or lists a <code>custom_resource_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_resource_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.custom_providers.custom_resource_providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | The manifest for the custom resource provider |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceProviderName, subscriptionId" /> | Gets the custom resource provider manifest. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the custom resource providers within a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the custom resource providers within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceProviderName, subscriptionId" /> | Creates or updates the custom resource provider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceProviderName, subscriptionId" /> | Deletes the custom resource provider. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceProviderName, subscriptionId" /> | Updates an existing custom resource provider. The only value that can be updated via PATCH currently is the tags. |

## `SELECT` examples

Gets all the custom resource providers within a subscription.


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.custom_providers.custom_resource_providers
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_resource_providers</code> resource.

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
INSERT INTO azure.custom_providers.custom_resource_providers (
resourceGroupName,
resourceProviderName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceProviderName }}',
'{{ subscriptionId }}',
'{{ properties }}',
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
        - name: actions
          value:
            - - name: routingType
                value: string
              - name: name
                value: string
              - name: endpoint
                value: string
        - name: resourceTypes
          value:
            - - name: routingType
                value: string
              - name: name
                value: string
              - name: endpoint
                value: string
        - name: validations
          value:
            - - name: validationType
                value: string
              - name: specification
                value: string
        - name: provisioningState
          value: string
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>custom_resource_providers</code> resource.

```sql
/*+ update */
UPDATE azure.custom_providers.custom_resource_providers
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceProviderName = '{{ resourceProviderName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>custom_resource_providers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.custom_providers.custom_resource_providers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceProviderName = '{{ resourceProviderName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
