---
title: sensitivity_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - sensitivity_settings
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

Creates, updates, deletes, gets or lists a <code>sensitivity_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sensitivity_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.sensitivity_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the sensitivity settings |
| <CopyableCode code="name" /> | `string` | The name of the sensitivity settings |
| <CopyableCode code="properties" /> | `object` | The sensitivity settings properties |
| <CopyableCode code="type" /> | `string` | The type of the sensitivity settings |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> | Gets data sensitivity settings for sensitive data discovery |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Gets a list with a single sensitivity settings resource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="data__sensitiveInfoTypesIds" /> | Create or update data sensitivity settings for sensitive data discovery |

## `SELECT` examples

Gets data sensitivity settings for sensitive data discovery


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.sensitivity_settings
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sensitivity_settings</code> resource.

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
INSERT INTO azure.security.sensitivity_settings (
data__sensitiveInfoTypesIds,
sensitiveInfoTypesIds,
sensitivityThresholdLabelOrder,
sensitivityThresholdLabelId
)
SELECT 
'{{ data__sensitiveInfoTypesIds }}',
'{{ sensitiveInfoTypesIds }}',
{{ sensitivityThresholdLabelOrder }},
'{{ sensitivityThresholdLabelId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: sensitiveInfoTypesIds
      value: []
    - name: sensitivityThresholdLabelOrder
      value: number
    - name: sensitivityThresholdLabelId
      value: string

```
</TabItem>
</Tabs>
