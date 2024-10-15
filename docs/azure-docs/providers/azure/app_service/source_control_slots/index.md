---
title: source_control_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control_slots
  - app_service
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

Creates, updates, deletes, gets or lists a <code>source_control_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_control_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.source_control_slots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | SiteSourceControl resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets the source control configuration of an app. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Updates the source control configuration of an app. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Deletes the source control configuration of an app. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Updates the source control configuration of an app. |

## `SELECT` examples

Description for Gets the source control configuration of an app.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.source_control_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>source_control_slots</code> resource.

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
INSERT INTO azure.app_service.source_control_slots (
name,
resourceGroupName,
slot,
subscriptionId,
kind,
properties
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ slot }}',
'{{ subscriptionId }}',
'{{ kind }}',
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
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: repoUrl
          value: string
        - name: branch
          value: string
        - name: isManualIntegration
          value: boolean
        - name: isGitHubAction
          value: boolean
        - name: deploymentRollbackEnabled
          value: boolean
        - name: isMercurial
          value: boolean
        - name: gitHubActionConfiguration
          value:
            - name: codeConfiguration
              value:
                - name: runtimeStack
                  value: string
                - name: runtimeVersion
                  value: string
            - name: containerConfiguration
              value:
                - name: serverUrl
                  value: string
                - name: imageName
                  value: string
                - name: username
                  value: string
                - name: password
                  value: string
            - name: isLinux
              value: boolean
            - name: generateWorkflowFile
              value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>source_control_slots</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.source_control_slots
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>source_control_slots</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.source_control_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```
