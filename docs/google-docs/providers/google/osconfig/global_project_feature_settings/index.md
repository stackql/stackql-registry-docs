
---
title: global_project_feature_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - global_project_feature_settings
  - osconfig
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

Creates, updates, deletes or gets an <code>global_project_feature_setting</code> resource or lists <code>global_project_feature_settings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_project_feature_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.osconfig.global_project_feature_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Immutable. Name specifies the URL for the ProjectFeatureSettings resource: projects/project_id/locations/global/projectFeatureSettings. |
| <CopyableCode code="patchAndConfigFeatureSet" /> | `string` | Set PatchAndConfigFeatureSet for the project. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_project_feature_settings" /> | `SELECT` | <CopyableCode code="projectsId" /> | GetProjectFeatureSettings returns the VM Manager feature settings for a project. |
| <CopyableCode code="update_project_feature_settings" /> | `UPDATE` | <CopyableCode code="projectsId" /> | UpdateProjectFeatureSettings sets the VM Manager features for a project. |

## `SELECT` examples

GetProjectFeatureSettings returns the VM Manager feature settings for a project.

```sql
SELECT
name,
patchAndConfigFeatureSet
FROM google.osconfig.global_project_feature_settings
WHERE projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a global_project_feature_setting only if the necessary resources are available.

```sql
UPDATE google.osconfig.global_project_feature_settings
SET 
name = '{{ name }}',
patchAndConfigFeatureSet = '{{ patchAndConfigFeatureSet }}'
WHERE 
projectsId = '{{ projectsId }}';
```
