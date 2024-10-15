---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
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

Creates, updates, deletes, gets or lists a <code>resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.saas.resources" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceId" /> | Gets information about the specified SaaS. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Get All Resources |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates a SaaS resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceId" /> | Updates a SaaS resource. |

## `SELECT` examples

Get All Resources


```sql
SELECT
id,
name,
properties,
tags,
type
FROM azure_extras.saas.resources
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resources</code> resource.

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
INSERT INTO azure_extras.saas.resources (
name,
tags,
location,
properties
)
SELECT 
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

Updates a <code>resources</code> resource.

```sql
/*+ update */
UPDATE azure_extras.saas.resources
SET 
name = '{{ name }}',
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resourceId = '{{ resourceId }}';
```
