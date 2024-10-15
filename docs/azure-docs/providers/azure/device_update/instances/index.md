---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - device_update
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

Creates, updates, deletes, gets or lists a <code>instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_update.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Device Update instance properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, instanceName, resourceGroupName, subscriptionId" /> | Returns instance details for the given instance and account name. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Returns instances for the given account name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, instanceName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, instanceName, resourceGroupName, subscriptionId" /> | Deletes instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, instanceName, resourceGroupName, subscriptionId" /> | Updates instance's tags. |

## `SELECT` examples

Returns instances for the given account name.


```sql
SELECT
location,
properties,
tags
FROM azure.device_update.instances
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instances</code> resource.

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
INSERT INTO azure.device_update.instances (
accountName,
instanceName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ accountName }}',
'{{ instanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: accountName
          value: string
        - name: iotHubs
          value:
            - - name: resourceId
                value: string
        - name: enableDiagnostics
          value: boolean
        - name: diagnosticStorageProperties
          value:
            - name: authenticationType
              value: string
            - name: connectionString
              value: string
            - name: resourceId
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>instances</code> resource.

```sql
/*+ update */
UPDATE azure.device_update.instances
SET 
tags = '{{ tags }}'
WHERE 
accountName = '{{ accountName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.device_update.instances
WHERE accountName = '{{ accountName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
