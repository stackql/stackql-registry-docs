---
title: entry_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - entry_groups
  - datacatalog
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

Creates, updates, deletes, gets or lists a <code>entry_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entry_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datacatalog.entry_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the entry group in URL format. Note: The entry group itself and its child resources might not be stored in the location specified in its name. |
| <CopyableCode code="description" /> | `string` | Entry group description. Can consist of several sentences or paragraphs that describe the entry group contents. Default value is an empty string. |
| <CopyableCode code="dataCatalogTimestamps" /> | `object` | Timestamps associated with this resource in a particular system. |
| <CopyableCode code="displayName" /> | `string` | A short name to identify the entry group, for example, "analytics data - jan 2011". Default value is an empty string. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_entry_groups_get" /> | `SELECT` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Gets an entry group. |
| <CopyableCode code="projects_locations_entry_groups_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists entry groups. |
| <CopyableCode code="projects_locations_entry_groups_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an entry group. An entry group contains logically related entries together with [Cloud Identity and Access Management](/data-catalog/docs/concepts/iam) policies. These policies specify users who can create, edit, and view entries within entry groups. Data Catalog automatically creates entry groups with names that start with the `@` symbol for the following resources: * BigQuery entries (`@bigquery`) * Pub/Sub topics (`@pubsub`) * Dataproc Metastore services (`@dataproc_metastore_{SERVICE_NAME_HASH}`) You can create your own entry groups for Cloud Storage fileset entries and custom entries together with the corresponding IAM policies. User-created entry groups can't contain the `@` symbol, it is reserved for automatically created groups. Entry groups, like entries, can be searched. A maximum of 10,000 entry groups may be created per organization across all locations. You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| <CopyableCode code="projects_locations_entry_groups_delete" /> | `DELETE` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Deletes an entry group. You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| <CopyableCode code="projects_locations_entry_groups_patch" /> | `UPDATE` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Updates an entry group. You must enable the Data Catalog API in the project identified by the `entry_group.name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |

## `SELECT` examples

Lists entry groups.

```sql
SELECT
name,
description,
dataCatalogTimestamps,
displayName
FROM google.datacatalog.entry_groups
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>entry_groups</code> resource.

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
INSERT INTO google.datacatalog.entry_groups (
locationsId,
projectsId,
name,
displayName,
description
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: description
      value: '{{ description }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>entry_groups</code> resource.

```sql
/*+ update */
UPDATE google.datacatalog.entry_groups
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}'
WHERE 
entryGroupsId = '{{ entryGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>entry_groups</code> resource.

```sql
/*+ delete */
DELETE FROM google.datacatalog.entry_groups
WHERE entryGroupsId = '{{ entryGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
