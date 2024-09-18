---
title: data_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - data_policies
  - bigquerydatapolicy
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

Creates, updates, deletes, gets or lists a <code>data_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigquerydatapolicy.data_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of this data policy, in the format of `projects/{project_number}/locations/{location_id}/dataPolicies/{data_policy_id}`. |
| <CopyableCode code="dataMaskingPolicy" /> | `object` | The data masking policy that is used to specify data masking rule. |
| <CopyableCode code="dataPolicyId" /> | `string` | User-assigned (human readable) ID of the data policy that needs to be unique within a project. Used as {data_policy_id} in part of the resource name. |
| <CopyableCode code="dataPolicyType" /> | `string` | Type of data policy. |
| <CopyableCode code="policyTag" /> | `string` | Policy tag resource name, in the format of `projects/{project_number}/locations/{location_id}/taxonomies/{taxonomy_id}/policyTags/{policyTag_id}`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataPoliciesId, locationsId, projectsId" /> | Gets the data policy specified by its resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List all of the data policies in the specified parent project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new data policy under a project with the given `dataPolicyId` (used as the display name), policy tag, and data policy type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataPoliciesId, locationsId, projectsId" /> | Deletes the data policy specified by its resource name. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="dataPoliciesId, locationsId, projectsId" /> | Updates the metadata for an existing data policy. The target data policy can be specified by the resource name. |
| <CopyableCode code="rename" /> | `EXEC` | <CopyableCode code="dataPoliciesId, locationsId, projectsId" /> | Renames the id (display name) of the specified data policy. |

## `SELECT` examples

List all of the data policies in the specified parent project.

```sql
SELECT
name,
dataMaskingPolicy,
dataPolicyId,
dataPolicyType,
policyTag
FROM google.bigquerydatapolicy.data_policies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_policies</code> resource.

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
INSERT INTO google.bigquerydatapolicy.data_policies (
locationsId,
projectsId,
policyTag,
dataMaskingPolicy,
dataPolicyType,
dataPolicyId
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ policyTag }}',
'{{ dataMaskingPolicy }}',
'{{ dataPolicyType }}',
'{{ dataPolicyId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
policyTag: string
dataMaskingPolicy:
  predefinedExpression: string
  routine: string
name: string
dataPolicyType: string
dataPolicyId: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>data_policies</code> resource.

```sql
/*+ update */
UPDATE google.bigquerydatapolicy.data_policies
SET 
policyTag = '{{ policyTag }}',
dataMaskingPolicy = '{{ dataMaskingPolicy }}',
dataPolicyType = '{{ dataPolicyType }}',
dataPolicyId = '{{ dataPolicyId }}'
WHERE 
dataPoliciesId = '{{ dataPoliciesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>data_policies</code> resource.

```sql
/*+ delete */
DELETE FROM google.bigquerydatapolicy.data_policies
WHERE dataPoliciesId = '{{ dataPoliciesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
