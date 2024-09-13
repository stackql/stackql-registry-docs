---
title: objects
hide_title: false
hide_table_of_contents: false
keywords:
  - objects
  - datastream
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

Creates, updates, deletes or gets an <code>object</code> resource or lists <code>objects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>objects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datastream.objects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The object resource's name. |
| <CopyableCode code="backfillJob" /> | `object` | Represents a backfill job on a specific stream object. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time of the object. |
| <CopyableCode code="displayName" /> | `string` | Required. Display name. |
| <CopyableCode code="errors" /> | `array` | Output only. Active errors on the object. |
| <CopyableCode code="sourceObject" /> | `object` | Represents an identifier of an object in the data source. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update time of the object. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, objectsId, projectsId, streamsId" /> | Use this method to get details about a stream object. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to list the objects of a specific stream. |
| <CopyableCode code="lookup" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to look up a stream object by its source object identifier. |
| <CopyableCode code="start_backfill_job" /> | `EXEC` | <CopyableCode code="locationsId, objectsId, projectsId, streamsId" /> | Use this method to start a backfill job for the specified stream object. |
| <CopyableCode code="stop_backfill_job" /> | `EXEC` | <CopyableCode code="locationsId, objectsId, projectsId, streamsId" /> | Use this method to stop a backfill job for the specified stream object. |

## `SELECT` examples

Use this method to list the objects of a specific stream.

```sql
SELECT
name,
backfillJob,
createTime,
displayName,
errors,
sourceObject,
updateTime
FROM google.datastream.objects
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND streamsId = '{{ streamsId }}'; 
```
