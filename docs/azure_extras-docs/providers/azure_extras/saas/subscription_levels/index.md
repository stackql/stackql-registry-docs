---
title: subscription_levels
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_levels
  - saas
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

Creates, updates, deletes, gets or lists a <code>subscription_levels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_levels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.saas.subscription_levels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource uri |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | saas properties |
| <CopyableCode code="tags" /> | `object` | the resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets information about the specified Subscription Level SaaS. |
| <CopyableCode code="list_by_azure_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets information about all the Subscription Level SaaS in a certain Azure subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets information about all the Subscription Level SaaS in a certain resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Creates or updates a SaaS resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Deletes the specified SaaS. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Updates a SaaS Subscription Level resource. |
| <CopyableCode code="move_resources" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Move a specified Subscription Level SaaS. |
| <CopyableCode code="validate_move_resources" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Validate whether a specified Subscription Level SaaS can be moved. |

## `SELECT` examples

Gets information about all the Subscription Level SaaS in a certain Azure subscription.


```sql
SELECT
id,
name,
properties,
tags,
type
FROM azure_extras.saas.subscription_levels
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subscription_levels</code> resource.

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
INSERT INTO azure_extras.saas.subscription_levels (
resourceGroupName,
resourceName,
subscriptionId,
name,
tags,
location,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ name }}',
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: tags
      value: []
    - name: location
      value: string
    - name: properties
      value:
        - name: offerId
          value: string
        - name: publisherId
          value: string
        - name: quantity
          value: number
        - name: skuId
          value: string
        - name: paymentChannelType
          value: string
        - name: paymentChannelMetadata
          value: object
        - name: saasResourceName
          value: string
        - name: termId
          value: string
        - name: autoRenew
          value: boolean
        - name: publisherTestEnvironment
          value: string
        - name: saasSubscriptionId
          value: string
        - name: saasSessionId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>subscription_levels</code> resource.

```sql
/*+ update */
UPDATE azure_extras.saas.subscription_levels
SET 
name = '{{ name }}',
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>subscription_levels</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.saas.subscription_levels
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
