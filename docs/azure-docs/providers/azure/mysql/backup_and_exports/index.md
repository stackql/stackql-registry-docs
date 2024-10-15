---
title: backup_and_exports
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_and_exports
  - mysql
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

Creates, updates, deletes, gets or lists a <code>backup_and_exports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_and_exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.backup_and_exports" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, data__backupSettings, data__targetDetails" /> | Exports the backup of the given server by creating a backup if not existing. |
| <CopyableCode code="validate_backup" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Validates if backup can be performed for given server. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backup_and_exports</code> resource.

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
INSERT INTO azure.mysql.backup_and_exports (
resourceGroupName,
serverName,
subscriptionId,
data__backupSettings,
data__targetDetails,
backupSettings,
targetDetails
)
SELECT 
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ data__backupSettings }}',
'{{ data__targetDetails }}',
'{{ backupSettings }}',
'{{ targetDetails }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: backupSettings
      value:
        - name: backupName
          value: []
        - name: backupFormat
          value: string
    - name: targetDetails
      value:
        - name: objectType
          value: string

```
</TabItem>
</Tabs>
