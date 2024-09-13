
---
title: findings_security_marks
hide_title: false
hide_table_of_contents: false
keywords:
  - findings_security_marks
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

Creates, updates, deletes or gets an <code>findings_security_mark</code> resource or lists <code>findings_security_marks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>findings_security_marks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.findings_security_marks" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_sources_findings_update_security_marks" /> | `UPDATE` | <CopyableCode code="findingsId, foldersId, sourcesId" /> | Updates security marks. |
| <CopyableCode code="organizations_sources_findings_update_security_marks" /> | `UPDATE` | <CopyableCode code="findingsId, organizationsId, sourcesId" /> | Updates security marks. |
| <CopyableCode code="projects_sources_findings_update_security_marks" /> | `UPDATE` | <CopyableCode code="findingsId, projectsId, sourcesId" /> | Updates security marks. |

## `UPDATE` example

Updates a findings_security_mark only if the necessary resources are available.

```sql
UPDATE google.securitycenter.findings_security_marks
SET 
name = '{{ name }}',
marks = '{{ marks }}',
canonicalName = '{{ canonicalName }}'
WHERE 
findingsId = '{{ findingsId }}'
AND foldersId = '{{ foldersId }}'
AND sourcesId = '{{ sourcesId }}';
```
