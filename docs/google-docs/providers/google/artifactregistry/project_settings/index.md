---
title: project_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - project_settings
  - artifactregistry
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

Creates, updates, deletes, gets or lists a <code>project_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.artifactregistry.project_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the project's settings. Always of the form: projects/{project-id}/projectSettings In update request: never set In response: always set |
| <CopyableCode code="legacyRedirectionState" /> | `string` | The redirection state of the legacy repositories in this project. |
| <CopyableCode code="pullPercent" /> | `integer` | The percentage of pull traffic to redirect from GCR to AR when using partial redirection. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_project_settings" /> | `SELECT` | <CopyableCode code="projectsId" /> | Retrieves the Settings for the Project. |
| <CopyableCode code="update_project_settings" /> | `UPDATE` | <CopyableCode code="projectsId" /> | Updates the Settings for the Project. |

## `SELECT` examples

Retrieves the Settings for the Project.

```sql
SELECT
name,
legacyRedirectionState,
pullPercent
FROM google.artifactregistry.project_settings
WHERE projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a <code>project_settings</code> resource.

```sql
/*+ update */
UPDATE google.artifactregistry.project_settings
SET 
name = '{{ name }}',
legacyRedirectionState = '{{ legacyRedirectionState }}',
pullPercent = '{{ pullPercent }}'
WHERE 
projectsId = '{{ projectsId }}';
```
