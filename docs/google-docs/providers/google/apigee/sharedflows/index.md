---
title: sharedflows
hide_title: false
hide_table_of_contents: false
keywords:
  - sharedflows
  - apigee
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

Creates, updates, deletes, gets or lists a <code>sharedflows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sharedflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.sharedflows" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The ID of the shared flow. |
| <CopyableCode code="latestRevisionId" /> | `string` | The id of the most recently created revision for this shared flow. |
| <CopyableCode code="metaData" /> | `object` | Metadata common to many entities in this API. |
| <CopyableCode code="revision" /> | `array` | A list of revisions of this shared flow. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_sharedflows_get" /> | `SELECT` | <CopyableCode code="organizationsId, sharedflowsId" /> | Gets a shared flow by name, including a list of its revisions. |
| <CopyableCode code="organizations_sharedflows_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all shared flows in the organization. |
| <CopyableCode code="organizations_sharedflows_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Uploads a ZIP-formatted shared flow configuration bundle to an organization. If the shared flow already exists, this creates a new revision of it. If the shared flow does not exist, this creates it. Once imported, the shared flow revision must be deployed before it can be accessed at runtime. The size limit of a shared flow bundle is 15 MB. |
| <CopyableCode code="organizations_sharedflows_delete" /> | `DELETE` | <CopyableCode code="organizationsId, sharedflowsId" /> | Deletes a shared flow and all it's revisions. The shared flow must be undeployed before you can delete it. |

## `SELECT` examples

Lists all shared flows in the organization.

```sql
SELECT
name,
latestRevisionId,
metaData,
revision
FROM google.apigee.sharedflows
WHERE organizationsId = '{{ organizationsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sharedflows</code> resource.

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
INSERT INTO google.apigee.sharedflows (
organizationsId,
contentType,
data,
extensions
)
SELECT 
'{{ organizationsId }}',
'{{ contentType }}',
'{{ data }}',
'{{ extensions }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: contentType
      value: string
    - name: data
      value: string
    - name: extensions
      value:
        - object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sharedflows</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.sharedflows
WHERE organizationsId = '{{ organizationsId }}'
AND sharedflowsId = '{{ sharedflowsId }}';
```
