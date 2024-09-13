
---
title: external_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - external_systems
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

Creates, updates, deletes or gets an <code>external_system</code> resource or lists <code>external_systems</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>external_systems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.external_systems" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_sources_findings_external_systems_patch" /> | `UPDATE` | <CopyableCode code="externalSystemsId, findingsId, foldersId, sourcesId" /> | Updates external system. This is for a given finding. |
| <CopyableCode code="organizations_sources_findings_external_systems_patch" /> | `UPDATE` | <CopyableCode code="externalSystemsId, findingsId, organizationsId, sourcesId" /> | Updates external system. This is for a given finding. |
| <CopyableCode code="projects_sources_findings_external_systems_patch" /> | `UPDATE` | <CopyableCode code="externalSystemsId, findingsId, projectsId, sourcesId" /> | Updates external system. This is for a given finding. |

## `UPDATE` example

Updates a external_system only if the necessary resources are available.

```sql
UPDATE google.securitycenter.external_systems
SET 
name = '{{ name }}',
assignees = '{{ assignees }}',
externalUid = '{{ externalUid }}',
status = '{{ status }}',
externalSystemUpdateTime = '{{ externalSystemUpdateTime }}',
caseUri = '{{ caseUri }}',
casePriority = '{{ casePriority }}',
caseSla = '{{ caseSla }}',
caseCreateTime = '{{ caseCreateTime }}',
caseCloseTime = '{{ caseCloseTime }}',
ticketInfo = '{{ ticketInfo }}'
WHERE 
externalSystemsId = '{{ externalSystemsId }}'
AND findingsId = '{{ findingsId }}'
AND foldersId = '{{ foldersId }}'
AND sourcesId = '{{ sourcesId }}';
```
