---
title: exclusions
hide_title: false
hide_table_of_contents: false
keywords:
  - exclusions
  - logging
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

Creates, updates, deletes, gets or lists a <code>exclusions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>exclusions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.logging.exclusions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. A client-assigned identifier, such as "load-balancer-exclusion". Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods. First character has to be alphanumeric. |
| <CopyableCode code="description" /> | `string` | Optional. A description of this exclusion. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of the exclusion.This field may not be present for older exclusions. |
| <CopyableCode code="disabled" /> | `boolean` | Optional. If set to True, then this exclusion is disabled and it does not exclude any log entries. You can update an exclusion to change the value of this field. |
| <CopyableCode code="filter" /> | `string` | Required. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-queries) that matches the log entries to be excluded. By using the sample function (https://cloud.google.com/logging/docs/view/advanced-queries#sample), you can exclude less than 100% of the matching log entries.For example, the following query matches 99% of low-severity log entries from Google Cloud Storage buckets:resource.type=gcs_bucket severity<ERROR sample(insertId, 0.99) |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of the exclusion.This field may not be present for older exclusions. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_exclusions_get" /> | `SELECT` | <CopyableCode code="billingAccountsId, exclusionsId" /> | Gets the description of an exclusion in the _Default sink. |
| <CopyableCode code="billing_accounts_exclusions_list" /> | `SELECT` | <CopyableCode code="billingAccountsId" /> | Lists all the exclusions on the _Default sink in a parent resource. |
| <CopyableCode code="exclusions_get" /> | `SELECT` | <CopyableCode code="name" /> | Gets the description of an exclusion in the _Default sink. |
| <CopyableCode code="exclusions_list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | Lists all the exclusions on the _Default sink in a parent resource. |
| <CopyableCode code="folders_exclusions_get" /> | `SELECT` | <CopyableCode code="exclusionsId, foldersId" /> | Gets the description of an exclusion in the _Default sink. |
| <CopyableCode code="folders_exclusions_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists all the exclusions on the _Default sink in a parent resource. |
| <CopyableCode code="organizations_exclusions_get" /> | `SELECT` | <CopyableCode code="exclusionsId, organizationsId" /> | Gets the description of an exclusion in the _Default sink. |
| <CopyableCode code="organizations_exclusions_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all the exclusions on the _Default sink in a parent resource. |
| <CopyableCode code="projects_exclusions_get" /> | `SELECT` | <CopyableCode code="exclusionsId, projectsId" /> | Gets the description of an exclusion in the _Default sink. |
| <CopyableCode code="projects_exclusions_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists all the exclusions on the _Default sink in a parent resource. |
| <CopyableCode code="billing_accounts_exclusions_create" /> | `INSERT` | <CopyableCode code="billingAccountsId" /> | Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource. |
| <CopyableCode code="exclusions_create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource. |
| <CopyableCode code="folders_exclusions_create" /> | `INSERT` | <CopyableCode code="foldersId" /> | Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource. |
| <CopyableCode code="organizations_exclusions_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource. |
| <CopyableCode code="projects_exclusions_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource. |
| <CopyableCode code="billing_accounts_exclusions_delete" /> | `DELETE` | <CopyableCode code="billingAccountsId, exclusionsId" /> | Deletes an exclusion in the _Default sink. |
| <CopyableCode code="exclusions_delete" /> | `DELETE` | <CopyableCode code="name" /> | Deletes an exclusion in the _Default sink. |
| <CopyableCode code="folders_exclusions_delete" /> | `DELETE` | <CopyableCode code="exclusionsId, foldersId" /> | Deletes an exclusion in the _Default sink. |
| <CopyableCode code="organizations_exclusions_delete" /> | `DELETE` | <CopyableCode code="exclusionsId, organizationsId" /> | Deletes an exclusion in the _Default sink. |
| <CopyableCode code="projects_exclusions_delete" /> | `DELETE` | <CopyableCode code="exclusionsId, projectsId" /> | Deletes an exclusion in the _Default sink. |
| <CopyableCode code="billing_accounts_exclusions_patch" /> | `UPDATE` | <CopyableCode code="billingAccountsId, exclusionsId" /> | Changes one or more properties of an existing exclusion in the _Default sink. |
| <CopyableCode code="exclusions_patch" /> | `UPDATE` | <CopyableCode code="name" /> | Changes one or more properties of an existing exclusion in the _Default sink. |
| <CopyableCode code="folders_exclusions_patch" /> | `UPDATE` | <CopyableCode code="exclusionsId, foldersId" /> | Changes one or more properties of an existing exclusion in the _Default sink. |
| <CopyableCode code="organizations_exclusions_patch" /> | `UPDATE` | <CopyableCode code="exclusionsId, organizationsId" /> | Changes one or more properties of an existing exclusion in the _Default sink. |
| <CopyableCode code="projects_exclusions_patch" /> | `UPDATE` | <CopyableCode code="exclusionsId, projectsId" /> | Changes one or more properties of an existing exclusion in the _Default sink. |

## `SELECT` examples

Gets the description of an exclusion in the _Default sink.

```sql
SELECT
name,
description,
createTime,
disabled,
filter,
updateTime
FROM google.logging.exclusions
WHERE name = '{{ name }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>exclusions</code> resource.

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
INSERT INTO google.logging.exclusions (
foldersId,
name,
description,
filter,
disabled,
createTime,
updateTime
)
SELECT 
'{{ foldersId }}',
'{{ name }}',
'{{ description }}',
'{{ filter }}',
true|false,
'{{ createTime }}',
'{{ updateTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: filter
      value: '{{ filter }}'
    - name: disabled
      value: '{{ disabled }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>exclusions</code> resource.

```sql
/*+ update */
UPDATE google.logging.exclusions
SET 
name = '{{ name }}',
description = '{{ description }}',
filter = '{{ filter }}',
disabled = true|false,
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}'
WHERE 
name = '{{ name }}';
```

## `DELETE` example

Deletes the specified <code>exclusions</code> resource.

```sql
/*+ delete */
DELETE FROM google.logging.exclusions
WHERE name = '{{ name }}';
```
