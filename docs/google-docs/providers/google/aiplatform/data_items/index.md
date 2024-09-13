---
title: data_items
hide_title: false
hide_table_of_contents: false
keywords:
  - data_items
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

Creates, updates, deletes or gets an <code>data_item</code> resource or lists <code>data_items</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.data_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the DataItem. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this DataItem was created. |
| <CopyableCode code="etag" /> | `string` | Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels with user-defined metadata to organize your DataItems. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one DataItem(System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| <CopyableCode code="payload" /> | `any` | Required. The data that the DataItem represents (for example, an image or a text snippet). The schema of the payload is stored in the parent Dataset's metadata schema's dataItemSchemaUri field. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this DataItem was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Lists DataItems in a Dataset. |

## `SELECT` examples

Lists DataItems in a Dataset.

```sql
SELECT
name,
createTime,
etag,
labels,
payload,
satisfiesPzi,
satisfiesPzs,
updateTime
FROM google.aiplatform.data_items
WHERE datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
