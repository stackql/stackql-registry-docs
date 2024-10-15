---
title: organization_api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_api_keys
  - confluent
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

Creates, updates, deletes, gets or lists a <code>organization_api_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.organization_api_keys" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterId, environmentId, organizationName, resourceGroupName, subscriptionId" /> |  |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>organization_api_keys</code> resource.

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
INSERT INTO azure_isv.confluent.organization_api_keys (
clusterId,
environmentId,
organizationName,
resourceGroupName,
subscriptionId,
name,
description
)
SELECT 
'{{ clusterId }}',
'{{ environmentId }}',
'{{ organizationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ name }}',
'{{ description }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: description
      value: string

```
</TabItem>
</Tabs>
