---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
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

Creates, updates, deletes, gets or lists a <code>views</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.logging.views" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view |
| <CopyableCode code="description" /> | `string` | Optional. Describes this view. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of the view. |
| <CopyableCode code="filter" /> | `string` | Optional. Filter that restricts which log entries in a bucket are visible in this view.Filters must be logical conjunctions that use the AND operator, and they can use any of the following qualifiers: SOURCE(), which specifies a project, folder, organization, or billing account of origin. resource.type, which specifies the resource type. LOG_ID(), which identifies the log.They can also use the negations of these qualifiers with the NOT operator.For example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND NOT LOG_ID("stdout") |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of the view. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_locations_buckets_views_get" /> | `SELECT` | <CopyableCode code="billingAccountsId, bucketsId, locationsId, viewsId" /> | Gets a view on a log bucket. |
| <CopyableCode code="billing_accounts_locations_buckets_views_list" /> | `SELECT` | <CopyableCode code="billingAccountsId, bucketsId, locationsId" /> | Lists views on a log bucket. |
| <CopyableCode code="folders_locations_buckets_views_get" /> | `SELECT` | <CopyableCode code="bucketsId, foldersId, locationsId, viewsId" /> | Gets a view on a log bucket. |
| <CopyableCode code="folders_locations_buckets_views_list" /> | `SELECT` | <CopyableCode code="bucketsId, foldersId, locationsId" /> | Lists views on a log bucket. |
| <CopyableCode code="locations_buckets_views_list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | Lists views on a log bucket. |
| <CopyableCode code="organizations_locations_buckets_views_get" /> | `SELECT` | <CopyableCode code="bucketsId, locationsId, organizationsId, viewsId" /> | Gets a view on a log bucket. |
| <CopyableCode code="organizations_locations_buckets_views_list" /> | `SELECT` | <CopyableCode code="bucketsId, locationsId, organizationsId" /> | Lists views on a log bucket. |
| <CopyableCode code="projects_locations_buckets_views_get" /> | `SELECT` | <CopyableCode code="bucketsId, locationsId, projectsId, viewsId" /> | Gets a view on a log bucket. |
| <CopyableCode code="projects_locations_buckets_views_list" /> | `SELECT` | <CopyableCode code="bucketsId, locationsId, projectsId" /> | Lists views on a log bucket. |
| <CopyableCode code="billing_accounts_locations_buckets_views_create" /> | `INSERT` | <CopyableCode code="billingAccountsId, bucketsId, locationsId" /> | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| <CopyableCode code="folders_locations_buckets_views_create" /> | `INSERT` | <CopyableCode code="bucketsId, foldersId, locationsId" /> | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| <CopyableCode code="locations_buckets_views_create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| <CopyableCode code="organizations_locations_buckets_views_create" /> | `INSERT` | <CopyableCode code="bucketsId, locationsId, organizationsId" /> | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| <CopyableCode code="projects_locations_buckets_views_create" /> | `INSERT` | <CopyableCode code="bucketsId, locationsId, projectsId" /> | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| <CopyableCode code="billing_accounts_locations_buckets_views_delete" /> | `DELETE` | <CopyableCode code="billingAccountsId, bucketsId, locationsId, viewsId" /> | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| <CopyableCode code="folders_locations_buckets_views_delete" /> | `DELETE` | <CopyableCode code="bucketsId, foldersId, locationsId, viewsId" /> | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| <CopyableCode code="organizations_locations_buckets_views_delete" /> | `DELETE` | <CopyableCode code="bucketsId, locationsId, organizationsId, viewsId" /> | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| <CopyableCode code="projects_locations_buckets_views_delete" /> | `DELETE` | <CopyableCode code="bucketsId, locationsId, projectsId, viewsId" /> | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| <CopyableCode code="billing_accounts_locations_buckets_views_patch" /> | `UPDATE` | <CopyableCode code="billingAccountsId, bucketsId, locationsId, viewsId" /> | Updates a view on a log bucket. This method replaces the value of the filter field from the existing view with the corresponding value from the new view. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |
| <CopyableCode code="folders_locations_buckets_views_patch" /> | `UPDATE` | <CopyableCode code="bucketsId, foldersId, locationsId, viewsId" /> | Updates a view on a log bucket. This method replaces the value of the filter field from the existing view with the corresponding value from the new view. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |
| <CopyableCode code="organizations_locations_buckets_views_patch" /> | `UPDATE` | <CopyableCode code="bucketsId, locationsId, organizationsId, viewsId" /> | Updates a view on a log bucket. This method replaces the value of the filter field from the existing view with the corresponding value from the new view. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |
| <CopyableCode code="projects_locations_buckets_views_patch" /> | `UPDATE` | <CopyableCode code="bucketsId, locationsId, projectsId, viewsId" /> | Updates a view on a log bucket. This method replaces the value of the filter field from the existing view with the corresponding value from the new view. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |

## `SELECT` examples

Lists views on a log bucket.

```sql
SELECT
name,
description,
createTime,
filter,
updateTime
FROM google.logging.views
WHERE parent = '{{ parent }}'
AND parentType = '{{ parentType }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>views</code> resource.

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
INSERT INTO google.logging.views (
parent,
parentType,
description,
filter
)
SELECT 
'{{ parent }}',
'{{ parentType }}',
'{{ description }}',
'{{ filter }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: description
      value: '{{ description }}'
    - name: filter
      value: '{{ filter }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>views</code> resource.

```sql
/*+ update */
UPDATE google.logging.views
SET 
description = '{{ description }}',
filter = '{{ filter }}'
WHERE 
bucketsId = '{{ bucketsId }}'
AND foldersId = '{{ foldersId }}'
AND locationsId = '{{ locationsId }}'
AND viewsId = '{{ viewsId }}';
```

## `DELETE` example

Deletes the specified <code>views</code> resource.

```sql
/*+ delete */
DELETE FROM google.logging.views
WHERE bucketsId = '{{ bucketsId }}'
AND foldersId = '{{ foldersId }}'
AND locationsId = '{{ locationsId }}'
AND viewsId = '{{ viewsId }}';
```
