---
title: authorized_views
hide_title: false
hide_table_of_contents: false
keywords:
  - authorized_views
  - bigtableadmin
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

Creates, updates, deletes, gets or lists a <code>authorized_views</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorized_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigtableadmin.authorized_views" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The name of this AuthorizedView. Values are of the form `projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{authorized_view}` |
| <CopyableCode code="deletionProtection" /> | `boolean` | Set to true to make the AuthorizedView protected against deletion. The parent Table and containing Instance cannot be deleted if an AuthorizedView has this bit set. |
| <CopyableCode code="etag" /> | `string` | The etag for this AuthorizedView. If this is provided on update, it must match the server's etag. The server returns ABORTED error on a mismatched etag. |
| <CopyableCode code="subsetView" /> | `object` | Defines a simple AuthorizedView that is a subset of the underlying Table. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizedViewsId, instancesId, projectsId, tablesId" /> | Gets information from a specified AuthorizedView. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instancesId, projectsId, tablesId" /> | Lists all AuthorizedViews from a specific table. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="instancesId, projectsId, tablesId" /> | Creates a new AuthorizedView in a table. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authorizedViewsId, instancesId, projectsId, tablesId" /> | Permanently deletes a specified AuthorizedView. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="authorizedViewsId, instancesId, projectsId, tablesId" /> | Updates an AuthorizedView in a table. |

## `SELECT` examples

Lists all AuthorizedViews from a specific table.

```sql
SELECT
name,
deletionProtection,
etag,
subsetView
FROM google.bigtableadmin.authorized_views
WHERE instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}'
AND tablesId = '{{ tablesId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorized_views</code> resource.

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
INSERT INTO google.bigtableadmin.authorized_views (
instancesId,
projectsId,
tablesId,
name,
subsetView,
etag,
deletionProtection
)
SELECT 
'{{ instancesId }}',
'{{ projectsId }}',
'{{ tablesId }}',
'{{ name }}',
'{{ subsetView }}',
'{{ etag }}',
{{ deletionProtection }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: subsetView
      value:
        - name: rowPrefixes
          value:
            - string
        - name: familySubsets
          value: object
    - name: etag
      value: string
    - name: deletionProtection
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>authorized_views</code> resource.

```sql
/*+ update */
UPDATE google.bigtableadmin.authorized_views
SET 
name = '{{ name }}',
subsetView = '{{ subsetView }}',
etag = '{{ etag }}',
deletionProtection = true|false
WHERE 
authorizedViewsId = '{{ authorizedViewsId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}'
AND tablesId = '{{ tablesId }}';
```

## `DELETE` example

Deletes the specified <code>authorized_views</code> resource.

```sql
/*+ delete */
DELETE FROM google.bigtableadmin.authorized_views
WHERE authorizedViewsId = '{{ authorizedViewsId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}'
AND tablesId = '{{ tablesId }}';
```
