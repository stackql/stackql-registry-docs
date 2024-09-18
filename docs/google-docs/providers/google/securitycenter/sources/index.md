---
title: sources
hide_title: false
hide_table_of_contents: false
keywords:
  - sources
  - securitycenter
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

Creates, updates, deletes, gets or lists a <code>sources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.sources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The relative resource name of this source. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name Example: "organizations/{organization_id}/sources/{source_id}" |
| <CopyableCode code="description" /> | `string` | The description of the source (max of 1024 characters). Example: "Web Security Scanner is a web security scanner for common vulnerabilities in App Engine applications. It can automatically scan and detect four common vulnerabilities, including cross-site-scripting (XSS), Flash injection, mixed content (HTTP in HTTPS), and outdated or insecure libraries." |
| <CopyableCode code="canonicalName" /> | `string` | The canonical name of the finding source. It's either "organizations/{organization_id}/sources/{source_id}", "folders/{folder_id}/sources/{source_id}", or "projects/{project_number}/sources/{source_id}", depending on the closest CRM ancestor of the resource associated with the finding. |
| <CopyableCode code="displayName" /> | `string` | The source's display name. A source's display name must be unique amongst its siblings, for example, two sources with the same parent can't share the same display name. The display name must have a length between 1 and 64 characters (inclusive). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_sources_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists all sources belonging to an organization. |
| <CopyableCode code="organizations_sources_get" /> | `SELECT` | <CopyableCode code="organizationsId, sourcesId" /> | Gets a source. |
| <CopyableCode code="organizations_sources_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all sources belonging to an organization. |
| <CopyableCode code="projects_sources_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists all sources belonging to an organization. |
| <CopyableCode code="organizations_sources_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a source. |
| <CopyableCode code="organizations_sources_patch" /> | `UPDATE` | <CopyableCode code="organizationsId, sourcesId" /> | Updates a source. |

## `SELECT` examples

Lists all sources belonging to an organization.

```sql
SELECT
name,
description,
canonicalName,
displayName
FROM google.securitycenter.sources
WHERE foldersId = '{{ foldersId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sources</code> resource.

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
INSERT INTO google.securitycenter.sources (
organizationsId,
name,
displayName,
description,
canonicalName
)
SELECT 
'{{ organizationsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ canonicalName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
displayName: string
description: string
canonicalName: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sources</code> resource.

```sql
/*+ update */
UPDATE google.securitycenter.sources
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
canonicalName = '{{ canonicalName }}'
WHERE 
organizationsId = '{{ organizationsId }}'
AND sourcesId = '{{ sourcesId }}';
```
