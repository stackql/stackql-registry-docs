---
title: external_users
hide_title: false
hide_table_of_contents: false
keywords:
  - external_users
  - elastic
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

Creates, updates, deletes, gets or lists a <code>external_users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>external_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.external_users" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>external_users</code> resource.

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
INSERT INTO azure_isv.elastic.external_users (
monitorName,
resourceGroupName,
subscriptionId,
userName,
fullName,
password,
emailId,
roles
)
SELECT 
'{{ monitorName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ userName }}',
'{{ fullName }}',
'{{ password }}',
'{{ emailId }}',
'{{ roles }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: userName
      value: string
    - name: fullName
      value: string
    - name: password
      value: string
    - name: emailId
      value: string
    - name: roles
      value:
        - string

```
</TabItem>
</Tabs>
