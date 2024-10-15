---
title: operators
hide_title: false
hide_table_of_contents: false
keywords:
  - operators
  - security
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

Creates, updates, deletes, gets or lists a <code>operators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.operators" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="pricingName, securityOperatorName, subscriptionId" /> | Get a specific security operator for the requested scope. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="pricingName, subscriptionId" /> | Lists Microsoft Defender for Cloud securityOperators in the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="pricingName, securityOperatorName, subscriptionId" /> | Creates Microsoft Defender for Cloud security operator on the given scope. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="pricingName, securityOperatorName, subscriptionId" /> | Delete Microsoft Defender for Cloud securityOperator in the subscription. |

## `SELECT` examples

Lists Microsoft Defender for Cloud securityOperators in the subscription.


```sql
SELECT
id,
name,
identity,
type
FROM azure.security.operators
WHERE pricingName = '{{ pricingName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>operators</code> resource.

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
INSERT INTO azure.security.operators (
pricingName,
securityOperatorName,
subscriptionId
)
SELECT 
'{{ pricingName }}',
'{{ securityOperatorName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>operators</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.operators
WHERE pricingName = '{{ pricingName }}'
AND securityOperatorName = '{{ securityOperatorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
