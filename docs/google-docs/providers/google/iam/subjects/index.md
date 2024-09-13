
---
title: subjects
hide_title: false
hide_table_of_contents: false
keywords:
  - subjects
  - iam
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

Creates, updates, deletes or gets an <code>subject</code> resource or lists <code>subjects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subjects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iam.subjects" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, subjectsId, workforcePoolsId" /> | Deletes a WorkforcePoolSubject. Subject must not already be in a deleted state. A WorkforcePoolSubject is automatically created the first time an external credential is exchanged for a Google Cloud credential using a mapped `google.subject` attribute. There is no endpoint to manually create a WorkforcePoolSubject. For 30 days after a WorkforcePoolSubject is deleted, using the same `google.subject` attribute in token exchanges with Google Cloud STS fails. Call UndeleteWorkforcePoolSubject to undelete a WorkforcePoolSubject that has been deleted, within within 30 days of deleting it. After 30 days, the WorkforcePoolSubject is permanently deleted. At this point, a token exchange with Google Cloud STS that uses the same mapped `google.subject` attribute automatically creates a new WorkforcePoolSubject that is unrelated to the previously deleted WorkforcePoolSubject but has the same `google.subject` value. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="locationsId, subjectsId, workforcePoolsId" /> | Undeletes a WorkforcePoolSubject, as long as it was deleted fewer than 30 days ago. |

## `DELETE` example

Deletes the specified subject resource.

```sql
DELETE FROM google.iam.subjects
WHERE locationsId = '{{ locationsId }}'
AND subjectsId = '{{ subjectsId }}'
AND workforcePoolsId = '{{ workforcePoolsId }}';
```
