---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - provider_hub
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

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the operation. |
| <CopyableCode code="actionType" /> | `string` |  |
| <CopyableCode code="display" /> | `object` | Display information of the operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | Indicates whether the operation applies to data-plane. |
| <CopyableCode code="origin" /> | `string` |  |
| <CopyableCode code="properties" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all the operations supported by Microsoft.ProviderHub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="providerNamespace, subscriptionId, data__contents" /> | Creates or updates the operation supported by the given provider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="providerNamespace, subscriptionId" /> | Deletes an operation. |
| <CopyableCode code="checkin_manifest" /> | `EXEC` | <CopyableCode code="providerNamespace, subscriptionId, data__baselineArmManifestLocation, data__environment" /> | Checkin the manifest. |
| <CopyableCode code="generate_manifest" /> | `EXEC` | <CopyableCode code="providerNamespace, subscriptionId" /> | Generates the manifest for the given provider. |
| <CopyableCode code="list_by_provider_registration" /> | `EXEC` | <CopyableCode code="providerNamespace, subscriptionId" /> | Gets the operations supported by the given provider. |

## `SELECT` examples

Lists all the operations supported by Microsoft.ProviderHub.


```sql
SELECT
name,
actionType,
display,
isDataAction,
origin,
properties
FROM azure.provider_hub.operations
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>operations</code> resource.

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
INSERT INTO azure.provider_hub.operations (
providerNamespace,
subscriptionId,
data__contents,
contents
)
SELECT 
'{{ providerNamespace }}',
'{{ subscriptionId }}',
'{{ data__contents }}',
'{{ contents }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: contents
      value:
        - - name: name
            value: string
          - name: isDataAction
            value: boolean
          - name: origin
            value: string
          - name: display
            value: string
          - name: actionType
            value: string
          - name: properties
            value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>operations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.provider_hub.operations
WHERE providerNamespace = '{{ providerNamespace }}'
AND subscriptionId = '{{ subscriptionId }}';
```
