---
title: arc_settings_identities
hide_title: false
hide_table_of_contents: false
keywords:
  - arc_settings_identities
  - azure_stack_hci
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

Creates, updates, deletes, gets or lists a <code>arc_settings_identities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>arc_settings_identities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.arc_settings_identities" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Create Aad identity for arc settings. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>arc_settings_identities</code> resource.

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
INSERT INTO azure_stack.azure_stack_hci.arc_settings_identities (
arcSettingName,
clusterName,
resourceGroupName,
subscriptionId
)
SELECT 
'{{ arcSettingName }}',
'{{ clusterName }}',
'{{ resourceGroupName }}',
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
