---
title: annotation_specs
hide_title: false
hide_table_of_contents: false
keywords:
  - annotation_specs
  - aiplatform
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

Creates, updates, deletes, gets or lists a <code>annotation_specs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>annotation_specs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.annotation_specs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the AnnotationSpec. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this AnnotationSpec was created. |
| <CopyableCode code="displayName" /> | `string` | Required. The user-defined name of the AnnotationSpec. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="etag" /> | `string` | Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when AnnotationSpec was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="annotationSpecsId, datasetsId, locationsId, projectsId" /> | Gets an AnnotationSpec. |

## `SELECT` examples

Gets an AnnotationSpec.

```sql
SELECT
name,
createTime,
displayName,
etag,
updateTime
FROM google.aiplatform.annotation_specs
WHERE annotationSpecsId = '{{ annotationSpecsId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
