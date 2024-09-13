
---
title: assets_security_marks
hide_title: false
hide_table_of_contents: false
keywords:
  - assets_security_marks
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

Creates, updates, deletes or gets an <code>assets_security_mark</code> resource or lists <code>assets_security_marks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets_security_marks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.assets_security_marks" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_assets_update_security_marks" /> | `UPDATE` | <CopyableCode code="assetsId, foldersId" /> | Updates security marks. |
| <CopyableCode code="organizations_assets_update_security_marks" /> | `UPDATE` | <CopyableCode code="assetsId, organizationsId" /> | Updates security marks. |
| <CopyableCode code="projects_assets_update_security_marks" /> | `UPDATE` | <CopyableCode code="assetsId, projectsId" /> | Updates security marks. |

## `UPDATE` example

Updates a assets_security_mark only if the necessary resources are available.

```sql
UPDATE google.securitycenter.assets_security_marks
SET 
name = '{{ name }}',
marks = '{{ marks }}',
canonicalName = '{{ canonicalName }}'
WHERE 
assetsId = '{{ assetsId }}'
AND foldersId = '{{ foldersId }}';
```
